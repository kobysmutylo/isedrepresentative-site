---
title: ISED Access to Information Requests for Certification Files
description: What to do when someone asks ISED for your wireless certification filings: section 20 of the Access to Information Act, the 20-day notice, and what to prepare.
h1: When someone asks ISED for your certification filings
short: Access to information requests
type: guide
date: 2026-10-19
updated: 2026-10-19
order: 23
---

<div class="answer" markdown="1">
ISED must release the records in your certification file unless an exemption in the *Access to Information Act* applies. For a manufacturer, the exemption that matters is section 20, which requires ISED to withhold third-party trade secrets and confidential commercial and technical information. It does not apply on its own: ISED will usually give you written notice, and you then have 20 days to explain, exhibit by exhibit and with evidence, why each item should be withheld. The confidentiality you requested when you filed is the starting point.
</div>

## How a request reaches your file

ISED is a federal institution under the *Access to Information Act*. A Canadian citizen or permanent resident, or any person or corporation present in Canada, can ask for records ISED holds without saying why. ISED does not normally tell the affected company who made the request. The requester may be a competitor, a journalist, a researcher, or a consultant acting for someone else.

A certification file typically holds the application form and cover letters, the test report and cover sheet, external and internal photos, test set-up photos, block diagrams, schematics, the operational description, the parts list, any tune-up procedure, the user manual, the confidentiality request, and correspondence with ISED or the certification body.

Some of this is already public. The certification number, model and holder details appear on ISED's [Radio Equipment List](/guides/ised-certification-number-lookup-rel/). Published material is excluded from the Act entirely (section 68), so it cannot be withheld now.

## What section 20 protects

Section 20(1) is mandatory: if information falls within it, ISED must refuse to release it. There are four routes, and more than one can apply to the same exhibit.

| Paragraph | What it covers | What you have to show | Exhibits it usually fits |
| --- | --- | --- | --- |
| 20(1)(a) | Your trade secrets | Information with commercial value, kept secret, that gives you an advantage | Schematics, firmware details, tune-up procedures |
| 20(1)(b) | Financial, commercial, scientific or technical information you supplied in confidence | It is technical or commercial; you supplied it; it is confidential on an objective basis; you have treated it consistently as confidential | Schematics, block diagrams, operational description, parts list, internal photos |
| 20(1)(c) | Information whose release could reasonably be expected to cause material financial loss or prejudice your competitive position | Evidence of a reasonable expectation of probable harm | Anything a competitor could use to copy or reverse-engineer the design |
| 20(1)(d) | Information whose release could reasonably be expected to interfere with your contractual or other negotiations | A real negotiation the release would affect | Pricing, supplier or OEM details in correspondence |

The leading case is *Merck Frosst Canada Ltd. v. Canada (Health)*, 2012 SCC 3. The Supreme Court held that the third party has to prove the exemption applies, and that general assertions of harm are not enough. A submission that says "this is confidential" without showing how the information has been protected, or what a competitor could do with it, is likely to fail.

## Why the confidentiality request you filed matters

RSP-100 section 12.4 requires the applicant to say which documents are confidential, and states that the *Access to Information Act* applies to all applicants. Block diagrams, the operational description, parts lists and tune-up information, software-defined radio and security information, and schematics qualify for confidential treatment; ISED may treat other exhibits as confidential on a justified request made before the application is submitted.

That request is your first evidence under section 20(1)(b). An exhibit you marked confidential at filing is easier to defend than one you did not. Consistency also counts outside ISED: a schematic published in a datasheet, shared with distributors without a non-disclosure agreement, or filed with another regulator without a confidentiality request will be hard to call confidential.

## Where the protection runs out

