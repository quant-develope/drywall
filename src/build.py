#!/usr/bin/env python3
"""Static site generator for the drywall installation site in Loutraki (Greek + English).

Run: python3 src/build.py   (rewrites ../site, which the Cloudflare worker serves as-is; no third-party modules)
Content: pages_el.py / pages_en.py (one dict per page, same keys in both languages).
Inside page text these short codes are expanded:
  {{k:KEY|text}}  link to page KEY in the same language (checked at build time)
  {{ill:NAME}}    illustration src/ill/NAME.svg or photo src/photos/NAME.jpg with its caption (ILL in pages_*.py)
  {{cta}}         a call-to-action box (quote + WhatsApp)
  {{note|text}}   a highlighted note from the crew
Page fields used by the layout: slug, title, desc, h1, short, card, kicker, lead, ill, ticks, answer, secs, faq, rel,
service (trust bar + Service schema), stype, parent, body (callable, replaces the standard layout), noindex, no_form.

All company details (name, phones, email, address) are in the CONFIG block below: change them there and rebuild.
"""
import hashlib
import html
import json
import os
import re
import shutil
import sys
from datetime import date

from PIL import Image, ImageOps

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..")
OUT = os.path.join(ROOT, "site")
sys.path.insert(0, HERE)

import pages_el  # noqa: E402
import pages_en  # noqa: E402


def site_url():
    """The site address lives in one place: vars.SITE_URL in wrangler.jsonc."""
    with open(os.path.join(ROOT, "wrangler.jsonc"), encoding="utf-8") as f:
        conf = json.loads(re.sub(r"^\s*//.*$", "", f.read(), flags=re.M))
    return conf["vars"]["SITE_URL"].rstrip("/")


# ---------------- CONFIG (placeholders until the owner sends the real details) ----------------
DOMAIN = site_url()
TODAY = date.today().isoformat()
VER = "1124a"
PHONE, PHONE_TEL = "+30 690 683 8669", "+306906838669"     # the owner's mobile (calls, WhatsApp, Viber)
MOBILE, WA = PHONE, "306906838669"
EMAIL = "info@handyman24.com"  # public address; forward it to the owner's inbox with Cloudflare Email Routing
BRAND = "Gypsos Loutraki"
NAME = {"el": "Γυψοσανίδες Λουτράκι", "en": "Gypsos Loutraki Drywall"}
ADDR = {"el": "Λουτράκι Κορινθίας, 203 00", "en": "Loutraki, Corinthia 203 00, Greece"}  # TODO: street address
GEO = (37.9752, 22.9775)
CONTENT = {"el": pages_el, "en": pages_en}
THEME = "#1e2a32"

UI = {
    "el": dict(skip="Μετάβαση στο περιεχόμενο", menu="Μενού", quote="Ζητήστε προσφορά", home="Αρχική", call="Τηλέφωνο",
               toc="Σε αυτή τη σελίδα", faq="Συχνές ερωτήσεις", rel="Δείτε επίσης", hours="Δευ–Σάβ 8:00–19:00",
               lang="EN", lang_t="English", priv="Απόρρητο", tag="Γυψοσανίδες σε Λουτράκι, Κόρινθο και Περαχώρα",
               price="Η τιμή δίνεται γραπτά μετά από αυτοψία και μέτρηση. Η αυτοψία είναι δωρεάν.",
               short_a="Με λίγα λόγια", cta_h="Στείλτε μας μια φωτογραφία του χώρου",
               cta_p="Με μια εικόνα και τις διαστάσεις σάς λέμε από το τηλέφωνο τι λύση ταιριάζει. Η αυτοψία μετά είναι δωρεάν.",
               wa="Μήνυμα στο WhatsApp", copy="Γυψοσανίδες Λουτράκι",
               rights="Γυψοσανίδες Λουτράκι · ψευδοροφές, χωρίσματα, επενδύσεις και μονώσεις με ξηρά δόμηση.",
               side_h="Δωρεάν αυτοψία", side_p="Ερχόμαστε στον χώρο σας σε Λουτράκι, Κόρινθο ή Περαχώρα, μετράμε και σας στέλνουμε γραπτή προσφορά.",
               note="Από το συνεργείο", top="Λουτράκι · Κόρινθος · Περαχώρα",
               trust=[("5–10", "μέρες για ένα τυπικό διαμέρισμα"), ("Knauf", "& Siniat, πιστοποιημένα υλικά"), ("Q1–Q4", "τελείωμα αρμών κατά EN 13963"), ("0 €", "για αυτοψία και προσφορά")]),
    "en": dict(skip="Skip to content", menu="Menu", quote="Get a quote", home="Home", call="Phone",
               toc="On this page", faq="Frequently asked questions", rel="See also", hours="Mon–Sat 8:00–19:00",
               lang="ΕΛ", lang_t="Ελληνικά", priv="Privacy", tag="Drywall in Loutraki, Corinth and Perachora",
               price="Prices are given in writing after a site visit and measurement. The visit is free.",
               short_a="In short", cta_h="Send us a photo of the room",
               cta_p="With one picture and the dimensions we can tell you on the phone which solution fits. The site visit afterwards is free.",
               wa="Message on WhatsApp", copy="Gypsos Loutraki",
               rights="Gypsos Loutraki · suspended ceilings, partitions, wall linings and insulation with dry construction.",
               side_h="Free site visit", side_p="We come to your place in Loutraki, Corinth or Perachora, measure, and send you a written quote.",
               note="From the crew", top="Loutraki · Corinth · Perachora",
               trust=[("5–10", "days for a typical apartment"), ("Knauf", "& Siniat certified systems"), ("Q1–Q4", "joint finish to EN 13963"), ("€0", "for the visit and the quote")]),
}

