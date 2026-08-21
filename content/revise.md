---
title: Revise an Existing Canadian Representative Letter | Add Models, Update Details
description: Request a revision to an existing ISED Canadian Representative attestation letter: added models or HVINs, corrected company details, new IC number. Free within 30 days of issue.
h1: Revise an existing attestation letter
short: Revise a letter
type: page
updated: 2026-08-20
---

<div class="answer" markdown="1">
Use this form when a letter we issued needs to change: a new model or HVIN under the same certification, a corrected applicant name or address, or an IC number that has now been assigned. Revisions within 30 days of issue are free. Between 30 and 90 days we quote a small administrative fee before doing the work; after 90 days a revision is treated as a new request at the standard fee (no extra charge for annual-plan clients). Revised letters issue the same business day.
</div>

<form name="revision" method="POST" action="/thank-you/" data-netlify="true" netlify-honeypot="website">
<input type="hidden" name="form-name" value="revision">
<p style="display:none"><label>Leave blank <input name="website"></label></p>
<label for="company">Company name on the existing letter</label>
<input id="company" name="company" required>
<label for="date">Date of the existing letter (approximate is fine)</label>
<input id="date" name="letter_date">
<label for="ic">IC certification number on the existing letter</label>
<input id="ic" name="ic_number">
<label for="name">Contact name</label>
<input id="name" name="contact_name" required>
<label for="email">Email</label>
<input id="email" name="email" type="email" required>
<label for="change">What needs to change</label>
<textarea id="change" name="change" required placeholder="e.g. Add models ABC-200 and ABC-210 (HVIN ABC2); company renamed from X Ltd to Y Ltd effective 1 July"></textarea>
<p><button class="btn btn-primary" type="submit">Request revision</button></p>
</form>

## Common revisions

A new model added under an existing certification (a Class I or Class II permissive change that keeps the IC number) is the most frequent request. A company rename under the same legal entity is the next. If the certificate is being transferred to a different legal entity, that is not a revision: the new holder needs its own appointment and letter, and the CB handles the transfer. See [changing your Canadian Representative](/guides/changing-your-canadian-representative/).
