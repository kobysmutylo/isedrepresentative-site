---
title: ICES-Gen Explained: Canada's Rules for Non-Radio Emissions
description: ICES-Gen Issue 2 (Feb 23, 2024) sets the procedure behind every ICES standard: the supplier, the SDoC and label, test-report rules, and where the Canadian Representative fits.
h1: ICES-Gen: the general procedure behind ICES-003 and every other ICES standard
short: ICES-Gen
type: guide
date: 2026-09-12
updated: 2026-09-12
order: 18
---

<div class="answer" markdown="1">
ICES-Gen, *General Requirements for Compliance of Interference-Causing Equipment*, is ISED's umbrella procedure for the non-radio side of electronic products. It does not contain emission limits itself; it sets the rules that every specific ICES standard (ICES-003 for digital apparatus, ICES-002 for vehicles and engines, ICES-005 for lighting, and the rest) shares: who is responsible, how compliance is declared, what the test report must contain, and what the label must say. The current edition is [Issue 2, published February 23, 2024](https://ised-isde.canada.ca/site/spectrum-management-telecommunications/en/devices-and-equipment/interference-causing-equipment-standards-ices/ices-gen-general-requirements-compliance-interference-causing-equipment) under Gazette notice SMSE-014-23; its one-year transition period has expired, so Issue 2 is the only edition that counts. Compliance is by Supplier's Declaration of Conformity. Nothing is filed with ISED, nothing is certified, and ICES-Gen contains no Canadian Representative requirement. That requirement lives in RSP-100 section 4.1 and applies only to certified radio apparatus.
</div>

## What ICES-Gen is, and what it is not

ISED regulates electronic equipment under three families of documents. The RSS standards and RSP-100 cover radio apparatus, which is certified. The CS standards and DC-01 cover terminal equipment that connects to the telephone network, which is registered. The ICES standards cover everything else that can interfere with radiocommunication because it contains digital circuitry, motors, switching power supplies or the like, and this equipment is neither certified nor registered. It is declared.

ICES-Gen is the general part of that third family. Its scope clause says it "shall be used in conjunction with the ICES standard applicable to the specific type of interference-causing equipment", and where the two disagree, the specific standard wins. So a laptop is assessed under ICES-003 for its limits and test methods and under ICES-Gen for the procedure around them. If you are reading ICES-003 and wondering who has to keep the test report or what the label must say, the answer is in ICES-Gen.

Issue 2 replaced Issue 1 (July 2018, amended February 2021). Section 3.1.2 gave a transition period "ending one year after the publication of this standard on ISED's website, within which compliance with either issue 1 or issue 2 of ICES-Gen is accepted". That year ran out on February 23, 2025. Equipment still manufactured, imported, distributed, leased, offered for sale or sold in Canada must now comply with Issue 2. Issue 1 used a different section numbering, so a compliance file that cites it by section should be read across to the new document.

## Category I and Category II

ICES-Gen borrows two terms from the Radiocommunication Regulations that turn up on every ISED page. Category I equipment "requires a technical acceptance certificate (TAC) issued by ISED's Certification and Engineering Bureau, or a certificate issued by a recognized certification body". That is certified radio apparatus: the Wi-Fi module, the cellular modem, the Bluetooth chip. Category II equipment is "radio apparatus, broadcasting equipment, or interference-causing equipment that is exempt from certification". All ICES equipment is Category II, and section 3.3 states the consequence plainly: "Category II equipment is exempt from certification and registration."

The distinction matters because a single product is often both. The digital electronics in a tablet are Category II under ICES-003; the Wi-Fi inside it is Category I under RSS-247. The two halves follow different procedures, and the Canadian Representative attaches to only one of them, which is the subject of the host equipment section below.

## The supplier and the Supplier's Declaration of Conformity

