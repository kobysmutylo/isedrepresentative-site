---
title: Canadian Radio Device Labelling Requirements: RSS-Gen Issue 6
description: What must be on the label of a radio device sold in Canada under RSS-Gen Issue 6: IC number, HVIN, PMN, module labels, QR codes, e-labels and bilingual manuals.
h1: Labelling radio equipment for Canada under RSS-Gen Issue 6
short: Canadian labelling requirements
type: guide
date: 2026-09-24
updated: 2026-09-24
order: 18
---

<div class="answer" markdown="1">
Every unit of a certified radio product sold in Canada must carry a label with its ISED certification number, preceded by "IC:", and its hardware version identification number (HVIN). The product marketing name (PMN) goes on the label, the packaging or the product literature, and all three must match the product's entry in the Radio Equipment List. The label must be permanently affixed and legible, or shown electronically where the device qualifies. A product built around a certified module shows the module's number as "Contains IC:". User-manual notices must be in English and French. The rules are in section 9 and Annex B of [RSS-Gen Issue 6](https://ised-isde.canada.ca/site/spectrum-management-telecommunications/en/devices-and-equipment/radio-equipment-standards/radio-standards-specifications-rss/rss-gen-general-requirements-compliance-radio-apparatus) (July 30, 2026, Amendment 1 of September 15, 2026).
</div>

## What the label must show

Section 9.4.4.1 applies to every unit of a certified model, including a module granted modular or limited modular approval. The label must include:

- **The ISED certification number, preceded by "IC:".** The format is IC: XXXXX-YYYYYYYYYYY. The first block is the [company number](/guides/ised-company-number/) ISED assigned to the certificate holder — five digits for new companies, while older company numbers may be shorter and end in a letter, such as "21A". The second block is the unique product number the applicant chose, up to eleven characters. Only digits and capital letters A–Z are allowed in either block. "IC:" identifies the number but is not part of it.
- **The HVIN**, with or without a prefix such as "HVIN:", "Model#", "M/N:" or "P/N:".

The PMN may be on the label, or on the packaging or in the product literature instead, provided that literature ships with the product or is readily available online. Where the firmware version (FVIN) is the only thing that differs between versions in a family certification, the FVIN must be displayed or stored electronically on the product and be easy to retrieve.

Two rules catch manufacturers who have worked from their FCC files. First, the PMN, HVIN and certification number on the product must match the REL listing exactly; check them with an [IC number lookup](/guides/ised-certification-number-lookup-rel/) before artwork is finalised. Second, none of the identifiers may use wildcard characters. An HVIN such as "47XP-820K/A21XX", where the XX stands for variants the manufacturer decides later, is not permitted. The same string is acceptable only if it identifies a single product version.

## Products built around a certified module

Section 9.4.4.2 governs host equipment. The host marketing name (HMN) must appear on the host's label, packaging or product literature. For each module inside, either the module's own certification number must be visible at all times when the module is installed, or the host must be labelled with the module's number preceded by "Contains", "Contient" or "Contains/Contient" — for example, "Contains IC: 20001-WILAN3". In a sealed product the second option is usually the only practical one.

Section 9.2 puts an obligation on the module side too: the module's certificate holder must give host manufacturers integration instructions, including a host label or a description of the host labelling requirements. If you are integrating a module, ask for that document before you design the enclosure.

## Where the label goes

**On the device.** The default under section 9.4.1 is a label permanently affixed to each unit, with indelible and clearly legible text.

**As a QR code.** Under section 9.4.2 the label may be a QR code, but only if all four conditions are met: the code itself contains the full required label content, not a link to a website; it is on the product, not shown electronically; generic QR apps can read it; and the user manual tells the user the code is there. A QR code that resolves to a web page does not satisfy the section.

**In the manual and on the packaging.** For equipment whose largest dimension is 2.5 cm or less, section 9.4.3.2 allows the label to go in the user manual instead of on the device, without prior approval, provided it also appears on the packaging. For multi-unit products, such as earbuds with a charging case, the label goes on any unit larger than 2.5 cm that is needed in at least one mode of operation. Equipment larger than 2.5 cm may move the label off the device only with approval from ISED's Certification and Engineering Bureau, and only if e-labelling is not an option; the request goes to the Bureau with the make, model, external photographs and the reason a label on the unit is impractical, and any approval conditions must be followed. Where RSS-Gen requires information on packaging, section 9.1 requires it on the exterior, not provided electronically.

**Electronically.** Annex B allows an e-label on a device with an integrated display. A device without a screen may use an e-label in only two ways: a bilingual audio message from the device, or display (or audio) on external equipment connected by cable, Bluetooth, Wi-Fi or similar, if that connection is mandatory to use the device. Users must be told how to reach the e-label, in the manual, on the packaging or on a product website. Where a host displays a module's number electronically, the module must either authenticate itself to the host through a secure exchange, or the host manufacturer must factory-encode the module's number in a way third parties cannot modify.

## What the user manual must contain

Section 9.3.1 requires the manual to include every notice and item of user information required by the applicable RSS standards, **in both English and French**. If the manual does not ship in the box, it must be available free of charge, for example on the manufacturer's website, for as long as the equipment is made, imported, distributed, leased, offered for sale or sold in Canada, and each unit must come with instructions for finding it. ISED recommends the manual name the HVIN or PMN so it can be tied to the model. For host equipment, the manual must carry the notices for every integrated module.

For licence-exempt radios — Wi-Fi, Bluetooth and similar — section 9.3.2.1 requires this notice, or an equivalent, in the manual, on the device or both, in English and in French:

> This device contains licence-exempt transmitter(s)/receiver(s) that comply with Innovation, Science and Economic Development Canada's licence-exempt RSS(s). Operation is subject to the following two conditions: This device may not cause interference. This device must accept any interference, including interference that can cause undesired operation of the device.

Licence-exempt transmitters with detachable antennas need a second notice under section 9.3.2.2, listing the approved antenna types and their maximum gain. RF exposure information comes from RSS-102 rather than RSS-Gen; the test laboratory will specify what your device needs.

## Other Canadian labels on the same product

The IC number covers the radio. The digital circuitry is declared separately under ICES-003, with the marking explained in our guide to [CAN ICES-003(B)/NMB-003(B)](/guides/can-ices-003-b-nmb-003-b-label/); a combined label needs to satisfy both RSS-Gen and ICES-Gen. The FCC ID and FCC statements do not satisfy either Canadian requirement — see [from FCC to ISED](/guides/fcc-to-ised/). Consumer-packaging and Quebec French-language rules are separate again and outside ISED's standards.

## Before you print

Confirm the company number and product number, and that the HVIN and PMN match the REL. If the product uses a module, get the module maker's host-labelling instructions and decide whether "Contains IC:" goes on the enclosure. Decide between a physical label, a QR code or an e-label against the conditions above, and ask the Certification and Engineering Bureau early if you need to move the label off a device larger than 2.5 cm. Put the manual notices in English and French, and keep the manual online for the product's whole Canadian sales life. What changed from Issue 5 is covered in our [update on RSS-Gen Issue 6 labelling](/updates/rss-gen-issue-6-labelling-qr-codes/); files under Issue 5 remain acceptable during the one-year transition. Your certification body has the final word on the label for a specific device, and a label that does not match the certification is one of the gaps described in [the consequences of non-compliance](/guides/ised-non-compliance-penalties/).

<div class="source" markdown="1">
**Sources.** [RSS-Gen, Issue 6](https://ised-isde.canada.ca/site/spectrum-management-telecommunications/en/devices-and-equipment/radio-equipment-standards/radio-standards-specifications-rss/rss-gen-general-requirements-compliance-radio-apparatus) (July 30, 2026; Amendment 1, September 15, 2026), sections 9.1, 9.2, 9.3.1, 9.3.2, 9.4.1 to 9.4.4 and Annex B. Reviewed September 2026.
</div>

<!--faq-->
### What must be on the label of a radio device sold in Canada?

The ISED certification number, preceded by "IC:", and the hardware version identification number (HVIN). The product marketing name (PMN) can be on the label, the packaging or the product literature. All three must match the Radio Equipment List.

### What is the format of an ISED certification number?

IC: XXXXX-YYYYYYYYYYY. The first block is the company number ISED assigns, five digits for new companies; the second is the applicant's product number, up to eleven characters. Only digits and capital letters are allowed, and wildcard characters are not permitted.

### How do I label a product that uses a certified module?

Label the host with the module's number preceded by "Contains", "Contient" or "Contains/Contient", for example "Contains IC: 20001-WILAN3", unless the module's own label stays visible when installed. The host marketing name must appear on the label, packaging or literature.

### Can I use a QR code as the ISED label?

Yes, under RSS-Gen Issue 6, if the QR code contains the full label content itself rather than a link, is on the product, can be read by generic QR apps, and the user manual points to it.

### Can the label go in the user manual instead of on the device?

Without approval, only if the device's largest dimension is 2.5 cm or less, and the label must then also be on the packaging. Larger devices need approval from ISED's Certification and Engineering Bureau, which is considered only where e-labelling cannot be used.

### Can a device without a screen use an e-label?

Only through a bilingual audio message, or through external equipment whose connection is mandatory to use the device. Otherwise, use a physical label or a QR code on the product.

### Does the user manual have to be in French?

The notices and user information required by the RSS standards must be in both English and French. The manual can be provided online if it stays freely available for as long as the product is sold in Canada.
<!--/faq-->

Related: [RSS-Gen Issue 6 labelling changes](/updates/rss-gen-issue-6-labelling-qr-codes/) · [IC ID lookup in the REL](/guides/ised-certification-number-lookup-rel/) · [The Canadian Representative service](/canadian-representative-service/).
