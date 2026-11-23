---
title: RSS-193 Issue 2 Is Published: The Six-Month Clock Starts
description: ISED published RSS-193 Issue 2 on October 29, 2026. The standard now covers 24.25-28.35 GHz and 37.6-40.0 GHz, and Issue 1 filings are accepted for six months.
h1: RSS-193 Issue 2 is published: six months to move your mmWave filings over
short: RSS-193 Issue 2
type: update
date: 2026-11-23
updated: 2026-11-23
---

<div class="answer" markdown="1">
ISED published [RSS-193, Issue 2](https://ised-isde.canada.ca/site/spectrum-management-telecommunications/en/devices-and-equipment/radio-equipment-standards/rss-193-flexible-use-broadband-equipment-operating-band-275-2835-ghz) on October 29, 2026. It replaces Issue 1, which was published on July 11, 2025. Issue 1 covered one band: 27.5–28.35 GHz. Issue 2 covers 24.25–28.35 GHz and 37.6–40.0 GHz, which takes the standard from 850 MHz of certifiable spectrum to 6,500 MHz. A transition period of six months runs from the publication date. During it ISED accepts applications under either issue; after it, only Issue 2. Equipment under RSS-193 stays Category I, so it must be certified, and an applicant whose company address sits outside Canada still needs a [Canadian Representative](/guides/canadian-representative-requirement-rsp-100/) under RSP-100 before the certificate can issue.
</div>

## What changed

We [covered the draft in August](/updates/rss-193-issue-2-consultation-mmwave/), when comments were still open through the Radio Advisory Board of Canada. The final standard does what the draft proposed. Its preface records two changes from Issue 1: technical requirements added for equipment in 24.25–27.5 GHz and 37.6–40.0 GHz, and editorial clean-up throughout. The equipment classes are unchanged — base station, fixed service, and subscriber equipment, which splits into fixed and mobile.

Section 5.5 sets the e.i.r.p. ceilings by class. Base station and fixed service equipment, adaptive antenna system or not, run to 75 dBm per 100 MHz, and the ceiling drops proportionally where the channel is narrower than 100 MHz. Fixed subscriber equipment runs to 55 dBm per channel bandwidth and mobile subscriber equipment to 43 dBm. Section 5.6 then adds a limit that bites outside the band entirely. For equipment in 24.25–27.5 GHz, unwanted emissions in any 200 MHz within 23.6–24.0 GHz must not exceed −39 dBW for base station equipment or −35 dBW for mobile subscriber equipment. That adjacent slice is passive-sensing spectrum, and the limit protects it.

Section 6 carries the requirement most likely to reach the people who print things. Base station equipment in 24.45–24.65 GHz must bear a label that reads "Operation within 24.45-24.65 GHz is intended for indoor use only", or carry that statement in the user manual. Two hundred megahertz inside a 4.1 GHz band — with its own printed wording.

## What it means for applicants

If your mmWave equipment is built for 27.5–28.35 GHz, nothing forces your hand today. The six-month window closes around the end of April 2027 — but ISED ties the period to the publication date rather than naming a calendar day, so confirm the cut-off with your certification body before you plan a test campaign against it. Applications filed after it closes have to meet Issue 2.

If your equipment operates in 24.25–27.5 GHz or 37.6–40.0 GHz, the change runs the other way. Those bands had no technical requirements in RSS-193 until October 29. They do now — which means a published certification path exists for radios you may already be shipping in the United States.

The 24.45–24.65 GHz label requirement is worth separating out, because it is exactly the sort of thing that gets found late. A certification body reviews the label and the manual as part of the application. If your base station tunes across 24.45–24.65 GHz and the artwork does not carry the indoor-use statement, the filing stalls on a document rather than on a measurement. Our [label and manual review](/label-and-manual-review/) exists for this kind of check.

None of the certification mechanics change. Test work goes through an accredited lab, the application goes through a [certification body or ISED's Certification and Engineering Bureau](/guides/representative-vs-certification-body-vs-test-lab/), and you appoint the representative per certification number. That last point probably matters more here than usual: equipment newly certifiable in 24 GHz or 39 GHz means new certification numbers, and each one needs its own letter.

## What to do

Ask your certification body which issue your open applications are filed under, and what they will accept as the window narrows. For products in the newly covered bands, read sections 5.5, 5.6 and 6 against your own test data before you commission anything — the 23.6–24.0 GHz limit in particular is easy to miss, because it falls outside the band you are actually testing. Check the artwork and the manual for any base station that reaches 24.45–24.65 GHz. And if you are filing from outside Canada, [appoint your representative](/canadian-representative-service/) before the application goes in rather than after, so the certificate is not waiting on a signature.

<!--faq-->
### When does the RSS-193 Issue 2 transition period end?
ISED provides a transition of six months from the publication date of October 29, 2026, which puts the end around late April 2027. The published standard states the period rather than a calendar date, so confirm the exact cut-off with your certification body before you rely on it.

### Can I still certify equipment under RSS-193 Issue 1?
Yes, during the transition period. ISED accepts applications under either Issue 1 or Issue 2 while it runs. Once it ends, only applications under Issue 2 are accepted.

### Does RSS-193 Issue 2 change the Canadian Representative requirement?
No. The requirement comes from RSP-100 and applies to any certification applicant whose company address is outside Canada, whichever RSS the equipment is certified against. Equipment under RSS-193 is Category I, so it must be certified, and you appoint a representative for each certification number.
<!--/faq-->