Issue 2 added a definition that changes how foreign manufacturers should read the standard. A supplier is a "person or entity located in Canada that is involved in one of the activities listed in subsections 4(2) and/or 4(3) of the Radiocommunication Act, i.e. manufacture, importation, distribution, lease, offering for sale, and sale". Issue 1 used the term "responsible party" for the same list of activities without the words "located in Canada". The new wording makes explicit what the Act already implied: ICES obligations sit with whoever performs a regulated activity in Canada. For a product made abroad, that is the Canadian importer or distributor.

Section 3.3 then describes the whole procedure in three sentences. "The supplier (see section 2) tests the Category II equipment and ensures that it meets the appropriate technical standards. The supplier also labels the equipment and fulfils any other administrative requirements as specified in the applicable standards (e.g. user manual notices, test report retention). Equipment testing does not have to be performed by a recognized ISED testing laboratory." And the declaration itself is not a document at all: "The label placed on each unit of the interference-causing equipment model, according to the applicable ICES standard, represents the SDoC with ISED requirements."

There is no form, no submission, no fee and no listing. The evidence of compliance is the test report, held privately, and the mark on the product. A manufacturer coming from the FCC will recognise this as the counterpart of Part 15 Subpart B, with one practical difference: the FCC's SDoC requires a US-based responsible party to be identified in the product literature, while ICES-Gen identifies nobody by name. The supplier is whoever is in the chain, and ISED finds them by asking.

## The test report: contents, retention and updating

Section 5 and Annex A set the documentary standard. The report must identify the ICES standard and issue tested against, the laboratory, the manufacturer, the model, the configuration used in each test, the class of limits applied, any alternative test methods chosen, the test equipment with calibration due dates, the test site and its validation, and the measurement uncertainty. Two housekeeping rules in section 4 are new in Issue 2 and worth checking with your laboratory: measurement equipment must be calibrated at intervals of no more than three years (or sooner if the applicable standard or the instrument manufacturer says so), and the test site validation must be confirmed at least once in any three-year period.

Retention is the rule most often missed. "The manufacturer or importer shall retain a copy of the test report for as long as the interference-causing equipment is manufactured, imported, distributed, leased, offered for sale, or sold in Canada and shall make the test report available to ISED upon request." That is an open-ended obligation, tied to the product's life on the Canadian market rather than to a fixed number of years.

The report also has to keep up with the standard. When a new issue of the applicable ICES standard is published and the product stays on the market past the transition period, "the manufacturer or importer shall update the test report with additional test results and/or engineering analysis, as necessary, such that the test report demonstrates compliance with the new issue". A report written against ICES-003 Issue 6 is not, on its own, evidence of compliance with Issue 7.

## What the label must say

Section 6.3.3 simplified the marking. The label must carry "the word 'Canada' (or 'CAN') and a generic reference to interference-causing equipment standards, in both English and French", plus the class where the applicable standard distinguishes Class A from Class B. The generic form ISED now gives is:

`CAN ICES (*) / NMB (*)`

where the asterisk is A or B, and, for equipment whose standard has no class split, simply `CAN ICES / NMB`. The standard-specific forms that Issue 1 required, such as "CAN ICES-3(B)/NMB-3(B)", "Canada ICES-005 (A) / NMB-005 (A)" and "CAN ICES-002 / NMB-002", remain compliant, and ISED says in terms that "a product already on the market need not be relabelled". Our guide to the [CAN ICES-003(B)/NMB-003(B) marking](/guides/can-ices-003-b-nmb-003-b-label/) walks through the ICES-003 version piece by piece.

Class follows section 3.5 and the definitions in section 2. Class A is equipment "highly unlikely to be used in a residential environment, including a home business", judged on price, marketing, functional design and the like. Everything that cannot be classified as Class A is Class B and must meet the tighter limits.

