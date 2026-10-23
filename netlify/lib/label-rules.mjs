// netlify/lib/label-rules.mjs
//
// Deterministic rules for the label checker. The vision model only TRANSCRIBES
// what is printed on the photos (see EXTRACTION_TOOL in label-check.mjs); every
// compliance judgment and every citation comes from this file, so the legal
// statements the tool makes are fixed text that can be reviewed and maintained.
//
// Sources (reviewed October 2026):
//   RSS-Gen Issue 6 (July 30, 2026; Amendment 1, Sept 15, 2026): ss. 9.1-9.4, Annex B
//   ICES-Gen Issue 2 (Feb 23, 2024): ss. 6.3.2, 6.3.3, Annex B
//   47 CFR 2.925, 2.926, 2.935, 2.1074, 2.1077, 15.19, 15.21, 15.105, 15.212 (eCFR, current Oct 2026)
//
// Statuses: fail  = the photo shows something the rule does not allow, or a required item is missing
//           warn  = probably a problem, or depends on a fact we can't see
//           check = cannot be decided from a photo; tells the user what to confirm
//           pass  = what the rule asks for is visible and in the right form

export const RULES_VERSION = '2026-10-23';

const RSSGEN = 'https://ised-isde.canada.ca/site/spectrum-management-telecommunications/en/devices-and-equipment/radio-equipment-standards/radio-standards-specifications-rss/rss-gen-general-requirements-compliance-radio-apparatus';
const ICESGEN = 'https://ised-isde.canada.ca/site/spectrum-management-telecommunications/en/devices-and-equipment/interference-causing-equipment-standards-ices/ices-gen-general-requirements-compliance-interference-causing-equipment';
const cfr = (s) => ({ label: `47 CFR ${s}`, url: `https://www.ecfr.gov/current/title-47/section-${s}` });
const rss = (s) => ({ label: `RSS-Gen Issue 6, s. ${s}`, url: RSSGEN });
const cfr212 = () => ({ label: '47 CFR 15.212(a)(1)(vi)(A)', url: 'https://www.ecfr.gov/current/title-47/section-15.212' });
const ices = (s) => ({ label: `ICES-Gen Issue 2, s. ${s}`, url: ICESGEN });

const FCC_15_19_A3 = 'This device complies with part 15 of the FCC Rules. Operation is subject to the following two conditions: (1) This device may not cause harmful interference, and (2) this device must accept any interference received, including interference that may cause undesired operation.';

// ---------- helpers ----------

const arr = (x) => (Array.isArray(x) ? x : []);
const norm = (s) => String(s || '').replace(/\s+/g, ' ').trim();
const up = (s) => norm(s).toUpperCase();
const esc = (s) => String(s ?? '').replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
const q = (s) => `“${norm(s)}”`;
const compact = (s) => String(s || '').replace(/\s+/g, '');
const words = (s) => norm(s).toLowerCase().replace(/[^a-z0-9() ]+/g, ' ').replace(/\s+/g, ' ').trim();

function item(market, id, status, title, detail, fix, cite) {
  return { market, id, status, title, detail, fix: fix || '', cite: arr(cite) };
}

function hasKind(ex, kinds) {
  return arr(ex.images).some((im) => kinds.includes(im.shows));
}

// Company number: five digits (current), or older forms of up to four digits followed by a letter (e.g. "21A", "4104A").
function checkIcNumber(text) {
  const raw = String(text || '').trim();
  const problems = [];
  if (/\s/.test(raw)) problems.push('it contains a space');
  const t = raw.replace(/\s+/g, '');
  if (/[a-z]/.test(t)) problems.push('it uses lower-case letters (only digits and capital letters A–Z are allowed)');
  const m = t.match(/^([^-]+)-(.+)$/);
  if (!m) {
    problems.push('there is no hyphen separating the company number from the product number');
    return { ok: false, problems };
  }
  const [, co, prod] = m;
  let soft = false;
  if (!/^(\d{5}|\d{1,4}[A-Z])$/i.test(co)) { problems.push(`the company number “${co}” is not in the usual form (five digits, or an older number of up to four digits followed by a letter, such as “21A”)`); soft = true; }
  if (/[^A-Za-z0-9]/.test(prod)) problems.push(`the product number “${prod}” contains a character other than a digit or letter`);
  if (prod.length > 11) problems.push(`the product number “${prod}” is ${prod.length} characters long (the maximum is 11)`);
  return { ok: problems.length === 0, problems, co, prod, soft: soft && problems.length === 1 };
}

// FCC ID: grantee code (3 characters for older grantees, 5 for codes issued since 2009, which begin with "2")
// followed by the product code (capital letters, digits and dashes, 1-14 characters).
function checkFccId(text) {
  const raw = String(text || '').trim();
  const problems = [];
  if (/\s/.test(raw)) problems.push('it contains a space');
  const t = raw.replace(/\s+/g, '');
  if (/[a-z]/.test(t)) problems.push('it uses lower-case letters (the grantee and product codes use capital letters)');
  if (/[^A-Za-z0-9-]/.test(t)) problems.push('it contains a character other than a capital letter, digit or dash');
  const gl = t.startsWith('2') ? 5 : 3;
  const grantee = t.slice(0, gl);
  const prod = t.slice(gl);
  if (grantee.length < gl || grantee.includes('-')) problems.push(`the grantee code “${grantee}” does not look complete`);
  if (!prod.length) problems.push('there is no product code after the grantee code');
  if (prod.length > 14) problems.push(`the product code “${prod}” is ${prod.length} characters long (the maximum is 14)`);
  return { ok: problems.length === 0, problems, grantee, prod };
}

