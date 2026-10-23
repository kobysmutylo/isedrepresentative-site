// netlify/functions/label-report.mjs  ->  POST /api/label-report
//
// Releases the full label-check report once the visitor gives an email address,
// and emails them a copy when RESEND_API_KEY is set. The lead itself is recorded
// by the browser as a Netlify Forms submission ("label-check"), which notifies
// info@isedrepresentative.com.
//
// Environment variables:
//   RESEND_API_KEY   optional; without it the report is shown on screen only
//   LABEL_FROM       optional, default "ISED Representative <reports@lawyercorporation.ca>"
//                    (must be on a domain verified in Resend)
//   LABEL_BCC        optional, address to receive a copy of each emailed report

import { unseal } from '../lib/label-seal.mjs';
import { reportHtml } from '../lib/label-rules.mjs';

export const config = { path: '/api/label-report' };

const json = (status, body) => new Response(JSON.stringify(body), { status, headers: { 'content-type': 'application/json; charset=utf-8', 'cache-control': 'no-store' } });

export default async (req) => {
  if (req.method !== 'POST') return json(405, { error: 'Method not allowed' });
  let body;
  try { body = await req.json(); } catch { return json(400, { error: 'Bad request' }); }
  if (body.website) return json(400, { error: 'Rejected.' });

  const email = String(body.email || '').trim().slice(0, 200);
  if (!/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(email)) return json(400, { error: 'Please enter a valid email address.' });

  let report;
  try { report = await unseal(body.sealed); } catch (e) {
    console.error('label-report: unseal failed', e && e.message);
    return json(400, { error: 'This result has expired. Please run the check again.' });
  }

  let emailed = false;
  if (process.env.RESEND_API_KEY) {
    const product = String(body.product || '').slice(0, 120);
    const when = new Date().toLocaleString('en-CA', { timeZone: 'America/Toronto', dateStyle: 'long', timeStyle: 'short' }) + ' ET';
    try {
      const res = await fetch('https://api.resend.com/emails', {
        method: 'POST',
        headers: { Authorization: `Bearer ${process.env.RESEND_API_KEY}`, 'content-type': 'application/json' },
        body: JSON.stringify({
          from: process.env.LABEL_FROM || 'ISED Representative <reports@lawyercorporation.ca>',
          to: [email],
          ...(process.env.LABEL_BCC ? { bcc: [process.env.LABEL_BCC] } : {}),
          reply_to: 'info@isedrepresentative.com',
          subject: `Your label check report${product ? ' — ' + product : ''}`,
          html: reportHtml(report, { when, product }),
        }),
      });
      emailed = res.ok;
      if (!res.ok) console.error('label-report: resend', res.status, (await res.text()).slice(0, 300));
    } catch (e) {
      console.error('label-report: resend failed', e && e.message);
    }
  }
  return json(200, { report, emailed });
};
