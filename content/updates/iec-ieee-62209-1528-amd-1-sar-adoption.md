---
title: ISED Adopts IEC/IEEE 62209-1528 AMD 1, With Four Exclusions
description: ISED has incorporated IEC/IEEE 62209-1528 Amendment 1 into its SAR framework with four clauses excluded, and rescinded three older applicability notices.
h1: What ISED adopted from IEC/IEEE 62209-1528 AMD 1 — and the four clauses it did not
short: 62209-1528 AMD 1
type: update
date: 2026-10-12
updated: 2026-10-12
---

<div class="answer" markdown="1">
On September 21, 2026 ISED issued <a href="https://ised-isde.canada.ca/site/certification-engineering-bureau/en/node/189" rel="noopener">Notice 2026-DRS0002</a>. The notice incorporates IEC/IEEE 62209-1528 AMD 1 into ISED's regulatory framework — the amendment to the measurement standard your lab uses for specific absorption rate on hand-held and body-worn devices. Four sets of clauses are excluded. In each case a part of <a href="https://ised-isde.canada.ca/site/spectrum-management-telecommunications/en/node/2049" rel="noopener">RSS-102.SAR.MEAS</a> keeps control instead. ISED has also marked three older notices rescinded this month, among them the two that told Canadian labs how 62209-1528 and IEC 62209-3 applied here. If you are certifying a portable device, your practical question is narrow: which edition does your test report cite, and does it lean on any of the four excluded clauses?
</div>

## What was adopted

IEC/IEEE 62209-1528 is the measurement procedure for SAR from hand-held and body-mounted wireless devices between 4 MHz and 10 GHz — phantoms, probes, positioning, the whole apparatus of a SAR bench. Amendment 1 revises it. ISED's notice says the amendment is incorporated by reference "with exclusions as noted below." So the amended text now governs your Canadian SAR assessment, except where ISED has carved something out and except where <a href="https://ised-isde.canada.ca/site/spectrum-management-telecommunications/en/node/280" rel="noopener">RSS-102</a> and its companion documents say otherwise.

RSS-102 itself has not actually been reissued. Issue 6 dates from December 2023. The measurement companion, RSS-102.SAR.MEAS, reached Issue 2 in August 2025. The notice is quite short and sets no transition date, so the four exclusions are the whole of the change.

## The four exclusions

| Excluded from AMD 1 | What applies instead |
|---|---|
| 7.6, time-period averaged SAR, and its sub-clauses | Annex G of RSS-102.SAR.MEAS "shall continue to be followed" |
| 7.9.3.1 e), test reduction of head phantom configurations based on psSAR from flat phantom configurations | Nothing — ISED "is not considering these test reduction methods at this time" |
| 7.9.3.7, test reduction of head phantom configurations based on flat phantom SAR | Same |
| 7.11, devices used next to the ear during voice calls, and its sub-clauses | Section 5.10 and Annex E of RSS-102.SAR.MEAS |

Two of these will matter to you more than the other two.

**Time-averaging.** Clause 7.6 is the part of the amended standard that deals with SAR averaged over a time period rather than at a worst-case continuous condition. A device that drops power on a duty cycle can show a much lower averaged figure, which is exactly why the method attracts scrutiny. Canada keeps its own text here. Annex G of RSS-102.SAR.MEAS is unchanged, and it is what your assessment has to follow.

**Head-phantom test reduction.** Clauses 7.9.3.1 e) and 7.9.3.7 both let a lab skip head-phantom configurations on the strength of flat-phantom results. For a phone that has to be tested in several positions against the head, the saving is genuine — real money and real bench time. ISED declined both. The wording repays a close read — not considering them *at this time*. ISED's own test-reduction guidance, <a href="https://ised-isde.canada.ca/site/certification-engineering-bureau/en/general-notices" rel="noopener">Notice 2025-DRS0007</a> of October 2025, remains in force, and it is what your lab actually works from.

## Three notices rescinded this month

ISED's general notices list now marks three notices rescinded in October 2026:

- **Notice 2020-DRS0001**, Applicability of IEC 62209-3 Standard (January 2020)
- **Notice 2020-DRS0020**, Applicability of IEC/IEEE 62209-1528 and IEC 62209-3 Standard (last updated April 2021)
- **Notice 2022-DRS0002**, Clarification on the recognition of the computational category associated with the RSS-102 scope for testing laboratories (March 2022)