function wildcardSuspect(s) {
  const t = String(s || '');
  return /[*?#]/.test(t) || /XX$/i.test(t) || /x{2,}/.test(t) || /\(.*?\)/.test(t);
}

function sameId(a, b) {
  return compact(a).toUpperCase() === compact(b).toUpperCase();
}

function diffNote(found, expected) {
  return `The photo shows ${q(found)}; you told us the certification shows ${q(expected)}.`;
}

// ---------- the 15.19 statement ----------

function part15Statement(st) {
  const text = words(st && st.verbatim_text);
  if (!st || !st.present || !text) return { present: false };
  const parts = {
    complies: /complies with part 15 of the fcc rules/.test(text),
    two: /following two conditions/.test(text),
    c1: /may not cause harmful interference/.test(text),
    c2: /must accept any interference received/.test(text),
    c3: /including interference that may cause undesired operation/.test(text),
  };
  const missing = [];
  if (!parts.complies) missing.push('“This device complies with part 15 of the FCC Rules”');
  if (!parts.c1) missing.push('condition (1), “may not cause harmful interference”');
  if (!parts.c2 || !parts.c3) missing.push('condition (2), “must accept any interference received, including interference that may cause undesired operation”');
  if (!parts.two) missing.push('“Operation is subject to the following two conditions”');
  return { present: true, missing };
}

// ---------- Canada ----------

function canada(ex, a) {
  const out = [];
  const add = (...args) => out.push(item('CA', ...args));
  const radio = a.radio !== 'none';
  const host = a.module === 'host';
  const small = a.small === 'yes';
  const display = a.display === 'yes';
  const ics = arr(ex.ic_numbers);
  const hw = arr(ex.hardware_ids);
  const names = arr(ex.product_names);
  const qrs = arr(ex.qr_codes);
  const decoded = arr(a.qr_decoded).filter(Boolean);
  const devicePhoto = hasKind(ex, ['device_label', 'marking_on_enclosure']);
  const packagingPhoto = hasKind(ex, ['packaging']);
  const manualPhoto = hasKind(ex, ['user_manual_page']);

  if (radio) {
    // 1. IC number present
    if (!ics.length) {
      if (small) {
        add('ca-ic-present', packagingPhoto ? 'fail' : 'check', 'IC certification number',
          `No IC number is visible. Because you said the device is 2.5 cm or less in its largest dimension, the label may go in the user manual instead of on the device, but it must then also appear on the packaging.${packagingPhoto ? ' The packaging photo does not show it either.' : ''}`,
          'Put “IC:” and the certification number in the user manual and on the exterior of the packaging.',
          [rss('9.4.3.2'), rss('9.1')]);
      } else if (display) {
        add('ca-ic-present', 'check', 'IC certification number',
          'No IC number is visible on the photos. A device with an integrated display may show it as an e-label instead, under the conditions in Annex B.',
          'If you rely on an e-label, confirm it shows the full label content, and that the manual, packaging or product website tells users how to reach it.',
          [rss('9.4.4.1'), { label: 'RSS-Gen Issue 6, Annex B', url: RSSGEN }]);
      } else if (qrs.length) {
        add('ca-ic-present', 'warn', 'IC certification number',
          'No IC number is printed in text, but the label has a QR code. A QR code can be the label only if the code itself contains the full label content (not a link), is on the product, can be read by generic QR apps, and the user manual says it is there.',
          'Confirm what the QR code contains. If it is a link, print the IC number as text.',
          [rss('9.4.2')]);
      } else {
        add('ca-ic-present', 'fail', 'IC certification number',
          `No IC certification number is visible.${devicePhoto ? '' : ' (We may not have a photo of the device label itself.)'} Every unit of a certified radio product sold in Canada must carry its ISED certification number, preceded by “IC:”.`,
          host ? 'For a host product, label the module’s number as “Contains IC: XXXXX-YYYYYYYYYYY”, unless the module’s own label stays visible once installed.' : 'Add “IC: ” followed by the certification number on the product label.',
          [rss(host ? '9.4.4.2' : '9.4.4.1')]);
      }
    }

    // 2-4. each IC number: prefix, format, match
    ics.forEach((ic, i) => {
      const label = ics.length > 1 ? `IC number ${i + 1} (${norm(ic.text)})` : `IC number (${norm(ic.text)})`;
      const pre = up(ic.prefix).replace(/\s*:\s*/g, ':');
      const isContains = /^(CONTAINS|CONTIENT|CONTAINS\/CONTIENT|CONTAINS \/ CONTIENT)\b/.test(pre) || /CONTAINS|CONTIENT/.test(pre);
      if (host) {
        if (isContains && /IC:$/.test(pre)) add(`ca-ic-prefix-${i}`, 'pass', `${label}: prefix`, `Printed as ${q((ic.prefix || '') + ' ' + ic.text)}, which matches the host form (“Contains”, “Contient” or “Contains/Contient” followed by “IC:”).`, '', [rss('9.4.4.2')]);
        else if (isContains) add(`ca-ic-prefix-${i}`, 'warn', `${label}: prefix`, `Printed as ${q((ic.prefix || '') + ' ' + ic.text)}. The host form is “Contains IC:” (or “Contient IC:” / “Contains/Contient IC:”), with the colon.`, 'Use exactly “Contains IC: ” before the module number.', [rss('9.4.4.2')]);
        else add(`ca-ic-prefix-${i}`, 'warn', `${label}: prefix`, `Printed with the prefix ${q(ic.prefix || '(none)')}. You told us the product is a host built around a certified module. In that case the host carries the module’s number after “Contains”, “Contient” or “Contains/Contient”, unless the module’s own label is visible when installed. A plain “IC:” on a host reads as if the host itself holds that certification.`, 'Change it to “Contains IC: ” followed by the module’s number, or confirm the product has its own certification.', [rss('9.4.4.2')]);
      } else {
        if (pre === 'IC:') add(`ca-ic-prefix-${i}`, 'pass', `${label}: prefix`, 'The number is preceded by “IC:”.', '', [rss('9.4.4.1')]);
        else if (isContains) add(`ca-ic-prefix-${i}`, 'warn', `${label}: prefix`, `Printed as ${q((ic.prefix || '') + ' ' + ic.text)}, which is the form for a module inside a host. You told us the product holds its own certification; its own number should be preceded by “IC:”.`, 'If this is a module number, also show the product’s own IC number, or change your answer to “host”.', [rss('9.4.4.1'), rss('9.4.4.2')]);
        else if (pre === 'IC') add(`ca-ic-prefix-${i}`, 'warn', `${label}: prefix`, 'The number is preceded by “IC” without the colon. The rule gives the prefix as “IC:”.', 'Print “IC:” with the colon.', [rss('9.4.4.1')]);
        else add(`ca-ic-prefix-${i}`, 'fail', `${label}: prefix`, `The number is preceded by ${q(ic.prefix || '(nothing)')}. The certification number must be preceded by “IC:”.`, 'Print “IC: ” immediately before the number.', [rss('9.4.4.1')]);
      }

      const f = checkIcNumber(ic.text);
      if (f.ok) add(`ca-ic-format-${i}`, 'pass', `${label}: format`, `The company number (${f.co}) and product number (${f.prod}) are in the IC: XXXXX-YYYYYYYYYYY format.`, '', [rss('9.4.4.1')]);
      else add(`ca-ic-format-${i}`, ic.confident === false ? 'check' : f.soft ? 'warn' : 'fail', `${label}: format`,
        `${ic.confident === false ? 'The photo was not clear enough to read every character with confidence, so treat this as a prompt to check. ' : ''}As read from the photo, ${f.problems.join('; ')}. The format is IC: XXXXX-YYYYYYYYYYY: the ISED company number, a hyphen, then a product number of up to eleven digits or capital letters.`,
        'Copy the number character for character from the certificate or the Radio Equipment List.', [rss('9.4.4.1')]);

      if (a.expected?.ic && !ics.some((x) => sameId(x.text, a.expected.ic))) {
        if (i === 0) add('ca-ic-match', 'fail', 'IC number matches the certification', `${diffNote(ic.text, a.expected.ic)} The number on the product must match the certification exactly.`, 'Correct the artwork, then check it against the Radio Equipment List entry.', [rss('9.4.4.1')]);
      } else if (a.expected?.ic && i === 0) {
        add('ca-ic-match', 'pass', 'IC number matches the certification', `The number on the photo matches the number you entered (${norm(a.expected.ic)}).`, 'Confirm it against the Radio Equipment List entry as well, since that is the record an auditor will use.', [rss('9.4.4.1')]);
      }
    });

    // 5. HVIN
    if (!hw.length) {
      const relief = small || display || (!ics.length && qrs.length);
      if (host) add('ca-hvin', 'check', 'Hardware version identification number (HVIN)', 'No HVIN is visible. For a host product the HVIN in the REL is the module’s; section 9.4.4.2 asks the host label for “Contains IC:” with the module’s number and the host marketing name.', 'Follow the module maker’s integration instructions for any other host-label content.', [rss('9.4.4.2')]);
      else add('ca-hvin', relief ? 'check' : 'fail', 'Hardware version identification number (HVIN)',
        `We could not find an HVIN or model identifier on the photos. The label must show the HVIN, with or without a prefix such as “HVIN:”, “Model#”, “M/N:” or “P/N:”.${relief ? ' Where the label is in the manual and packaging, or on an e-label, the HVIN goes there with the rest of the label.' : ''}`,
        'Add the HVIN exactly as it appears in the Radio Equipment List.', [rss('9.4.4.1')]);
    } else {
      const wild = hw.filter((h) => wildcardSuspect(h.text));
      add('ca-hvin', wild.length ? 'warn' : 'pass', 'Hardware version identification number (HVIN)',
        wild.length
          ? `Found ${hw.map((h) => q(((h.label_as_printed || '') + ' ' + h.text))).join(', ')}. ${wild.map((h) => q(h.text)).join(', ')} looks as if it may contain a placeholder or wildcard. Identifiers may not use wildcard characters standing for variants; the same string is acceptable only if it identifies a single product version.`
          : `Found ${hw.map((h) => q(((h.label_as_printed || '') + ' ' + h.text))).join(', ')}.`,
        wild.length ? 'Use the exact HVIN of this version, as listed in the REL.' : 'Confirm it matches the HVIN in the Radio Equipment List character for character.', [rss('9.4.4.1')]);
      if (a.expected?.hvin && !host) {
        const ok = hw.some((h) => sameId(h.text, a.expected.hvin));
        add('ca-hvin-match', ok ? 'pass' : 'fail', 'HVIN matches the certification', ok ? `The HVIN on the photo matches what you entered (${norm(a.expected.hvin)}).` : `None of the identifiers on the photo (${hw.map((h) => q(h.text)).join(', ')}) matches the HVIN you entered (${q(a.expected.hvin)}).`, ok ? '' : 'Correct the HVIN so it matches the REL exactly.', [rss('9.4.4.1')]);
      }
    }

    // 6. PMN
    if (names.length) {
      add('ca-pmn', 'pass', 'Product marketing name (PMN)', `Found ${names.map((n) => q(n.text)).join(', ')}. The PMN may be on the label, the packaging or the product literature.`, 'Confirm it matches the PMN in the Radio Equipment List.', [rss('9.4.4.1')]);
      if (a.expected?.pmn && !host && !names.some((n) => up(n.text) === up(a.expected.pmn))) {
        add('ca-pmn-match', 'warn', 'PMN matches the certification', `The names on the photo (${names.map((n) => q(n.text)).join(', ')}) do not exactly match the PMN you entered (${q(a.expected.pmn)}). The PMN shown with the product has to match the REL.`, 'If the PMN is printed elsewhere (packaging or literature), check it there; otherwise align the name.', [rss('9.4.4.1')]);
      }
    } else {
      add('ca-pmn', 'check', 'Product marketing name (PMN)', 'No product marketing name is visible. That can be fine: the PMN may be on the packaging or in product literature that ships with the product or is readily available online, instead of on the label.', 'Confirm where the PMN appears and that it matches the REL.', [rss('9.4.4.1')]);
    }

    // 7. Host marketing name
    if (host) add('ca-hmn', names.length ? 'pass' : 'check', 'Host marketing name (HMN)', names.length ? `A product name is visible (${names.map((n) => q(n.text)).join(', ')}). For host equipment, the host marketing name goes on the host label, packaging or literature.` : 'For host equipment, the host marketing name must appear on the host’s label, packaging or product literature. We could not see it on the photos.', 'Also check the module maker’s integration instructions for any host-label wording they require.', [rss('9.4.4.2'), rss('9.2')]);

    // 8. QR code
    if (qrs.length || decoded.length) {
      const urlOnly = decoded.length && decoded.every((d) => /^\s*(https?:\/\/|www\.)\S+\s*$/i.test(d));
      const hasIc = decoded.some((d) => /IC\s*:/i.test(d));
      if (urlOnly) add('ca-qr', ics.length ? 'check' : 'fail', 'QR code', `The QR code decodes to a web address (${q(decoded[0])}). A QR code can serve as the ISED label only if the code itself contains the full label content. A link to a web page does not qualify.${ics.length ? ' The IC number is also printed as text, so the QR code is not doing the work of the label here; this is only a problem if you intended it to.' : ''}`, 'Print the label content as text, or encode the label content itself in the QR code.', [rss('9.4.2')]);
      else if (hasIc) add('ca-qr', 'check', 'QR code', 'The QR code contains label content, including an IC number. The other conditions also have to be met: it is permanently on the product (not shown on a screen), generic QR apps can read it, and the user manual tells the user it is there.', 'Confirm the manual explains the QR code, and that the encoded IC number and HVIN match the REL.', [rss('9.4.2')]);
      else add('ca-qr', 'check', 'QR code', `There is a QR code on the photo${decoded.length ? ` (it decodes to ${q(decoded[0].slice(0, 120))})` : ', but we could not decode it'}. If you rely on it as the label, the code itself must contain the full label content (not a link), be on the product, be readable by generic QR apps, and be explained in the user manual.`, 'If the IC number and HVIN are printed as text as well, the QR code is optional and these conditions do not apply.', [rss('9.4.2')]);
    }

    // 9. Licence-exempt notice
    if (a.radio === 'licence_exempt') {
      const le = ex.ised_licence_exempt_notice || {};
      if (le.english_present && le.french_present) add('ca-le-notice', 'pass', 'Licence-exempt notice (English and French)', 'The licence-exempt notice appears in both English and French on the photos.', 'Check the wording against section 9.3.2.1, or use the exact wording the standard gives.', [rss('9.3.2.1')]);
      else if (le.english_present) add('ca-le-notice', manualPhoto ? 'fail' : 'check', 'Licence-exempt notice (English and French)', `The licence-exempt notice appears in English but we could not find the French version${manualPhoto ? ' on the photos, which include a manual page' : ''}. It must be given in both languages, in the manual, on the device or both.`, manualPhoto ? 'Add the French text of the notice.' : 'Confirm the French version is in the manual.', [rss('9.3.2.1'), rss('9.3.1')]);
      else add('ca-le-notice', 'check', 'Licence-exempt notice (English and French)', `We did not see the licence-exempt notice${manualPhoto ? '' : ' (it usually sits in the user manual, which the photos may not include)'}. For Wi-Fi, Bluetooth and similar radios, the manual, the device or both must carry it in English and French: “This device contains licence-exempt transmitter(s)/receiver(s) that comply with Innovation, Science and Economic Development Canada’s licence-exempt RSS(s). Operation is subject to the following two conditions: This device may not cause interference. This device must accept any interference, including interference that can cause undesired operation of the device.”`, 'Confirm both language versions are in the manual. Products with detachable antennas also need the antenna notice under section 9.3.2.2.', [rss('9.3.2.1'), rss('9.3.2.2')]);
    }

    // 10. Manual
    add('ca-manual', 'check', 'User manual notices in English and French', 'A label photo cannot show this. Every notice and item of user information required by the applicable RSS standards must be in the manual in English and French, including any RF exposure information required under RSS-102. If the manual is online, it must stay freely available for as long as the product is sold in Canada, and each unit must explain how to find it.', 'Check the French notices before printing; this is the most common gap we see on a first Canadian filing.', [rss('9.3.1')]);
  } else if (ics.length) {
    add('ca-ic-unexpected', 'warn', 'IC number on a product with no radio', `The photo shows an IC number (${q(ics[0].text)}), but you told us the product has no radio. IC numbers are issued for certified radio apparatus. If there is a radio module inside, change your answer and run the check again.`, '', [rss('9.4.4.1')]);
  }

  // 11. ICES marking
  if (a.digital !== 'no') {
    const ms = arr(ex.ices_markings);
    if (!ms.length) {
      const relief = small || display;
      add('ca-ices', relief ? 'check' : 'fail', 'ICES marking (CAN ICES-003 / NMB-003)',
        `We could not find the ICES marking. Equipment with digital circuitry must carry it on the equipment, in English and French, in the form CAN ICES(*)/NMB(*) with the standard’s class letter; for ICES-003 that is “CAN ICES-003(B)/NMB-003(B)” (or (A)).${small ? ' A device of 2.5 cm or less may carry it in the manual and on the packaging instead.' : ' Larger equipment may carry it elsewhere only with ISED approval under section 6.3.2.1.'}${display ? ' A device with an integral display may use an e-label under ICES-Gen Annex B.' : ''}`,
        'Add the marking, for example “CAN ICES-003(B)/NMB-003(B)” for a Class B product.', [ices('6.3.3'), ices('6.3.2.1'), ices('6.3.2.2')]);
    } else {
      ms.forEach((m, i) => {
        const t = up(m.text).replace(/\s+/g, '');
        const hasCan = /CAN|CANADA/.test(t);
        const hasIces = /ICES/.test(t);
        const hasNmb = /NMB/.test(t);
        const cls = t.match(/\(([AB])\)/g) || [];
        const old = /ICES-3|NMB-3\b/.test(t) && !/ICES-003/.test(t);
        const probs = [];
        if (!hasCan) probs.push('it does not include “CAN” or “Canada”');
        if (!hasIces) probs.push('it does not include “ICES”');
        if (!hasNmb) probs.push('the French part (“NMB”) is missing');
        if (probs.length) add(`ca-ices-${i}`, m.confident === false ? 'check' : 'fail', 'ICES marking (CAN ICES-003 / NMB-003)', `The photo shows ${q(m.text)}: ${probs.join('; ')}. The marking must be in both English and French.`, 'Use the form “CAN ICES-003(B)/NMB-003(B)” (or (A) for a Class A product).', [ices('6.3.3')]);
        else if (cls.length >= 2 && new Set(cls).size > 1) add(`ca-ices-${i}`, m.confident === false ? 'check' : 'fail', 'ICES marking (CAN ICES-003 / NMB-003)', `The photo shows ${q(m.text)}. The English and French class letters differ.`, 'Use the class letter from your ICES-003 test report on both halves of the marking.', [ices('6.3.3')]);
        else if (cls.length < 2) add(`ca-ices-${i}`, 'warn', 'ICES marking (CAN ICES-003 / NMB-003)', `The photo shows ${q(m.text)}. The class letter (A or B) should follow both the English and the French reference where the standard distinguishes classes, as ICES-003 does.`, 'Use the class letter from your ICES-003 test report on both halves of the marking.', [ices('6.3.3')]);
        else add(`ca-ices-${i}`, 'pass', 'ICES marking (CAN ICES-003 / NMB-003)', `The photo shows ${q(m.text)}, which has the bilingual form and a class letter.${old ? ' This is the older “ICES-3” format used before ICES-003 Issue 7; new artwork usually reads “CAN ICES-003(B)/NMB-003(B)”.' : ''}`, 'Confirm the class letter matches your ICES-003 test report.', [ices('6.3.3')]);
      });
    }
  }

  // 12. Legibility and permanence
  const poor = arr(ex.images).some((im) => im.quality === 'poor');
  const concern = norm(ex.legibility_concerns);
  add('ca-legible', concern ? 'warn' : 'check', 'Permanently affixed and legible', `${concern ? `The reader noted: ${concern}. ` : ''}The label must be permanently affixed to each unit, with indelible and clearly legible text. A photo cannot show how durable a label is${poor ? ', and at least one photo was too unclear to judge legibility' : ''}.`, 'Use a printed, etched or moulded label, or a durable nameplate. Avoid paper stickers that can peel or fade.', [rss('9.4.1')]);

  return out;
}

// ---------- United States ----------

function usa(ex, a) {
  const out = [];
  const add = (...args) => out.push(item('US', ...args));
  const radio = a.radio !== 'none';
  const host = a.module === 'host';
  const small = a.small === 'yes';
  const display = a.display === 'yes';
  const ids = arr(ex.fcc_ids);
  const hw = arr(ex.hardware_ids);
  const names = arr(ex.product_names);
  const part15 = a.radio === 'licence_exempt' || a.digital !== 'no';
  const packagingPhoto = hasKind(ex, ['packaging']);

  if (radio) {
    if (!ids.length) {
      if (small) add('us-fccid-present', packagingPhoto ? 'fail' : 'check', 'FCC ID', `No FCC ID is visible. If the device is too small for a label in at least 4-point type and has no display, the FCC ID goes in the user manual, and also on the packaging or on a removable label attached to the device. (We used your answer on the 2.5 cm question as a stand-in; the FCC test is whether a legible label in 4-point type fits on the device.)${packagingPhoto ? ' The packaging photo does not show it.' : ''}`, 'Put the FCC ID in the manual and on the packaging (or a removable label).', [cfr('2.925')]);
      else if (display) add('us-fccid-present', 'check', 'FCC ID', 'No FCC ID is visible on the photos. A device with an integrated display may show it electronically under section 2.935, but it still needs a physical label on the device or its packaging at import, marketing and sale, carrying the FCC ID or other identifying information.', 'Confirm the e-label conditions (below) and that the packaging carries the FCC ID or model and regulatory web address.', [cfr('2.935')]);
      else add('us-fccid-present', 'fail', 'FCC ID', 'No FCC ID is visible. Each unit of certified equipment must carry a permanently affixed label showing “FCC ID” followed by its identifier, visible from outside the enclosure at the time of purchase.', host ? 'For a host product, label it “Contains FCC ID: ” followed by the module’s FCC ID, unless the module’s label stays visible once installed.' : 'Add “FCC ID: ” followed by the grantee code and product code.', [cfr('2.925'), ...(host ? [cfr212()] : [])]);
    }

    ids.forEach((id, i) => {
      const label = ids.length > 1 ? `FCC ID ${i + 1} (${norm(id.text)})` : `FCC ID (${norm(id.text)})`;
      const preRaw = norm(id.prefix);
      const pre = up(id.prefix);
      const contains = /CONTAINS/.test(pre);
      const hasFccId = /FCC ID/.test(preRaw); // capitals as printed
      if (!/FCC\s?ID/i.test(preRaw)) add(`us-fccid-prefix-${i}`, 'fail', `${label}: prefix`, `The identifier is preceded by ${q(preRaw || '(nothing)')}. It must be preceded by the term “FCC ID” in capital letters.`, 'Print “FCC ID: ” before the identifier.', [cfr('2.925')]);
      else if (!hasFccId) add(`us-fccid-prefix-${i}`, 'fail', `${label}: prefix`, `Printed as ${q(preRaw)}. The rule requires the term “FCC ID”, in capital letters, with the space.`, 'Print “FCC ID” in capitals.', [cfr('2.925')]);
      else if (id.on_single_line === false) add(`us-fccid-prefix-${i}`, 'fail', `${label}: one line`, '“FCC ID” and the identifier appear to be split across two lines. The term “FCC ID” must precede the identifier on a single line.', 'Keep “FCC ID: ” and the full identifier on one line.', [cfr('2.925')]);
      else if (host && !contains) add(`us-fccid-prefix-${i}`, 'warn', `${label}: host wording`, `Printed as ${q(preRaw + ' ' + id.text)}. You told us the product is a host built around a certified module. If the module’s FCC ID is not visible once installed, the host’s exterior label should refer to the enclosed module, for example “Contains FCC ID: ${norm(id.text)}”. A plain “FCC ID:” reads as if the host itself is certified.`, 'Use “Contains FCC ID: ” or similar wording, or confirm the host has its own grant.', [cfr212()]);
      else if (!host && contains) add(`us-fccid-prefix-${i}`, 'warn', `${label}: prefix`, `Printed as ${q(preRaw + ' ' + id.text)}, which is host wording for an enclosed module. You told us the product has its own certification; its own FCC ID should be shown as “FCC ID”.`, 'Check which grant applies to the finished product.', [cfr('2.925'), cfr212()]);
      else add(`us-fccid-prefix-${i}`, 'pass', `${label}: prefix`, `Printed as ${q(preRaw + ' ' + id.text)}, on one line.`, '', [host ? cfr212() : cfr('2.925')]);

      const f = checkFccId(id.text);
      if (f.ok) add(`us-fccid-format-${i}`, 'pass', `${label}: format`, `Grantee code ${f.grantee}, product code ${f.prod}; the characters and lengths are within the rule.`, 'Confirm it against the grant on the FCC Equipment Authorization database.', [cfr('2.926')]);
      else add(`us-fccid-format-${i}`, id.confident === false ? 'check' : 'warn', `${label}: format`, `${id.confident === false ? 'The photo was not clear enough to read every character with confidence. ' : ''}As read, ${f.problems.join('; ')}. The FCC ID is the grantee code followed by a product code of capital letters, digits and dashes, no more than 14 characters.`, 'Copy the identifier from the grant.', [cfr('2.926')]);

      if (a.expected?.fcc && i === 0) {
        const ok = ids.some((x) => sameId(x.text, a.expected.fcc));
        add('us-fccid-match', ok ? 'pass' : 'fail', 'FCC ID matches the grant', ok ? `Matches the FCC ID you entered (${norm(a.expected.fcc)}).` : `${diffNote(id.text, a.expected.fcc)} The label must show the identifier of the grant exactly.`, ok ? '' : 'Correct the artwork.', [cfr('2.925')]);
      }
    });

    if (display && !ids.length) {
      add('us-elabel', 'check', 'Electronic label conditions (2.935)', 'If you rely on an e-label: it must be readily accessible on the display, reachable in no more than three steps from the settings menu without special codes or accessories, and legible without magnification; users need prominent instructions on how to find it; the information must be programmed by the responsible party and secured so third parties cannot change it; and the device or its packaging still needs a physical label at import and sale.', 'Check each condition, and keep a copy of the access instructions for the certification file.', [cfr('2.935')]);
    }
  } else {
    // No radio: SDoC equipment
    if (ids.length) add('us-sdoc-fccid', 'warn', 'FCC ID on a product with no radio', `The photo shows an FCC ID (${q(ids[0].text)}), but you told us the product has no radio. Equipment authorised under a Supplier’s Declaration of Conformity must be uniquely identified with an identifier that does not resemble an FCC ID.`, 'If there is a radio module inside, change your answer and run the check again.', [cfr('2.1074')]);
    add('us-sdoc-id', hw.length || names.length ? 'pass' : 'check', 'Unique product identification (SDoC)', hw.length || names.length ? `The product is identified as ${[...hw, ...names].map((x) => q(x.text)).join(', ')}. SDoC equipment must be uniquely identified by the responsible party.` : 'We could not see a model number or other unique identifier. SDoC equipment must be uniquely identified by the party responsible for marketing or importing it in the United States.', hw.length || names.length ? '' : 'Confirm the product carries or is accompanied by a unique identifier (see also section 2.1077(a)(1)).', [cfr('2.1074'), cfr('2.1077')]);
    add('us-sdoc-logo', 'pass', 'FCC logo', ex.fcc_logo_present ? 'The FCC logo appears. It is optional for SDoC equipment, and using it does not replace the compliance information.' : 'No FCC logo. That is fine: the logo is voluntary for SDoC equipment.', '', [cfr('2.1074')]);
  }

  // Compliance information with US responsible party (SDoC, including the digital part of radio products)
  if (a.digital !== 'no' || !radio) {
    add('us-2-1077', 'check', 'SDoC compliance information (US responsible party)', 'Where any part of the product is authorised under SDoC (for example its digital circuitry under Part 15 Subpart B), compliance information must accompany it at marketing or import: the product’s identification, a compliance statement, and the name, address and telephone number or internet contact of the responsible party, which must be located in the United States. It may be in the manual or on a separate sheet.', 'Confirm the manual or an insert carries this, with a US responsible party.', [cfr('2.1077')]);
  }

  // 15.19 statement
  if (part15) {
    const s = part15Statement(ex.fcc_part15_statement);
    if (s.present && !s.missing.length) add('us-15-19', 'pass', 'Part 15 compliance statement', 'The statement under section 15.19(a)(3) appears, with both conditions. It may be on a separate label from the FCC ID.', 'Check the exact wording against the rule text.', [cfr('15.19')]);
    else if (s.present) add('us-15-19', ex.fcc_part15_statement.confident === false ? 'check' : 'fail', 'Part 15 compliance statement', `A Part 15 statement appears, but as read it is missing ${s.missing.join('; ')}. The required statement is: “${FCC_15_19_A3}”`, 'Use the statement word for word.', [cfr('15.19')]);
    else if (small || display) add('us-15-19', 'check', 'Part 15 compliance statement', `We did not see the Part 15 statement. ${small ? 'If the device cannot carry it in at least 4-point type and has no display, the statement goes in the user manual and also on the packaging or a removable label. (We used your answer on the 2.5 cm question as a stand-in; the FCC test is whether a legible label in 4-point type fits on the device.)' : 'With a display, it may be shown as part of an e-label under section 2.935.'} The statement is: “${FCC_15_19_A3}”`, 'Confirm where the statement appears.', [cfr('15.19'), cfr('2.935')]);
    else add('us-15-19', 'fail', 'Part 15 compliance statement', `We did not see the Part 15 compliance statement. Part 15 devices must carry it on the device (on the main control unit for multi-part systems): “${FCC_15_19_A3}” Receivers associated with licensed radio services and stand-alone cable input selector switches use different wording.`, 'Add the statement to the device label, or to a separate label on the device.', [cfr('15.19')]);
  } else if (a.radio === 'licensed') {
    add('us-15-19', 'check', 'Part 15 compliance statement', 'You told us the product has a licensed-service radio and no digital circuitry. The Part 15 statement applies to Part 15 devices; most products also contain digital circuitry that brings it in.', 'Confirm with your test lab which rule parts apply to the finished product.', [cfr('15.19')]);
  }

  // Manual statements
  add('us-manual', 'check', 'User manual statements (15.21, 15.105)', `A label photo cannot show this. The manual for any Part 15 device must warn that changes or modifications not expressly approved by the party responsible for compliance could void the user’s authority to operate the equipment.${a.digital !== 'no' ? ' For a Class A or Class B digital device, the manual must also carry the Class A or Class B information statement in a prominent location (the Class B one begins “This equipment has been tested and found to comply with the limits for a Class B digital device…”).' : ''} An online manual is acceptable if users can reasonably be expected to reach it.`, 'Check the manual text against sections 15.21 and 15.105.', [cfr('15.21'), ...(a.digital !== 'no' ? [cfr('15.105')] : [])]);

  // Legibility / permanence
  add('us-legible', norm(ex.legibility_concerns) ? 'warn' : 'check', 'Permanent, visible and legible', `The FCC label must be permanently affixed (etched, engraved, stamped, printed on a durable part of the enclosure, or a nameplate that lasts the life of the equipment), visible from outside the enclosure at the time of purchase, and legible without magnification. Type need not exceed 8-point.${norm(ex.legibility_concerns) ? ` The reader noted: ${norm(ex.legibility_concerns)}.` : ''}`, 'Check the printed type size and durability on a production sample.', [cfr('2.925')]);

  return out;
}

// ---------- entry point ----------

export function evaluate(extraction, answers) {
  const ex = extraction || {};
  const a = answers || {};
  const items = [];
  if (a.markets?.ca !== false) items.push(...canada(ex, a));
  if (a.markets?.us !== false) items.push(...usa(ex, a));
  const count = (m, s) => items.filter((i) => (!m || i.market === m) && i.status === s).length;
  const markets = ['CA', 'US'].filter((m) => items.some((i) => i.market === m));
  const summary = {
    version: RULES_VERSION,
    overall: count(null, 'fail') ? 'fail' : count(null, 'warn') ? 'warn' : 'ok',
    markets: Object.fromEntries(markets.map((m) => [m, { fail: count(m, 'fail'), warn: count(m, 'warn'), check: count(m, 'check'), pass: count(m, 'pass') }])),
    headlines: items.filter((i) => i.status === 'fail' || i.status === 'warn').map((i) => ({ market: i.market, status: i.status, title: i.title })),
    seen: {
      ic: arr(ex.ic_numbers).map((x) => norm((x.prefix || '') + ' ' + x.text)),
      fcc: arr(ex.fcc_ids).map((x) => norm((x.prefix || '') + ' ' + x.text)),
      hvin: arr(ex.hardware_ids).map((x) => norm((x.label_as_printed || '') + ' ' + x.text)),
      names: arr(ex.product_names).map((x) => norm(x.text)),
      ices: arr(ex.ices_markings).map((x) => norm(x.text)),
      images: arr(ex.images).map((x) => ({ shows: x.shows, quality: x.quality })),
    },
  };
  return { summary, items, notes: arr(ex.reader_notes).slice(0, 5).map(norm).filter(Boolean) };
}

// Plain-HTML rendering of the full report, used for the email copy.
export function reportHtml(report, meta = {}) {
  const color = { fail: '#af3c43', warn: '#8a5a00', check: '#284162', pass: '#2f6b3a' };
  const word = { fail: 'Fix', warn: 'Review', check: 'Confirm', pass: 'OK' };
  const mk = { CA: 'Canada (ISED)', US: 'United States (FCC)' };
  let h = `<div style="font-family:Arial,Helvetica,sans-serif;font-size:15px;line-height:1.55;color:#1c2733;max-width:680px">`;
  h += `<h2 style="color:#26374a;margin:0 0 6px">Label check report</h2><p style="color:#5b6775;margin:0 0 18px">${esc(meta.when || '')}${meta.product ? ' · ' + esc(meta.product) : ''}</p>`;
  for (const m of ['CA', 'US']) {
    const list = report.items.filter((i) => i.market === m);
    if (!list.length) continue;
    h += `<h3 style="color:#26374a;border-bottom:1px solid #e3e8ee;padding-bottom:4px">${mk[m]}</h3>`;
    for (const i of list) {
      h += `<p style="margin:14px 0 2px"><b style="color:${color[i.status]}">[${word[i.status]}]</b> <b>${esc(i.title)}</b></p>`;
      h += `<p style="margin:0 0 4px">${esc(i.detail)}</p>`;
      if (i.fix) h += `<p style="margin:0 0 4px;color:#5b6775"><i>${esc(i.fix)}</i></p>`;
      if (i.cite.length) h += `<p style="margin:0;font-size:13px;color:#66717f">${i.cite.map((c) => `<a href="${esc(c.url)}" style="color:#284162">${esc(c.label)}</a>`).join(' · ')}</p>`;
    }
  }
  if (report.notes?.length) h += `<h3 style="color:#26374a">Reader notes (automated, unverified)</h3><ul>${report.notes.map((n) => `<li>${esc(n)}</li>`).join('')}</ul>`;
  h += `<p style="font-size:13px;color:#66717f;margin-top:24px;border-top:1px solid #e3e8ee;padding-top:12px">This is an automated reading of the photos you uploaded, checked against the labelling rules listed above. It is general information, not legal advice, and not a review by a lawyer. It does not test the product or decide which standards apply to it, and your certification body or test lab has the final word on the label for a specific device. Rules version ${esc(report.summary.version)}.</p>`;
  h += `<p style="font-size:14px">For a lawyer’s review of your label, manual and packaging before you print (US$249 per IC certification number, one re-check included): <a href="https://www.isedrepresentative.com/label-and-manual-review/">https://www.isedrepresentative.com/label-and-manual-review/</a>. Reply to this email or write to info@isedrepresentative.com.</p></div>`;
  return h;
}
