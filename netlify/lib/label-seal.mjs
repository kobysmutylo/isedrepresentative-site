// netlify/lib/label-seal.mjs
// Seals the full label report so the browser can hold it without reading it.
// The report is released by /api/label-report once the visitor gives an email address.
// No database: the sealed blob carries the report and its timestamp.
import { createCipheriv, createDecipheriv, createHash, randomBytes } from 'node:crypto';

const MAX_AGE_MS = 24 * 60 * 60 * 1000;

function key() {
  const secret = process.env.LABEL_SECRET || process.env.ANTHROPIC_API_KEY || '';
  if (!secret) throw new Error('no sealing secret configured');
  return createHash('sha256').update('label-report:' + secret).digest();
}

export function seal(obj) {
  const iv = randomBytes(12);
  const c = createCipheriv('aes-256-gcm', key(), iv);
  const body = Buffer.concat([c.update(JSON.stringify({ t: Date.now(), r: obj }), 'utf8'), c.final()]);
  return Buffer.concat([iv, c.getAuthTag(), body]).toString('base64url');
}

export function unseal(token) {
  const buf = Buffer.from(String(token || ''), 'base64url');
  if (buf.length < 29) throw new Error('bad token');
  const d = createDecipheriv('aes-256-gcm', key(), buf.subarray(0, 12));
  d.setAuthTag(buf.subarray(12, 28));
  const out = JSON.parse(Buffer.concat([d.update(buf.subarray(28)), d.final()]).toString('utf8'));
  if (Date.now() - out.t > MAX_AGE_MS) throw new Error('expired');
  return out.r;
}