ARROW = '<svg aria-hidden="true" viewBox="0 0 20 20" width="16" height="16"><path fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" d="M4 10h11m-4-4 4 4-4 4"/></svg>'
WA_ICON = ('<svg aria-hidden="true" viewBox="0 0 24 24" width="20" height="20"><path fill="currentColor" d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2a8.2 8.2 0 0 1-4.2-1.1l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.6.1-.6.8-.8 1-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.3-.4.7-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.8 11.9 11.9 0 0 0 4.6 4c1.7.7 2.3.8 3.2.7a2.7 2.7 0 0 0 1.8-1.3 2.2 2.2 0 0 0 .2-1.3c-.1-.1-.2-.2-.5-.3z"/></svg>')
PHONE_ICON = '<svg aria-hidden="true" viewBox="0 0 24 24" width="17" height="17"><path fill="currentColor" d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.3 11.4 11.4 0 0 0 3.6.6 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.3.2 2.5.6 3.6a1 1 0 0 1-.3 1z"/></svg>'
LOGO = open(os.path.join(HERE, "static", "logo.svg"), encoding="utf-8").read().replace("<svg ", '<svg aria-hidden="true" class="logo" ', 1)
LOGO = re.sub(r"<title>.*?</title>", "", LOGO)


def esc(s):
    return html.escape(s, quote=True)


def strip(s):
    return re.sub(r"\s+", " ", re.sub("<[^>]+>", " ", s)).strip()


# ---------------- illustrations and photos ----------------
ILL_SIZE = {}  # name -> (w, h): svg viewBox, or the published jpg size for photos
PHOTO = set()  # names that are photos (src/photos/NAME.jpg -> img/NAME.jpg + NAME-600.webp + NAME-1200.webp)
OG = "saloni-kryfos-fotismos"  # photo used for og:image (cropped to 1200x630)


def build_images():
    src, dst = os.path.join(HERE, "photos"), os.path.join(OUT, "img")
    os.makedirs(dst, exist_ok=True)
    for f in sorted(os.listdir(src)):
        if not f.endswith(".jpg"):
            continue
        name = f[:-4]
        im = ImageOps.exif_transpose(Image.open(os.path.join(src, f))).convert("RGB")
        big = im.copy()
        big.thumbnail((1200, 1500), Image.LANCZOS)
        big.save(os.path.join(dst, name + ".jpg"), quality=80, optimize=True, progressive=True)
        ILL_SIZE[name] = big.size
        PHOTO.add(name)
        for w in (600, 1200):
            r = im.copy()
            r.thumbnail((w, w * 2), Image.LANCZOS)
            r.save(os.path.join(dst, "%s-%d.webp" % (name, w)), "WEBP", quality=74, method=6)
        if name == OG:
            ImageOps.fit(im, (1200, 630), Image.LANCZOS).save(os.path.join(OUT, "og.jpg"), quality=80, optimize=True, progressive=True)


