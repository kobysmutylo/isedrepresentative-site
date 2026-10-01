---
title: ISED Label and Manual Self-Check: Nine Checks Before You Print
description: Nine checks to run on your label artwork, bilingual user manual and packaging before the print order goes out, each tied to the RSS-Gen or ICES-Gen section it comes from.
h1: Nine checks before you print
short: Label self-check
type: guide
date: 2026-10-01
updated: 2026-10-01
order: 18
cta: review
---

<div class="answer" markdown="1">
Run these nine checks on your label artwork, your user manual and your packaging before the print order goes out. Five are on the label: the IC number format, the identifiers matching your Radio Equipment List entry with no wildcards, the "Contains IC:" marking where a module sits inside a host, the QR-code and electronic-label routes, and the bilingual ICES marking. Nothing here needs a lawyer; it needs twenty minutes and the file. Three are on the manual: English and French notices, Canadian RF exposure information, and module integration instructions. One is on the packaging. Each names its section in [RSS-Gen Issue 6](https://ised-isde.canada.ca/site/spectrum-management-telecommunications/en/devices-and-equipment/radio-equipment-standards/radio-standards-specifications-rss/rss-gen-general-requirements-compliance-radio-apparatus) (July 30, 2026, Amendment 1 of September 15, 2026) or [ICES-Gen Issue 2](https://ised-isde.canada.ca/site/spectrum-management-telecommunications/en/devices-and-equipment/interference-causing-equipment-standards-ices/ices-gen-general-requirements-compliance-interference-causing-equipment), so you can take any item straight to your certification body. The certification body approves the label; this is the list of things that tend to be wrong when it does not.
</div>

## Why run it now rather than in July

Certification applications are accepted under RSS-Gen Issue 5 or Issue 6 until July 30, 2027. That is the date most people have diarised, and it is the wrong one to worry about. The date that costs money is whenever your next print run is scheduled. A label error found before the cartons are ordered costs an afternoon; the same error found after they arrive costs the print run.

One edition note before the list. If your test report is dated after September 15, 2026, it should cite Issue 6 as amended — see [Amendment 1 and the amended lab checklist](/updates/rss-gen-issue-6-amendment-1-lab-checklist/). Amendment 1 itself only opens 101.4 kHz for buried-cable locating equipment, so for most products it changes the edition line and nothing else.

## The label

**1. The IC number is in the right form.** Section 9.4.4.1 gives it as IC: XXXXX-YYYYYYYYYYY — the [company number](/guides/ised-company-number/) ISED assigned you, a hyphen, then the unique product number you chose, up to eleven characters. Only digits and capital letters are allowed in either block. "IC:" identifies the number and is not part of it. The errors worth looking for are a missing "IC:" prefix, a lower-case letter, and a character dropped when the number was transcribed from the test report.

**2. Every identifier matches the REL entry exactly, and none of them contains a wildcard.** The certification number, the HVIN and the PMN on the product have to match the product's [Radio Equipment List entry](/guides/ised-certification-number-lookup-rel/) character for character. Wildcards are not permitted: an HVIN like "47XP-820K/A21XX", where the XX stands for variants you will decide later, fails — the same string is fine only where it identifies one version. Check this against the REL rather than against your own file, because the REL is what an auditor will open.

**3. A host containing a certified module says so.** Under section 9.4.4.2, either the module's certification number is visible whenever the module is installed, or the host carries it preceded by "Contains", "Contient" or "Contains/Contient" — "Contains IC: 20001-WILAN3". In a sealed product the second is usually the only option that works. The host marketing name (HMN) goes on the host's label, packaging or literature.

**4. If you use a QR code or an electronic label, it meets that route's own rule.** Issue 6 lets a QR code be the label, provided it carries the label information itself rather than pointing at a page that holds it, reads with an ordinary phone app rather than a proprietary one, is permanently affixed, and is explained in the user manual. A code resolving to your website is the usual way this fails. Electronic labelling now sits in Annex B, which is normative — that is the useful part of the change, since there is finally one place that says what counts. The e-label route needs a display; without a screen it is open to you only in narrow circumstances, so check the annex before designing around it.

**5. The ICES marking is bilingual and the class letter is the one that was assessed.** ICES-Gen section 6.3.3 sets the pattern CAN ICES (*) / NMB (*), with the class letter where the applicable standard distinguishes classes — CAN ICES-003(B) / NMB-003(B) is the familiar form for digital apparatus. Two things go wrong here: the French half is missing altogether, or the letter on the artwork is the letter from the last product you shipped rather than the letter in this report. If the product has digital circuitry as well as a radio, it needs both markings, and a combined label has to satisfy both standards.

## The user manual

**6. Every required notice appears in English and in French.** Section 9.3.1 requires the notices and information to the user in both languages, and the manual has to stay available — shipped with the product or readily available online — for as long as the product is sold in Canada. This is the most common finding I see on a first Canadian filing, and probably the most expensive to fix late: a translated manual is a new print file, not an edit. The French is required whether or not you expect a French-speaking buyer.

**7. The RF exposure information is the Canadian text.** Where an RSS-102 evaluation applies, the manual needs the exposure information that goes with it. FCC exposure wording is not a substitute for it, and a manual carrying only the FCC text is a plain gap rather than an arguable one. This is the item that most often survives an otherwise careful adaptation of a US file.

**8. If you hold a module certification, your integration instructions have gone out.** Section 9.2 puts that on the module certificate holder: the host manufacturer gets what it needs to keep the finished product compliant in its intended use and configuration. Write it once and send it to every host customer. If you are on the other side of that — building a host around somebody else's module — this is the document to ask your supplier for, and the request is better made now than during the certification.

## The packaging

**9. Where you are relying on the small-device relief, the packaging carries the marking too.** The threshold is 2.5 cm, and it is not a soft one. Under ICES-Gen section 6.3.2.2, equipment 2.5 cm or smaller in its largest dimension may carry the marking in the user manual without prior ISED approval, **and it must then also appear on the packaging**. The same size test governs moving the ISED label off the device: above 2.5 cm you need approval from the Certification and Engineering Bureau, and that is considered only where e-labelling cannot be used. So "it is a small device" is not on its own an answer — measure it. Then check the carton, because taking the relief for the manual and forgetting the packaging is the half-done version of this, and it happens easily: the carton is usually drawn by a different team on a different schedule from the manual.

## What a failure actually costs

This is worth stating exactly, because it is usually described wrongly in both directions.

A labelling error does not by itself take a product off the Radio Equipment List. What section 3.4.1 says is that no person shall manufacture, import, distribute, lease, offer for sale or sell Category I radio apparatus in Canada unless it is listed, and ICES-Gen section 3.4 sets an equivalent bar for interference-causing equipment. Labelling sits in section 9 as a compliance requirement in its own right, so a non-compliant label makes a non-compliant product whatever the test report says.

In practice the finding reaches you from your certification body, or through an [audit sample](/guides/ised-audit-samples-who-provides-who-pays/) — the certificate holder provides those at its own expense on request — well before it reaches you from ISED. So the realistic cost of items 1 to 9 going wrong is a reprint, a delayed shipment and a conversation with your certification body. The regulator is rarely the expensive part. The cartons are. What happens in the rarer cases is set out in [non-compliance](/guides/ised-non-compliance-penalties/).

Two of the nine account for most of what I see: the bilingual manual at item 6, and the half-taken small-device relief at item 9. Both are cheap on a file and expensive on a pallet.

For the requirements in full rather than the checklist, see [labelling radio equipment for Canada under RSS-Gen Issue 6](/guides/canadian-radio-equipment-labelling-requirements/). The separate question of who must be appointed in Canada, and for how long, is [RSP-100 section 4.1](/guides/canadian-representative-requirement-rsp-100/).

<!--faq-->

### Does a labelling error remove my product from the Radio Equipment List?

No. A label error does not of itself delist a product. Labelling is a compliance requirement under RSS-Gen section 9, so a non-compliant label makes a non-compliant product, and section 3.4.1 bars manufacturing, importing, distributing, leasing, offering for sale or selling Category I radio apparatus that is not listed. The practical consequence is usually a reprint and a delay, raised by a certification body or an audit sample rather than by ISED directly.

### Do I have to translate the whole user manual into French?

Section 9.3.1 requires the notices and information to the user to appear in both English and French. That is narrower than translating every page of a product manual and broader than most first-time exporters expect. It is the most common finding on a first Canadian filing.

### Can the QR code on my label link to a page with the label information?

No. Where a QR code serves as the label under RSS-Gen Issue 6, it must carry the label information itself, read with a generic QR app, be permanently affixed to the product, and be explained in the user manual. A code that resolves to a URL does not meet that.

### My device is smaller than 2.5 cm. Where does the marking go?

Under ICES-Gen section 6.3.2.2, equipment 2.5 cm or smaller in its largest dimension may carry the marking in the user manual without prior ISED approval, and it must then also appear on the packaging. Both places, not one. Above 2.5 cm, moving the ISED label off the device needs approval from the Certification and Engineering Bureau, and that is considered only where e-labelling cannot be used.

### Can I use my FCC exposure wording in the Canadian manual?

Not as a substitute. Where an RSS-102 evaluation applies to the product, the manual needs the Canadian RF exposure information that goes with it. FCC text alone leaves a gap.

### When do I have to be on Issue 6?

Certification applications are accepted under either Issue 5 or Issue 6 until July 30, 2027. The decision that arrives sooner is which issue your current artwork and test plans cite, since changing a printed label costs more than changing a file. If your report is dated after September 15, 2026, it should cite Issue 6 as amended by Amendment 1.

<!--/faq-->

**Sources.** [RSS-Gen, Issue 6](https://ised-isde.canada.ca/site/spectrum-management-telecommunications/en/devices-and-equipment/radio-equipment-standards/radio-standards-specifications-rss/rss-gen-general-requirements-compliance-radio-apparatus) (July 30, 2026; Amendment 1, September 15, 2026), sections 3.4.1, 9.2, 9.3.1, 9.4.4.1, 9.4.4.2 and Annex B. [ICES-Gen, Issue 2](https://ised-isde.canada.ca/site/spectrum-management-telecommunications/en/devices-and-equipment/interference-causing-equipment-standards-ices/ices-gen-general-requirements-compliance-interference-causing-equipment) (February 23, 2024), sections 3.4, 6.3.2.2 and 6.3.3. ISED, RSP-100, Issue 12, sections 4.1 and 12.2. Reviewed October 2026.
