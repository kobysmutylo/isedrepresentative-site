---
title: ISED Family Certification: One IC Number for Many Models
description: RSP-100 section 9.3 lets multiple product versions share one ISED certification number, and one representative letter. The four conditions, and what breaks a family.
h1: Family certification under RSP-100: one IC number across your models, and the rule that breaks it
short: Family certification
type: update
date: 2026-11-09
updated: 2026-11-09
---

<div class="answer" markdown="1">
Section 9.3 of <a href="https://ised-isde.canada.ca/site/spectrum-management-telecommunications/en/devices-and-equipment/radio-standards-procedures-rsp/rsp-100-certification-radio-apparatus-and-broadcasting-equipment" rel="noopener">RSP-100</a> permits multiple versions of a product design to be certified under a single family certification service with one ISED certification number. It sets no cap on how many versions. It sets four conditions, and the one that catches manufacturers is the second circuit board: two or more versions with two or more PCB designs enabling different frequency bands or technologies, inside identical enclosures, are not permitted in a family certification. That is exactly the difference between one IC number and two — and because the Canadian Representative is appointed per certification, it is the difference between one representative letter and two.
</div>

## What section 9.3 allows

RSP-100, Issue 12 of August 2019, remains the current procedure. Section 9.3 states the permission in a single sentence — multiple versions of a product design may be certified under a single family certification service with one ISED certification number — and then conditions it on four things. Every variant you put in the family has to meet all four.

The first condition is cosmetic. The enclosure and general appearance of all product versions in the family shall be identical except for enclosure colour and minor external cosmetic differences. Your white one and your black one are the same product. A wall-mount version with a different footprint is not.

The second condition describes the arrangement the whole rule is built around: two or more versions of a product with one printed circuit board design, with different frequency bands or technologies enabled by software. One board, different radios turned on in firmware. A single hardware design that you ship as a 2.4 GHz-only SKU in one market and a dual-band SKU in another sits squarely inside it.

The third condition covers the later model. A new version of a certified product may have minor PCB modifications to improve existing frequency bands or technologies, or to add non-RF features. Improve, not extend. A revised board that tightens your existing radio or adds a second USB port stays in the family; a revised board that opens a band the family never had is a new certification, and we set out why in [permissive changes, Class I to Class IV](/updates/permissive-changes-rsp-100-class-i-to-iv/).

The fourth condition is the backstop. All versions in the family shall be identical, or differ only as permitted under Class I and Class III permissive changes — non-RF changes, and firmware changes that alter RF characteristics with a new FVIN. A Class II change — hardware that alters RF characteristics — falls outside the family unless ISED says otherwise. Section 9.3 is genuinely strict about how: an approval from ISED for an exceptional circumstance, where your versions differ in a way that falls under Class II permissive changes, shall be submitted with the application. You ask first, and you file the answer with everything else. There is no retroactive version of that step.

## The rule that breaks a family

Read the four conditions together and one arrangement is ruled out by name. Two or more versions of a product with two or more PCB designs with different frequency bands or technologies, within identical enclosures, are not permitted within a family certification.

This is the arrangement a lot of product lines actually have. The enclosure is tooled once because tooling is expensive. Inside it, the North American SKU gets one board and the European SKU gets another, because the radios differ enough that software could not do the job. From the outside your two products are indistinguishable, which is exactly why manufacturers assume they certify as one. RSP-100 looks at the boards, not the housing.

Two PCB designs means two families: one per board, each covering its own software variants. Two IC certification numbers, two REL entries, two sets of labels and manuals, and two of every fee in the chain — what ISED charges to list, what your certification body charges to review, and, if your company has no address in Canada, two Canadian Representative letters.

## The legacy exemption, and what ISED stopped accepting

Section 9.3.2 keeps one combination alive that the four conditions would otherwise kill. ISED will accept one certification or registration number under a family for a base telephone unit and one or more wireless handsets sold with the base unit. The base unit and the handset cannot share an HVIN. Only identical handsets may share one HVIN between themselves.

Everything else sold as a set lost that treatment. Different products sold together as a system — ISED's examples are baby monitor systems and speaker systems — will no longer be accepted under a family. A unique ISED certification number is required for each transmitter. If you sell a camera and a parent unit in one box, or a soundbar with wireless satellites, that is one certification per transmitting device, and for a foreign applicant one representative letter per certification. Your buyer sees one box and one price. ISED counts the transmitters inside it.

## What the family certification asks you to file

Section 9.3.1 opens with a precondition that is easy to trip over on a refiling. You may file the application provided you have never been granted certification for the assigned HVINs or ISED certification number in it. Then four things go in. At least one field — PMN, HVIN or FVIN — shall be unique to identify each different version. A detailed description of how your unique versions are alike and how they differ, in hardware and in software: RF characteristics, circuitry design, function. The HMN, where a module was assessed for compliance in a host. And the documents the checklist in Form C asks for.