def load_ill():
    for f in sorted(os.listdir(os.path.join(HERE, "ill"))):
        if f.endswith(".svg"):
            src = open(os.path.join(HERE, "ill", f), encoding="utf-8").read()
            m = re.search(r'viewBox="0 0 (\d+) (\d+)"', src)
            ILL_SIZE[f[:-4]] = (int(m.group(1)), int(m.group(2)))
    for lang in ("el", "en"):
        missing = set(ILL_SIZE) ^ set(CONTENT[lang].ILL)
        if missing:
            sys.exit("illustration without caption (or caption without file) in %s: %s" % (lang, missing))


def ill(name, lang, eager=False, alt=None, sizes="(min-width: 1000px) 50vw, 100vw"):
    if name not in ILL_SIZE:
        raise SystemExit("unknown illustration " + name)
    w, h = ILL_SIZE[name]
    alt = alt if alt is not None else CONTENT[lang].ILL[name]
    if name in PHOTO:
        return ('<picture><source type="image/webp" srcset="/img/%s-600.webp 600w, /img/%s-1200.webp 1200w" sizes="%s">'
                '<img src="/img/%s.jpg" width="%d" height="%d" alt="%s"%s></picture>') % (
            name, name, sizes, name, w, h, esc(alt), ' fetchpriority="high"' if eager else ' loading="lazy" decoding="async"')
    return '<img src="/ill/%s.svg" width="%d" height="%d" alt="%s"%s>' % (
        name, w, h, esc(alt), ' fetchpriority="high"' if eager else ' loading="lazy" decoding="async"')


def fig(name, lang, cls="ph"):
    return '<figure class="%s">%s<figcaption>%s</figcaption></figure>' % (cls, ill(name, lang), CONTENT[lang].ILL[name])


# ---------------- pages ----------------
PAGES = {}  # (lang, key) -> page dict


def path_of(lang, key):
    return PAGES[(lang, key)]["path"]


def cta_box(lang):
    u = UI[lang]
    return ('<aside class="callout"><div><b>%s</b><p>%s</p></div><div class="callout-b">'
            '<a class="btn" href="#prosfora">%s%s</a><a class="btn btn-ghost" href="https://wa.me/%s">%s%s</a></div></aside>') % (
        u["cta_h"], u["cta_p"], u["quote"], ARROW, WA, WA_ICON, u["wa"])


def expand(text, lang, used=None):
    def link(m):
        key, label = m.group(1), m.group(2)
        if (lang, key) not in PAGES:
            raise SystemExit("unknown link key %s in %s" % (key, lang))
        return '<a href="%s">%s</a>' % (path_of(lang, key), label)

    text = text.replace("{{cta}}", cta_box(lang))
    text = re.sub(r"\{\{note\|([^}]+)\}\}", lambda m: '<p class="note"><b>%s</b>%s</p>' % (UI[lang]["note"], m.group(1)), text)
    text = re.sub(r"\{\{k:([a-z0-9_]+)\|([^}]+)\}\}", link, text)
    return re.sub(r"\{\{ill:([a-z0-9-]+)\}\}", lambda m: fig(m.group(1), lang), text)


def brand(lang):
    return ('<a class="brand" href="%s">%s<span class="brand-t"><b>%s</b><small>%s</small></span></a>'
            % (path_of(lang, "home"), LOGO, "Γυψοσανίδες" if lang == "el" else "Gypsos", "Λουτράκι · Κορινθία" if lang == "el" else "Loutraki · Corinthia"))


