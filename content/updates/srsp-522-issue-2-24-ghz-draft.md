---
title: SRSP-522 Issue 2 Draft: 24 GHz Local Licensed Systems
description: ISED's draft SRSP-522 Issue 2 extends non-competitive local licensing to 24.25-25.1 GHz. Comments close January 15, 2027, and RSS-193 has not caught up.
h1: Draft SRSP-522 Issue 2 opens 24.25–25.1 GHz — before the equipment standard exists
short: SRSP-522 draft
type: update
date: 2026-10-26
updated: 2026-10-26
---

<div class="answer" markdown="1">
On October 19, 2026 ISED put a draft of <a href="https://www.rabc-cccr.ca/ised-standard-radio-system-plan-srsp-522-issue-2-technical-requirements-for-non-competitive-local-licensed-systems-including-fixed-and-or-mobile-systems-and-flexible-use-broadband-systems-in-the/" rel="noopener">SRSP-522, Issue 2</a> out for comment through the Radio Advisory Board of Canada. Issue 1 covers one band: 27.5&ndash;28.35 GHz. Issue 2 adds a second, 24.25&ndash;25.1 GHz — the 850 MHz ISED decided in May to release through non-competitive local licensing. Comments are due January 15, 2027. A standard radio system plan binds the licensee who deploys the system, not the applicant who certifies the radio, so nothing in the draft changes your certification file directly. The thing worth noticing is the order. <a href="https://ised-isde.canada.ca/site/spectrum-management-telecommunications/en/devices-and-equipment/radio-equipment-standards/rss-193-flexible-use-broadband-equipment-operating-band-275-2835-ghz" rel="noopener">RSS-193</a>, the equipment standard SRSP-522 points to, still stops at 27.5 GHz. The band that now has a draft licensing plan has no published standard to certify equipment against.
</div>

## What changed

SRSP-522 sets the minimum technical requirements — power limits, antenna heights, licence area sizes, coexistence with other services — for non-competitive local licensed fixed, mobile and flexible use broadband systems. Issue 1 was published in September 2025 and divides 27.5&ndash;28.35 GHz into 17 unpaired 50 MHz blocks for time division duplex systems. Issue 2 keeps that band and extends the plan to 24.25&ndash;25.1 GHz. RABC's posting flags the new material in the draft in yellow and says that new material is the scope of the consultation; the draft itself is a Word document on RABC's site, and the technical detail for the new band is in it rather than on the page.

The 24 GHz half of this comes from ISED's decision of May 14, 2026 on repurposing the 26 GHz band (SPB-003-26). That decision designated 24.25&ndash;26.5 GHz for flexible use, set aside 850 MHz at 24.25&ndash;25.1 GHz for non-competitive local licensing, and sent the 2.4 GHz above it to auction with the 38 GHz band. It also stopped new first-come, first-served site-specific fixed licence applications across 24.25&ndash;26.5 GHz. The draft SRSP-522 is the technical plan that decision promised.

## The equipment standard is a document behind

Section 3.2 of RSS-193 classifies the equipment it covers as Category I: it shall be certified, either by ISED's Certification and Engineering Bureau or by a recognised certification body. RSS-193 Issue 1 was published July 11, 2025 under notice SMSE-005-25, and its title names the band it covers — 27.5&ndash;28.35 GHz. Nothing in it reaches 24 GHz.

ISED consulted this summer on a draft [RSS-193, Issue 2](/updates/rss-193-issue-2-consultation-mmwave/) that would widen the standard to 24.25&ndash;28.35 GHz and 37.6&ndash;40.0 GHz. Comments closed September 21, 2026. As of today the ISED page for RSS-193 still shows Issue 1 as the standard in force. So a licensing plan for 24.25&ndash;25.1 GHz is out for comment until January, while the standard a manufacturer would certify against for that band is finished being consulted on and not yet published.

## What it means if you manufacture outside Canada

For planning, the date that actually matters is the publication of RSS-193 Issue 2, not the close of this consultation. That publication is what lets a certification body accept a 24 GHz flexible use application at all, and it starts the paperwork that applies to you: Category I equipment needs a certification, and under [RSP-100 section 4.1](/guides/canadian-representative-requirement-rsp-100/) an applicant whose company address is outside Canada needs a Canadian Representative identified on a signed Application and Agreement for Certification Services, held for as long as the product is offered in Canada.

SRSP-522 itself will not ask anything of you. Your Canadian customer — the licensee deploying the system — is the one who has to meet it, and the figures in it tell that customer whether your radio is deployable here at the power and antenna height the business case assumes. A limit settled in January may decide whether there is a Canadian buyer for the radio you are designing now. That is the reason to read a system plan you are not bound by.

## What to do

If you build flexible use broadband equipment for these bands, download the draft from RABC and comment by January 15, 2027; comments go through RABC rather than directly to ISED. Check which band edges your product actually sits on, because 24.25&ndash;25.1 GHz, 25.1&ndash;27.5 GHz and 27.5&ndash;28.35 GHz are now on three different licensing paths with one published equipment standard between them, and the roughly 850 MHz at the bottom is the piece most likely to move first. And if you expect to file a Canadian certification once RSS-193 Issue 2 lands, settle the representative appointment before the certification body asks for it — [the letter](/guides/attestation-letter-required-fields/) is the part of the application that depends on someone outside your company.

<!--faq-->
### Does SRSP-522 apply to my certification application?

No. SRSP-522 is a standard radio system plan: it sets technical requirements for the systems a licensee deploys. Your certification is granted against a radio standards specification — RSS-193 for flexible use broadband equipment in these bands, together with RSS-Gen and RSS-102 — under the procedures in RSP-100. The system plan matters to you commercially, not procedurally.

### Can I certify a 24 GHz flexible use radio in Canada now?

Not under RSS-193. Issue 1, in force since July 11, 2025, covers 27.5&ndash;28.35 GHz only. The draft Issue 2 would extend the standard to 24.25&ndash;28.35 GHz and 37.6&ndash;40.0 GHz; its consultation closed September 21, 2026 and ISED has not published it. Which standard applies to a particular product is a question for your [certification body](/guides/how-to-choose-an-ised-certification-body-and-test-lab/).

### Will a 24 GHz certification need a Canadian Representative?

If the equipment is Category I and your company address is outside Canada, yes. The requirement comes from RSP-100 section 4.1 and attaches to the applicant, not to the band or the standard. See [how to appoint one](/guides/how-to-appoint-a-canadian-representative/).
<!--/faq-->