Placement has three routes. The default is on the equipment. Equipment whose largest dimension is 2.5 cm or less may carry the marking in the user manual instead, without asking ISED. Larger equipment may move the label off the device only with ISED approval under section 6.3.2.1. Two options added in Issue 2 are the QR code and the e-label. A QR code may stand in for the printed text, but it "shall contain the required product label" itself and "shall not be provided by means of a link to a website or refer to another location". Under Annex B, equipment with an integral display may present the label electronically if it can be reached in no more than three steps from the main menu, cannot be modified by the user, and a physical label still appears on the packaging at the point of import and sale.

## Host equipment: when the product has a radio inside

Section 3.6 is the part of ICES-Gen that foreign manufacturers most need to read, because it is where the declared world and the certified world meet. Host equipment is a product whose main function makes it interference-causing equipment but which "incorporates one or more radio apparatus modules". A smart thermostat, a point-of-sale terminal, an industrial gateway.

The rule has two branches. "If the interference-causing equipment incorporates certified Category I radio apparatus, then the equipment (host) usually does not require certification. Consult RSP-100 to determine if certification of the host is necessary." But "if the interference-causing equipment incorporates Category I radio apparatus modules or subassemblies/subcircuits that have not been certified, the combination ... i.e. the complete product model, shall be certified."

Certification is the trigger for the Canadian Representative. If the host relies on a certified module, integrated as the module's certificate holder instructs, the host itself is declared under ICES and the module's certification already carries its own representative. If the host must be certified, whether because the module is uncertified, modified, or integrated outside its conditions, the host manufacturer becomes an applicant under RSP-100, and an applicant outside Canada [needs a Canadian Representative under section 4.1](/guides/canadian-representative-requirement-rsp-100/). Either way, section 4.1 of ICES-Gen still requires the final product, module included, to meet RSS-Gen and the RF exposure requirements of RSS-102, and section 6.3.4 sends the host to RSS-Gen and RSP-100 for the certification-number label. The ICES marking on a host is optional if the entire device is certified and labelled with its IC number.

The [RSS-247 guide](/guides/rss-247-wifi-bluetooth-certification-canada/) covers the modular route from the radio side; [Do you need a Canadian Representative for ICES-003 SDoC?](/guides/ices-003-sdoc-canadian-representative/) covers the case where there is no radio at all.

## Composite and multifunction equipment, demo units and ISED's powers

Three shorter provisions round out the standard. Section 4.2 requires composite equipment, a system assembled from units that each comply, to comply as a system, and multifunction equipment to comply in each operating mode, including modes running simultaneously. Section 3.8 exempts equipment used "solely for purposes of research and development, experimentation, demonstration, or assessment of marketability" from demonstrating compliance, provided it is marked "Demo unit. Not to be leased, sold or offered for sale in Canada" in both languages. And section 3.4 preserves ISED's power under the Radiocommunication Act to determine that a model causes or is likely to cause interference, give notice, and thereby stop its manufacture, import and sale.

## Where the Canadian Representative fits, and where it does not

ICES-Gen does not use the words "Canadian Representative". The requirement to name one is in RSP-100 section 4.1 and applies to an applicant for certification of radio apparatus whose place of business is outside Canada. A product that is only ICES equipment, a monitor, a printer, an LED driver, has no application, no applicant, and no representative to appoint. The Canadian importer is the supplier, and the test report should be in the importer's hands or reachable from them.

Where a foreign manufacturer does need us is the radio: the certified module in the host, or the host itself when it must be certified. That is a single letter against a single IC certification number, issued the same business day, and it covers the certification for its ten-year term. If you are unsure which side of the line your product falls on, the [process overview](/guides/ised-certification-process-overview/) sets out the three routes side by side, and manufacturers in [Germany](/countries/germany/), the [United Kingdom](/countries/united-kingdom/), [China](/countries/china/), [Taiwan](/countries/taiwan/), [Japan](/countries/japan/), [South Korea](/countries/south-korea/), [India](/countries/india/) and the [United States](/countries/united-states/) will find country-specific notes on how ICES and RSS obligations line up with their home regime.