def header(p):
    lang, u = p["lang"], UI[p["lang"]]
    C = CONTENT[lang]
    nav = "".join('<a href="%s"%s>%s</a>' % (path_of(lang, k), ' aria-current="page"' if k == p["key"] else "", n) for k, n in C.NAV)
    groups = "".join('<div class="mcol"><p>%s</p>%s</div>' % (g, "".join('<a href="%s">%s</a>' % (path_of(lang, k), n) for k, n in links))
                     for g, links in C.MENU)
    other = "en" if lang == "el" else "el"
    return """<a class="skip" href="#main">{skip}</a>
<div class="topline"><div class="w topline-in"><span>{top}</span><span><a href="mailto:{email}">{email}</a> · {hours}</span></div></div>
<header class="hd"><div class="w hd-in">
 {brand}
 <nav class="hd-nav" aria-label="main">{nav}</nav>
 <div class="hd-act">
  <a class="hd-lang" href="{alt}" hreflang="{other}" lang="{other}" title="{lang_t}">{lang_b}</a>
  <a class="hd-tel" href="tel:{tel}" aria-label="{call} {phone}">{pi}<span>{phone}</span></a>
  <a class="btn btn-sm hide-s" href="#prosfora">{quote}</a>
  <details class="dd"><summary aria-label="{menu}"><i></i><i></i><i></i></summary>
   <div class="dd-p"><div class="w dd-grid">{groups}
    <div class="mcol mcol-c"><p>{call}</p><a href="tel:{tel}">{phone}</a><a href="https://wa.me/{wa}">WhatsApp · Viber</a><a href="mailto:{email}">{email}</a><span>{hours}</span><a class="mlang" href="{alt}" hreflang="{other}" lang="{other}">{lang_t}</a></div>
   </div></div>
  </details>
 </div>
</div></header>
""".format(skip=u["skip"], top=u["top"], brand=brand(lang), nav=nav, alt=path_of(other, p["key"]), hours=u["hours"],
           other=other, lang_t=u["lang_t"], lang_b=u["lang"], quote=u["quote"], pi=PHONE_ICON,
           menu=u["menu"], groups=groups, call=u["call"], tel=PHONE_TEL, phone=PHONE, wa=WA, mobile=MOBILE, email=EMAIL)


def crumbs_list(p):
    lang = p["lang"]
    items = [(UI[lang]["home"], path_of(lang, "home"))]
    if p.get("parent"):
        pp = PAGES[(lang, p["parent"])]
        items.append((pp.get("short", pp["h1"]), pp["path"]))
    items.append((p.get("short", p["h1"]), p["path"]))
    return items


def crumbs(p):
    items = crumbs_list(p)
    li = "".join('<li><a href="%s">%s</a></li>' % (h, esc(n)) for n, h in items[:-1])
    li += '<li><span aria-current="page">%s</span></li>' % esc(items[-1][0])
    return '<nav class="bc" aria-label="breadcrumb"><ol>%s</ol></nav>' % li


def lead_form(lang, title=None, wide=False):
    """The quote form. wide=True: the bar right under the home hero; otherwise the card in the closing section."""
    f = CONTENT[lang].FORM
    opts = "".join('<option>%s</option>' % esc(o) for o in f["opts"])
    areas = "".join('<option>%s</option>' % esc(o) for o in f["areas"])
    return """<form class="lf{wide}" novalidate>
  <p class="lf-h">{h}</p>
  <label>{name}<input name="name" autocomplete="name" required></label>
  <label>{phl}<input name="phone" type="tel" autocomplete="tel" required></label>
  <label>{area}<select name="area">{areas}</select></label>
  <label>{type}<select name="type">{opts}</select></label>
  <label class="lf-msg">{msg}<textarea name="msg" rows="2" placeholder="{ph}"></textarea></label>
  <input class="hp" name="_honey" tabindex="-1" autocomplete="off" aria-hidden="true">
  <div class="lf-go"><button class="btn btn-lg" type="submit">{send}{arrow}</button></div>
  <p class="lf-alt">{alt} <button class="lnk" type="button" data-via="wa">WhatsApp</button> · <button class="lnk" type="button" data-via="viber">Viber</button> · <button class="lnk" type="button" data-via="mail">Email</button></p>
  <div class="lf-res" hidden role="status"></div>
  <p class="lf-small">{note} <a href="{priv}">{privt}</a></p>
 </form>""".format(wide=" lf-wide" if wide else "", h=title or f["card"], opts=opts, areas=areas, phl=f["phone"], arrow=ARROW,
                   priv=path_of(lang, "privacy"),
                   **{k: v for k, v in f.items() if k not in ("opts", "areas", "phone", "perks", "h", "card")})


