// netlify/functions/deploy-succeeded.mjs
//
// Event-triggered function: Netlify invokes this automatically after every
// successful production deploy (the name "deploy-succeeded" is the trigger).
//
// Job: ping IndexNow (Bing, and via it Yahoo/DuckDuckGo/Copilot) for every
// page whose <lastmod> in sitemap.xml is within the last 48 hours — i.e. the
// pages this deploy just published or edited. Google has no IndexNow; its
// nudge stays manual in Search Console, with the sitemap as the backstop.
//
// No secrets: the IndexNow key is public by design (it is verified against
// the key file served at the site root, built from static/).
//
// Failure policy: log and return 200. A missed ping costs a few hours of
// crawl latency; it must never look like a failed deploy.

const HOST = 'www.isedrepresentative.com';
const KEY = '9279a62d1caf98dfc70863bfef70cf17';
const SITEMAP = `https://${HOST}/sitemap.xml`;
const WINDOW_MS = 48 * 60 * 60 * 1000; // 48 hours
const MAX_URLS = 50;

export const handler = async () => {
  try {
    const res = await fetch(SITEMAP);
    if (!res.ok) throw new Error(`sitemap fetch ${res.status}`);
    const xml = await res.text();

    const now = Date.now();
    const urls = [];
    const re = /<loc>([^<]+)<\/loc>\s*<lastmod>([^<]+)<\/lastmod>/g;
    let m;
    while ((m = re.exec(xml)) !== null && urls.length < MAX_URLS) {
      const when = Date.parse(m[2]);
      if (!Number.isNaN(when) && now - when <= WINDOW_MS) urls.push(m[1]);
    }

    if (urls.length === 0) {
      console.log('indexnow: no pages modified in the last 48h; nothing to ping.');
      return { statusCode: 200, body: 'nothing to ping' };
    }

    const ping = await fetch('https://api.indexnow.org/indexnow', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json; charset=utf-8' },
      body: JSON.stringify({
        host: HOST,
        key: KEY,
        keyLocation: `https://${HOST}/${KEY}.txt`,
        urlList: urls,
      }),
    });
    console.log(`indexnow: submitted ${urls.length} url(s), status ${ping.status}:`, urls.join(' '));
    return { statusCode: 200, body: `pinged ${urls.length}` };
  } catch (err) {
    console.error('indexnow: ping skipped:', err && err.message);
    return { statusCode: 200, body: 'skipped' };
  }
};
