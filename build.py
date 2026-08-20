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
INDEXNOW_KEY = os.environ.get("INDEXNOW_KEY", "9279a62d1caf98dfc70863bfef70cf17")

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
    "areaServed": [{"@type": "Country", "name": "Canada"}, {"@type": "Place", "name": "Worldwide (applicants outside Canada)"}],
    "knowsLanguage": ["en", "fr", "zh", "zh-TW", "ko", "ja", "de"],
    "contactPoint": {"@type": "ContactPoint", "contactType": "customer service", "telephone": PHONE, "email": EMAIL,
                     "areaServed": "Worldwide", "availableLanguage": ["English"],
                     "hoursAvailable": {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "opens": "09:00", "closes": "17:00"}},
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
    "areaServed": [{"@type": "Country", "name": n} for n in ["Canada", "United States", "China", "Taiwan", "South Korea", "Japan", "Germany", "United Kingdom", "India", "France"]] + [{"@type": "Place", "name": "Worldwide"}],
    "availableLanguage": ["en", "fr", "zh", "zh-TW", "ko", "ja", "de"],
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


LSO = "https://lsodirectory.lso.ca/en-US/licensee-detail/?lawsocietynumber=44441E"
LANGS = {
    "en": dict(html="en-CA", og="en_CA", name="English", home="Home", nav=[("/canadian-representative-service/","Service"),("/pricing/","Pricing"),("/how-it-works/","How it works"),("/guides/","Guides"),("/faq/","FAQ"),("/about/","About"),("/contact/","Contact")],
               cta_btn="Request your letter", cta_h="Need your attestation letter today?", cta_p="US ${per} per certification (10-year appointment) or US ${ann} per year for unlimited certifications. Every request is reviewed personally by Koby Smutylo before the signed PDF is issued, the same business day. Prefer email? Write to <a href=\"mailto:info@isedrepresentative.com\">info@isedrepresentative.com</a>.", cta_price="See pricing",
               skip="Skip to content", tag="A service of Smutylo Law+ · est. 2010", top1="Canadian Representative for ISED certification · RSP-100 s. 4.1", top2="Ottawa, Canada · Eastern Time",
               byline='Written by <a href="/about/">Koby Smutylo</a>, lawyer (<a href="{lso}" rel="noopener">Law Society of Ontario</a>, called 2001), ISED Canadian Representative since 2010. Last reviewed <time datetime="{d}">{dp}</time>.',
               trust=[("Regulated law firm",'Koby Smutylo, <a href="{lso}" rel="noopener">Law Society of Ontario licensee 44441E</a>, called 2001.'),("Since 2010","Canadian Representative appointments held continuously for foreign manufacturers for over fifteen years."),("Same business day","Signed attestation letter delivered by email after payment, Eastern Time."),("Trusted by",'Roku, Kamstrup, Bevi and Eurofins. <a href="/clients/">Clients</a> · <a href="/case-examples/">Case examples</a>')],
               form_note="", lang_label="Language"),
    "zh": dict(html="zh-CN", og="zh_CN", name="简体中文", home="首页", nav=[("/canadian-representative-service/","服务内容"),("/pricing/","价格"),("/how-it-works/","办理流程"),("/faq/","常见问题"),("/countries/china/","中国制造商"),("/about/","关于我们")],
               cta_btn="立即申请代表函", cta_h="今天就需要加拿大代表函？", cta_p="每个认证 {per} 美元（10 年任期），或每年 {ann} 美元不限认证数量。付款后当个工作日内签发 PDF 签字函。支持信用卡（Stripe）或电汇。", cta_price="查看价格",
               skip="跳到正文", tag="Smutylo Law+ 律师事务所提供 · 2010 年起", top1="ISED 认证加拿大代表 · RSP-100 第 4.1 条", top2="加拿大渥太华 · 东部时间",
               byline='作者：<a href="/about/">Koby Smutylo</a> 律师（<a href="{lso}" rel="noopener">安大略省律师协会</a>，2001 年执业），自 2010 年起担任 ISED 加拿大代表。最后审核：<time datetime="{d}">{d}</time>。',
               trust=[("受监管的律师事务所",'Koby Smutylo，<a href="{lso}" rel="noopener">安大略省律师协会执业编号 44441E</a>，2001 年执业。'),("自 2010 年起","十五年以上持续为境外制造商担任加拿大代表。"),("当个工作日签发","付款确认后当日（东部时间）通过电子邮件发送签字代表函。"),("客户包括",'Roku、Kamstrup、Bevi、Eurofins。<a href="/clients/">客户</a> · <a href="/case-examples/">案例</a>')],
               form_note="申请表为英文，直接提交给我们；我们以英文回复。", lang_label="语言"),
    "zh-tw": dict(html="zh-TW", og="zh_TW", name="繁體中文", home="首頁", nav=[("/canadian-representative-service/","服務內容"),("/pricing/","價格"),("/how-it-works/","辦理流程"),("/faq/","常見問題"),("/countries/taiwan/","台灣製造商"),("/about/","關於我們")],
               cta_btn="立即申請代表函", cta_h="今天就需要加拿大代表函？", cta_p="每件認證 {per} 美元（10 年任期），或每年 {ann} 美元不限認證件數。付款後當個工作日簽發 PDF 簽署函。接受信用卡（Stripe）或電匯。", cta_price="查看價格",
               skip="跳至內容", tag="Smutylo Law+ 律師事務所提供 · 2010 年起", top1="ISED 認證加拿大代表 · RSP-100 第 4.1 條", top2="加拿大渥太華 · 東部時間",
               byline='作者：<a href="/about/">Koby Smutylo</a> 律師（<a href="{lso}" rel="noopener">安大略省律師公會</a>，2001 年執業），自 2010 年起擔任 ISED 加拿大代表。最後審閱：<time datetime="{d}">{d}</time>。',
               trust=[("受監管的律師事務所",'Koby Smutylo，<a href="{lso}" rel="noopener">安大略省律師公會執業編號 44441E</a>，2001 年執業。'),("自 2010 年起","十五年以上持續為境外製造商擔任加拿大代表。"),("當個工作日簽發","付款確認後當日（東部時間）以電子郵件寄送簽署代表函。"),("客戶包括",'Roku、Kamstrup、Bevi、Eurofins。<a href="/clients/">客戶</a> · <a href="/case-examples/">案例</a>')],
               form_note="申請表為英文，直接送交我們；我們以英文回覆。", lang_label="語言"),
    "ko": dict(html="ko", og="ko_KR", name="한국어", home="홈", nav=[("/canadian-representative-service/","서비스"),("/pricing/","요금"),("/how-it-works/","진행 절차"),("/faq/","자주 묻는 질문"),("/countries/south-korea/","한국 제조사"),("/about/","소개")],
               cta_btn="대리인 확인서 신청", cta_h="오늘 캐나다 대리인 확인서가 필요하십니까?", cta_p="인증 1건당 US${per}(10년 임기) 또는 연 US${ann}로 인증 건수 무제한. 결제 후 당일 영업일 내 서명된 PDF 발급. 카드(Stripe) 또는 송금 결제.", cta_price="요금 보기",
               skip="본문으로 건너뛰기", tag="Smutylo Law+ 법률사무소 제공 · 2010년 설립", top1="ISED 인증 캐나다 대리인 · RSP-100 제4.1조", top2="캐나다 오타와 · 동부 표준시",
               byline='작성: <a href="/about/">Koby Smutylo</a> 변호사(<a href="{lso}" rel="noopener">온타리오주 변호사협회</a>, 2001년 등록), 2010년부터 ISED 캐나다 대리인. 최종 검토: <time datetime="{d}">{d}</time>.',
               trust=[("규제받는 법률사무소",'Koby Smutylo, <a href="{lso}" rel="noopener">온타리오주 변호사협회 등록번호 44441E</a>, 2001년 등록.'),("2010년부터","15년 이상 해외 제조사의 캐나다 대리인을 지속적으로 수행."),("당일 발급","결제 확인 후 당일(동부 표준시) 이메일로 서명된 확인서 전달."),("주요 고객",'Roku, Kamstrup, Bevi, Eurofins. <a href="/clients/">고객</a> · <a href="/case-examples/">사례</a>')],
               form_note="신청서는 영문이며 저희에게 직접 접수됩니다. 회신은 영문으로 드립니다.", lang_label="언어"),
    "ja": dict(html="ja", og="ja_JP", name="日本語", home="ホーム", nav=[("/canadian-representative-service/","サービス"),("/pricing/","料金"),("/how-it-works/","手続きの流れ"),("/faq/","よくある質問"),("/countries/japan/","日本のメーカー"),("/about/","会社概要")],
               cta_btn="代理人証明書を申し込む", cta_h="本日中にカナダ代理人証明書が必要ですか？", cta_p="認証1件につき US${per}（10年間）、または年額 US${ann} で認証件数無制限。お支払い後、当営業日内に署名済みPDFを発行。カード（Stripe）または銀行送金。", cta_price="料金を見る",
               skip="本文へ", tag="Smutylo Law+ 法律事務所のサービス · 2010年創業", top1="ISED認証のカナダ代理人 · RSP-100 第4.1条", top2="カナダ・オタワ · 東部時間",
               byline='執筆：<a href="/about/">Koby Smutylo</a> 弁護士（<a href="{lso}" rel="noopener">オンタリオ州法曹協会</a>、2001年登録）、2010年よりISEDカナダ代理人。最終確認：<time datetime="{d}">{d}</time>。',
               trust=[("規制下にある法律事務所",'Koby Smutylo、<a href="{lso}" rel="noopener">オンタリオ州法曹協会 登録番号 44441E</a>、2001年登録。'),("2010年より","15年以上にわたり海外メーカーのカナダ代理人を継続して受任。"),("当営業日に発行","お支払い確認後、当日（東部時間）に署名済み証明書をメールで送付。"),("主なお客様",'Roku、Kamstrup、Bevi、Eurofins。<a href="/clients/">お客様</a> · <a href="/case-examples/">事例</a>')],
               form_note="申込フォームは英語で、当事務所に直接届きます。返信は英語で行います。", lang_label="言語"),
    "de": dict(html="de", og="de_DE", name="Deutsch", home="Startseite", nav=[("/canadian-representative-service/","Leistung"),("/pricing/","Preise"),("/how-it-works/","Ablauf"),("/faq/","FAQ"),("/countries/germany/","Hersteller in Deutschland"),("/about/","Über uns")],
               cta_btn="Bestätigungsschreiben anfordern", cta_h="Brauchen Sie Ihr Bestätigungsschreiben noch heute?", cta_p="US$ {per} je Zertifizierung (10-Jahres-Bestellung) oder US$ {ann} pro Jahr für unbegrenzt viele Zertifizierungen. Unterzeichnetes PDF am selben Werktag. Zahlung per Karte (Stripe) oder Überweisung.", cta_price="Preise ansehen",
               skip="Zum Inhalt springen", tag="Ein Angebot von Smutylo Law+ · seit 2010", top1="Kanadischer Vertreter für die ISED-Zertifizierung · RSP-100 Abs. 4.1", top2="Ottawa, Kanada · Eastern Time",
               byline='Verfasst von <a href="/about/">Koby Smutylo</a>, Rechtsanwalt (<a href="{lso}" rel="noopener">Law Society of Ontario</a>, zugelassen 2001), kanadischer ISED-Vertreter seit 2010. Zuletzt geprüft am <time datetime="{d}">{d}</time>.',
               trust=[("Regulierte Anwaltskanzlei",'Koby Smutylo, <a href="{lso}" rel="noopener">Law Society of Ontario, Zulassung 44441E</a>, seit 2001.'),("Seit 2010","Seit über fünfzehn Jahren ununterbrochen kanadischer Vertreter ausländischer Hersteller."),("Am selben Werktag","Unterzeichnetes Bestätigungsschreiben per E-Mail nach Zahlungseingang, Eastern Time."),("Vertrauen uns",'Roku, Kamstrup, Bevi und Eurofins. <a href="/clients/">Kunden</a> · <a href="/case-examples/">Fallbeispiele</a>')],
               form_note="Das Formular ist auf Englisch und geht direkt bei uns ein; wir antworten auf Englisch.", lang_label="Sprache"),
    "fr": dict(html="fr-CA", og="fr_CA", name="Français", home="Accueil", nav=[("/canadian-representative-service/","Service"),("/pricing/","Tarifs"),("/how-it-works/","Fonctionnement"),("/faq/","FAQ"),("/about/","À propos"),("/contact/","Contact")],
               cta_btn="Obtenir votre lettre", cta_h="Besoin de votre lettre d’attestation aujourd’hui?", cta_p="{per} $ US par certification (mandat de 10 ans) ou {ann} $ US par année pour un nombre illimité de certifications. PDF signé livré le jour ouvrable même. Paiement par carte (Stripe) ou virement.", cta_price="Voir les tarifs",
               skip="Aller au contenu", tag="Un service de Smutylo Law+ · depuis 2010", top1="Représentant canadien pour la certification ISDE · CPR-100 art. 4.1", top2="Ottawa, Canada · heure de l’Est",
               byline='Rédigé par <a href="/about/">Koby Smutylo</a>, avocat (<a href="{lso}" rel="noopener">Barreau de l’Ontario</a>, admis en 2001), représentant canadien ISDE depuis 2010. Dernière révision : <time datetime="{d}">{d}</time>.',
               trust=[("Cabinet d’avocats réglementé",'Koby Smutylo, <a href="{lso}" rel="noopener">Barreau de l’Ontario, permis 44441E</a>, admis en 2001.'),("Depuis 2010","Mandats de représentant canadien exercés sans interruption pour des fabricants étrangers depuis plus de quinze ans."),("Le jour ouvrable même","Lettre d’attestation signée envoyée par courriel après le paiement, heure de l’Est."),("Ils nous font confiance",'Roku, Kamstrup, Bevi et Eurofins. <a href="/clients/">Clients</a> · <a href="/case-examples/">Exemples</a>')],
               form_note="Le formulaire est en anglais et nous parvient directement; nous répondons en anglais.", lang_label="Langue"),
}
TRANSLATIONS = {}   # english slug -> {lang: slug}
meta_en_for = {}    # translated slug -> english slug


