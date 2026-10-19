---
title: RSS-247 Amendment 1: DFS timing in the 5600-5650 MHz band
description: ISED's October 8, 2026 amendment to RSS-247 writes ETSI's 10-minute channel availability check and 1-second closing transmission time into the 5600-5650 MHz band.
h1: RSS-247 Amendment 1: the DFS clock changes for 5600-5650 MHz
short: RSS-247 Amendment 1
type: update
date: 2026-10-19
updated: 2026-10-19
---

<div class="answer" markdown="1">
ISED amended <a href="https://ised-isde.canada.ca/site/spectrum-management-telecommunications/en/devices-and-equipment/radio-equipment-standards/radio-standards-specifications-rss/rss-247-digital-transmission-systems-dtss-frequency-hopping-systems-fhss-and-licence-exempt-local" rel="noopener">RSS-247</a> on October 8, 2026. Amendment 1 changes one section — 7.3.6.3, the operational requirements for dynamic frequency selection. It adds two numbers. They bind only where your device's emission bandwidth falls completely or partly in the 5600&ndash;5650 MHz band: a channel availability check time of 10 minutes rather than 60 seconds, and a channel closing transmission time of 1 second rather than the 200 ms plus a 60 ms aggregate the rest of the section states. Both apply when the ETSI EN 301 893 test procedure is used, and for that band it is the only procedure ISED accepts. If your 5 GHz radio stays out of 5600&ndash;5650 MHz, nothing in the amendment reaches your file. The Canadian Representative requirement in RSP-100 is untouched.
</div>

## What changed

Issue 4 of RSS-247, published July 24, 2025, opened a segment Canada had kept closed. The first technical change listed in its preface is the removal of the restriction on operation between 5600 MHz and 5650 MHz — the part of the 5 GHz band carrying Wi-Fi channels 120, 124 and 128, where meteorological radars also operate. Section 7.3.6.1 attached a condition to the opening. A device operating in 5600&ndash;5650 MHz may demonstrate DFS compliance only through the ETSI EN 301 893 procedure, not through FCC KDB Procedure 905462. A device tested to the KDB must operate exclusively within 5250&ndash;5350 MHz, 5470&ndash;5600 MHz, 5650&ndash;5725 MHz, or some combination of those.

Issue 4 left section 7.3.6.3 alone. It still read the way it had before the band was opened: check the channel for 60 seconds before transmitting, cease transmission within 10 seconds of detecting a radar, keep the closing transmissions to 200 ms plus an aggregate 60 ms of control signalling over the rest of the channel move time. A lab testing a channel-120 device to EN 301 893 was working to ETSI's figures while the Canadian standard on its desk recited different ones.

Amendment 1 puts the ETSI figures in the standard. Paragraph (b) of section 7.3.6.3 now carries a second sentence: for devices with an emission bandwidth falling completely or partly in 5600&ndash;5650 MHz, the channel availability check time is 10 minutes when the EN 301 893 procedure is used. Paragraph (d) carries the matching sentence for the channel closing transmission time, which becomes 1 second. Everything else in the section holds. The 10-second channel move time and the 30-minute non-occupancy period are unchanged, as are the detection thresholds in Table 2 — &minus;62 dBm below 200 mW e.i.r.p. with power spectral density under 10 dBm/MHz, &minus;64 dBm from 200 mW to 1 W. ISED's own note on the document says only that section 7.3.6.3 was updated "following the publication of RSS-Gen Issue 6."

## Why the numbers come from ETSI

ISED keeps a separate page listing the <a href="https://ised-isde.canada.ca/site/certification-engineering-bureau/en/wireless-program/normative-test-standards-and-acceptable-alternate-procedures" rel="noopener">normative test standards and acceptable alternate procedures</a> for each RSS, and the RSS-247 entry for DFS testing moved earlier this year. Until July 20, 2026, a lab could use either EN 301 893 v1.8.1 of March 2015 or v2.2.1 of November 2024. After July 20, 2026, only v2.2.1 is accepted. A footnote on the same page states that for the 5600&ndash;5650 MHz band this is the only standard ISED accepts for demonstration of compliance.

On that footing the two numbers were arguably binding already, on anyone testing a device in the segment — they arrived through the test standard rather than through the RSS. The amendment changes what the person reading your report sees. A certification body comparing it against section 7.3.6.3 of the current issue will now find exactly the figures your lab measured to.

## What it means for your filing

