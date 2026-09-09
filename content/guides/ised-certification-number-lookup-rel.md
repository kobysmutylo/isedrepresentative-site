---
title: IC ID Lookup: Check an ISED Certification Number in the REL
description: How to look up an IC certification number, company or model in ISED's Radio Equipment List, what a listing proves, what a missing listing means for import and sale in Canada, and how the IC number differs from an FCC ID.
h1: How to look up an ISED certification number (IC ID) in the Radio Equipment List
short: IC ID lookup
type: guide
date: 2026-09-09
updated: 2026-09-09
order: 15
---

<div class="answer" markdown="1">
To check whether a radio product is certified for Canada, search ISED's [Radio Equipment List](https://sms-sgs.ic.gc.ca/equipmentSearch/searchRadioEquipments?execution=e1s1&lang=en_CA) by the IC certification number printed on the label (the "IC:" number, in the form company number-product identifier), by company name, or by model name (PMN) or hardware version (HVIN). A listing shows that a certification body certified the device and ISED accepted it. Under RSS-Gen section 3.4.1, a Category I device that is not on the REL may not be imported, distributed, offered for sale or sold in Canada.
</div>

## What the number looks like

The identifier on a Canadian-certified radio product reads IC: followed by two blocks joined by a hyphen, for example IC: 1234A-ABC123 or IC: 20001-XYZ100. The first block is the [ISED company number](/guides/ised-company-number/) assigned to the certificate holder. The second is the product identifier chosen by the applicant or its certification body, up to eleven characters. The whole string is the IC certification number, still called the IC ID after Industry Canada, ISED's name until 2015.

It is not the FCC ID. A product sold in both countries carries both, and the two are assigned by different regulators under different procedures. The FCC ID is looked up on the FCC's equipment authorization search; the IC number is looked up on the REL. Third-party sites that mirror both databases are convenient but are not the register; when it matters, use ISED's own search.

## Searching

The REL search takes seven fields: HVIN, PMN, HMN, certification number, company name, company number and equipment description. The exact search is the certification number. The forgiving search is the company name. A search on the company number alone returns every certification that company holds, which is the quickest way to see a manufacturer's whole Canadian portfolio. Results group by company, sort by any column, and download as CSV.

If a search on the number printed on the label returns nothing, check three things before concluding the product is uncertified. Labels sometimes drop the hyphen or the "IC:" prefix, and the search wants the number exactly. The label may show a module's number rather than the end product's, which is legitimate where the product relies on a certified module. And a listing may be deferred: RSS-Gen section 3.4.1 lets an applicant ask ISED for a deferred listing date, during which the product can be imported and distributed but not sold.

## What a listing tells you, and what it does not

The detail record shows the certificate holder's name and company number, the approval date, the HVIN, PMN, HMN and FVIN, the equipment description, the certification body and test laboratory, and the emissions by standard and issue. It is enough to confirm that the product is certified and to whom.

It does not show the [Canadian Representative](/canadian-representative-service/), the applicant's address, or any test report. A Canadian importer, retailer or marketplace doing diligence on a foreign supplier will therefore ask the supplier for the representative's letter directly, because the register cannot confirm that the section 4.1 requirement was met. A fuller walk-through of the record, including the asterisk that marks a superseded issue of the standard, is in [how to read your REL entry](/updates/reading-your-ised-rel-listing/).

## If the entry is wrong or missing

Corrections go through the certification body that issued the certificate, as a permissive change under RSP-100 section 10; there is no public edit route. A product that was never certified needs a certification, and if the applicant is outside Canada, a Canadian Representative. See [the ISED certification process overview](/guides/ised-certification-process-overview/) and [how to appoint a Canadian Representative](/guides/how-to-appoint-a-canadian-representative/).

<div class="source" markdown="1">
**Sources.** [Radio Equipment Search](https://sms-sgs.ic.gc.ca/equipmentSearch/searchRadioEquipments?execution=e1s1&lang=en_CA), ISED Spectrum Management System, as displayed September 2026. [RSS-Gen, Issue 6](https://ised-isde.canada.ca/site/spectrum-management-telecommunications/en/devices-and-equipment/radio-equipment-standards/radio-standards-specifications-rss/rss-gen-general-requirements-compliance-radio-apparatus), section 3.4.1. [RSP-100, Issue 12](https://ised-isde.canada.ca/site/spectrum-management-telecommunications/en/devices-and-equipment/radio-standards-procedures-rsp/rsp-100-certification-radio-apparatus-and-broadcasting-equipment), sections 4.1 and 10.
</div>

<!--faq-->
### How do I look up an IC certification number?

Enter it in the certification number field of ISED's Radio Equipment List search, exactly as printed after "IC:" on the label, including the hyphen.

### Is the IC ID the same as the FCC ID?

No. The FCC ID is assigned under US rules and searched on the FCC's site; the IC certification number is assigned under Canadian rules and searched on the REL. A product sold in both countries carries both.

### What does it mean if a product is not in the REL?

For Category I radio apparatus, that it may not be imported, distributed, offered for sale or sold in Canada under RSS-Gen section 3.4.1, unless ISED has approved a deferred listing date. Check the number was entered exactly and whether the label shows a module's number before concluding.

### Can I see who the Canadian Representative is from the REL?

No. The REL does not display the representative or the applicant's address. Ask the certificate holder for the representative's letter.

### How do I find every product a company has certified for Canada?

Search the REL by company name, or by company number for an exact match, and download the CSV.
<!--/faq-->
