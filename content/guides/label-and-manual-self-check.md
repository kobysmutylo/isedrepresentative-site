---
title: ISED Label and Manual Self-Check: Nine Checks Before You Print
description: Nine checks to run on your label artwork, bilingual user manual and packaging before the print order goes out, each tied to the RSS-Gen or ICES-Gen section it comes from.
h1: Nine checks before you print
short: Label self-check
type: guide
date: 2026-10-01
updated: 2026-10-06
order: 18
cta: review
---

<div class="answer" markdown="1">
Here are nine things to check before your Canadian label artwork, user manual and packaging go to print. Five are on the label: the IC number's format, the identifiers matching your Radio Equipment List entry, the "Contains IC:" marking for a module inside a host, the QR code and e-label rules, and the bilingual ICES marking. Three are on the manual: English and French notices, Canadian RF exposure text, and module integration instructions. One is on the packaging. Each check names its section in [RSS-Gen Issue 6](https://ised-isde.canada.ca/site/spectrum-management-telecommunications/en/devices-and-equipment/radio-equipment-standards/radio-standards-specifications-rss/rss-gen-general-requirements-compliance-radio-apparatus) or [ICES-Gen Issue 2](https://ised-isde.canada.ca/site/spectrum-management-telecommunications/en/devices-and-equipment/interference-causing-equipment-standards-ices/ices-gen-general-requirements-compliance-interference-causing-equipment), so you can take any of them to your certification body. Your certification body approves the label. This is simply the list of things that are usually wrong when it does not.
</div>

## Why do this now

You have until July 30, 2027. Until then ISED accepts applications under RSS-Gen Issue 5 or Issue 6, so most people have diarised that date and moved on.

It is the wrong date to watch. Your next print run is the one that actually costs you money. Find a label error before you order the cartons and you lose an afternoon — find it afterwards and you lose the cartons.

One note on editions first. If your test report is dated after September 15, 2026, it should cite Issue 6 as amended. Amendment 1 opened 101.4 kHz for buried-cable locating equipment and did nothing else, so for most products it changes the edition line and very little besides. We wrote it up in [Amendment 1 and the amended lab checklist](/updates/rss-gen-issue-6-amendment-1-lab-checklist/).

## The label

**1. Check the IC number's format.** Section 9.4.4.1 gives it as IC: XXXXX-YYYYYYYYYYY. First your [company number](/guides/ised-company-number/) from ISED, then a hyphen, then the product number you chose, up to eleven characters. Digits and capital letters only — "IC:" identifies the number but is not part of it. Three things go wrong: the "IC:" is missing, somebody has used a lower-case letter, or a character went astray when the number came off the test report. The last one is probably the most common, and it is the hardest to see on your own artwork.

**2. Check every identifier against the REL, not against your own file.** The certification number, the HVIN and the PMN on your product have to match the [Radio Equipment List entry](/guides/ised-certification-number-lookup-rel/) character for character. Wildcards are not allowed. An HVIN like "47XP-820K/A21XX", where XX stands for variants you will name later, fails — the same string is fine if it identifies exactly one version. Open the REL to do this check, because the REL is what an auditor will open.

**3. If there is a certified module inside, say so on the host.** Section 9.4.4.2 gives you two ways. Either the module's own certification number stays visible while the module is installed, or the host carries that number after the word "Contains", "Contient" or "Contains/Contient" — "Contains IC: 20001-WILAN3". In a sealed product only the second one actually works. Your host marketing name goes on the host label, the packaging or the literature.

**4. If you are using a QR code or an e-label, check it against that route's own rule.** Issue 6 lets a QR code be the label. It has to hold the label information itself, not a link to a page that holds it. An ordinary phone app has to read it. It has to be permanently affixed, and your manual has to explain it. Most of the ones I see point at a website, which does not qualify — arguably the single easiest item here to get wrong, because a link is what a QR code usually means everywhere else. The e-label route now sits in Annex B, and the annex is normative — so there is finally one place that tells you what counts. You need a display. Without a screen, e-labelling is open to you in only narrow cases, so read the annex before you design around it.

**5. Check that the ICES marking is bilingual and carries the right class letter.** ICES-Gen section 6.3.3 sets the pattern CAN ICES (*) / NMB (*). The class letter goes in where the applicable standard separates classes, which gives you the familiar CAN ICES-003(B) / NMB-003(B) for digital apparatus. Two things go wrong. The French half is missing altogether — or the letter on the artwork is the one from your last product rather than the one in this report, which is exactly the kind of error that survives a careful proofread. If your product has digital circuitry as well as a radio it needs both markings, and a combined label has to satisfy both standards.

## The user manual

**6. Check that every required notice is in English and in French.** Section 9.3.1 asks for the notices and information to the user in both languages. The manual also has to stay available for as long as you sell the product in Canada — in the box, or online. This is genuinely the most common thing I find on a first Canadian filing, and probably the most expensive one to leave late, because a translated manual is a new print file rather than an edit. You need the French whether or not you expect a French-speaking buyer.

**7. Check that the RF exposure text is the Canadian one.** If an RSS-102 evaluation applies to your product, your manual needs the exposure information that goes with it. Your FCC wording will not substitute. A manual that carries only the FCC text has a plain gap in it, not an arguable one. In my experience this is the item that most often survives an otherwise careful adaptation of a US file.