def form(lang, title=None):
    f = CONTENT[lang].FORM
    perks = "".join("<li><b>%02d</b>%s</li>" % (i + 1, x) for i, x in enumerate(f["perks"]))
    return """<section class="close" id="prosfora"><div class="w close-in">
 <div class="close-t"><p class="eyebrow">{eb}</p><h2>{h}</h2><p>{p}</p><ol class="steps3">{perks}</ol>
  <p class="close-call"><a href="tel:{tel}">{pi}{phone}</a><a href="https://wa.me/{wa}">{wai}WhatsApp · Viber</a></p>
 </div>
 {card}
</div></section>
""".format(perks=perks, tel=PHONE_TEL, phone=PHONE, wa=WA, wai=WA_ICON, pi=PHONE_ICON, mobile=MOBILE, eb=f["eb"],
           h=title or f["h"], p=f["p"], card=lead_form(lang))


def trust(lang):
    return '<div class="facts"><div class="w facts-in">%s</div></div>' % "".join(
        "<div><b>%s</b><span>%s</span></div>" % t for t in UI[lang]["trust"])


def footer(p):
    lang, u = p["lang"], UI[p["lang"]]
    C = CONTENT[lang]
    cols = "".join('<div><h3>%s</h3>%s</div>' % (g, "".join('<a href="%s">%s</a>' % (path_of(lang, k), n) for k, n in links))
                   for g, links in C.MENU)
    return """<footer class="ft"><div class="w ft-g">
 <div class="ft-b">{brand}
  <p>{addr}<br><a href="tel:{tel}">{phone}</a> · <a href="https://wa.me/{wa}">WhatsApp</a> · Viber<br><a href="mailto:{email}">{email}</a><br>{hours}</p>
  <p class="ft-s">{price}</p></div>
 {cols}
</div><div class="w ft-e"><span>© 2026 {rights}</span><a href="{priv}">{privt}</a></div></footer>
<a class="wa-btn" href="https://wa.me/{wa}" aria-label="WhatsApp">{wai}</a>
<nav class="mob" aria-label="contact"><a href="tel:{tel}">{pi}{call}</a><a href="https://wa.me/{wa}">{wai}WhatsApp</a><a class="mob-q" href="#prosfora">{quote}</a></nav>
""".format(brand=brand(lang), addr=ADDR[lang], tel=PHONE_TEL, phone=PHONE, wa=WA, wai=WA_ICON, pi=PHONE_ICON, hours=u["hours"],
           mobile=MOBILE, email=EMAIL, price=u["price"], cols=cols, rights=u["rights"],
           priv=path_of(lang, "privacy"), privt=u["priv"], call=u["call"], quote=u["quote"])


AREAS = {"el": ["Λουτράκι", "Κόρινθος", "Περαχώρα", "Πίσια", "Λίμνη Βουλιαγμένη"],
         "en": ["Loutraki", "Corinth", "Perachora", "Pisia", "Lake Vouliagmeni"]}


def place(n, lang):
    return {"@type": "Place", "name": n, "containedInPlace": {"@type": "AdministrativeArea", "name": "Κορινθία" if lang == "el" else "Corinthia"}}


def business_ld(lang):
    return {
        "@context": "https://schema.org", "@type": "HomeAndConstructionBusiness", "@id": DOMAIN + "/#business",
        "name": NAME[lang], "alternateName": [BRAND, "Γυψοσανίδες Λουτράκι", "Gypsos Loutraki"],
        "description": "Ψευδοροφές, χωρίσματα, επενδύσεις τοίχων και μονώσεις με γυψοσανίδα στο Λουτράκι και την Κορινθία." if lang == "el"
        else "Drywall ceilings, partitions, wall linings and insulation in Loutraki and Corinthia.",
        "url": DOMAIN + path_of(lang, "home"), "logo": DOMAIN + "/icon-512.png", "image": DOMAIN + "/img/%s.jpg" % OG,
        "telephone": PHONE_TEL, "email": EMAIL,
        "address": {"@type": "PostalAddress", "addressLocality": "Λουτράκι" if lang == "el" else "Loutraki", "postalCode": "203 00",
                    "addressRegion": "Κορινθία" if lang == "el" else "Corinthia", "addressCountry": "GR"},
        "geo": {"@type": "GeoCoordinates", "latitude": GEO[0], "longitude": GEO[1]},
        "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
                                       "opens": "08:00", "closes": "19:00"}],
        "areaServed": [place(n, lang) for n in AREAS[lang]], "priceRange": "κατόπιν αυτοψίας" if lang == "el" else "after a site visit",
        "contactPoint": [{"@type": "ContactPoint", "telephone": "+" + WA, "contactType": "sales", "areaServed": "GR", "availableLanguage": ["el", "en"]}],
    }


