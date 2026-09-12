---
title: RSS-247 Explained: Certifying Wi-Fi and Bluetooth Devices in Canada
description: RSS-247 is ISED's standard for licence-exempt Wi-Fi, Bluetooth and similar radios at 902 MHz, 2.4 GHz and 5 GHz. What Issue 4 changed and what foreign makers must do.
h1: RSS-247: what it covers, what Issue 4 changed, and what you have to do
short: RSS-247 explained
type: guide
date: 2026-09-10
updated: 2026-09-10
order: 17
---

<div class="answer" markdown="1">
RSS-247 is the Radio Standards Specification that Innovation, Science and Economic Development Canada applies to digital transmission systems, frequency-hopping systems and licence-exempt local area network devices in the 902&ndash;928 MHz, 2400&ndash;2483.5 MHz, 5150&ndash;5350 MHz and 5470&ndash;5895 MHz bands. In plain terms: Wi-Fi 4/5/6, Bluetooth, Zigbee, LoRa in the 915 MHz band, and most short-range consumer radios. Equipment under RSS-247 is Category I, which means it must be certified &mdash; a recognised certification body reviews the test report and issues an IC certification number &mdash; and an applicant with no address in Canada must appoint a [Canadian Representative](/canadian-representative-service/) under RSP-100 section 4.1 before the certificate is issued. The current version is Issue 4, published July 24, 2025; after the six-month transition ended on January 24, 2026, new applications must be assessed against Issue 4. Wi-Fi 6E and Wi-Fi 7 radios in the 5925&ndash;7125 MHz band are covered by a different standard, RSS-248.
</div>

## What RSS-247 actually is