- **Government testing (section 20(2)).** ISED cannot use section 20(1) to withhold the results of product testing carried out by or for a government institution. Test reports from your own accredited laboratory are supplied by you and, in our view, fall outside this rule. Results of ISED's own [audit](/guides/ised-audit-samples-who-provides-who-pays/) testing of your device are likely to be released, with a written explanation of the test methods (section 20(3)).
- **Public interest (section 20(6)).** ISED may release information protected by paragraphs (b) to (d) where disclosure relates to public health, public safety or protection of the environment and the public interest clearly outweighs the harm to you. Trade secrets under paragraph (a) are not subject to this override.
- **Severance (section 25).** ISED must release whatever can reasonably be separated from the protected parts. Expect a redacted release rather than a full refusal; the realistic aim is to keep the sensitive exhibits back.
- **Consent (section 20(5)).** ISED may release protected information if you consent. Consenting to make the request go away gives up the protection permanently.

Section 19 separately requires ISED to withhold personal information, such as the names and signatures of individual employees. ISED applies it on its own; it does not protect the device information.

## The notice process and deadlines

1. **Notice (section 27).** If ISED intends to release a record that may contain your section 20 information, it must make every reasonable effort to give you written notice within 30 days of receiving the request. The notice describes the records concerned.
2. **Your representations (section 28(1)(a)).** You have 20 days after the notice is given to explain in writing why the records, or parts of them, should not be released.
3. **ISED's decision (section 28(1)(b)).** ISED must decide within 30 days after the notice and tell you in writing.
4. **Federal Court (section 44).** If ISED decides to release over your objection, it must wait 20 days after notifying you. Within that window you can apply to the Federal Court for review; if you do not, the records are released.

The notice goes to the contact ISED has on file for the certification. If that contact has left the company or the address is out of date, the 20 days can run before anyone sees the letter. The same is true of your [Canadian Representative's](/guides/canadian-representative-requirement-rsp-100/) details.

## What to prepare

Most of the work can be done before the notice arrives, which leaves the 20 days for writing rather than gathering.

- Contact ISED's access to information office, identify yourself as the affected third party, and ask to receive the notice and a copy of the records proposed for release.
- Pull the confidentiality request from the original application and list which exhibits it covered.
- Check what is already public: the Radio Equipment List, your website and datasheets, and filings with other regulators such as the FCC.
- Go through the records exhibit by exhibit and note which paragraph of section 20(1) applies to each.
- Gather evidence of confidential treatment: non-disclosure agreements with suppliers and contract manufacturers, access controls, confidentiality markings.
- Prepare a harm statement, ideally a sworn declaration from an engineering or product lead, explaining what a competitor could do with each exhibit and what that would cost you.
- Mark proposed redactions on the actual pages and concede material that is plainly public. ISED is more likely to accept a focused objection than a blanket one.

<div class="source" markdown="1">
**Sources.** [Access to Information Act](https://laws-lois.justice.gc.ca/eng/acts/a-1/), sections 19, 20, 25, 27, 28, 44 and 68 (consolidated to September 30, 2026). [RSP-100, Issue 12](https://ised-isde.canada.ca/site/spectrum-management-telecommunications/en/devices-and-equipment/radio-standards-procedures-rsp/rsp-100-certification-radio-apparatus-and-broadcasting-equipment), section 12.4 (disclosure of information). *Merck Frosst Canada Ltd. v. Canada (Health)*, 2012 SCC 3. This guide is general information, not legal advice about a specific file.
</div>

<!--faq-->
### Will ISED tell me who asked for my filings?

Not normally. The Act protects the requester's identity, and the notice describes the records concerned rather than the person asking for them.

### Can ISED release my schematics?

Only if they are not protected by section 20. Schematics usually qualify as confidential technical information or trade secrets, particularly if you marked them confidential under RSP-100 section 12.4 and have not published them elsewhere. You still have to make the case in your representations.

### Are test reports confidential?

RSP-100 section 12.4 does not list test reports among the exhibits that qualify for confidential treatment, and they are often published after certification. Results of ISED's own audit testing are generally releasable under section 20(2).

### What happens if I miss the 20-day deadline?

ISED can decide on the record it has, and is likely to release what you did not object to. Keeping the contact details on your certification current is the simplest protection.

### Does a Canadian Representative deal with access requests?

The representative's duties under RSP-100 section 4.1 concern enquiries from ISED about the certified product. If a notice reaches us as your representative, we pass it to you the same day; responding to it is legal work that we can take on for you separately.
<!--/faq-->
