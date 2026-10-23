// netlify/lib/label-seal.mjs
// Seals the full label report so the browser can hold it without reading it.
// The report is released by /api/label-report once the visitor gives an email address.
// No database: the sealed blob carries the report and its timestamp.
//
// Key: LABEL_SECRET if set; otherwise a random secret created once and kept in
// Netlify Blobs (store "label-checker", key "config/seal-secret"). The AI Gateway's
// ANTHROPIC_API_KEY is not used because it is not the same in every function.
import { createCipheriv, createDecipheriv, createHash, randomBytes } from 'node:crypto';
import { getStore } from '@netlify/blobs';

const MAX_AGE_MS = 24 * 60 * 60 * 1000;
let cached = null;

async function key() {
  if (cached) return cached;
  let secret = process.env.LABEL_SECRET || '';
  if (!secret) {
    const store = getStore({ name: 'label-checker', consistency: 'strong' });
    secret = await store.get('config/seal-secret', { type: 'text' });
    if (!secret) {
      await store.set('config/seal-secret', randomBytes(32).toString('hex'), { onlyIfNew: true });
      secret = await store.get('config/seal-secret', { type: 'text' });
    }
  }
  if (!secret) throw new Error('no sealing secret available');
  cached = createHash('sha256').update('label-report:' + secret).digest();
  return cached;
}

export async function seal(obj) {
  const iv = randomBytes(12);
  const c = createCipheriv('aes-256-gcm', await key(), iv);
  const body = Buffer.concat([c.update(JSON.stringify({ t: Date.now(), r: obj }), 'utf8'), c.final()]);
  return Buffer.concat([iv, c.getAuthTag(), body]).toString('base64url');
}

export async function unseal(token) {
  const buf = Buffer.from(String(token || ''), 'base64url');
  if (buf.length < 29) throw new Error('bad token');
  const d = createDecipheriv('aes-256-gcm', await key(), buf.subarray(0, 12));
  d.setAuthTag(buf.subarray(12, 28));
  const out = JSON.parse(Buffer.concat([d.update(buf.subarray(28)), d.final()]).toString('utf8'));
  if (Date.now() - out.t > MAX_AGE_MS) throw new Error('expired');
  return out.r;
}
