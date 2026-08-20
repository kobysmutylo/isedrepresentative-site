---
title: Order Your ISED Canadian Representative Letter | US$499 | Same Business Day
description: Order an RSP-100 Canadian Representative attestation letter. US$499 per certification or US$999/year unlimited. Submit product details, pay by card or wire, receive the signed PDF the same business day.
h1: Order your attestation letter
short: Order
type: page
updated: 2026-08-20
---

<div class="answer" markdown="1">
US$499 per certification (ten-year appointment) or US$999 per year unlimited. Submit the details below; you will receive a Stripe payment link by email within the business day, and the signed letter follows as soon as payment clears. Questions first? [Email us](mailto:info@isedrepresentative.com) or call +1 613 869 5440.
</div>

<form name="order" method="POST" action="/thank-you/" data-netlify="true" netlify-honeypot="website">
<input type="hidden" name="form-name" value="order">
<p style="display:none"><label>Leave blank <input name="website"></label></p>

<fieldset>
<legend>Plan</legend>
<label><input type="radio" name="plan" value="per-certification" checked style="width:auto"> Per certification, US$499 one-time (ten-year appointment)</label>
<label><input type="radio" name="plan" value="annual" style="width:auto"> Annual plan, US$999 per year (unlimited certifications)</label>
</fieldset>

<fieldset>
<legend>Applicant (as it will appear on the certification application)</legend>
<label for="company">Legal company name</label>
<input id="company" name="company" required autocomplete="organization">
<label for="address">Company address</label>
<textarea id="address" name="address" required autocomplete="street-address"></textarea>
<label for="cn">ISED Company Number</label>
<input id="cn" name="ised_company_number" placeholder="Leave blank if not yet assigned">
<p class="hint">If you do not have one, we explain how to obtain it in the order confirmation.</p>
<label for="country">Country</label>
<input id="country" name="country" required autocomplete="country-name">
</fieldset>

<fieldset>
<legend>Contact</legend>
<label for="name">Contact name</label>
<input id="name" name="contact_name" required autocomplete="name">
<label for="email">Email</label>
<input id="email" name="email" type="email" required autocomplete="email">
<label for="phone">Phone (optional)</label>
<input id="phone" name="phone" type="tel" autocomplete="tel">
<label for="role">You are</label>
<select id="role" name="role">
<option>The manufacturer / applicant</option>
<option>A test laboratory ordering for a client</option>
<option>A certification body ordering for a client</option>
<option>A consultant ordering for a client</option>
</select>
</fieldset>

<fieldset>
<legend>Product</legend>
<label for="desc">Product description</label>
<input id="desc" name="product_description" required placeholder="e.g. Wi-Fi 6 / Bluetooth LE streaming media player">
<label for="ic">IC certification number</label>
<input id="ic" name="ic_number" placeholder="e.g. 12345A-ABC123 — leave blank if not yet assigned">
<label for="pmn">PMN (product marketing name)</label>
<input id="pmn" name="pmn">
<label for="hvin">HVIN(s)</label>
<input id="hvin" name="hvin" placeholder="Separate multiple with commas">
<label for="models">Model number(s)</label>
<input id="models" name="models" placeholder="Separate multiple with commas">
<label for="cb">Certification body (optional)</label>
<input id="cb" name="certification_body" placeholder="Helps us match their preferred template">
<label for="more">Additional products or notes</label>
<textarea id="more" name="notes" placeholder="List further certifications here, or attach details by reply email."></textarea>
</fieldset>

<fieldset>
<legend>Payment</legend>
<label><input type="radio" name="payment" value="card" checked style="width:auto"> Card via Stripe (letter issues same business day)</label>
<label><input type="radio" name="payment" value="wire" style="width:auto"> Wire transfer (letter issues when funds arrive)</label>
<label><input type="checkbox" name="terms" required style="width:auto"> I accept the <a href="/terms/">terms of service</a> and confirm the applicant details are accurate.</label>
</fieldset>

<p><button class="btn btn-primary" type="submit">Submit order</button></p>
<p class="hint">Your details are used only to prepare the letter and maintain the appointment. See the <a href="/privacy/">privacy policy</a>.</p>
</form>

## What happens next

1. We confirm receipt and send the Stripe link or wire instructions within the business day.
2. Once payment clears, we issue the signed PDF letter, the same business day, Eastern Time.
3. You forward the letter to your certification body. If the CB has its own template, reply with it and we sign that instead.