def head(p):
    lang = p["lang"]
    url = DOMAIN + p["path"]
    el, en = (p["path"], path_of("en", p["key"])) if lang == "el" else (path_of("el", p["key"]), p["path"])
    alt = ('<link rel="alternate" hreflang="el" href="%s%s"><link rel="alternate" hreflang="en" href="%s%s">'
           '<link rel="alternate" hreflang="x-default" href="%s%s">') % (DOMAIN, el, DOMAIN, en, DOMAIN, el)
    ld = [business_ld(lang)]
    if p["key"] != "home":
        ld.append({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": n, "item": DOMAIN + h} for i, (n, h) in enumerate(crumbs_list(p))]})
    if p.get("service"):
        ld.append({"@context": "https://schema.org", "@type": "Service", "name": p["h1"], "serviceType": p.get("stype", p.get("short", p["h1"])),
                   "description": p["desc"], "url": url, "provider": {"@id": DOMAIN + "/#business"},
                   "areaServed": [place(n, lang) for n in AREAS[lang]]})
    ld.append({"@context": "https://schema.org", "@type": "WebPage", "@id": url + "#page", "name": p["h1"], "description": p["desc"],
               "url": url, "inLanguage": lang, "isPartOf": {"@type": "WebSite", "name": NAME[lang], "url": DOMAIN + "/"},
               "publisher": {"@id": DOMAIN + "/#business"}, "dateModified": p.get("mod", TODAY)})
    if p.get("faq"):
        ld.append({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": strip(a)}} for q, a in p["faq"]]})
    lds = "".join('<script type="application/ld+json">%s</script>' % json.dumps(x, ensure_ascii=False) for x in ld)
    return """<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="{robots}">
<link rel="canonical" href="{url}">{alt}
<meta name="geo.region" content="GR-J">
<meta name="geo.placename" content="{geo}">
<meta name="geo.position" content="{lat};{lon}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{site}">
<meta property="og:locale" content="{locale}">
<meta property="og:locale:alternate" content="{olocale}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{domain}/og.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="{theme}">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/icon-192.png" type="image/png" sizes="192x192">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Commissioner:wght@500;700;800&family=Inter:wght@400;500;600;700&display=swap">
<link rel="stylesheet" href="/assets/style.css?v={ver}">
{lds}
</head>
""".format(lang=lang, title=esc(p["title"]), desc=esc(p["desc"]), url=url, alt=alt, site=NAME[lang], domain=DOMAIN,
           robots="noindex, follow" if p.get("noindex") else "index, follow, max-image-preview:large",
           geo="Λουτράκι, Κορινθία" if lang == "el" else "Loutraki, Corinthia", lat=GEO[0], lon=GEO[1],
           locale="el_GR" if lang == "el" else "en_GB", olocale="en_GB" if lang == "el" else "el_GR",
           theme=THEME, ver=VER, lds=lds)


def sid(t):
    return "t-" + hashlib.md5(t.encode("utf-8")).hexdigest()[:6]


def page_body(p):
    """Inner page: split intro (text left, illustration right), short answer, contents, article + sticky side card."""
    lang, u = p["lang"], UI[p["lang"]]
    ticks = "".join("<li>%s</li>" % t for t in p.get("ticks", []))
    top = """<section class="intro"><div class="w intro-in">
 <div class="intro-t">{crumbs}<p class="eyebrow">{kicker}</p><h1>{h1}</h1><p class="lead">{lead}</p>
  {ticks}
  <div class="cta"><a class="btn" href="#prosfora">{quote}{arrow}</a><a class="btn btn-ghost" href="https://wa.me/{wa}">{wai}WhatsApp</a></div>
 </div>
 <figure class="intro-ph">{img}<figcaption>{cap}</figcaption></figure>
</div></section>""".format(crumbs=crumbs(p), kicker=p.get("kicker", ""), h1=p["h1"], lead=expand(p["lead"], lang),
                           ticks='<ul class="ok">%s</ul>' % ticks if ticks else "", quote=u["quote"], wa=WA, wai=WA_ICON, arrow=ARROW,
                           img=ill(p["ill"], lang, eager=True), cap=CONTENT[lang].ILL[p["ill"]])
    secs = p.get("secs", [])
    body = []
    if p.get("answer"):
        body.append('<div class="short"><p class="eyebrow">%s</p><p>%s</p></div>' % (u["short_a"], expand(p["answer"], lang)))
    if len(secs) > 2:
        body.append('<nav class="toc" aria-label="%s"><p>%s</p><ol>%s</ol></nav>' % (
            u["toc"], u["toc"], "".join('<li><a href="#%s">%s</a></li>' % (sid(h), h) for h, _ in secs)))
    for i, (h2, txt) in enumerate(secs):
        body.append('<section id="%s"><h2>%s</h2>%s</section>' % (sid(h2), h2, expand(txt, lang)))
        if i == 1 and len(secs) > 3:
            body.append(cta_box(lang))
    side = """<aside class="aside"><div class="aside-c"><p class="aside-h">{h}</p><p>{p}</p><a class="btn" href="#prosfora">{quote}{arrow}</a>
<a class="aside-tel" href="tel:{tel}">{pi}{phone}</a><a class="aside-tel" href="https://wa.me/{wa}">{wai}WhatsApp · Viber</a></div></aside>""".format(
        h=u["side_h"], p=u["side_p"], quote=u["quote"], tel=PHONE_TEL, phone=PHONE, arrow=ARROW, pi=PHONE_ICON, wa=WA, wai=WA_ICON, mobile=MOBILE)
    return top + '<div class="w doc"><article class="txt">%s</article>%s</div>' % ("".join(body), side)


def faq_html(faq, title):
    return '<section class="sec"><div class="w faq"><h2>%s</h2><div>%s</div></div></section>' % (title, "".join(
        '<details class="fq"><summary>%s</summary><div><p>%s</p></div></details>' % (q, a) for q, a in faq))


def related(p):
    lang = p["lang"]
    cards = []
    for k in p.get("rel", []):
        r = PAGES[(lang, k)]
        cards.append('<a class="card" href="%s"><span class="card-i">%s</span><span class="card-t"><b>%s</b><small>%s</small></span></a>' % (
            r["path"], ill(r["ill"], lang, alt=""), r.get("short", r["h1"]), r.get("card", r["desc"])))
    if not cards:
        return ""
    return '<section class="sec sec-stone"><div class="w"><h2>%s</h2><div class="cards">%s</div></div></section>' % (UI[lang]["rel"], "".join(cards))


def render(p):
    lang = p["lang"]
    if p.get("secs"):
        main = page_body(p)
    else:
        main = expand(p["body"](p, sys.modules[__name__]) if callable(p["body"]) else p["body"], lang)
    if p.get("service"):
        main += trust(lang)
    if p.get("faq"):
        main += faq_html(p["faq"], p.get("faq_title", UI[lang]["faq"]))
    main += related(p)
    if not p.get("no_form"):
        main += form(lang, p.get("form_title"))
    return "".join([head(p), '<body class="%s">' % p.get("cls", "inner"), header(p), '<main id="main">', main, "</main>",
                    footer(p), '<script src="/assets/app.js?v=%s" defer></script></body></html>\n' % VER])


def write(path, text):
    full = os.path.join(OUT, path.lstrip("/"))
    if full.endswith("/"):
        full += "index.html"
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(text)


def lastmods(pages):
    """lastmod changes only when a page's own text changes (src/lastmod.json, commit it)."""
    fn = os.path.join(HERE, "lastmod.json")
    try:
        old = json.load(open(fn, encoding="utf-8"))
    except FileNotFoundError:
        old = {}
    new = {}
    for p in pages:
        h = hashlib.sha1((DOMAIN + strip(p["html"].split('<main id="main">', 1)[1])).encode("utf-8")).hexdigest()[:12]
        prev = old.get(p["path"])
        new[p["path"]] = prev if prev and prev[0] == h else [h, TODAY]
    json.dump(new, open(fn, "w", encoding="utf-8"), ensure_ascii=False, indent=0, sort_keys=True)
    return {k: v[1] for k, v in new.items()}


def sitemaps(pages):
    mod = lastmods(pages)
    rows = []
    for p in pages:
        if p.get("noindex"):
            continue
        el, en = path_of("el", p["key"]), path_of("en", p["key"])
        alts = ('<xhtml:link rel="alternate" hreflang="el" href="%s%s"/><xhtml:link rel="alternate" hreflang="en" href="%s%s"/>'
                '<xhtml:link rel="alternate" hreflang="x-default" href="%s%s"/>') % (DOMAIN, el, DOMAIN, en, DOMAIN, el)
        rows.append("<url><loc>%s%s</loc><lastmod>%s</lastmod>%s</url>" % (DOMAIN, p["path"], mod[p["path"]], alts))
    write("/sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
          + "\n".join(rows) + "\n</urlset>\n")


def main():
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    os.makedirs(os.path.join(OUT, "assets"))
    build_images()
    load_ill()
    shutil.copytree(os.path.join(HERE, "ill"), os.path.join(OUT, "ill"))
    for f in os.listdir(os.path.join(HERE, "static")):
        shutil.copy(os.path.join(HERE, "static", f), os.path.join(OUT, "assets" if f.endswith((".css", ".js")) else "", f))
    for lang in ("el", "en"):
        for key, p in CONTENT[lang].PAGES.items():
            p.update(key=key, lang=lang)
            p.setdefault("path", ("/" if lang == "el" else "/en/") + (p["slug"] + "/" if p.get("slug") else ""))
            PAGES[(lang, key)] = p
    keys = {lang: {k for (l, k) in PAGES if l == lang} for lang in ("el", "en")}
    if keys["el"] != keys["en"]:
        sys.exit("pages missing in one language: %s" % (keys["el"] ^ keys["en"]))
    pages = list(PAGES.values())
    for p in pages:
        p["html"] = render(p)
        write(p["path"], p["html"])
    # checks: internal links, title/description length, duplicate titles
    paths = {p["path"] for p in pages}
    bad = sorted({(p["path"], h) for p in pages for h in re.findall(r'href="(/[^"#?]*)', p["html"])
                  if not h.startswith(("/ill/", "/img/", "/assets/")) and "." not in h.rsplit("/", 1)[-1] and h not in paths})
    for b in bad:
        print("BROKEN LINK", *b)
    titles = {}
    for p in pages:
        titles.setdefault(p["title"], []).append(p["path"])
        if not 25 <= len(p["title"]) <= 70:
            print("TITLE LENGTH %d %s" % (len(p["title"]), p["path"]))
        if not 70 <= len(p["desc"]) <= 165:
            print("DESC LENGTH %d %s" % (len(p["desc"]), p["path"]))
    for t, ps in titles.items():
        if len(ps) > 1:
            print("DUPLICATE TITLE", t, ps)
    for lang in ("el", "en"):
        nf = dict(CONTENT[lang].NOT_FOUND, key="home", lang=lang, path="/404.html" if lang == "el" else "/en/404.html", noindex=True)
        write(nf["path"], render(nf))
    sitemaps(pages)
    write("/robots.txt", "User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n" % DOMAIN)
    write("/_headers", "/img/*\n  Cache-Control: public, max-age=2592000\n/ill/*\n  Cache-Control: public, max-age=2592000\n/assets/*\n  Cache-Control: public, max-age=31536000, immutable\n"
          "/*\n  X-Content-Type-Options: nosniff\n  Referrer-Policy: strict-origin-when-cross-origin\n")
    write("/site.webmanifest", json.dumps({"name": NAME["el"], "short_name": "Γυψοσανίδες", "start_url": "/", "display": "browser",
                                           "background_color": "#f6f4ef", "theme_color": THEME,
                                           "icons": [{"src": "/icon-192.png", "sizes": "192x192", "type": "image/png"},
                                                     {"src": "/icon-512.png", "sizes": "512x512", "type": "image/png"}]}, ensure_ascii=False))
    words = sum(len(strip(p["html"].split('<main id="main">', 1)[1]).split()) for p in pages)
    print("pages:", len(pages), "words:", words, "illustrations:", len(ILL_SIZE), "broken links:", len(bad))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