def lang_of(slug):
    for code in LANGS:
        if code != "en" and slug.startswith(f"/{code}/"):
            return code
    return "en"


def localize(slug, lang):
    if lang == "en":
        return slug
    return TRANSLATIONS.get(slug, {}).get(lang, slug)


def hreflang_links(slug):
    lang = lang_of(slug)
    en = slug if lang == "en" else meta_en_for.get(slug)
    if not en or en not in TRANSLATIONS:
        return ""
    alts = {"en": en, **TRANSLATIONS[en]}
    out = [f'<link rel="alternate" hreflang="{LANGS[c]["html"]}" href="{SITE}{s}">' for c, s in alts.items()]
    out.append(f'<link rel="alternate" hreflang="x-default" href="{SITE}{en}">')
    return "\n".join(out)


def lang_switcher(slug):
    lang = lang_of(slug)
    en = slug if lang == "en" else meta_en_for.get(slug)
    alts = dict(TRANSLATIONS.get(en, {})) if en else {}
    alts["en"] = en or "/"
    for c in LANGS:
        alts.setdefault(c, f"/{c}/" if c != "en" else "/")
    items = "".join(f'<a href="{alts[c]}" lang="{LANGS[c]["html"]}" hreflang="{LANGS[c]["html"]}"{" aria-current=true" if c == lang else ""}>{LANGS[c]["name"]}</a>' for c in LANGS)
    return f'<nav class="langs" aria-label="{LANGS[lang]["lang_label"]}">{items}</nav>'

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
    lang = lang_of(slug)
    crumbs = [(f"/{lang}/" if lang != "en" else "/", LANGS[lang]["home"])]
    parts = [p for p in slug.strip("/").split("/") if p]
    if lang != "en":
        parts = parts[1:]
    acc = "" if lang == "en" else f"/{lang}"
    for i, p in enumerate(parts):
        acc += "/" + p
        if i == len(parts) - 1:
            crumbs.append((acc + "/", meta.get("short", meta.get("h1", meta["title"]))))
        else:
            label = {"guides": "Guides", "industries": "Industries", "countries": "Countries"}.get(p, p.title())
            crumbs.append(((acc if lang == "en" else "/" + p) + "/", label))
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
        "about": {"@id": SERVICE_JSON["@id"]}, "inLanguage": LANGS[lang_of(slug)]["html"],
        "dateModified": meta.get("updated", meta.get("date", TODAY)),
        "reviewedBy": {"@id": PERSON_JSON["@id"]},
    }
    if slug != "/" and slug not in [f"/{c}/" for c in LANGS]:
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
            "inLanguage": LANGS[lang_of(slug)]["html"], "isAccessibleForFree": True,
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
    lang = lang_of(slug)
    L = LANGS[lang]
    home = "/" if lang == "en" else f"/{lang}/"
    nav_items = [(localize(u, lang), n) for u, n in L["nav"]]
    nav_html = "".join(f'<li><a href="{u}"{" aria-current=page" if slug.startswith(u) and u != home else ""}>{n}</a></li>' for u, n in nav_items)
    crumbs_html = ""
    if slug != "/" and slug != home:
        cs = breadcrumbs(slug, meta)
        crumbs_html = '<nav class="crumbs" aria-label="Breadcrumb"><ol>' + "".join(
            f'<li><a href="{u}">{html.escape(n)}</a></li>' if i < len(cs) - 1 else f'<li aria-current="page">{html.escape(n)}</li>'
            for i, (u, n) in enumerate(cs)) + "</ol></nav>"
    t = meta.get("type", "page")
    byline = ""
    if t in ("guide", "industry", "country", "faq", "service", "howto"):
        d = meta.get("updated", meta.get("date", TODAY))
        byline = '<p class="byline">' + L["byline"].format(lso=LSO, d=d, dp=pretty(d)) + "</p>"
    schema = json.dumps(schema_for(slug, meta, faqs, re.sub(r"<[^>]+>", " ", body_html)), ensure_ascii=False)
    robots = '<meta name="robots" content="noindex,follow">' if meta.get("noindex") else '<meta name="robots" content="index,follow,max-snippet:-1,max-image-preview:large">'
    ga = ""
    if GA4:
        ga = (f'<script async src="https://www.googletagmanager.com/gtag/js?id={GA4}"></script>'
              f"<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments)}}gtag('js',new Date());gtag('config','{GA4}');"
              "document.addEventListener('click',e=>{const a=e.target.closest('a');if(!a)return;if(/^(mailto:|tel:)/.test(a.getAttribute('href')||'')||a.href.includes('/quote/'))gtag('event','contact_click',{link:a.href})});</script>")
    cta = "" if slug in ("/quote/", "/contact/") else cta_html(lang)
    hreflangs = hreflang_links(slug)
    switcher = lang_switcher(slug)
    form_note = f'<p class="formnote">{L["form_note"]}</p>' if (L["form_note"] and "/quote/" in body_html) else ""
    return f"""<!DOCTYPE html>
<html lang="{L["html"]}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{canonical}">
{robots}
<meta name="author" content="Koby Smutylo">
<meta name="msvalidate.01" content="A07B34E0A94F161CEBFF00AAB28227C5">
<meta property="og:type" content="{'article' if t in ('guide','industry','country') else 'website'}">
<meta property="og:site_name" content="{SITE_NAME}">
<meta property="og:url" content="{canonical}">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:image" content="{SITE}/og.png">
<meta property="og:locale" content="{L["og"]}">
{hreflangs}
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="alternate" type="application/rss+xml" title="ISED Representative guides" href="/feed.xml">
<style>{CSS}</style>
<script type="application/ld+json">{schema}</script>
{ga}
</head>
<body>
<a class="skip" href="#main">{L["skip"]}</a>
<div class="topbar"><div class="wrap"><div><span>{L["top1"]}</span><span>{L["top2"]}</span></div><div><span><a href="tel:{PHONE}">+1 613 869 5440</a></span><span><a href="mailto:{EMAIL}">{EMAIL}</a></span>{switcher}</div></div></div>
<header class="site-header">
<div class="wrap">
<a class="brand" href="{home}" aria-label="ISED Representative home"><img src="/logo.svg" alt="" width="40" height="40"><span>ISEDRepresentative.com<small>{L["tag"]}</small></span></a>
<nav class="nav" aria-label="Main"><ul>{nav_html}</ul></nav>
<a class="btn btn-primary nav-cta" href="/quote/">{L["cta_btn"]}</a>
</div>
</header>
<main id="main" class="wrap">
{crumbs_html}
<article class="prose{' home' if slug == home else ''}">
<h1>{h1}</h1>
{byline}
{form_note}
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
<ul><li><a href="/canadian-representative-service/">Canadian Representative service</a></li><li><a href="/pricing/">Pricing</a></li><li><a href="/how-it-works/">How it works</a></li><li><a href="/quote/">Request your attestation letter</a></li><li><a href="/revise/">Revise an existing letter</a></li><li><a href="/for-labs-and-certification-bodies/">For labs and certification bodies</a></li></ul>
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


ICONS = ['<path d="M12 2l8 4v6c0 5-3.5 8.5-8 10-4.5-1.5-8-5-8-10V6z"/><path d="M9 12l2 2 4-4"/>',
         '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
         '<path d="M4 7h16v12H4z"/><path d="M4 7l8 6 8-6"/>',
         '<path d="M3 21h18M5 21V8l7-5 7 5v13"/><path d="M9 21v-6h6v6"/>']


def trust_html(lang):
    L = LANGS[lang]
    cells = "".join(f'<div><svg viewBox="0 0 24 24">{ICONS[i]}</svg><b>{h}</b>{b.format(lso=LSO)}</div>' for i, (h, b) in enumerate(L["trust"]))
    return f'<section class="trust" aria-label="Trust">{cells}</section>'


def cta_html(lang):
    L = LANGS[lang]
    return (f'<aside class="cta"><h2>{L["cta_h"]}</h2><p>{L["cta_p"].format(per=PRICE_PER, ann=PRICE_ANNUAL)}</p>'
            f'<p><a class="btn btn-primary" href="/quote/">{L["cta_btn"]}</a> <a class="btn" href="{localize("/pricing/", lang)}">{L["cta_price"]}</a></p></aside>')


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
        if meta.get("translation_of"):
            TRANSLATIONS.setdefault(meta["translation_of"], {})[lang_of(slug)] = slug
            meta_en_for[slug] = meta["translation_of"]

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
        body_html = body_html.replace("<!--trust-->", trust_html(lang_of(slug)))
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
        lang = lang_of(slug)
        en = slug if lang == "en" else meta_en_for.get(slug)
        xh = ""
        if en and en in TRANSLATIONS:
            alts = {"en": en, **TRANSLATIONS[en]}
            xh = "".join(f'<xhtml:link rel="alternate" hreflang="{LANGS[c]["html"]}" href="{SITE}{s}"/>' for c, s in alts.items()) + f'<xhtml:link rel="alternate" hreflang="x-default" href="{SITE}{en}"/>'
        urls.append(f"<url><loc>{SITE}{slug}</loc><lastmod>{lastmod}</lastmod><priority>{pri}</priority>{xh}</url>")
    (DIST / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + "\n".join(urls) + "\n</urlset>\n")

    (DIST / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")

    # llms.txt
    lines = [f"# {SITE_NAME}", "",
             f"> Canadian Representative service for ISED radio equipment certification (RSP-100 s. 4.1), operated by Koby Smutylo, an Ontario lawyer, since 2010. Flat fee US ${PRICE_PER} per certification (10-year appointment) or US ${PRICE_ANNUAL}/year unlimited. Signed attestation letter the same business day.",
             "", "Key facts: provider Smutylo Law+, Ottawa, Ontario, Canada. Contact info@isedrepresentative.com, +1 613 869 5440. Primary regulatory source: RSP-100 Issue 12 section 4.1.", ""]
    OTHER = "Other languages (中文 / 한국어 / 日本語 / Deutsch / Français)"
    groups = {"Core pages": [], "Guides": [], "Industries": [], "Countries": [], OTHER: []}
    for slug, meta, _, _ in pages:
        if meta.get("noindex"):
            continue
        g = OTHER if lang_of(slug) != "en" else "Guides" if slug.startswith("/guides/") else "Industries" if slug.startswith("/industries/") else "Countries" if slug.startswith("/countries/") else "Core pages"
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

    # Netlify serves /404.html for unmatched routes
    p404 = DIST / "404" / "index.html"
    if p404.exists():
        shutil.move(p404, DIST / "404.html"); (DIST / "404").rmdir()
    shutil.copy(ROOT / "_redirects", DIST / "_redirects")
    shutil.copy(ROOT / "_headers", DIST / "_headers")
    print(f"built {len(pages)} pages -> {DIST}")


if __name__ == "__main__":
    main()
