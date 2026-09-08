---
title: ISED Permissive Changes: Class I to IV Under RSP-100 Explained
description: Which product changes need a notice to ISED after certification, which need a new IC number, and what each class does to your Canadian Representative letter. RSP-100 section 10.
h1: Permissive changes after ISED certification: Class I to Class IV, and what each does to your representative letter
short: Permissive changes
type: update
date: 2026-09-08
updated: 2026-09-08
---

<div class="answer" markdown="1">
[RSP-100 section 10](https://ised-isde.canada.ca/site/spectrum-management-telecommunications/en/devices-and-equipment/radio-standards-procedures-rsp/rsp-100-certification-radio-apparatus-and-broadcasting-equipment) sorts changes to a certified product into four classes. Class I (no effect on RF or emissions) needs no notice to ISED unless you also change the HVIN or PMN. Class II (hardware that changes RF characteristics), Class III (firmware that changes RF characteristics, with a new FVIN) and Class IV (a certified module in a new host, with the HMN) each need a notice filed through a certification body. None of the four creates a new IC certification number, so none needs a new Canadian Representative letter — the appointment follows the certificate. The one change RSP-100 refuses as a permissive change is adding a frequency band by hardware; that is a new certification, and for an applicant outside Canada it needs its own letter.
</div>

## The rule the four classes sit under

Section 10 opens with one sentence that governs everything after it: "Any modifications to a certified product may require recertification with ISED. The certificate holder shall inform the certification body (CB) or ISED of any changes that may affect compliance with the technical requirements of the regulations under which the product was originally certified." The four classes are ISED's way of telling you, in advance, which changes it will accept without a fresh certification, and what paperwork each one costs. The current text is RSP-100 Issue 12 (August 2019).

## Class I — no notice, one condition

A Class I permissive change (C1PC) covers "modifications that do not change the fundamental RF characteristics and that do not degrade the unwanted emissions of the certified product," and modifications that "do not change physical characteristics significantly." A new capacitor value away from the radio, a different plastic colour, a re-laid power section — these stay in Class I if the radio's measured behaviour does not move. Most engineering changes are Class I.

"Notice to ISED is not required for Class I modifications unless the HVIN or PMN is also modified." The condition matters more than it looks. Companies rename products constantly, actually far more often than they change the radio, and a marketing rename is a PMN change — which turns a silent Class I change into one that must be notified. The section also adds that the certificate holder "shall ensure that the product continues to remain compliant as per the original RSS-102 attestation on file," so an RF-exposure assessment done for the original enclosure has to still hold for the new one. For final products built from several separately certified modules, RSP-100 allows Class I treatment where the device operates beyond 20 cm from the body, the modules were certified stand-alone, and the combined exposure ratio at 20 cm stays below 1.0.

## Class II — hardware that moves the RF, filed through a CB

Class II (C2PC) is for "hardware modifications to the certified product that affect fundamental RF characteristics and/or degrade the unwanted emissions," provided "the requirements established in the applicable RSS or BETS in the original certification are still met." A new antenna, a new power amplifier, a shielding change that shifts spurious emissions — still within the limits, but not the numbers ISED has on file. A significant change to physical characteristics and "any changes to the PMN or HVIN" also fall here. "Notice to ISED is required for Class II permissive changes," and certification bodies expect test data covering what moved. The one exclusion is absolute. Adding a frequency band by hardware is not a permissive change of any class. That product is certified again, under a new IC number.

## Class III — firmware, new FVIN

Class III (C3PC) covers "firmware modifications to a certified product that affect the RF characteristics of the product" and "firmware modifications to enable frequency bands without hardware modification." The asymmetry with Class II is deliberate: a band the hardware can already reach may be switched on by firmware and notified as Class III; a band that needs new hardware cannot be added at all. "Notice to ISED is required for Class III permissive changes and a new and unique FVIN shall be provided." ISED will also, voluntarily, take applications for firmware that *disables* a band. Software-defined radios, Wi-Fi modules with regional band tables and cellular modems get most of their post-certification traffic here.

## Class IV — a certified module in a new host

Class IV (C4PC) exists for modular approvals: "A certified module(s) (LMA or MA) that is integrated into a new host product that results in changes to the original reported RF emissions characteristics and/or RF exposure assessment is permitted under C4PC, with or without firmware modification." The notice must supply the HMN — the host marketing name — so the host appears against the module's certification on the [Radio Equipment List](/updates/reading-your-ised-rel-listing/). This is the class integrators most often miss: they assume the module's certificate covers any host, and it does only where the host does not change what was reported. See the [RF modules](/industries/rf-modules/) page for the split between module maker and integrator.

## What each class does to the Canadian Representative letter

Nothing, in three of the four. This surprises people. The representative under [RSP-100 section 4.1](/guides/canadian-representative-requirement-rsp-100/) is recorded on the Application and Agreement for Certification Services for the certified product, and the agreement has to stay valid "for as long as the certified product is offered on the Canadian market." A Class I, II or III change keeps the same IC number, so the same appointment and the same letter continue. If the change adds models or an HVIN, ask us to reissue the letter with the updated list — [revisions are free](/pricing/), with no time limit — but the appointment itself does not move.

Class IV is the one to think about. The notice is filed on the module maker's certificate, so it is the module maker's representative that answers for it. The host integrator needs a representative only if it holds a certification of its own, and a Class IV notice is not one. We see integrators ordering letters they do not need; the [one letter per IC ID](/guides/one-representative-letter-per-ic-id/) guide sets out who is the applicant in each configuration.

The new-band case is different. It is a new certification. A new IC number means a new application, a new agreement, and, for an applicant outside Canada, a new letter at US$499. A [multiple listing](https://ised-isde.canada.ca/site/spectrum-management-telecommunications/en/devices-and-equipment/radio-standards-procedures-rsp/rsp-100-certification-radio-apparatus-and-broadcasting-equipment) under section 11.5 works the same way. There a distributor or OEM customer takes its own IC number on the strength of your certification; the new applicant is the certificate holder, and if its address is outside Canada it needs its own representative.

## What to do before the engineering change ships

Ask your certification body to classify the change before production, not after. The CB decides the class, and it will want the delta test data for Class II and III in hand. If the change touches the PMN or HVIN, treat it as notifiable even when the electronics are unchanged. Keep the RSS-102 exposure assessment in the file current; Class I depends on it. And when the CB confirms which models and HVINs now sit under the IC number, send us the list so the [representative letter](/canadian-representative-service/) in the certification file matches the REL.

<div class="source" markdown="1">
**Sources.** [RSP-100, Issue 12 (August 2019)](https://ised-isde.canada.ca/site/spectrum-management-telecommunications/en/devices-and-equipment/radio-standards-procedures-rsp/rsp-100-certification-radio-apparatus-and-broadcasting-equipment), section 4.1 (Canadian representative), section 9.3 (family certification), section 10 (modification of certified products, 10.1–10.4), section 11.5 (multiple listing of certification).
</div>

<!--faq-->
### Does a permissive change need a new Canadian Representative letter?
No. Class I to IV permissive changes keep the same IC certification number, and the representative is recorded against that certification. If the change adds models or HVINs, have the letter reissued with the updated list; the appointment is unchanged.

### Can I add a new frequency band as a permissive change?
Only by firmware, on hardware that already reaches the band, as a Class III change with a new FVIN. Adding a band by hardware modification is not permitted as a permissive change under RSP-100 section 10.2 and requires a new certification.

### We only renamed the product. Do we have to tell ISED?
Yes. A change to the PMN or HVIN must be notified even where nothing in the electronics changed. RSP-100 section 10.1 excludes HVIN and PMN changes from the no-notice rule for Class I.

### Who files the permissive change notice?
The certificate holder is responsible under section 10 for informing the CB or ISED; in practice the notice and supporting test data go through a certification body, the same route as the original application.
<!--/faq-->

Related reading: [Does each IC ID need a separate Canadian Representative letter?](/guides/one-representative-letter-per-ic-id/), [Changing your Canadian Representative](/guides/changing-your-canadian-representative/), and [How to read your Radio Equipment List entry](/updates/reading-your-ised-rel-listing/).
