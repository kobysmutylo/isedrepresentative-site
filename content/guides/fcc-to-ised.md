---
title: From FCC to ISED: Certifying a US-Approved Wireless Product for Canada
description: What changes when a product with FCC certification enters Canada: RSS standards vs FCC Part 15, the IC certification number, labelling, using a US FCB under the mutual recognition arrangement, and the Canadian Representative requirement.
h1: From FCC to ISED: bringing a US-certified product into Canada
short: FCC to ISED
type: guide
date: 2026-08-20
updated: 2026-08-20
order: 09
---

<div class="answer" markdown="1">
An FCC grant does not authorize sale in Canada. The product needs its own ISED certification under the applicable RSS standards, an IC certification number, Canadian labelling and user notices, and, because the applicant is outside Canada, a Canadian Representative under RSP-100 section 4.1. The good news: the test data usually transfers, and the FCB that handled your FCC grant can often issue the ISED certificate too.
</div>

## A note on names

US engineers usually know the Canadian regime as "IC certification" or "Industry Canada certification", and the approval as an "IC ID", by analogy with the FCC ID. Industry Canada became ISED in 2015, but the IC prefix on certification numbers and the habit of saying "IC" survived. "ISED certification", "IC certification" and "Industry Canada certification" are the same process under RSP-100, and the "IC representative" or "Industry Canada representative" that your TCB asks for is the Canadian Representative described below.

## What carries over and what does not

**Test data, largely.** ISED's RSS standards are closely harmonized with the corresponding FCC rules for most unlicensed and licensed radio categories (RSS-247 alongside Part 15.247 for Wi-Fi and Bluetooth, RSS-210 for licence-exempt devices, RSS-130 and RSS-132/133/139 families for cellular bands, RSS-102 for RF exposure alongside the FCC's SAR and MPE requirements). A competent lab tests to both at the same time. Where Canadian limits or band plans differ, supplementary measurements are needed; your lab will know.

**The certification body, often.** Under the Canada–United States mutual recognition arrangement, ISED recognizes US-based foreign certification bodies (FCBs) to issue ISED certificates, and most US TCBs hold that recognition. The same FCB can issue the FCC grant and the ISED certificate from one test campaign.

**The approval itself, never.** The product is certified separately, receives an IC certification number, and is listed in ISED's Radio Equipment List.

## What is new

**Canadian labelling and notices.** RSS-Gen sets the labelling requirements: the IC certification number on the product (or e-label where permitted), and the user-manual notices in English and French that RSS-Gen prescribes for licence-exempt devices and RF exposure. These are separate from the FCC Part 15 statements and both must appear.

**An ISED Company Number.** The applicant obtains one from ISED; the CB's application requires it, and it forms the prefix of the IC certification number.

**A Canadian Representative.** The FCC has no equivalent requirement for foreign applicants. ISED does: if the applicant's company address is outside Canada, a Canadian Representative must be identified on the application and must be maintained for as long as the product is offered in Canada. The FCB will ask for the representative's letter before issuing. See [the RSP-100 requirement explained](/guides/canadian-representative-requirement-rsp-100/) and [attestation letter required fields](/guides/attestation-letter-required-fields/).

## A typical sequence for a US manufacturer

1. Lab tests to FCC and RSS requirements together.
2. FCB reviews for both. The FCC grant issues.
3. FCB asks for the ISED Company Number and the Canadian Representative letter. Applicant orders the letter (same business day from us), forwards it.
4. FCB issues the ISED certificate; product is listed in the REL.
5. Labels and manual updated with the IC number and RSS-Gen notices.
6. Representative remains on file; the applicant keeps its contact details current.

Most US companies hit step 3 without warning, and it is the representative letter, not the testing, that ends up holding the certificate. Ordering it in parallel with FCB review removes the delay.

## Permissive changes

ISED's Class I and Class II permissive change framework in RSP-100 section 10 parallels the FCC's. A change filed with the FCC usually needs the equivalent filing with ISED, and a Class II change that keeps the IC number stays within the existing representative appointment.

## Modules

A US-certified module used in a host needs its own ISED modular certification for the host to rely on it in Canada; FCC modular approval does not transfer. The module maker, if outside Canada, needs a Canadian Representative for that certification. See [one representative letter per IC ID](/guides/one-representative-letter-per-ic-id/).

<div class="source" markdown="1">
**Sources.** [RSP-100, Issue 12](https://ised-isde.canada.ca/site/spectrum-management-telecommunications/en/devices-and-equipment/radio-standards-procedures-rsp/rsp-100-certification-radio-apparatus-and-broadcasting-equipment), sections 4.1, 5, 8 and 10. ISED's [Certification and Engineering Bureau](https://ised-isde.canada.ca/site/certification-engineering-bureau/en) (recognized FCBs, Radio Equipment List, RSS-Gen). Standard numbers cited are for orientation; confirm the current issue of each RSS with your lab.
</div>

<!--faq-->
### Our FCB is in the US. Does that satisfy the Canadian Representative requirement?

No. The FCB is recognized to certify; it is not your representative in Canada. Section 4.1 looks at the applicant's address.

### Can our US regulatory consultant be our Canadian Representative?

Only if it has a Canadian place of business. A US address does not qualify.

### Do we need a Canadian importer as well?

That is a customs and tax question separate from certification. The Canadian Representative is not an importer of record and does not take title to goods.
<!--/faq-->
