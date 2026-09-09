---
title: ISED Certification Glossary: HVIN, PMN, HMN, FVIN, IC ID, CN
description: Plain definitions of the terms on an ISED certificate, label and REL entry — HVIN, PMN, HMN, FVIN, company number, IC certification number, Category I and II, CB and FCB, RSP, RSS, ICES, SDoC, permissive change, Canadian Representative — with the ISED source for each.
h1: ISED certification glossary
short: Glossary
type: guide
date: 2026-09-09
updated: 2026-09-09
order: 16
---

<div class="answer" markdown="1">
The identifiers on an ISED certificate come from RSP-100. The HVIN identifies the hardware version, the PMN is the name the product is sold under in Canada, the HMN is the host a certified module was assessed in, and the FVIN is the firmware version that affects RF behaviour. The IC certification number is the company number ISED assigned the applicant, a hyphen, and a product identifier. Definitions below are quoted from or paraphrase the ISED documents named against each term.
</div>

## Identifiers

**IC certification number (IC ID, ISED certification number).** The identifier a certification body assigns to one certified radio product, in the form company number-product identifier, for example 1234A-ABC123. It appears on the label after "IC:" and is the exact-match key in the [Radio Equipment List](/guides/ised-certification-number-lookup-rel/). "IC" survives from Industry Canada, ISED's name until 2015.

**Company number (CN).** The identifier ISED assigns to a company registered in its Spectrum Management System for equipment certification or registration. It is the first block of every IC number the company holds. Older numbers are four digits and a letter; DC-01 section 8.2.1 describes new assignments as five digits. See [ISED company number](/guides/ised-company-number/).

**HVIN (Hardware Version Identification Number).** RSP-100: "The HVIN identifies hardware specifications of a product version." One certification can carry several HVINs where the CB accepts them as the same certified design. The HVIN is the key that opens a detail record in the REL.

**PMN (Product Marketing Name).** RSP-100: "The PMN is the name or model number under which the product will be marketed/offered for sale in Canada." A change of PMN is a notifiable permissive change.

**HMN (Host Marketing Name).** RSP-100: "The HMN is the name or model number of a final product, which contains a certified radio module." Populated for modular certifications where a host has been recorded; empty otherwise.

**FVIN (Firmware Version Identification Number).** RSP-100: "The FVIN identifies the firmware version used by the product, which controls/affects the RF characteristics of the product." Recorded where firmware changes are filed as permissive changes.

**UPN (Unique Product Number).** DC-01's term for the product identifier that follows the company number in a terminal equipment registration number, up to eleven characters.

## Parties

**Applicant / certificate holder.** The legal entity that applies for and holds the certification. Its address decides whether a Canadian Representative is required.

**Canadian Representative.** RSP-100 section 4.1: required "when the applicant's company address is not within Canada"; "responsible for responding to all enquiries from ISED regarding the certified product(s), including providing audit samples at no charge to ISED." Also called the ISED representative, IC representative, Industry Canada representative or Canadian agent. See [the requirement explained](/guides/canadian-representative-requirement-rsp-100/).

**Certification body (CB).** An organization recognized by ISED to certify radio apparatus. A **foreign certification body (FCB)** is one located outside Canada and recognized under a mutual recognition arrangement, such as a US FCB under the Canada–US MRA. See [representative vs CB vs test lab](/guides/representative-vs-certification-body-vs-test-lab/).

**Test laboratory.** The ISED-recognized lab that measures the product against the applicable RSS. It does not certify.

**Responsible party.** ICES-Gen section 3.2: the party involved in "manufacture, importation, distribution, lease, offering for sale, and sale" of interference-causing equipment. A status that follows the activity, not an appointment. See [ICES-003 SDoC](/guides/ices-003-sdoc-canadian-representative/).

## Documents and procedures

**RSP (Radio Standards Procedure).** ISED's procedural documents. **RSP-100** is the certification procedure for radio apparatus and broadcasting equipment; the current issue is Issue 12.

