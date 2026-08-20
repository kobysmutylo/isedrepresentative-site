#!/usr/bin/env python3
"""Static build for www.isedrepresentative.com.

content/**/*.md  ->  dist/**/index.html  (+ sitemap.xml, robots.txt, llms.txt, feed.xml)

Front matter is simple `key: value` lines between `---` fences.
Keys: title, description, h1, type (page|guide|industry|country|faq|howto|service|pricing|about),
      date, updated, nav (section label for breadcrumbs), faq (inline FAQ block markers in body), noindex.
"""
import datetime as dt
import html
import json
import os
import re
import shutil
import sys
from pathlib import Path

import markdown

ROOT = Path(__file__).parent
CONTENT = ROOT / "content"
STATIC = ROOT / "static"
DIST = ROOT / "dist"

SITE = "https://www.isedrepresentative.com"
SITE_NAME = "ISED Representative"
ORG_NAME = "ISED Representative (Smutylo Law+)"
PERSON = "Koby Smutylo"
PHONE = "+1-613-869-5440"
EMAIL = "info@isedrepresentative.com"
PRICE_PER = "499"
PRICE_ANNUAL = "999"
GA4 = os.environ.get("GA4_ID", "")  # set to G-XXXX when the property exists
INDEXNOW_KEY = os.environ.get("INDEXNOW_KEY", "")

PERSON_JSON = {
    "@type": "Person",
    "@id": SITE + "/about/#koby-smutylo",
    "name": PERSON,
    "url": SITE + "/about/",
    "image": SITE + "/koby-smutylo.jpg",
    "jobTitle": "Lawyer; ISED Canadian Representative",
    "worksFor": {"@id": SITE + "/#organization"},
    "alumniOf": [
        {"@type": "CollegeOrUniversity", "name": "Western University, Faculty of Law"},
        {"@type": "CollegeOrUniversity", "name": "Queen's University"},
    ],
    "hasCredential": {
        "@type": "EducationalOccupationalCredential",
        "credentialCategory": "Licence to practise law",
        "recognizedBy": {"@type": "Organization", "name": "Law Society of Ontario", "url": "https://lso.ca/"},
        "dateCreated": "2001",
        "url": "https://lsodirectory.lso.ca/en-US/licensee-detail/?lawsocietynumber=44441E",
        "identifier": "44441E",
    },
    "knowsAbout": [
        "ISED certification", "RSP-100", "Canadian Representative", "Radio equipment certification Canada",
        "Attestation letter", "Wireless device market access Canada",
    ],
    "sameAs": [
        "https://www.linkedin.com/in/koby-smutylo-businesslaw",
        "https://lsodirectory.lso.ca/en-US/licensee-detail/?lawsocietynumber=44441E",
        "https://lawyercorporation.ca/about-koby-smutylo/",
        "https://lawyercorporation.ca/canadian-representative/",
    ],
}

ORG_JSON = {
    "@type": ["Organization", "LegalService"],
    "@id": SITE + "/#organization",
    "name": SITE_NAME,
    "alternateName": "ISEDRepresentative.com",
    "legalName": "Smutylo Law+",
    "url": SITE + "/",
    "logo": SITE + "/logo.svg",
    "image": SITE + "/og.png",
    "telephone": PHONE,
    "email": EMAIL,
    "founder": {"@id": SITE + "/about/#koby-smutylo"},
    "foundingDate": "2010",
    "address": {"@type": "PostalAddress", "addressLocality": "Ottawa", "addressRegion": "ON", "addressCountry": "CA"},
    "areaServed": {"@type": "Country", "name": "Canada"},
    "knowsLanguage": ["en", "fr"],
    "priceRange": "$499 - $999 USD",
    "sameAs": [
        "https://lawyercorporation.ca/canadian-representative/",
        "https://www.linkedin.com/in/koby-smutylo-businesslaw",
    ],
}

