---
title: RSS-Gen Issue 6 Amendment 1 and ISED's Amended Lab Checklist
description: ISED's two September follow-ups to RSS-Gen Issue 6: Amendment 1 opens 101.4 kHz for cable locators, and the lab checklist moves site validation to C63.25.2.
h1: RSS-Gen Issue 6, six weeks on: Amendment 1 and the amended lab checklist
short: Amendment 1 and lab checklist
type: update
date: 2026-09-21
updated: 2026-09-21
---

<div class="answer" markdown="1">
ISED has made two follow-up changes to [RSS-Gen Issue 6](/updates/rss-gen-issue-6-published/) in September 2026. On September 4 it issued <a href="https://ised-isde.canada.ca/site/certification-engineering-bureau/en/node/188" rel="noopener">Notice 2026-DRS0001</a>: the Testing Laboratory Technical Assessment Checklist is amended so that radiated-emission test sites are validated to ANSI/USEMCSC C63.25.2 between 30 MHz and 1 GHz, as section 3.8.2 of Issue 6 requires; the old checklist remains usable until July 30, 2027. On September 15 it published <a href="https://ised-isde.canada.ca/site/spectrum-management-telecommunications/en/devices-and-equipment/radio-equipment-standards/radio-standards-specifications-rss/rss-gen-general-requirements-compliance-radio-apparatus" rel="noopener">RSS-Gen Issue 6, Amendment 1</a>, which carves 101.4 kHz out of the 90–110 kHz restricted band for equipment that locates buried cable markers. Neither change touches the Canadian Representative requirement in RSP-100.
</div>

## The amended lab checklist

The <a href="https://ised-isde.canada.ca/site/spectrum-management-telecommunications/en/devices-and-equipment/procedures-conformity-assessment-bodies/testing-laboratory-technical-assessment-checklist" rel="noopener">Testing Laboratory Technical Assessment Checklist</a> is the form an assessor completes when a laboratory is evaluated for its capability to test to Canadian requirements. It feeds ISED's recognition process under REC-LAB, which is how a lab gets onto the Wireless Device Testing Laboratories list — and section 3.8.1 of RSS-Gen Issue 6 requires that every compliance assessment of Category I radio apparatus be performed by a lab on that list.

Only three questions changed — Q2a, Q9 and Q40b — and all three concern site validation, the periodic measurement that proves a chamber or open-area test site is good enough to produce trustworthy radiated-emission results. Under RSS-Gen Issue 5, sites were validated to ANSI C63.4 for 30 MHz to 1 GHz and to ANSI C63.25.1 or CISPR 16-1-4 above 1 GHz. Section 3.8.2 of Issue 6 replaces C63.4 with ANSI/USEMCSC C63.25.2 for the 30 MHz to 1 GHz range and keeps C63.25.1 or CISPR 16-1-4 at and above 1 GHz. The checklist now asks the same thing: whether a lab that validates its own sites is competent to do so to C63.25.2, whether its sites meet C63.25.2 between 30 MHz and 1 GHz, and — where an outside firm does the validation — whether that firm is ISO/IEC 17025 accredited for C63.25.2.

## The transition

ISED has tied the checklist to the RSS-Gen transition in section 3.1 of Issue 6. From July 30, 2026 to July 30, 2027, site validation may still be performed to the Issue 5 standards, and the previous checklist (dated June 25, 2024) may still be used. After July 30, 2027, ISED says, only the amended checklist will be accepted. A lab that wants a copy of the old version has to ask for it by email; the web page now carries only the new one.

## What it means for manufacturers

You will probably never see the checklist itself. Its effect reaches you in two places.

- **The lab's site validation.** If a campaign is run against Issue 6, it is being run against a standard whose section 3.8.2 names C63.25.2 for the 30 MHz to 1 GHz range. Ask your lab which standard its chamber was last validated to and when — it is a one-line answer, and it is better to have it at quotation than after the report is written.
- **The three-year window.** Section 3.8.2 also says the date of each radiated-emissions test in the report must be no more than three years after the most recent successful site validation. That is a report-level check your certification body can make, which means a stale validation can cost you a retest.