- **A radio that touches 5600&ndash;5650 MHz.** The DFS portion of your report has to show the 10-minute channel availability check and the 1-second channel closing transmission time, measured to EN 301 893 v2.2.1. Ask your lab which version it tested to, and when. A campaign run to v1.8.1 before July 2026 is probably not evidence you can file on now.
- **A radio that does not.** The KDB 905462 route is still open, on the condition in 7.3.6.1 that the device operate exclusively in 5250&ndash;5350 MHz, 5470&ndash;5600 MHz, 5650&ndash;5725 MHz or a combination. Confirm with your lab that your product's emission bandwidth, not just its channel list, actually stays clear of the segment — 7.3.6.3 is written in terms of emission bandwidth falling "completely or partly" in the band.
- **The edition cited in the report.** A report dated after October 8, 2026 should cite RSS-247 Issue 4, Amendment 1. It is the same housekeeping that [RSS-Gen Issue 6, Amendment 1](/updates/rss-gen-issue-6-amendment-1-lab-checklist/) created in September, and it tends to come back as a question from the certification body rather than as a refusal.
- **No new transition.** The amendment states none, and the transition language in section 2.1 still describes the issue 3 to issue 4 changeover, which closed on January 24, 2026. Applications are assessed against the standard in force.
- **Equipment you already have certified.** A certificate issued under Issue 4 before October 8 does not lapse because the document was amended. The live question is what happens at your next modification that requires re-assessment, which is the ground covered in [what the RSS-Gen transition means for products already certified](/updates/rss-gen-issue-6-existing-certifications/).

ISED issued no general notice for this amendment. The most recent in the Directorate of Regulatory Standards series is Notice 2026-DRS0003 of September 22, 2026, on cable-locating equipment, and the only notice still linked from the RSS-247 page is SMSE-006-25, which announced Issue 4 last year. The amendment shows up in the document's own header and in the date-modified stamp at the foot of the page. If you track Canadian requirements by watching the notices page, this one went past it. I read the document pages for that reason.

## What to do

- **If you are filing a 5 GHz device this quarter,** ask your lab in one line: which EN 301 893 version, and does the emission bandwidth touch 5600&ndash;5650 MHz.
- **If your report is already written,** check that the DFS section's channel availability check and closing transmission times match the band your device actually occupies.
- **If you are the applicant and you are outside Canada,** your representative side is unaffected. The appointment requirement is section 4.1 of <a href="https://ised-isde.canada.ca/site/spectrum-management-telecommunications/en/devices-and-equipment/radio-standards-procedures-rsp/rsp-100-certification-radio-apparatus-and-broadcasting-equipment" rel="noopener">RSP-100</a>, and an amendment to a technical RSS does not change who must be appointed, or for how long.

For the standing picture of this standard, see the guide to [RSS-247 and Wi-Fi and Bluetooth certification in Canada](/guides/rss-247-wifi-bluetooth-certification-canada/), and for the sequence a foreign applicant works through, the [certification process overview](/guides/ised-certification-process-overview/).

<div class="source" markdown="1">
**Sources.** ISED, RSS-247, Issue 4 (July 24, 2025), Amendment 1 (October 8, 2026), preface and sections 2.1, 7.3.6.1, 7.3.6.2 and 7.3.6.3. ISED Certification and Engineering Bureau, <a href="https://ised-isde.canada.ca/site/certification-engineering-bureau/en/wireless-program/normative-test-standards-and-acceptable-alternate-procedures" rel="noopener">Normative Test Standards and Acceptable Alternate Procedures</a> (page modified October 5, 2026), RSS-247 DFS testing entries and footnote 3. ISED, Notice No. SMSE-006-25, Publication of RSS-247, Issue 4. ISED, <a href="https://ised-isde.canada.ca/site/certification-engineering-bureau/en/general-notices" rel="noopener">General notices</a>, most recent entry Notice 2026-DRS0003 (September 22, 2026). ISED, RSP-100, section 4.1.
</div>

<!--faq-->
### What did RSS-247 Amendment 1 change?
Section 7.3.6.3 only. Two figures were added for devices whose emission bandwidth falls completely or partly in the 5600-5650 MHz band: a channel availability check time of 10 minutes, and a channel closing transmission time of 1 second, both when the ETSI EN 301 893 test procedure is used.

### Does the amendment affect devices that avoid 5600-5650 MHz?
No. The generic figures in section 7.3.6.3 still apply: a 60-second channel availability check in controller mode, a 10-second channel move time, 200 ms plus an aggregate 60 ms of closing transmissions, and a 30-minute non-occupancy period.

### Which DFS test procedure does ISED accept for RSS-247?
FCC KDB Procedure 905462 or ETSI EN 301 893. For the 5600-5650 MHz band only EN 301 893 is accepted, and since July 20, 2026 only version 2.2.1 of November 2024 is accepted.

### Is there a transition period for Amendment 1?
The amendment states none. RSS-247 is in force from its publication date, and the transition provision in section 2.1 relates to the issue 3 to issue 4 changeover, which ended on January 24, 2026.

### Does this change the Canadian Representative requirement?
No. That requirement comes from section 4.1 of RSP-100, not from RSS-247, and it is unchanged.
<!--/faq-->

If you need a Canadian Representative appointed for an ISED certification, the [Canadian Representative service](/canadian-representative-service/) is US$499 per certification for a ten-year term, or US$999 per year for unlimited certifications; see [pricing](/pricing/).