SERVICE_JSON = {
    "@type": "Service",
    "@id": SITE + "/canadian-representative-service/#service",
    "name": "ISED Canadian Representative Service",
    "serviceType": "Canadian Representative for ISED radio equipment certification (RSP-100 section 4.1)",
    "provider": {"@id": SITE + "/#organization"},
    "areaServed": {"@type": "Country", "name": "Canada"},
    "audience": {"@type": "BusinessAudience", "audienceType": "Manufacturers and applicants located outside Canada"},
    "url": SITE + "/canadian-representative-service/",
    "termsOfService": SITE + "/terms/",
    "offers": [
        {"@type": "Offer", "name": "Per-certification appointment (10-year term)", "price": PRICE_PER,
         "priceCurrency": "USD", "url": SITE + "/pricing/", "availability": "https://schema.org/InStock"},
        {"@type": "Offer", "name": "Annual plan, unlimited certifications", "price": PRICE_ANNUAL,
         "priceCurrency": "USD", "url": SITE + "/pricing/", "availability": "https://schema.org/InStock"},
    ],
}

NAV = [
    ("/canadian-representative-service/", "Service"),
    ("/pricing/", "Pricing"),
    ("/how-it-works/", "How it works"),
    ("/guides/", "Guides"),
    ("/faq/", "FAQ"),
    ("/about/", "About"),
    ("/contact/", "Contact"),
]

CSS = (STATIC / "site.css").read_text()


def parse(path: Path):
    raw = path.read_text()
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", raw, re.S)
    meta, body = {}, raw
    if m:
        for line in m.group(1).splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                meta[k.strip()] = v.strip()
        body = m.group(2)
    return meta, body


def slug_for(path: Path):
    rel = path.relative_to(CONTENT).with_suffix("")
    if rel.name == "index":
        rel = rel.parent
    s = "/" + str(rel).strip("/.") + "/"
    return "/" if s == "//" else s


def extract_faqs(body: str):
    """Blocks delimited by <!--faq--> ... <!--/faq--> with ### Question / answer paragraphs."""
    faqs = []
    for block in re.findall(r"<!--faq-->(.*?)<!--/faq-->", body, re.S):
        parts = re.split(r"^###\s+", block.strip(), flags=re.M)
        for p in parts:
            if not p.strip():
                continue
            q, _, a = p.partition("\n")
            a_html = markdown.markdown(a.strip())
            a_text = re.sub(r"<[^>]+>", "", a_html).strip()
            faqs.append((q.strip(), a_text))
    body = body.replace("<!--faq-->", "").replace("<!--/faq-->", "")
    return faqs, body


def md(body: str):
    return markdown.markdown(body, extensions=["tables", "toc", "attr_list", "md_in_html"])


def breadcrumbs(slug, meta):
    crumbs = [("/", "Home")]
    parts = [p for p in slug.strip("/").split("/") if p]
    acc = ""
    for i, p in enumerate(parts):
        acc += "/" + p
        if i == len(parts) - 1:
            crumbs.append((acc + "/", meta.get("short", meta.get("h1", meta["title"]))))
        else:
            label = {"guides": "Guides", "industries": "Industries", "countries": "Countries"}.get(p, p.title())
            crumbs.append((acc + "/", label))
    return crumbs


