---
title: CAN ICES-003(B)/NMB-003(B): What the Label on Your Device Means
description: The CAN ICES-003(B)/NMB-003(B) marking (formerly CAN ICES-3(B)/NMB-3(B)) is Canada's digital-emissions declaration under ICES-003 and ICES-Gen. What Class A and Class B mean, who puts it there, what has to be on file, and when a radio inside changes the rules.
h1: CAN ICES-003(B)/NMB-003(B): what that label actually means
short: CAN ICES-003(B) label
type: guide
date: 2026-09-10
updated: 2026-09-10
order: 16
---

<div class="answer" markdown="1">
"CAN ICES-003(B)/NMB-003(B)" is a Canadian compliance marking, not a certification number. It says the manufacturer or importer declares that the product's digital circuitry meets the Class B (residential) emission limits in ISED's standard ICES-003, *Information Technology Equipment (Including Digital Apparatus)*. "NMB-003" is the same standard in French (*Norme sur le matériel brouilleur*). Nothing is filed with ISED and nothing appears in a public register; the label itself is the declaration. Older products carry the same declaration as "CAN ICES-3 (B)/NMB-3 (B)", the format used before Issue 7 of ICES-003 took effect. If the product also contains Wi-Fi, Bluetooth or cellular, that radio is certified separately and carries an IC certification number; the ICES marking does not cover it.
</div>

## Reading the marking, piece by piece

**CAN** is the country. ICES-Gen, the general procedure that governs every ICES standard, requires the label to carry "the word 'Canada' (or 'CAN') and a generic reference to interference-causing equipment standards, in both English and French".