Labs recognized through an accreditation body that assesses every two years but renews accreditation annually already give ISED a statement that they remain compliant with the checklist they last submitted — that mechanism was added to REC-LAB Issue 8 in February 2025. When the lab's next full assessment falls after July 30, 2027, it will be against the amended checklist.

## Amendment 1: 101.4 kHz for cable locators

RSS-Gen Issue 6 was amended for the first time on September 15, 2026. ISED's note on the page says the amendment "updated section 7.5 to allow operation of cable-locating equipment at 101.4 kHz," and describes the equipment as used by telecommunications companies.

Section 7.5 lists the restricted bands — frequencies set aside for safety-of-life services, satellite downlinks, radio astronomy and government uses — where a licence-exempt device's occupied bandwidth may not sit. The first entry in Table 6 is 0.09 to 0.11 MHz. It now carries an asterisk, and the note under the table says 101.4 kHz is not a restricted frequency for transmitters used to detect buried electronic markers, and that these devices may transmit on it.

If you make locating equipment for utility or telecom crews, this is the change that matters to you: a transmitter at 101.4 kHz used for that purpose is no longer outside the rules by frequency alone. It still has to meet everything else in RSS-Gen and the RSS that applies to it. For everyone else, note that the document now reads "Issue 6, Amendment 1", and make sure your lab's report cites the edition it actually tested to.

## What to do

- **At your next quotation,** ask the lab whether its 30 MHz to 1 GHz site validation is to C63.25.2 or C63.4, and the date of the most recent validation.
- **If you are filing under Issue 6,** confirm the test report cites RSS-Gen Issue 6 — and Amendment 1 if the report is dated after September 15.
- **If you make buried-marker locators,** read the note under Table 6 with your lab before your next campaign.
- **Nothing to do on the representative side.** The Canadian Representative requirement comes from <a href="https://ised-isde.canada.ca/site/spectrum-management-telecommunications/en/devices-and-equipment/radio-standards-procedures-rsp/rsp-100-certification-radio-apparatus-and-broadcasting-equipment" rel="noopener">RSP-100</a>, not RSS-Gen, and neither September change affects it.

For the wider Issue 6 picture, see [what the transition means for products already certified](/updates/rss-gen-issue-6-existing-certifications/) and [how to choose an ISED certification body and test lab](/guides/how-to-choose-an-ised-certification-body-and-test-lab/).

<div class="source" markdown="1">
**Sources.** ISED Certification and Engineering Bureau, <a href="https://ised-isde.canada.ca/site/certification-engineering-bureau/en/node/188" rel="noopener">Notice 2026-DRS0001, Testing Laboratory Technical Assessment Checklist</a> (September 4, 2026). ISED, <a href="https://ised-isde.canada.ca/site/spectrum-management-telecommunications/en/devices-and-equipment/procedures-conformity-assessment-bodies/testing-laboratory-technical-assessment-checklist" rel="noopener">Testing Laboratory Technical Assessment Checklist</a>, amendments August 2026. ISED, RSS-Gen, Issue 6 (July 30, 2026), Amendment 1 (September 15, 2026), sections 3.1, 3.8 and 7.5. ISED, REC-LAB, Issue 8, Amendment 1 (February 14, 2025).
</div>

<!--faq-->
### What did RSS-Gen Issue 6 Amendment 1 change?
Only section 7.5. A note under Table 6 now says 101.4 kHz is not a restricted frequency for transmitters used to detect buried electronic markers, which telecommunications companies use. Those devices may transmit on 101.4 kHz.

### What changed in ISED's testing laboratory checklist?
Questions Q2a, Q9 and Q40b now reflect RSS-Gen Issue 6 section 3.8.2: site validation to ANSI/USEMCSC C63.25.2 for 30 MHz to 1 GHz, and ANSI C63.25.1 or CISPR 16-1-4 at and above 1 GHz.

### Can labs still use the old checklist?
Yes, until the RSS-Gen Issue 6 transition period ends on July 30, 2027. After that date ISED will accept only the amended checklist.

### Does either change affect the Canadian Representative requirement?
No. That requirement is in RSP-100 and is unchanged.
<!--/faq-->

If you need a Canadian Representative appointed for an ISED certification, the [Canadian Representative service](/canadian-representative-service/) is US$499 per certification for a ten-year term, or US$999 per year for unlimited certifications; see [pricing](/pricing/).