**8. If you hold a module certification, check that your integration instructions have gone out.** Section 9.2 puts this on you as the module certificate holder. Your host manufacturer needs what it takes to keep the finished product compliant in the use and configuration you intend. Write it once, send it to every host customer. If you are on the other side of this and building a host around somebody else's module, ask your supplier for that document now rather than during the certification.

## The packaging

**9. If you are relying on the small-device relief, check the carton as well as the manual.** Measure the device first, because 2.5 cm is a measurement and not a judgment call. At 2.5 cm or under, ICES-Gen section 6.3.2.2 lets the marking go in the user manual with no approval from ISED, and it then has to appear on your packaging as well. Both places. The same size test governs the ISED label: over 2.5 cm you need the Certification and Engineering Bureau to approve moving it off the device, and they will consider that only where e-labelling cannot be used. So "it is a small device" is not an answer by itself — measure it. Then look at the carton. This is the easy half to forget, because a different team usually draws it, on a different schedule from the manual.

## What it costs you to get one wrong

A label error does not take your product off the Radio Equipment List. Section 3.4.1 says that no person shall manufacture, import, distribute, lease, offer for sale or sell Category I radio apparatus in Canada unless it is listed, and ICES-Gen section 3.4 does the same for interference-causing equipment. But labelling is its own requirement under section 9. So a label that does not comply gives you a product that does not comply, whatever your test report says.

In practice your certification body tells you first. Or it surfaces through an [audit sample](/guides/ised-audit-samples-who-provides-who-pays/), which you supply at your own expense when ISED or your certification body asks. Either way you hear about it long before ISED does anything about it. So one of these nine going wrong costs you a reprint, a late shipment and an awkward call. The regulator is rarely the expensive part — the cartons are. For the rarer cases, see [non-compliance](/guides/ised-non-compliance-penalties/).

Two of the nine account for most of what I see: the bilingual manual at item 6, and the half-taken small-device relief at item 9. Both are cheap to fix on a file and expensive to fix on a pallet.

If you want the requirements in full rather than this list, they are in [labelling radio equipment for Canada under RSS-Gen Issue 6](/guides/canadian-radio-equipment-labelling-requirements/). Who has to be appointed in Canada, and for how long, is a separate question — that one is [RSP-100 section 4.1](/guides/canadian-representative-requirement-rsp-100/). If the applicant’s address is outside Canada, that appointment is one we hold: US$499 per certified product, paid once, in place for as long as the product is offered on the Canadian market. No renewal, no second invoice. [What we charge](/pricing/) sets out that fee and the review fee together.

<!--faq-->

### Does a labelling error remove my product from the Radio Equipment List?

No. A label error does not delist a product on its own. But labelling is a requirement under RSS-Gen section 9, so a label that does not comply gives you a product that does not comply, and section 3.4.1 bars anyone from manufacturing, importing, distributing, leasing, offering for sale or selling Category I radio apparatus that is not listed. In practice it costs you a reprint and a delay, and you will usually hear about it from a certification body or an audit sample rather than from ISED.

### Do I have to translate my whole user manual into French?

Section 9.3.1 asks for the notices and information to the user in both English and French. That is narrower than translating every page, and broader than most first-time exporters expect. It is the most common finding on a first Canadian filing.

### Can my QR code link to a page with the label information?

No. If a QR code is your label under RSS-Gen Issue 6, it has to hold the label information itself, read with a generic QR app, stay permanently affixed to the product, and be explained in your manual. A code that resolves to a URL does not qualify.

### My device is smaller than 2.5 cm. Where does the marking go?

In the user manual and on the packaging. ICES-Gen section 6.3.2.2 lets equipment 2.5 cm or smaller in its largest dimension carry the marking in the manual with no approval from ISED, and it then has to appear on the packaging too. Both places, not one. Over 2.5 cm, you need the Certification and Engineering Bureau to approve moving the ISED label off the device, and they will consider it only where e-labelling cannot be used.

### Can I use my FCC exposure wording in the Canadian manual?

Not instead of the Canadian text. Where an RSS-102 evaluation applies, your manual needs the Canadian RF exposure information that goes with it. FCC wording on its own leaves a gap.

### When do I have to move to Issue 6?

ISED accepts applications under Issue 5 or Issue 6 until July 30, 2027. The decision that reaches you sooner is which issue your current artwork and test plans cite, because a printed label costs more to change than a file does. If your report is dated after September 15, 2026, it should cite Issue 6 as amended by Amendment 1.

<!--/faq-->

**Sources.** [RSS-Gen, Issue 6](https://ised-isde.canada.ca/site/spectrum-management-telecommunications/en/devices-and-equipment/radio-equipment-standards/radio-standards-specifications-rss/rss-gen-general-requirements-compliance-radio-apparatus) (July 30, 2026; Amendment 1, September 15, 2026), sections 3.4.1, 9.2, 9.3.1, 9.4.4.1, 9.4.4.2 and Annex B. [ICES-Gen, Issue 2](https://ised-isde.canada.ca/site/spectrum-management-telecommunications/en/devices-and-equipment/interference-causing-equipment-standards-ices/ices-gen-general-requirements-compliance-interference-causing-equipment) (February 23, 2024), sections 3.4, 6.3.2.2 and 6.3.3. ISED, RSP-100, Issue 12, sections 4.1 and 12.2. Reviewed October 2026.