That description decides the file. Your certification body reads the four conditions against your actual bill of materials and answers the only question that matters here: is this one product in several versions, or several products.

Adding a version later is not free of the standard, either. ISED's Certification and Engineering Bureau has said that a new product version added to an existing family through a Class I permissive change must show compliance with the current published version of the standard — by a declaration where no new requirement affects the product, or by a supplementary test report where one does. For RSS-Gen that clock runs to July 30, 2027, as we covered in [what the RSS-Gen Issue 6 transition means for your test reports](/updates/rss-gen-issue-6-existing-certifications/).

## What it does to the representative letter

Section 4.1 of RSP-100 requires a Canadian representative when the applicant's company address is not within Canada, and it hangs that on the Application and Agreement for Certification Services behind a certification. One certification, one appointment. A family certification covering eleven of your SKUs is still one certification, so it is still one letter, and every PMN, HVIN and FVIN listed under that number is inside it. Our [one letter per IC ID](/guides/one-representative-letter-per-ic-id/) guide works through the boundaries.

Getting it wrong costs money in both directions. Split what could have been one family into separate applications and you pay for representation you did not need. Push products into a family where section 9.3 does not permit them and your certification body sends the file back, usually after you have paid for the testing and built the label artwork.

## What to do

- **Count PCB designs, not SKUs.** Your housing is irrelevant to section 9.3. If two of your variants carry different bands on different boards, they are two certifications however identical they look on a shelf.
- **Decide the family before the lab quotes.** The description 9.3.1 asks for has to reconcile every variant against the four conditions, and your certification body wants it when you file, not after.
- **If two versions differ by a Class II change, get ISED's approval first.** Section 9.3 requires that approval to go in with the application. There is simply no way to add it afterwards.
- **Do not put a system in a family.** A multi-transmitter set needs a certification number per transmitter, whatever your packaging says.
- **Make the distinguishing field retrievable.** At least one of PMN, HVIN or FVIN must be unique per version, and where firmware is the only difference the FVIN has to be readable from the product itself. The [labelling requirements guide](/guides/canadian-radio-equipment-labelling-requirements/) sets out what has to appear where.
- **Budget one representative letter per certification number.** Not per model, and not per market. See [the RSP-100 requirement](/guides/canadian-representative-requirement-rsp-100/).

<div class="source" markdown="1">
**Sources.** ISED, <a href="https://ised-isde.canada.ca/site/spectrum-management-telecommunications/en/devices-and-equipment/radio-standards-procedures-rsp/rsp-100-certification-radio-apparatus-and-broadcasting-equipment" rel="noopener">RSP-100, Certification of Radio Apparatus and Broadcasting Equipment, Issue 12</a> (August 2019), sections 4.1, 9.1, 9.3, 9.3.1, 9.3.2 and 10.1 to 10.4, and Form C. ISED Certification and Engineering Bureau, <a href="https://ised-isde.canada.ca/site/certification-engineering-bureau/en/common-questions-and-answers" rel="noopener">Common questions and answers</a>, on compliance with the current issue of a standard when a version is added to an existing family.
</div>

<!--faq-->
### How many models can one ISED family certification cover?
RSP-100 section 9.3 states no numeric limit. The constraint is qualitative: every version must satisfy the four conditions in section 9.3 — identical enclosure and general appearance except for colour and minor cosmetic differences, one PCB design with bands or technologies enabled by software, minor PCB modifications only to improve existing bands or add non-RF features, and no differences beyond those permitted under Class I and Class III permissive changes.

### Can two different circuit boards be certified in the same family?
No, where the boards enable different frequency bands or technologies and sit inside identical enclosures. Section 9.3 rules that out by name. Each PCB design needs certifying on its own, with its own ISED certification number.

### Does a family certification need more than one Canadian Representative letter?
No. Under section 4.1 the appointment attaches to the applicant who files, and a family is one application with one ISED certification number. Every model, HVIN, PMN and FVIN listed under that number is covered by the same letter.

### Can a baby monitor or a speaker system be certified as a family?
No. Section 9.3.2 says different products sold together as a system will no longer be accepted under a family certification, and it names baby monitor systems and speaker systems as its examples. A unique ISED certification number is required for each transmitter.

### What happens when I add a model to an existing family?
It is normally a Class I permissive change, which you file through your certification body against the certification you already hold. ISED's Certification and Engineering Bureau has said the added version must show compliance with the current published version of the standard, by a declaration of compliance or a supplementary test report. No new IC number is created, so no new representative letter is needed.
<!--/faq-->

If you need a Canadian Representative appointed for an ISED certification, the [Canadian Representative service](/canadian-representative-service/) is US$499 per certification, whatever the number of models listed under it; see [pricing](/pricing/).
