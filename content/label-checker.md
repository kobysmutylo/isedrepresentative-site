---
title: Free ISED and FCC Label Checker: Upload a Photo of Your Label
description: Upload a photo of your product label for a free check against Canada's RSS-Gen and ICES-Gen labelling rules and the FCC's Part 2 and Part 15 rules, with citations.
h1: ISED and FCC label checker
short: Label checker
type: service
date: 2026-10-23
updated: 2026-10-23
cta: review
---

<div class="answer" markdown="1">
Take or upload a photo of your product label. The checker reads what is printed — the IC number, FCC ID, HVIN, product name, ICES marking and FCC Part 15 statement — and tests each item against the Canadian rules in [RSS-Gen Issue 6](https://ised-isde.canada.ca/site/spectrum-management-telecommunications/en/devices-and-equipment/radio-equipment-standards/radio-standards-specifications-rss/rss-gen-general-requirements-compliance-radio-apparatus) and [ICES-Gen Issue 2](https://ised-isde.canada.ca/site/spectrum-management-telecommunications/en/devices-and-equipment/interference-causing-equipment-standards-ices/ices-gen-general-requirements-compliance-interference-causing-equipment) and the US rules in [47 CFR Parts 2 and 15](https://www.ecfr.gov/current/title-47/chapter-I/subchapter-A/part-15). You see a summary straight away. The full report, with the section behind each finding and the change to make, appears when you give an email address, and a copy is sent to you. It is free. It reads labels; it does not test products, and your certification body has the final word on the label for a specific device.
</div>

<div id="lc" class="lc">
<link rel="stylesheet" href="/label-checker.css">
<noscript><p class="note">The label checker needs JavaScript. You can also email your label artwork to <a href="mailto:info@isedrepresentative.com">info@isedrepresentative.com</a>.</p></noscript>
<form id="lc-form" class="lc-step" autocomplete="off">
<fieldset>
<legend>1. Photos of the label</legend>
<p class="hint">Up to three photos: the label on the device, and if you like the packaging or the e-label screen. Shoot straight on, in good light, with the whole label in frame and in focus.</p>
<div class="lc-pick">
<label class="btn btn-primary lc-filebtn">Take a photo<input id="lc-camera" type="file" accept="image/*" capture="environment"></label>
<label class="btn lc-filebtn">Choose files<input id="lc-files" type="file" accept="image/jpeg,image/png,image/webp,image/heic,image/heif" multiple></label>
</div>
<ul id="lc-thumbs" class="lc-thumbs"></ul>
</fieldset>
<fieldset>
<legend>2. About the product</legend>
<p class="lc-q">Markets</p>
<label class="lc-inline"><input type="checkbox" name="mk_ca" checked> Canada (ISED)</label>
<label class="lc-inline"><input type="checkbox" name="mk_us" checked> United States (FCC)</label>
<p class="lc-q">Does it have a radio?</p>
<label class="lc-inline"><input type="radio" name="radio" value="licence_exempt" checked> Yes: Wi-Fi, Bluetooth, NFC, sub-GHz or other licence-exempt</label>
<label class="lc-inline"><input type="radio" name="radio" value="licensed"> Yes: cellular or another licensed service only</label>
<label class="lc-inline"><input type="radio" name="radio" value="none"> No radio</label>
<div id="lc-radio-more">
<p class="lc-q">Whose certification covers the radio?</p>
<label class="lc-inline"><input type="radio" name="module" value="own" checked> The product has its own IC number / FCC ID</label>
<label class="lc-inline"><input type="radio" name="module" value="host"> It relies on a certified module inside (host product)</label>
</div>
<p class="lc-q">Does it have digital circuitry (a processor, memory, a display)?</p>
<label class="lc-inline"><input type="radio" name="digital" value="yes" checked> Yes</label>
<label class="lc-inline"><input type="radio" name="digital" value="no"> No</label>
<p class="lc-q">Is the device 2.5 cm (about 1 inch) or smaller in its largest dimension?</p>
<label class="lc-inline"><input type="radio" name="small" value="no" checked> No</label>
<label class="lc-inline"><input type="radio" name="small" value="yes"> Yes</label>
<p class="lc-q">Does it have a built-in screen?</p>
<label class="lc-inline"><input type="radio" name="display" value="no" checked> No</label>
<label class="lc-inline"><input type="radio" name="display" value="yes"> Yes</label>
<details>
<summary>Optional: compare against your certification</summary>
<p class="hint">Enter the identifiers from your certificate or grant and we flag any difference from what is printed.</p>
<label for="lc-ic">IC certification number</label><input id="lc-ic" name="exp_ic" placeholder="e.g. 12345-ABC123">
<label for="lc-fcc">FCC ID</label><input id="lc-fcc" name="exp_fcc" placeholder="e.g. 2ABCD-XYZ100">
<label for="lc-hvin">HVIN</label><input id="lc-hvin" name="exp_hvin">
<label for="lc-pmn">PMN (product marketing name)</label><input id="lc-pmn" name="exp_pmn">
</details>
</fieldset>
<p style="display:none"><label>Leave blank <input name="website" tabindex="-1"></label></p>
<p><button id="lc-go" class="btn btn-primary" type="submit" disabled>Check my label</button></p>
<p class="hint">Photos are resized in your browser and sent to Anthropic’s Claude model to read the text. We do not store them. See <a href="#how-photos-are-handled">how photos are handled</a>.</p>
</form>
<div id="lc-busy" class="lc-busy" hidden><span class="lc-spin" aria-hidden="true"></span><p><b>Reading your label…</b><br>This usually takes 15 to 40 seconds.</p></div>
<div id="lc-error" class="lc-error" role="alert" hidden></div>
<section id="lc-summary" class="lc-result" hidden aria-live="polite"></section>
<form id="lc-gate" name="label-check" method="POST" action="/thank-you/" data-netlify="true" netlify-honeypot="website" class="lc-gate" hidden>
<input type="hidden" name="form-name" value="label-check">
<p style="display:none"><label>Leave blank <input name="website"></label></p>
<input type="hidden" name="summary">
<input type="hidden" name="read_from_label">
<input type="hidden" name="answers">
<h2>Get the full report</h2>
<p>Each finding with what we read, the rule it comes from, and the change to make. Shown here and sent to your inbox.</p>
<label for="lc-email">Email</label><input id="lc-email" name="email" type="email" required autocomplete="email">
<label for="lc-name">Name (optional)</label><input id="lc-name" name="name" autocomplete="name">
<label for="lc-company">Company (optional)</label><input id="lc-company" name="company" autocomplete="organization">
<label for="lc-product">Product (optional)</label><input id="lc-product" name="product" placeholder="e.g. Acme Hub 2">
<label class="lc-inline"><input type="checkbox" name="updates" value="yes"> Send me occasional updates on Canadian and US labelling and certification rules. You can unsubscribe at any time.</label>
<p><button class="btn btn-primary" type="submit">Show my full report</button></p>
<p class="hint">We use your email to send the report and may follow up once about it. Handled under Canada’s PIPEDA; see the <a href="/privacy/">privacy policy</a>.</p>
</form>
<section id="lc-report" class="lc-result" hidden></section>
</div>

## What the checker looks at

| | Canada | United States |
|---|---|---|
| Radio certification number | “IC:” prefix; company number and product number format; “Contains IC:” on host products (RSS-Gen 9.4.4.1, 9.4.4.2) | “FCC ID” in capitals on one line; grantee and product code; “Contains FCC ID:” on hosts (47 CFR 2.925, 2.926, 15.212) |
| Model identifiers | HVIN present, no wildcards; PMN on the label, packaging or literature (9.4.4.1) | Unique identification for SDoC equipment (2.1074) |
| Digital emissions | Bilingual CAN ICES-003(*)/NMB-003(*) marking with class letter (ICES-Gen 6.3.3) | Part 15 compliance statement, both conditions (15.19) |
| QR codes and e-labels | QR code must hold the label content itself, not a link (9.4.2); e-labels under Annex B | E-label conditions (2.935) |
| Small devices | Label in the manual and on the packaging at 2.5 cm or less (9.4.3.2; ICES-Gen 6.3.2.2) | Manual plus packaging or removable label below 4-point type (2.925(f), 15.19(a)(5)) |
| Manual and literature | Licence-exempt notice in English and French (9.3.2.1); bilingual notices (9.3.1) | 15.21 modification warning; 15.105 Class A/B statement; SDoC compliance information with a US responsible party (2.1077) |

Items a photo can show, it scores. Items a photo cannot show, such as the French manual or the durability of a sticker, it lists for you to confirm, so you finish with a complete list rather than a partial one.

## What it does not do

It reads what is printed and compares it with the published labelling rules. It does not decide which RSS standards or FCC rule parts apply to your product, test anything, look up your Radio Equipment List or FCC grant, or check consumer-packaging, Quebec French-language, safety or customs marking rules. Automated reading can misread a character, so the summary shows exactly what was read from your photo; check it before relying on a result. A clean result is not a certification. For a lawyer’s review of the label artwork, manual and packaging before you print, see the [label and manual review](/label-and-manual-review/) (US$249 per IC certification number).

## How photos are handled {#how-photos-are-handled}

Your photos are resized in your browser and sent to Anthropic’s Claude model, which transcribes the text on the label. Anthropic processes them as our service provider, under its commercial terms. We do not store the photos. We keep what the reader transcribed and your answers only if you ask for the full report, as part of that request. If the product is unreleased and you would rather not upload it, email the artwork to [info@isedrepresentative.com](mailto:info@isedrepresentative.com) instead.

<!--faq-->
### Is the label checker free?

Yes. The summary appears straight away. The full report is shown, and emailed to you, when you give an email address. There is a limit of a few checks per person per day.

### Which rules does it check my label against?

For Canada, the labelling sections of RSS-Gen Issue 6 (as amended September 15, 2026) and ICES-Gen Issue 2. For the United States, 47 CFR 2.925, 2.926, 2.935, 2.1074, 2.1077, 15.19, 15.21, 15.105 and 15.212, as published on eCFR. The rules were last reviewed in October 2026.

### Does a clean result mean my product complies?

No. It means the items the checker can see are in the form the rules ask for. It does not test the product or confirm which standards apply, and your certification body has the final word on the label for a specific device.

### Can it read a QR code on my label?

On most phones and in Chrome and Edge, the checker decodes the QR code in your browser. If it decodes to a web address, it tells you that a link does not satisfy RSS-Gen section 9.4.2, which requires the code to contain the label content itself.

### What photo works best?

A sharp photo taken straight on, in even light, with the whole label in frame. If the identifiers are on a small nameplate, move closer rather than zooming. Add a photo of the packaging if the product name or small-device label is printed there.

### Will you see my photos?

No. The photos are sent to Anthropic’s Claude model to be read, and are not stored by us. If you ask for the full report, we receive the text that was read from the label, your answers and your contact details.
<!--/faq-->

<div class="source" markdown="1">
**Sources.** [RSS-Gen, Issue 6](https://ised-isde.canada.ca/site/spectrum-management-telecommunications/en/devices-and-equipment/radio-equipment-standards/radio-standards-specifications-rss/rss-gen-general-requirements-compliance-radio-apparatus) (July 30, 2026; Amendment 1, September 15, 2026), sections 9.1 to 9.4 and Annex B. [ICES-Gen, Issue 2](https://ised-isde.canada.ca/site/spectrum-management-telecommunications/en/devices-and-equipment/interference-causing-equipment-standards-ices/ices-gen-general-requirements-compliance-interference-causing-equipment) (February 23, 2024), sections 6.3.2 and 6.3.3. 47 CFR [2.925](https://www.ecfr.gov/current/title-47/section-2.925), [2.926](https://www.ecfr.gov/current/title-47/section-2.926), [2.935](https://www.ecfr.gov/current/title-47/section-2.935), [2.1074](https://www.ecfr.gov/current/title-47/section-2.1074), [2.1077](https://www.ecfr.gov/current/title-47/section-2.1077), [15.19](https://www.ecfr.gov/current/title-47/section-15.19), [15.21](https://www.ecfr.gov/current/title-47/section-15.21), [15.105](https://www.ecfr.gov/current/title-47/section-15.105) and [15.212](https://www.ecfr.gov/current/title-47/section-15.212). Reviewed October 2026.
</div>

Related: [Canadian radio labelling requirements](/guides/canadian-radio-equipment-labelling-requirements/) · [Nine checks before you print](/guides/label-and-manual-self-check/) · [CAN ICES-003(B)/NMB-003(B) explained](/guides/can-ices-003-b-nmb-003-b-label/) · [From FCC to ISED](/guides/fcc-to-ised/)

<script src="/label-checker.js" defer></script>