def schema_for(slug, meta, faqs, body_text):
    graph = [ORG_JSON, PERSON_JSON, SERVICE_JSON,
             {"@type": "WebSite", "@id": SITE + "/#website", "url": SITE + "/", "name": SITE_NAME,
              "publisher": {"@id": SITE + "/#organization"}, "inLanguage": "en-CA"}]
    page_id = SITE + slug + "#webpage"
    t = meta.get("type", "page")
    page = {
        "@type": "WebPage", "@id": page_id, "url": SITE + slug, "name": meta["title"],
        "description": meta["description"], "isPartOf": {"@id": SITE + "/#website"},
        "about": {"@id": SERVICE_JSON["@id"]}, "inLanguage": "en-CA",
        "dateModified": meta.get("updated", meta.get("date", TODAY)),
        "reviewedBy": {"@id": PERSON_JSON["@id"]},
    }
    if slug != "/":
        crumbs = breadcrumbs(slug, meta)
        graph.append({"@type": "BreadcrumbList", "@id": SITE + slug + "#breadcrumb", "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + u} for i, (u, n) in enumerate(crumbs)]})
        page["breadcrumb"] = {"@id": SITE + slug + "#breadcrumb"}
    if t in ("guide", "industry", "country"):
        graph.append({
            "@type": "Article", "@id": SITE + slug + "#article", "headline": meta.get("h1", meta["title"]),
            "description": meta["description"], "url": SITE + slug, "mainEntityOfPage": {"@id": page_id},
            "author": {"@id": PERSON_JSON["@id"]}, "publisher": {"@id": ORG_JSON["@id"]},
            "datePublished": meta.get("date", TODAY), "dateModified": meta.get("updated", meta.get("date", TODAY)),
            "inLanguage": "en-CA", "isAccessibleForFree": True,
            "citation": [{"@type": "CreativeWork", "name": "RSP-100, Issue 12 — Certification of Radio Apparatus and Broadcasting Equipment (ISED)", "url": RSP100}],
            "wordCount": len(body_text.split()),
        })
    if faqs:
        graph.append({"@type": "FAQPage", "@id": SITE + slug + "#faq", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]})
    if t == "howto":
        steps = re.findall(r"<h2[^>]*>(Step \d+[^<]*)</h2>\s*<p>(.*?)</p>", body_text_html_cache[slug], re.S)
        if steps:
            graph.append({"@type": "HowTo", "@id": SITE + slug + "#howto", "name": meta.get("h1", meta["title"]),
                          "description": meta["description"], "totalTime": "PT1D",
                          "step": [{"@type": "HowToStep", "position": i + 1, "name": re.sub(r"<[^>]+>", "", n),
                                    "text": re.sub(r"<[^>]+>", "", s)} for i, (n, s) in enumerate(steps)]})
    graph.append(page)
    return {"@context": "https://schema.org", "@graph": graph}


RSP100 = ("https://ised-isde.canada.ca/site/spectrum-management-telecommunications/en/devices-and-equipment/"
          "radio-standards-procedures-rsp/rsp-100-certification-radio-apparatus-and-broadcasting-equipment")
TODAY = dt.date.today().isoformat()
body_text_html_cache = {}


def render(slug, meta, body_html, faqs):
    title = meta["title"]
    desc = meta["description"]
    h1 = meta.get("h1", title)
    canonical = SITE + slug
    nav_html = "".join(f'<li><a href="{u}"{" aria-current=page" if slug.startswith(u) and u != "/" else ""}>{n}</a></li>' for u, n in NAV)
    crumbs_html = ""
    if slug != "/":
        cs = breadcrumbs(slug, meta)
        crumbs_html = '<nav class="crumbs" aria-label="Breadcrumb"><ol>' + "".join(
            f'<li><a href="{u}">{html.escape(n)}</a></li>' if i < len(cs) - 1 else f'<li aria-current="page">{html.escape(n)}</li>'
            for i, (u, n) in enumerate(cs)) + "</ol></nav>"
    t = meta.get("type", "page")
    byline = ""
    if t in ("guide", "industry", "country", "faq", "service", "howto"):
        d = meta.get("updated", meta.get("date", TODAY))
        byline = (f'<p class="byline">Written by <a href="/about/">Koby Smutylo</a>, lawyer (<a href="https://lsodirectory.lso.ca/en-US/licensee-detail/?lawsocietynumber=44441E" rel="noopener">Law Society of Ontario</a>, called 2001), '
                  f'ISED Canadian Representative since 2010. Last reviewed <time datetime="{d}">{pretty(d)}</time>.</p>')
    schema = json.dumps(schema_for(slug, meta, faqs, re.sub(r"<[^>]+>", " ", body_html)), ensure_ascii=False)
    robots = '<meta name="robots" content="noindex,follow">' if meta.get("noindex") else '<meta name="robots" content="index,follow,max-snippet:-1,max-image-preview:large">'
    ga = ""
    if GA4:
        ga = (f'<script async src="https://www.googletagmanager.com/gtag/js?id={GA4}"></script>'
              f"<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments)}}gtag('js',new Date());gtag('config','{GA4}');"
              "document.addEventListener('click',e=>{const a=e.target.closest('a');if(!a)return;if(/^(mailto:|tel:)/.test(a.getAttribute('href')||'')||a.href.includes('/quote/'))gtag('event','contact_click',{link:a.href})});</script>")
    cta = "" if slug in ("/quote/", "/contact/") else CTA_HTML
    return f"""<!DOCTYPE html>
<html lang="en-CA">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{canonical}">
{robots}
<meta name="author" content="Koby Smutylo">
<meta property="og:type" content="{'article' if t in ('guide','industry','country') else 'website'}">
<meta property="og:site_name" content="{SITE_NAME}">
<meta property="og:url" content="{canonical}">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:image" content="{SITE}/og.png">
<meta property="og:locale" content="en_CA">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="alternate" type="application/rss+xml" title="ISED Representative guides" href="/feed.xml">
<style>{CSS}</style>
<script type="application/ld+json">{schema}</script>
{ga}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<div class="topbar"><div class="wrap"><div><span>Canadian Representative for ISED certification · RSP-100 s. 4.1</span><span>Ottawa, Canada · Eastern Time</span></div><div><span><a href="tel:{PHONE}">+1 613 869 5440</a></span><span><a href="mailto:{EMAIL}">{EMAIL}</a></span></div></div></div>
<header class="site-header">
<div class="wrap">
<a class="brand" href="/" aria-label="ISED Representative home"><img src="/logo.svg" alt="" width="40" height="40"><span>ISEDRepresentative.com<small>A service of Smutylo Law+ · est. 2010</small></span></a>
<nav class="nav" aria-label="Main"><ul>{nav_html}</ul></nav>
<a class="btn btn-primary nav-cta" href="/quote/">Get your letter</a>
</div>
</header>
<main id="main" class="wrap">
{crumbs_html}
<article class="prose{' home' if slug == '/' else ''}">
<h1>{h1}</h1>
{byline}
{body_html}
</article>
{cta}
</main>
<footer class="site-footer">
<div class="wrap foot-grid">
<div>
<p class="foot-brand">ISEDRepresentative.com</p>
<p>Canadian Representative for ISED radio equipment certification under RSP-100 section 4.1. A service of Smutylo Law+, Ottawa, Ontario. Operated by Koby Smutylo, lawyer, <a href="https://lsodirectory.lso.ca/en-US/licensee-detail/?lawsocietynumber=44441E" rel="noopener">Law Society of Ontario licensee 44441E</a>.</p>
<p><a href="mailto:{EMAIL}">{EMAIL}</a><br><a href="tel:{PHONE}">{PHONE.replace('-', ' ', 1)}</a><br>Eastern Time (UTC−5 / UTC−4)</p>
</div>
<div>
<p class="foot-h">Service</p>
<ul><li><a href="/canadian-representative-service/">Canadian Representative service</a></li><li><a href="/pricing/">Pricing</a></li><li><a href="/how-it-works/">How it works</a></li><li><a href="/quote/">Get your attestation letter</a></li><li><a href="/revise/">Revise an existing letter</a></li><li><a href="/for-labs-and-certification-bodies/">For labs and certification bodies</a></li></ul>
</div>
<div>
<p class="foot-h">Learn</p>
<ul><li><a href="/guides/">All guides</a></li><li><a href="/guides/canadian-representative-requirement-rsp-100/">The RSP-100 requirement</a></li><li><a href="/guides/attestation-letter-required-fields/">Attestation letter fields</a></li><li><a href="/guides/how-long-must-a-canadian-representative-be-appointed/">How long the appointment lasts</a></li><li><a href="/faq/">FAQ</a></li><li><a href="/industries/">Industries</a></li><li><a href="/countries/">Countries</a></li></ul>
</div>
<div>
<p class="foot-h">Company</p>
<ul><li><a href="/about/">About Koby Smutylo</a></li><li><a href="/clients/">Clients</a></li><li><a href="/case-examples/">Case examples</a></li><li><a href="/contact/">Contact</a></li><li><a href="/terms/">Terms of service</a></li><li><a href="/privacy/">Privacy</a></li><li><a href="https://lawyercorporation.ca/" rel="noopener">Smutylo Law+</a></li></ul>
</div>
</div>
<div class="wrap foot-legal"><p>© 2010–{dt.date.today().year} Smutylo Law+. ISED and Innovation, Science and Economic Development Canada are names of the Government of Canada; this site is an independent professional service and is not affiliated with ISED. Primary source: <a href="{RSP100}" rel="noopener">RSP-100, Issue 12</a>.</p></div>
</footer>
</body>
</html>
"""


TRUST_HTML = """<section class="trust" aria-label="Why you can rely on us">
<div><svg viewBox="0 0 24 24"><path d="M12 2l8 4v6c0 5-3.5 8.5-8 10-4.5-1.5-8-5-8-10V6z"/><path d="M9 12l2 2 4-4"/></svg><b>Regulated law firm</b>Koby Smutylo, <a href="https://lsodirectory.lso.ca/en-US/licensee-detail/?lawsocietynumber=44441E" rel="noopener">Law Society of Ontario licensee 44441E</a>, called 2001.</div>
<div><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg><b>Since 2010</b>Canadian Representative appointments held continuously for foreign manufacturers for over fifteen years.</div>
<div><svg viewBox="0 0 24 24"><path d="M4 7h16v12H4z"/><path d="M4 7l8 6 8-6"/></svg><b>Same business day</b>Signed attestation letter delivered by email after payment, Eastern Time.</div>
<div><svg viewBox="0 0 24 24"><path d="M3 21h18M5 21V8l7-5 7 5v13"/><path d="M9 21v-6h6v6"/></svg><b>Trusted by</b>Roku, Kamstrup, Bevi and Eurofins. <a href="/clients/">Clients</a> · <a href="/case-examples/">Case examples</a></div>
</section>"""

CTA_HTML = f"""<aside class="cta">
<h2>Need your attestation letter today?</h2>
<p>US ${PRICE_PER} per certification (10-year appointment) or US ${PRICE_ANNUAL} per year for unlimited certifications. Signed PDF delivered the same business day. Pay by card (Stripe) or wire.</p>
<p><a class="btn btn-primary" href="/quote/">Get your letter</a> <a class="btn" href="/pricing/">See pricing</a></p>
</aside>"""


def pretty(d):
    try:
        return dt.date.fromisoformat(d).strftime("%-d %B %Y")
    except Exception:
        return d


def main():
    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir()
    for f in STATIC.iterdir():
        if f.name != "site.css":
            shutil.copy(f, DIST / f.name)

    pages = []
    for path in sorted(CONTENT.rglob("*.md")):
        meta, body = parse(path)
        slug = slug_for(path)
        faqs, body = extract_faqs(body)
        body_html = md(body)
        body_text_html_cache[slug] = body_html
        pages.append((slug, meta, body_html, faqs))

    # auto index listings
    listing = {}
    for slug, meta, _, _ in pages:
        for sec in ("guides", "industries", "countries"):
            if slug.startswith(f"/{sec}/") and slug != f"/{sec}/":
                listing.setdefault(sec, []).append((slug, meta))

    for slug, meta, body_html, faqs in pages:
        sec = slug.strip("/")
        if sec in listing and "<!--list-->" in body_html:
            items = sorted(listing[sec], key=lambda x: x[1].get("order", x[1]["title"]))
            lis = "".join(f'<li><a href="{s}">{html.escape(m.get("h1", m["title"]))}</a><span>{html.escape(m["description"])}</span></li>' for s, m in items)
            body_html = body_html.replace("<!--list-->", f'<ul class="cards">{lis}</ul>')
        body_html = body_html.replace("<!--trust-->", TRUST_HTML)
        out = DIST / slug.strip("/") / "index.html" if slug != "/" else DIST / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(render(slug, meta, body_html, faqs))

    # sitemap
    urls = []
    for slug, meta, _, _ in pages:
        if meta.get("noindex"):
            continue
        lastmod = meta.get("updated", meta.get("date", TODAY))
        pri = "1.0" if slug == "/" else "0.9" if slug.count("/") == 2 else "0.7"
        urls.append(f"<url><loc>{SITE}{slug}</loc><lastmod>{lastmod}</lastmod><priority>{pri}</priority></url>")
    (DIST / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(urls) + "\n</urlset>\n")

    (DIST / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")

    # llms.txt
    lines = [f"# {SITE_NAME}", "",
             f"> Canadian Representative service for ISED radio equipment certification (RSP-100 s. 4.1), operated by Koby Smutylo, an Ontario lawyer, since 2010. Flat fee US ${PRICE_PER} per certification (10-year appointment) or US ${PRICE_ANNUAL}/year unlimited. Signed attestation letter the same business day.",
             "", "Key facts: provider Smutylo Law+, Ottawa, Ontario, Canada. Contact info@isedrepresentative.com, +1 613 869 5440. Primary regulatory source: RSP-100 Issue 12 section 4.1.", ""]
    groups = {"Core pages": [], "Guides": [], "Industries": [], "Countries": []}
    for slug, meta, _, _ in pages:
        if meta.get("noindex"):
            continue
        g = "Guides" if slug.startswith("/guides/") else "Industries" if slug.startswith("/industries/") else "Countries" if slug.startswith("/countries/") else "Core pages"
        groups[g].append(f"- [{meta.get('h1', meta['title'])}]({SITE}{slug}): {meta['description']}")
    for g, items in groups.items():
        lines += [f"## {g}", ""] + items + [""]
    (DIST / "llms.txt").write_text("\n".join(lines))
    full = []
    for slug, meta, body_html, _ in pages:
        if meta.get("noindex"):
            continue
        text = re.sub(r"\n{3,}", "\n\n", re.sub(r"<[^>]+>", "", body_html))
        full.append(f"# {meta.get('h1', meta['title'])}\nURL: {SITE}{slug}\n\n{html.unescape(text).strip()}\n")
    (DIST / "llms-full.txt").write_text("\n\n---\n\n".join(full))

    # RSS for guides
    items = []
    for slug, meta, _, _ in sorted(pages, key=lambda p: p[1].get("date", ""), reverse=True):
        if slug.startswith("/guides/") and slug != "/guides/":
            items.append(f"<item><title>{html.escape(meta.get('h1', meta['title']))}</title><link>{SITE}{slug}</link><guid>{SITE}{slug}</guid><description>{html.escape(meta['description'])}</description><pubDate>{dt.date.fromisoformat(meta.get('date', TODAY)).strftime('%a, %d %b %Y 09:00:00 -0400')}</pubDate></item>")
    (DIST / "feed.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?><rss version="2.0"><channel><title>ISED Representative guides</title><link>{SITE}/guides/</link><description>Operational guides on the ISED Canadian Representative requirement.</description>' + "".join(items) + "</channel></rss>")

    if INDEXNOW_KEY:
        (DIST / f"{INDEXNOW_KEY}.txt").write_text(INDEXNOW_KEY)

    shutil.copy(ROOT / "_redirects", DIST / "_redirects")
    shutil.copy(ROOT / "_headers", DIST / "_headers")
    print(f"built {len(pages)} pages -> {DIST}")


if __name__ == "__main__":
    main()