ISED regulates radio equipment through a family of Radio Standards Specifications. [RSS-Gen](https://ised-isde.canada.ca/site/spectrum-management-telecommunications/en/devices-and-equipment/radio-equipment-standards/radio-standards-specifications-rss/rss-gen-general-requirements-compliance-radio-apparatus) sets the requirements common to every radio &mdash; labelling, user notices, the Radio Equipment List rule &mdash; and a specific RSS sets the technical limits for each category of device. [RSS-247](https://ised-isde.canada.ca/site/spectrum-management-telecommunications/en/devices-and-equipment/radio-equipment-standards/radio-standards-specifications-rss/rss-247-digital-transmission-systems-dtss-frequency-hopping-systems-fhss-and-licence-exempt-local) is the one that matters for the largest share of consumer electronics, because it is the standard for the unlicensed spread-spectrum and wideband radios that Wi-Fi and Bluetooth are built on. It is the Canadian counterpart to the FCC's Part 15.247 and 15.407, and it is harmonised closely enough that one test campaign usually serves both markets, with supplementary measurements where the Canadian band plan or limits differ.

The standard sets, for each band, the maximum conducted output power and e.i.r.p., the rules for antenna gain, the emission masks and out-of-band limits, the occupied-bandwidth and power-spectral-density requirements for digital transmission systems, the hopping requirements for frequency-hopping systems, and, in the 5 GHz bands shared with radar, the dynamic frequency selection and transmit power control requirements. RSS-102 applies alongside it for RF exposure, and if the product also contains digital circuitry &mdash; which every Wi-Fi product does &mdash; the [ICES-003 declaration](/guides/can-ices-003-b-nmb-003-b-label/) applies to that part separately.

## What Issue 4 changed

ISED published RSS-247 Issue 4 on July 24, 2025, replacing Issue 3 of August 2023, with a six-month transition period. From January 24, 2026, certification applications must be assessed against Issue 4. Equipment certified under Issue 3 before that date does not lose its certification; the change bites on new certifications and on modifications that require re-assessment.

The changes that a manufacturer is most likely to notice, based on ISED's published text and the certification bodies' summaries, are these. The measurement procedures now reference ANSI C63.10-2020, the current US test method, which reduces the gap between an FCC test report and what a Canadian certification body will accept. The previous prohibition on operation in the 5600&ndash;5650 MHz band, which Canada had kept for weather-radar protection after the United States relaxed it, has been removed. Requirements for hybrid devices that combine digital-transmission and frequency-hopping modes have been clarified, and the reporting requirements around transmit power control and antenna gain have been tightened and simplified. None of these change who needs certification or who needs a representative; they change what the test report has to show. Confirm the specifics against the current issue on ISED's site before you rely on them, and expect your lab to have already done so.

## Who has to do what

RSS-247 equipment is Category I. Under [RSP-100](https://ised-isde.canada.ca/site/spectrum-management-telecommunications/en/devices-and-equipment/radio-equipment-standards/radio-standards-procedures-rsp/rsp-100-certification-radio-apparatus-and-broadcasting-equipment), Category I equipment must be certified before it is manufactured, imported, distributed, leased, offered for sale or sold in Canada. The applicant &mdash; usually the manufacturer or the brand owner &mdash; has the product tested by an accredited laboratory, submits the report and the technical file to a certification body recognised by ISED, and receives an IC certification number when the certification body is satisfied. The product is then listed in the [Radio Equipment List](/guides/ised-certification-number-lookup-rel/), which is what a customs broker or a retailer checks.

If the applicant has no address in Canada, RSP-100 section 4.1 requires a Canadian Representative: a person or entity in Canada, named in the application, who accepts responsibility for the certification with ISED and who can be reached for audits, sample requests and enforcement questions. The representative's attestation letter is part of the application package and the certification body will not issue the certificate without it. That is the whole of our service, and it is described in [how to appoint a Canadian Representative](/guides/how-to-appoint-a-canadian-representative/).

## A note on the neighbouring standards

Because RSS-247 is so often the first standard a manufacturer meets, it is also the one most often cited when it does not apply. Three neighbours cause most of the confusion.

**RSS-248** covers radio local area network devices in the 5925&ndash;7125 MHz band, which is where Wi-Fi 6E and Wi-Fi 7 operate. A tri-band router is RSS-247 for its 2.4 GHz and 5 GHz radios and RSS-248 for its 6 GHz radio, and both appear on the certificate.

**RSS-210** covers licence-exempt radios that are not digital transmission or frequency-hopping systems &mdash; the wide range of low-power devices from garage-door openers to RFID readers &mdash; and it is the standard a product falls under when it uses an unlicensed band in a way RSS-247 does not describe.

**RSS-Gen** applies to everything. The label format, the two-line user notice in English and French, the requirement that the IC certification number be marked on the product and the rule that equipment not listed in the REL is not certified all come from RSS-Gen, not RSS-247. A product that passes every RSS-247 measurement and ships with the wrong label has failed RSS-Gen.

## Modules and hosts

Most products do not contain a purpose-built Wi-Fi radio; they contain a certified module. Under ISED's modular certification rules, a host that integrates a certified modular transmitter without modification can rely on the module's certification for the radio, provided the host follows the module's integration instructions and the module's grantee has certified it for that use. The host still needs its own ICES-003 declaration for the digital side (the host rules are in [ICES-Gen section 3.6](/guides/ices-gen-explained/)), its own RSS-102 assessment if the module's exposure conditions do not cover the host, and its own label showing the module's IC number in the required format. The module's certification carries the module manufacturer's Canadian Representative; the host manufacturer only needs one if the host itself is certified, which happens when the module is modified, when its integration conditions are not met, or when the host contains other radios of its own.

## What a foreign manufacturer should do before submitting

Confirm which issue the test report was written to. A report to Issue 3, submitted after January 24, 2026, will come back with a request for supplementary testing to the Issue 4 provisions that differ. Confirm which bands the product uses and which standards each triggers, so that a product with a 6 GHz radio is not submitted as RSS-247 only. Confirm the module route if you are using one, and obtain the module's integration guide and the grantee's permission for your use case. Prepare the RSS-Gen labelling and user-manual text before the certificate issues, because a certificate for a product that ships without the notices is not much protection. And appoint the Canadian Representative before the certification body asks for the attestation, because it is the one document on the list that nobody outside Canada can produce for you.

<!--faq-->
### What is RSS-247?
RSS-247 is ISED's Radio Standards Specification for digital transmission systems, frequency-hopping systems and licence-exempt local area network devices operating in the 902&ndash;928 MHz, 2400&ndash;2483.5 MHz, 5150&ndash;5350 MHz and 5470&ndash;5895 MHz bands. It is the standard that applies to most Wi-Fi, Bluetooth, Zigbee and similar short-range radios sold in Canada.

### What is the current issue of RSS-247?
Issue 4, published by ISED on July 24, 2025. A six-month transition period ended on January 24, 2026, after which certification applications are assessed against Issue 4. Issue 3, from August 2023, applied before that.

### Does RSS-247 equipment need to be certified?
Yes. RSS-247 equipment is Category I under RSP-100, which means it must be certified by a certification body recognised by ISED, receive an IC certification number and be listed in the Radio Equipment List before it can be imported, sold or distributed in Canada.

### Do I need a Canadian Representative for RSS-247 certification?
If the applicant for certification has no address in Canada, yes. RSP-100 section 4.1 requires a Canadian Representative for every certification held by a foreign applicant, and the certification body will not issue the certificate without the representative's attestation letter.

### Does RSS-247 cover Wi-Fi 6E and Wi-Fi 7?
Only their 2.4 GHz and 5 GHz radios. The 6 GHz radio (5925&ndash;7125 MHz) is covered by RSS-248. A tri-band device is certified under both standards.

### Is an FCC Part 15.247 test report enough for RSS-247?
Usually most of it. RSS-247 is closely harmonised with FCC Part 15.247 and 15.407 and Issue 4 references the same ANSI C63.10-2020 test method, so a lab normally tests to both at once. Where Canadian limits or band rules differ, supplementary measurements are needed, and the report must be assessed by an ISED-recognised certification body, which many US TCBs are.

### If my product uses a certified Wi-Fi module, do I still need RSS-247 certification?
Not for the radio, if the module is integrated without modification and in accordance with its integration instructions. The host still needs ICES-003 compliance for its digital side, appropriate RF exposure assessment, and the correct label showing the module's IC number. The host needs its own certification, and its own Canadian Representative if the manufacturer is outside Canada, only if the module is modified, its conditions are not met, or the host has other radios.

### What happens to a product certified under RSS-247 Issue 3?
It stays certified. The transition to Issue 4 affects new certification applications and modifications that require re-assessment after January 24, 2026, not existing certificates.
<!--/faq-->

*Sources: ISED, RSS-247 Issue 4 (July 24, 2025) and the accompanying transition notice; ISED, RSS-Gen; ISED, RSS-248 Issue 1 (November 2021); ISED, RSP-100 section 4.1. Verify technical limits against the current issue on ISED's website before relying on them.*
