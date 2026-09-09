---
title: How to Read Your ISED Radio Equipment List (REL) Entry
description: What the REL shows for a certified device — IC number, HVIN, PMN, HMN, FVIN, CB, lab, emissions — what it does not show, why a missing listing bars sale in Canada, and how to fix an error.
h1: How to read your ISED Radio Equipment List entry — and what is not in it
short: Reading the REL
type: update
date: 2026-09-08
updated: 2026-09-09
---

<div class="answer" markdown="1">
The [Radio Equipment List](https://sms-sgs.ic.gc.ca/equipmentSearch/searchRadioEquipments?execution=e1s1&lang=en_CA) is ISED's public register of every Category I radio device certified for Canada. A listing shows the company number and name, the IC certification number, the approval date, the HVIN, PMN, HMN and FVIN, the equipment description, the certification body and test laboratory, and an emissions table by standard and issue. It does not show the Canadian Representative, the applicant's address, or any test report. Under [RSS-Gen Issue 6](https://ised-isde.canada.ca/site/spectrum-management-telecommunications/en/devices-and-equipment/radio-equipment-standards/radio-standards-specifications-rss/rss-gen-general-requirements-compliance-radio-apparatus) section 3.4.1, a Category I device that is not on the REL cannot be sold, leased, imported or distributed in Canada, so a buyer, customs broker or retailer who cannot find your entry has a legitimate reason to stop.
</div>

## Why the list has legal weight

RSS-Gen section 3.4.1 puts it in one sentence: "No person shall manufacture, import, distribute, lease, offer for sale, or sell Category I radio apparatus in Canada unless this apparatus is listed on the REL." The certificate your CB issues is the decision. The REL entry is the public evidence of it. ISED's own footnote on every page — the table "is generated based on information received from Certification Bodies, Manufacturers or Suppliers at time of certification" — is the reminder that the register is only as accurate as the application that fed it. RSS-Gen adds the other edge: where ISED finds a model non-compliant or the information submitted was incorrect, "ISED may remove the model from the REL, in which case it shall no longer be manufactured, imported, distributed, leased, offered for sale or sold in Canada."

There is one relief valve. An applicant can ask ISED for a deferred REL listing date, which lets a product be manufactured, imported and distributed in Canada ahead of the public listing — but not leased, offered for sale or sold until the entry appears. It is the route for a product launching on a fixed date.

## Finding an entry

The search page takes seven fields: HVIN, PMN, HMN, certification number, company name, company number, and equipment description. An advanced panel adds the radio standard (a pick-list from BETS-1 to RSS-310, with RSS-247 split into DFS and non-DFS), frequency range, occupied bandwidth, emission code and power. Company name is the forgiving search. Certification number is the exact one. The IC number itself is two parts joined by a hyphen — the [company number](/guides/ised-company-number/) ISED assigned you (four digits and a letter for older assignments, five digits for newer ones) and the product identifier your CB chose — so a search on the company number alone returns everything you have ever certified.

Results come back grouped by company, sortable by HVIN, PMN, HMN, FVIN, certification number or approval date, with a CSV download. That CSV is the quickest way to reconcile the register against your own product list, and we suggest doing it once a year when you confirm to us which products are still on the Canadian market.

## Reading the detail page

Click an HVIN and the record opens. It is roughly a page long. The top block is identity: company number and name, certification number, approval date, and the certification type. Below it, the four identifiers ISED uses to tell versions apart: the HVIN (hardware version), the PMN (the name on the box), the HMN (for a module, the host it was assessed in), and the FVIN (firmware version, populated where a [Class III permissive change](/updates/permissive-changes-rsp-100-class-i-to-iv/) has been filed). An empty HMN or FVIN is normal. It means no host or firmware notice has been recorded.

Then the compliance block: the equipment description, the type of radio equipment (the ISED categories the CB selected — WLAN, modular approval, local-area-network device and so on), the certification body with its recognition number, and the wireless test laboratory with its ISED lab number. Last, the emissions table, one row per tested band: the specification, the issue number, frequency range, emission designator, and conducted or radiated power. An asterisk on the issue number carries a footnote — "This product was certified to a previous issue of the standard. A new issue is available." After [RSS-Gen Issue 6](/updates/rss-gen-issue-6-published/), a large share of the register now carries that asterisk. It is not a compliance finding. It is a prompt to check the transition rules for [existing certifications](/updates/rss-gen-issue-6-existing-certifications/).

## What is not there

Three things people expect to find and will not. The first is probably the one that brought you here. The Canadian Representative is not displayed anywhere on the REL — the appointment sits in the Application and Agreement for Certification Services held by the CB and ISED, which is why a buyer or a Canadian distributor doing diligence will ask you for the [representative letter](/canadian-representative-service/) directly. The applicant's address is not shown either, so the REL cannot tell a reader whether a representative was required at all. And no test report, exposure assessment or user manual is public; those stay in the certification file, and RSP-100 section 12 requires the holder to keep them for as long as the product is on the market.

## Fixing a wrong or stale entry

A wrong PMN, a missing HVIN, a model that shipped under a name the REL has never heard of — these are corrected through the CB, not by writing to ISED's public site. There is no edit button. Under RSP-100 section 10, a change to the PMN or HVIN is itself a notifiable permissive change, so the fix is a Class I or Class II notice from your CB with the corrected identifiers, and the register updates when ISED processes it. A company that has changed its legal name, or has been acquired, has a bigger job: the certificate holder changes, and with it the certification agreement and the representative — see [changing your Canadian Representative](/guides/changing-your-canadian-representative/).

If you certified through us at any point since 2010, send us the IC number and we will check the entry against the letter on file and tell you where the two disagree.

<div class="source" markdown="1">
**Sources.** [RSS-Gen, Issue 6 (July 30, 2026)](https://ised-isde.canada.ca/site/spectrum-management-telecommunications/en/devices-and-equipment/radio-equipment-standards/radio-standards-specifications-rss/rss-gen-general-requirements-compliance-radio-apparatus), section 3.4.1 (REL listing requirement, deferred listing, removal). [RSP-100, Issue 12](https://ised-isde.canada.ca/site/spectrum-management-telecommunications/en/devices-and-equipment/radio-standards-procedures-rsp/rsp-100-certification-radio-apparatus-and-broadcasting-equipment), sections 4.1, 10 and 12. [Radio Equipment Search](https://sms-sgs.ic.gc.ca/equipmentSearch/searchRadioEquipments?execution=e1s1&lang=en_CA), ISED Spectrum Management System, as displayed September 2026.
</div>

<!--faq-->
### Does the REL show who the Canadian Representative is?
No. The REL displays the certificate holder, the CB, the lab and the technical record. The Canadian Representative is recorded on the Application and Agreement for Certification Services held by the CB and ISED, and is evidenced by the representative letter in the certification file.

### Can we sell in Canada before the REL entry appears?
Not unless ISED has approved a deferred REL listing date, and even then RSS-Gen section 3.4.1 allows only manufacture, import and distribution before listing — not lease, offer for sale or sale.

### Our product name on the REL is wrong. How do we fix it?
Through your certification body. A PMN or HVIN change is a notifiable permissive change under RSP-100 section 10; the CB files the corrected identifiers and the entry updates when ISED processes the notice.

### The issue number on our listing has an asterisk. Is the certification still valid?
Yes. The asterisk means a newer issue of the standard has been published since certification. The certification stands; the transition rules of the new issue decide what, if anything, has to be updated in the test report.
<!--/faq-->

Related reading: [Permissive changes under RSP-100](/updates/permissive-changes-rsp-100-class-i-to-iv/), [the ISED certification process overview](/guides/ised-certification-process-overview/), and [Does each IC ID need a separate Canadian Representative letter?](/guides/one-representative-letter-per-ic-id/).