## What changed in Issue 2

For anyone holding a compliance file written against Issue 1, ISED's preface lists the substantive changes: the definition of "residential environment" was clarified and "composite equipment", "host equipment", "multifunction equipment" and "supplier" were added; a transition period was specified; host equipment requirements were updated in sections 3.6, 4.1 and 6.3.4; accessory requirements were clarified; calibration and test-site validation intervals were added; DC- and AC-operated equipment and external power supply testing were clarified; the label format was simplified; the QR-code option was added; and the e-labelling rules in Annex B were expanded. The section numbering also changed, so a file that cites "ICES-Gen section 5.3.2" for labelling is citing Issue 1 and should be updated to section 6.3.3.

<!--faq-->
### What is ICES-Gen?
ICES-Gen is ISED's general standard for interference-causing equipment, the non-radio side of electronic products. It sets the procedure that every specific ICES standard shares: who is responsible, how compliance is declared, what the test report must contain and what the label must say. The current edition is Issue 2, published February 23, 2024.

### Is ICES-Gen Issue 1 still accepted?
No. Section 3.1.2 of Issue 2 allowed compliance with either issue for one year after publication on ISED's website. That period ended February 23, 2025. Equipment still sold in Canada must comply with Issue 2, and test reports should be updated where the new requirements affect them.

### Does ICES-Gen require certification?
No. ICES equipment is Category II, which ICES-Gen says "is exempt from certification and registration". Compliance is by Supplier's Declaration of Conformity: the supplier tests, labels and keeps the report. The label on each unit is the declaration.

### Who is the "supplier" under ICES-Gen?
A person or entity located in Canada that manufactures, imports, distributes, leases, offers for sale or sells the equipment. Issue 1 called this the "responsible party". For a foreign-made product, the supplier is the Canadian importer or distributor.

### Does ICES-Gen require a Canadian Representative?
No. The Canadian Representative requirement is in RSP-100 section 4.1 and applies to certification of radio apparatus by an applicant outside Canada. If the product also contains a radio that must be certified, the representative is needed for that certification, not for the ICES declaration.

### How long must the ICES test report be kept?
For as long as the equipment is manufactured, imported, distributed, leased, offered for sale or sold in Canada, and it must be produced to ISED on request. If a new issue of the applicable ICES standard takes effect while the product is still on the market, the report must be updated to show compliance with the new issue.

### What does the ICES label have to say?
"Canada" or "CAN" plus a generic reference to the ICES standards in English and French, with the class where the applicable standard splits Class A and Class B, for example "CAN ICES (B) / NMB (B)". Older standard-specific forms such as "CAN ICES-3(B)/NMB-3(B)" remain compliant and products already on the market need not be relabelled.

### My product has a certified Wi-Fi module. Do I certify the whole product?
Usually not. If the host incorporates a certified Category I module, integrated as the module's certificate holder instructs, ICES-Gen section 3.6 says the host usually does not require certification, though RSP-100 should be consulted. If the module is uncertified, modified or integrated outside its conditions, the complete product must be certified, and a foreign applicant then needs a Canadian Representative.
<!--/faq-->

*Sources: ISED, [ICES-Gen Issue 2](https://ised-isde.canada.ca/site/spectrum-management-telecommunications/en/devices-and-equipment/interference-causing-equipment-standards-ices/ices-gen-general-requirements-compliance-interference-causing-equipment) (February 23, 2024, Gazette notice SMSE-014-23), Preface and sections 1, 2, 3.1, 3.3, 3.4, 3.5, 3.6, 3.8, 4.1, 4.2, 4.5, 4.6, 5, 6.3 and Annexes A and B; ISED, ICES-Gen Issue 1 with Amendment 1 (February 2021), section 3.2; ISED, RSP-100 section 4.1; Radiocommunication Regulations, subsections 21(1) and 21(5).*