**RSS (Radio Standards Specification).** The technical standards a radio must meet, for example RSS-247 for licence-exempt 2.4 GHz and 5 GHz devices, RSS-210 for other licence-exempt devices, RSS-130 and RSS-132 for cellular bands. **RSS-Gen** sets the general requirements common to all, including labelling and the REL listing rule in section 3.4.1.

**ICES (Interference-Causing Equipment Standard).** Standards for the non-radio, emissions side of equipment. **ICES-003** covers information technology equipment; **ICES-Gen** is the general procedure. Compliance is by SDoC.

**DC-01.** The procedure for declaration of conformity and registration of terminal equipment (equipment that connects to the public telephone network). Its section 6 carries the same Canadian Representative requirement as RSP-100 section 4.1. See [terminal equipment](/guides/dc-01-terminal-equipment-canadian-representative/).

**SDoC (Supplier's Declaration of Conformity).** The self-declaration route: test, label, keep the report, no application to ISED. Used for ICES equipment and for Category II radio apparatus.

**Category I / Category II.** RSS-Gen's split of radio apparatus. Category I requires certification and a REL listing before sale. Category II is exempt from certification and registration and complies by SDoC; licence-exempt receivers are the usual example.

**Application and Agreement for Certification Services (form A).** The application the CB collects under RSP-100. It is where the Canadian Representative's details are recorded.

**Attestation letter.** The representative's signed statement, accepted by CBs as evidence of the section 4.1 appointment. See [required fields](/guides/attestation-letter-required-fields/).

**Permissive change.** RSP-100 section 10: a change to a certified product that can be filed against the existing certification rather than as a new one, in Classes I to IV. A change that keeps the IC number stays inside the existing representative appointment.

**Multiple listing.** RSP-100 section 11.5: a new certification obtained on the strength of an existing one, typically so a distributor or OEM customer can hold its own certificate for the same design.

**Audit sample.** A unit ISED requests after certification to verify continued compliance. See [who provides, who pays](/guides/ised-audit-samples-who-provides-who-pays/).

**REL (Radio Equipment List).** ISED's public register of certified Category I radio apparatus. **TAR** is the equivalent list for registered terminal equipment.

**SMS (Spectrum Management System).** ISED's online system where company profiles are created, company numbers assigned, and the REL and company-name searches are hosted.

<div class="source" markdown="1">
**Sources.** [RSP-100, Issue 12](https://ised-isde.canada.ca/site/spectrum-management-telecommunications/en/devices-and-equipment/radio-standards-procedures-rsp/rsp-100-certification-radio-apparatus-and-broadcasting-equipment), sections 4.1, 10, 11.5 and the glossary. [RSS-Gen, Issue 6](https://ised-isde.canada.ca/site/spectrum-management-telecommunications/en/devices-and-equipment/radio-equipment-standards/radio-standards-specifications-rss/rss-gen-general-requirements-compliance-radio-apparatus), section 3.4.1. [ICES-Gen, Issue 1](https://ised-isde.canada.ca/site/spectrum-management-telecommunications/sites/default/files/attachments/2022/ICES-Gen-i1-A1-2021-02EN.pdf), sections 3.2 and 3.3. [DC-01, Issue 7](https://ised-isde.canada.ca/site/spectrum-management-telecommunications/en/devices-and-equipment/terminal-attachment-program-procedures/dc-01-procedure-declaration-conformity-and-registration-terminal-equipment), sections 6 and 8.2.1.
</div>

<!--faq-->
### What is the difference between HVIN and PMN?

The HVIN identifies a hardware version of the certified design; the PMN is the name or model number the product is sold under in Canada. One HVIN can be sold under several PMNs, and both are recorded on the REL.

### What does IC stand for on a product label?

Industry Canada, the department's name until 2015. The number after "IC:" is the ISED certification number.

### Is the ISED company number the same as the IC ID?

No. The company number identifies the certificate holder and is the first block of the IC ID; the IC ID identifies one certified product.

### What is a Category II radio device?

A device RSS-Gen exempts from certification and REL listing, complying instead by Supplier's Declaration of Conformity. Licence-exempt receivers are the common case.
<!--/faq-->