The first two told Canadian labs precisely when and how the 62209 measurement standards applied here. With AMD 1 incorporated and the exclusions set out in one place, ISED no longer maintains them. All three are delinked from the notices page. The entries remain in the table; the documents are gone.

That is a documentation problem before it is a technical one. Laboratory quality procedures, certification-body checklists and internal test plans written in 2021 or 2022 cite these notices by number. A report that justifies a method with a reference to Notice 2020-DRS0020 now refers to nothing. Your method may genuinely be fine. The citation is not.

## What to do

- **Ask your lab which edition it tests to.** The answer should name IEC/IEEE 62209-1528 and, for work after September 21, 2026, Amendment 1. Get it at quotation rather than after the report is drafted.
- **If your file relies on time-averaged SAR,** confirm the assessment follows Annex G of RSS-102.SAR.MEAS and not clause 7.6 of the amended standard.
- **If your test plan drops head-phantom positions** on the basis of flat-phantom results, check which clause it leans on. Neither 7.9.3.1 e) nor 7.9.3.7 is available in Canada.
- **Search your procedures for the three rescinded notice numbers.** Replace each reference with a current source — Notice 2026-DRS0002, RSS-102.SAR.MEAS, or ISED's standing SAR guidance notices.
- **Nothing changes on the representative side.** Your Canadian Representative requirement sits in <a href="https://ised-isde.canada.ca/site/spectrum-management-telecommunications/en/devices-and-equipment/radio-standards-procedures-rsp/rsp-100-certification-radio-apparatus-and-broadcasting-equipment" rel="noopener">RSP-100</a>, not RSS-102, and this notice leaves it untouched.

For how the pieces fit together, see the [ISED certification process overview](/guides/ised-certification-process-overview/) and [how to choose an ISED certification body and test lab](/guides/how-to-choose-an-ised-certification-body-and-test-lab/). For the other recent change on the laboratory side, see [RSS-Gen Issue 6, Amendment 1 and the amended lab checklist](/updates/rss-gen-issue-6-amendment-1-lab-checklist/).

<div class="source" markdown="1">
**Sources.** ISED Certification and Engineering Bureau, <a href="https://ised-isde.canada.ca/site/certification-engineering-bureau/en/node/189" rel="noopener">Notice 2026-DRS0002, Adoption of IEC/IEEE 62209-1528 AMD 1</a> (September 21, 2026). ISED Certification and Engineering Bureau, <a href="https://ised-isde.canada.ca/site/certification-engineering-bureau/en/general-notices" rel="noopener">General notices</a> (rescission entries for Notices 2020-DRS0001, 2020-DRS0020 and 2022-DRS0002, October 2026; Notice 2025-DRS0007, October 20, 2025). ISED, RSS-102, Issue 6 (Notice 2023-DRS0014, December 15, 2023); RSS-102.SAR.MEAS, Issue 2 (Notice 2025-DRS0005, August 15, 2025).
</div>

<!--faq-->
### What did Notice 2026-DRS0002 do?
It incorporated IEC/IEEE 62209-1528 AMD 1 into ISED's regulatory framework on September 21, 2026, with four exclusions: clause 7.6 and its sub-clauses, clauses 7.9.3.1 e) and 7.9.3.7, and clause 7.11 and its sub-clauses.

### Can a Canadian SAR report use the amended standard's head-phantom test reductions?
No. ISED says it is not considering the test reduction methods in clauses 7.9.3.1 e) and 7.9.3.7 at this time. A test plan that drops head-phantom configurations on that basis sits outside what ISED has adopted.

### What governs time-averaged SAR in Canada?
Annex G of RSS-102.SAR.MEAS. ISED excluded clause 7.6 of the amendment and said Annex G shall continue to be followed.

### Which notices were rescinded, and does that change my test method?
Notices 2020-DRS0001, 2020-DRS0020 and 2022-DRS0002 were rescinded in October 2026. The first two concerned the applicability of the 62209 standards, which Notice 2026-DRS0002 now covers. Your method may be unaffected, but a procedure or report that cites a rescinded notice should be updated.

### Does any of this affect the Canadian Representative requirement?
No. That requirement comes from RSP-100 and is unchanged.
<!--/faq-->

If you need a Canadian Representative appointed for an ISED certification, the [Canadian Representative service](/canadian-representative-service/) is US$499 per certification for a ten-year term, or US$999 per year for unlimited certifications; see [pricing](/pricing/).
