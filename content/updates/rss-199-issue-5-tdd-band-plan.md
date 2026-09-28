---
title: RSS-199 Issue 5 Draft: A TDD Band Plan for 2500-2690 MHz
description: ISED's draft RSS-199 Issue 5 adds an all-TDD band plan across 2500-2690 MHz in 38 unpaired 5 MHz blocks. Comments through RABC close December 4, 2026.
h1: RSS-199 Issue 5 draft: an all-TDD band plan for the whole 2500–2690 MHz band
short: RSS-199 draft
type: update
date: 2026-09-28
updated: 2026-09-28
---

<div class="answer" markdown="1">
ISED is consulting on a draft of <a href="https://www.rabc-cccr.ca/ised-radio-standards-specification-rss-199-issue-5-broadband-radio-service-brs-equipment-operating-in-the-band-2500-2690-mhz/" rel="noopener">RSS-199, Issue 5</a>, the certification standard for Broadband Radio Service equipment in 2500–2690 MHz. The draft is dated September 22, 2026 and adds exactly one substantive thing — an alternative band plan that divides the entire band into 38 unpaired 5 MHz blocks, which only equipment using time division duplexing may use. A companion draft, SRSP-517 Issue 3, carries the detailed plan. Comments are due no later than December 4, 2026 through the Radio Advisory Board of Canada. Nothing in the draft changes how your equipment gets certified: it stays Category I, so certification is mandatory, and an applicant with no address in Canada still needs a [Canadian Representative](/guides/canadian-representative-requirement-rsp-100/) under RSP-100.
</div>

## What changed

The standard in force is <a href="https://ised-isde.canada.ca/site/spectrum-management-telecommunications/en/devices-and-equipment/radio-standards-procedures-rsp/rss-199-broadband-radio-service-brs-equipment-operating-band-2500-2690-mhz" rel="noopener">RSS-199 Issue 4</a>, published in July 2023 under Gazette notice SMSE-009-23. It works against the band plan in <a href="https://ised-isde.canada.ca/site/spectrum-management-telecommunications/en/devices-and-equipment/standard-radio-system-plans/srsp-517-technical-requirements-broadband-radio-service-brs-band-2500-2690-mhz" rel="noopener">SRSP-517 Issue 2</a> of the same month, and that plan is mostly paired: seven 10+10 MHz FDD blocks, the lower halves in 2500–2570 MHz and the upper halves in 2620–2690 MHz, with two 25 MHz unpaired blocks in the middle at 2570–2620 MHz. A radio that duplexes in time rather than in frequency has 50 MHz to work with.

The draft's own list of changes from Issue 4 runs to two lines. The first: "added alternative band plan for TDD equipment operating in the band 2500-2690 MHz." The second is editorial changes and clarifications. The alternative plan appears in Table 3 as 38 unpaired blocks of 5 MHz each, labelled A1 at 2500–2505 MHz through U2 at 2685–2690 MHz — and the draft is exact about who may use it: "Only equipment employing time division duplexing (TDD) technology shall be permitted to use this band plan option."

The draft also proposes the transition ISED normally uses for an RSS. Six months from the publication date, applications under either Issue 5 or Issue 4 are accepted. After that, Issue 5 only.

## What it means for manufacturers

RSS-199 covers base stations (active antenna systems included), fixed service equipment, fixed subscriber equipment and mobile subscriber equipment. All of it is Category I and must be certified before you can market it in Canada, either by a recognised [certification body](/guides/representative-vs-certification-body-vs-test-lab/) or by ISED's Certification and Engineering Bureau. The band is licensed, so your buyer needs a spectrum licence under subsection 4(1) of the *Radiocommunication Act*. Your certification does not give them one.

If you build 2.5 GHz TDD radios for other markets, this draft is probably the part of Canada's rules you have been waiting on. The paired plan asks a full-band TDD radio to be described against a channel arrangement it does not actually use; the alternative plan describes 190 MHz the way the radio operates. Read it as an option rather than a replacement. The paired blocks stay, and you can only take the unpaired option if your equipment duplexes in time.

The test burden is unchanged. It is worth knowing before you book lab time. Equipment certified under RSS-199 must also meet RSS-Gen — and the draft requires testing for every channel bandwidth you specify. Multi-carrier equipment is tested at both the maximum and the minimum number of carriers. Unwanted emissions are measured and reported at two channel frequencies, one as close as possible to the low end of the equipment's operating frequency range and one as close as possible to the high end. Declaring the full 190 MHz means declaring a wider range than a product confined to the middle blocks, and the emission measurements follow your declaration.

## What to do

If the draft genuinely touches a product line, read it and comment. The consultation runs through the <a href="https://www.rabc-cccr.ca/ised-radio-standards-specification-rss-199-issue-5-broadband-radio-service-brs-equipment-operating-in-the-band-2500-2690-mhz/" rel="noopener">RABC consultation page</a> until December 4, 2026, and the draft also names ISED's Standard Change Request form and the Regulatory Standards Directorate as routes for comment. Read SRSP-517 Issue 3 beside it, since the detailed band plan lives there rather than in RSS-199.

If you are planning a Canadian launch, time the test campaign against the final publication rather than the draft, and treat the six months after publication as your window for moving applications onto Issue 5. The administrative pieces can be settled well ahead of the filing: an [ISED company number](/guides/ised-company-number/) and, if you are outside Canada, the [Canadian Representative appointment](/canadian-representative-service/) your certification body will ask for. This is the second consultation of the quarter aimed at 5G hardware — the [RSS-193 Issue 2 draft](/updates/rss-193-issue-2-consultation-mmwave/) for the 24 GHz and 39 GHz bands closed on September 21 — so a compliance team with radios in both ranges arguably has one exercise here, not two.

<!--faq-->
### Can I certify a full-band TDD radio for 2500–2690 MHz in Canada today?
The plan in force gives unpaired TDD operation two 25 MHz blocks at 2570–2620 MHz. The all-TDD alternative across the full band sits in the draft Issue 5, which is not in force. Ask your certification body what is possible for your radio under Issue 4 in the meantime.

### Does RSS-199 Issue 5 change the Canadian Representative requirement?
No. The requirement sits in RSP-100 and applies to any certification applicant whose address is outside Canada, whatever standard the equipment is certified under. BRS equipment is Category I, so certification is mandatory and the representative requirement comes with it.

### When would Issue 5 take effect?
ISED reviews the comments after December 4, 2026 and publishes on its own schedule. The draft proposes six months from publication during which applications under Issue 4 or Issue 5 are both accepted, then Issue 5 alone.
<!--/faq-->