**ICES-003** is the standard: [ICES-003 Issue 7](https://ised-isde.canada.ca/site/spectrum-management-telecommunications/en/devices-and-equipment/interference-causing-equipment-standards-ices/ices-003-information-technology-equipment-including-digital-apparatus), published October 15, 2020, mandatory since October 15, 2021. It applies to information technology equipment that generates or uses timing signals of at least 9 kHz and employs digital techniques &mdash; which in practice is anything with a processor, a display or a memory chip: laptops, monitors, routers, set-top boxes, printers, game consoles, the control board in a coffee machine.

**(B)** is the class. ICES-Gen defines Class A as equipment "highly unlikely to be used in a residential environment" and Class B as "equipment that cannot be classified as Class A". Class B limits are the tighter ones, because a television in the next apartment is closer than a server in a data centre. Consumer products are Class B by default; a manufacturer who marks a product Class A is saying it will never be sold for home use, and takes on the argument if it is.

**NMB-003** is the French designation of the same standard. Both languages are required on the marking.

The specific format is the manufacturer's choice, so you will see the marking with and without spaces, on one line or two, on the product, on the power adapter, or in the manual. All of those can be correct.

## Who puts it there, and what has to sit behind it

ICES compliance runs on a Supplier's Declaration of Conformity. Under [ICES-Gen Issue 2](https://ised-isde.canada.ca/site/spectrum-management-telecommunications/en/devices-and-equipment/interference-causing-equipment-standards-ices/ices-gen-general-requirements-compliance-interference-causing-equipment) (February 23, 2024) the "supplier" is the person or entity in Canada involved in manufacturing, importing, distributing, leasing, offering for sale or selling the equipment. The manufacturer or importer tests the product to ICES-003 using one of the two permitted methods &mdash; CAN/CSA-CISPR 32:17 or ANSI C63.4 &mdash; and, in ISED's words, "the label placed on each unit... represents the SDoC with ISED requirements". The manufacturer or importer "shall retain a copy of the test report for as long as the interference-causing equipment is manufactured, imported, distributed, leased, offered for sale, or sold in Canada". That is the whole procedure: test, keep the report, label, sell. ISED can ask for the report; it does not receive one in advance.

A foreign manufacturer with no Canadian entity therefore has no ICES filing to make and no representative to appoint for the ICES declaration. The Canadian importer or distributor is the supplier that ICES-Gen reaches, and the test report should be in their hands, or reachable from them, when a customs or market-surveillance question arrives.

## Where the label goes

Section 6.3.3 of [ICES-Gen](/guides/ices-gen-explained/) puts the marking on the equipment itself. Three alternatives exist. Equipment measuring 2.5 cm or less may carry the marking in the user manual and on the packaging without asking anyone. Larger equipment may move the marking to the manual or packaging only with ISED's approval under section 6.3.2.1. And equipment with an integral display may use an electronic label under Annex B, subject to its access and durability conditions. If the product also has a radio, the IC certification number follows the labelling rules in RSS-Gen, which are similar but not identical, so a combined label needs to satisfy both.

## The radio inside is a different regime

This is the point that catches foreign manufacturers. A tablet is ICES-003 for its digital electronics and RSS-247 for its Wi-Fi and Bluetooth. The digital side is declared; the radio side is certified &mdash; a recognised certification body reviews the test report, issues an IC certification number, and the product is listed in the [Radio Equipment List](/guides/ised-certification-number-lookup-rel/). Section 3.6 of ICES-Gen notes that a host containing a certified Category I module usually does not itself need certification, but the module does, and section 4.1 still requires the final product to meet RSS-Gen and RSS-102.

The certification is where a foreign applicant needs a [Canadian Representative](/canadian-representative-service/) under RSP-100 section 4.1. The ICES-003 declaration never does; we have set out that distinction in detail in [Do you need a Canadian Representative for ICES-003 SDoC?](/guides/ices-003-sdoc-canadian-representative/). The short version: if your label carries only "CAN ICES-003(B)/NMB-003(B)", you have a digital product and no representative to appoint. If it also carries "IC: 1234A-XXXX", someone in Canada is on file for that number, and if you are outside Canada, that someone is a representative you appointed.

## For US manufacturers

ICES-003 is Canada's counterpart to FCC Part 15 Subpart B. Both are supplier declarations, both split Class A and Class B on the same residential logic, and ANSI C63.4 is an accepted test method on both sides, so a single test campaign often supports both markings. The paperwork differs: the FCC declaration carries the responsible party's US contact information in the manual, while Canada relies on the marking and the retained report. Our [FCC to ISED guide](/guides/fcc-to-ised/) covers the radio side, where the differences are larger.

<!--faq-->
### What does CAN ICES-003(B)/NMB-003(B) mean?
It is Canada's compliance marking for digital equipment. The manufacturer or importer declares that the product meets the Class B (residential) emission limits in ISED standard ICES-003. "NMB-003" is the French name of the same standard. It is a declaration, not a certification, and nothing is filed with ISED.

### Is CAN ICES-3(B)/NMB-3(B) the same thing?
Yes. "CAN ICES-3 (B)/NMB-3 (B)" is the format used under earlier issues of ICES-003. Issue 7, mandatory since October 15, 2021, uses the three-digit form "CAN ICES-003(B)/NMB-003(B)". Products built and labelled under the earlier issue remain compliant; new declarations should use the current form.

### What is the difference between Class A and Class B?
ICES-Gen defines Class A as equipment highly unlikely to be used in a residential environment and Class B as everything else. Class B limits are stricter. Consumer products are Class B; Class A is for commercial and industrial equipment that will not end up in a home.

### Does ICES-003 require a Canadian Representative?
No. The Canadian Representative requirement is in RSP-100 section 4.1 and applies to radio apparatus certified by an applicant outside Canada. ICES-003 compliance is a supplier's declaration with no filing and no representative. If the product also contains a certified radio, the representative is needed for that certification, not for the ICES declaration.

### Who is responsible for the ICES-003 label on an imported product?
ICES-Gen defines the supplier as the person or entity in Canada that manufactures, imports, distributes, leases, offers for sale or sells the equipment. For a foreign-made product, that is the Canadian importer or distributor, who should hold or be able to produce the test report for as long as the product is sold in Canada.

### Can the label be in the manual instead of on the device?
Only in limited cases. Equipment 2.5 cm or smaller may carry the marking in the user manual and on the packaging. Larger equipment needs ISED's approval to move the marking off the device. Equipment with a built-in display may use an electronic label under Annex B of ICES-Gen.

### Does the ICES-003 label cover the Wi-Fi or Bluetooth in my product?
No. Radio transmitters are certified under the RSS standards and RSP-100 and carry a separate IC certification number that you can look up in the Radio Equipment List. The ICES marking covers only the digital emissions of the product.
<!--/faq-->

*Sources: ISED, ICES-003 Issue 7 (October 15, 2020, Gazette Notice SMSE-013-20); ISED, ICES-Gen Issue 2 (February 23, 2024), sections 3.6, 4.1, 6.3.2.1, 6.3.3 and Annex B; ISED, RSP-100 section 4.1.*
