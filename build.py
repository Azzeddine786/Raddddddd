#!/usr/bin/env python3
"""
Radio Maroc static site builder (stdlib only).

Usage:
  python3 build.py                       # builds ./site for GitHub Pages project path
  python3 build.py --url https://radiomaroc.ma --base "" --email contact@radiomaroc.ma
  python3 build.py --adsense ca-pub-1234567890123456   # only AFTER AdSense gives you the code

Edit content in ./content (articles/*.html, pages/*.html, stations.json), then re-run.
"""
import argparse, json, math, os, re, shutil, sys
from html import escape as esc

ROOT = os.path.dirname(os.path.abspath(__file__))

ap = argparse.ArgumentParser()
ap.add_argument("--url", default="https://azzeddine786.github.io/Raddddddd", help="public site URL, no trailing slash")
ap.add_argument("--base", default=None, help="path prefix ('' for a custom domain). Default: derived from --url")
ap.add_argument("--email", default="contact@radiomaroc.example", help="public contact email")
ap.add_argument("--adsense", default="", help="AdSense publisher id, e.g. ca-pub-1234567890123456")
ap.add_argument("--out", default=os.path.join(ROOT, "site"))
args = ap.parse_args()

SITE_URL = args.url.rstrip("/")
if args.base is None:
    m = re.match(r"https?://[^/]+(/.*)?$", SITE_URL)
    BASE = (m.group(1) or "").rstrip("/")
else:
    BASE = args.base.rstrip("/")
EMAIL = args.email
ADSENSE = args.adsense.strip()
OUT = args.out

SITE_NAME = "راديو المغرب"
SITE_TAGLINE = "دليل مستقل للاستماع إلى الإذاعات المغربية"
APP_URL = "https://play.google.com/store/apps/details?id=com.maradioazdhj.radiomoroccoandab"
PUBLISHED = "2026-11-18"
MODIFIED = "2026-11-18"
MONTHS = ["يناير", "فبراير", "مارس", "أبريل", "ماي", "يونيو", "يوليوز", "غشت", "شتنبر", "أكتوبر", "نونبر", "دجنبر"]


def ar_date(iso):
    y, m, d = iso.split("-")
    return "%d %s %s" % (int(d), MONTHS[int(m) - 1], y)


UPDATED = ar_date(MODIFIED)

ARTICLE_ORDER = [
    "best-moroccan-radio-stations-2026",
    "history-of-moroccan-radio",
    "choose-radio-car-phone-morocco",
    "regional-moroccan-radio-guide",
    "listen-radio-online-morocco",
]
PAGE_ORDER = ["about", "contact", "privacy", "terms", "disclaimer", "cookies"]
PAGE_TYPES = {"about": "AboutPage", "contact": "ContactPage"}


def fill(t):
    return (t.replace("{{BASE}}", BASE).replace("{{SITE_URL}}", SITE_URL).replace("{{EMAIL}}", EMAIL)
             .replace("{{APP_URL}}", APP_URL).replace("{{SITE_NAME}}", SITE_NAME).replace("{{UPDATED}}", UPDATED))


def read_content(path):
    raw = open(path, encoding="utf8").read()
    m = re.match(r"\s*<!--(.*?)-->(.*)", raw, re.S)
    meta = {}
    for line in m.group(1).strip().splitlines():
        k, v = line.split(":", 1)
        meta[k.strip()] = v.strip()
    return meta, fill(m.group(2).strip())


def words(html):
    return len(re.findall(r"\S+", re.sub(r"<[^>]+>", " ", html)))


def url(path):
    """path like '/articles/x/' -> absolute canonical"""
    return SITE_URL + path


def href(path):
    return BASE + path


# ------------------------------------------------------------------ data
stations = json.load(open(os.path.join(ROOT, "content", "stations.json"), encoding="utf8"))
articles = []
for slug in ARTICLE_ORDER:
    meta, body = read_content(os.path.join(ROOT, "content", "articles", slug + ".html"))
    n = words(body)
    articles.append(dict(slug=slug, meta=meta, body=body, words=n, minutes=max(1, math.ceil(n / 200))))
pages = {}
for slug in PAGE_ORDER:
    meta, body = read_content(os.path.join(ROOT, "content", "pages", slug + ".html"))
    pages[slug] = dict(slug=slug, meta=meta, body=body)

# ------------------------------------------------------------------ fragments
WAVES = ('<svg width="170" height="170" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1" aria-hidden="true">'
         '<circle cx="12" cy="12" r="2.2" fill="#fff"/><path d="M7.5 7.5a6.4 6.4 0 000 9M16.5 7.5a6.4 6.4 0 010 9M4.8 4.8a10.2 10.2 0 000 14.4M19.2 4.8a10.2 10.2 0 010 14.4" stroke-linecap="round"/></svg>')

ICON_PLAY = '<svg width="13" height="13" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M8 5v14l11-7z"/></svg>'
ICON_FAV = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" aria-hidden="true"><path d="M19 21l-7-5-7 5V5a2 2 0 012-2h10a2 2 0 012 2z"/></svg>'


def app_icon(size, cls="app-icon", eager=False):
    return ('<span class="%s" style="width:%dpx;height:%dpx"><img src="%s" alt="أيقونة تطبيق راديو المغرب" width="%d" height="%d" decoding="async"%s></span>'
            % (cls, size, size, href("/assets/app-icon.png"), size, size, "" if eager else ' loading="lazy"'))


def article_card(a):
    return ('<a class="acard" href="%s"><div class="band">%s</div><div class="body"><span class="pill">%s</span>'
            '<h3>%s</h3><p>%s</p><span class="more">اقرأ المقال ←</span></div></a>'
            % (href("/articles/%s/" % a["slug"]), WAVES, esc(a["meta"]["category"]), esc(a["meta"]["title"]), esc(a["meta"]["description"])))


def station_card(s):
    search = " ".join([s["name"], s["cat"], s["city"], s["lang"], s["desc"]]).lower()
    return (
        '<article class="station" data-id="%d" data-cat="%s" data-lang="%s" data-search="%s">'
        '<div class="tile-top"><div class="logo"><span>%s</span><img src="%s" alt="شعار %s" width="62" height="62" loading="lazy" decoding="async" referrerpolicy="no-referrer" onerror="this.remove()"></div>'
        '<button class="fav" type="button" data-fav="%d" aria-pressed="false" aria-label="حفظ %s في المفضلة">%s</button></div>'
        '<h3>%s</h3><p class="meta">%s • %s</p>'
        '<div class="tile-foot"><button class="play" type="button" data-play="%d" aria-label="استمع إلى %s">'
        '<span class="disc">%s</span><span class="play-label">استمع</span></button><span class="tag">%s</span></div></article>'
        % (s["id"], esc(s["cat"]), esc(s["lang"]), esc(search), esc(s["init"]), esc(s["logo"]), esc(s["name"]),
           s["id"], esc(s["name"]), ICON_FAV, esc(s["name"]), esc(s["city"]), esc(s["lang"]),
           s["id"], esc(s["name"]), ICON_PLAY, esc(s["cat"])))


def jsonld(*objs):
    return "".join('<script type="application/ld+json">%s</script>\n' % json.dumps(o, ensure_ascii=False, separators=(",", ":")) for o in objs)


ORG = {
    "@type": "Organization", "@id": SITE_URL + "/#org", "name": SITE_NAME, "url": SITE_URL + "/",
    "logo": {"@type": "ImageObject", "url": url("/assets/app-icon.png"), "width": 512, "height": 512},
}


def breadcrumb(items):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": u} for i, (n, u) in enumerate(items)]}


NAV = [("home", "المحطات", "/#radios"), ("articles", "المقالات", "/articles/"), ("about", "من نحن", "/about/"), ("contact", "اتصل بنا", "/contact/")]


def shell(*, title, desc, path, body, og_type="website", ld="", current="", is_home=False, noindex=False, og_extra=""):
    canonical = url(path)
    robots = "noindex,follow" if noindex else "index,follow,max-image-preview:large"
    nav = "".join('<a href="%s"%s>%s</a>' % (href(p), ' aria-current="page"' if k == current else "", t) for k, t, p in NAV)
    ads = ('<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=%s" crossorigin="anonymous"></script>\n' % esc(ADSENSE)) if ADSENSE else ""
    foot_articles = "".join('<a href="%s">%s</a>' % (href("/articles/%s/" % a["slug"]), esc(a["meta"]["title"])) for a in articles[:3])
    player = ""
    promo = ""
    if is_home:
        player = ('<div class="player" id="playerBar" role="region" aria-label="مشغّل الإذاعة"><div class="wrap player-in">'
                  '<div class="logo" id="pLogo">RM</div><div class="pid"><b id="pName">اختر محطة</b>'
                  '<div class="pstat"><span class="dot" id="pDot" style="background:#777"></span><span id="pStatus" aria-live="polite">جاهز</span></div></div>'
                  '<button class="pbtn" id="playBtn" type="button" aria-label="تشغيل أو إيقاف مؤقت"><svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg></button>'
                  '<button class="pstop" id="stopBtn" type="button" aria-label="إغلاق المشغّل"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 6L6 18M6 6l12 12"/></svg></button>'
                  '</div></div>')
        promo = ('<div class="promo" id="promo" role="complementary">%s<div class="p-txt"><b>تطبيق راديو المغرب متاح الآن</b>'
                 '<small>استماع مباشر أسرع وواجهة مصممة للهاتف</small></div>'
                 '<a class="p-btn" href="%s" target="_blank" rel="noopener">تحميل</a>'
                 '<button class="p-close" id="promoClose" type="button" aria-label="إغلاق">✕</button></div>'
                 % (app_icon(40, "app-icon p-ico", True), APP_URL))
    return """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>%(title)s</title>
<meta name="description" content="%(desc)s">
<link rel="canonical" href="%(canonical)s">
<meta name="robots" content="%(robots)s">
<meta name="theme-color" content="#b63539">
<link rel="icon" href="%(favicon)s" type="image/svg+xml">
<link rel="icon" href="%(icon192)s" sizes="192x192" type="image/png">
<link rel="apple-touch-icon" href="%(apple)s">
<meta property="og:site_name" content="%(site)s">
<meta property="og:locale" content="ar_MA">
<meta property="og:type" content="%(og_type)s">
<meta property="og:title" content="%(title)s">
<meta property="og:description" content="%(desc)s">
<meta property="og:url" content="%(canonical)s">
<meta property="og:image" content="%(og_image)s">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="%(site)s - دليل الإذاعات المغربية">
%(og_extra)s<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="%(title)s">
<meta name="twitter:description" content="%(desc)s">
<meta name="twitter:image" content="%(og_image)s">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Arabic:wght@400;500;600;700&amp;display=swap" onload="this.onload=null;this.rel='stylesheet'">
<noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Arabic:wght@400;500;600;700&amp;display=swap"></noscript>
<link rel="stylesheet" href="%(css)s">
%(ads)s%(ld)s</head>
<body>
<a class="skip" href="#main">تخطَّ إلى المحتوى</a>
<header class="top"><div class="wrap top-inner">
<a class="brand" href="%(home)s" aria-label="%(site)s - الرئيسية">%(logo)s<span><span class="brand-name">راديو <em>المغرب</em></span><span class="brand-sub">RADIO MAROC</span></span></a>
<nav class="nav" id="mainNav" aria-label="التنقل الرئيسي">%(nav)s</nav>
<div class="tools"><time class="clock" id="clock" aria-hidden="true"></time><button class="menu-btn" id="menuBtn" type="button" aria-expanded="false" aria-controls="mainNav">القائمة</button></div>
</div></header>
%(promo)s
<main id="main">
%(body)s
</main>
<footer class="foot"><div class="wrap">
<div class="foot-in">
<div><b>%(site)s</b><p>%(tagline)s. نكتب أدلتنا بأنفسنا ولا نتبع أي محطة.</p></div>
<nav class="foot-links" aria-label="روابط التذييل"><a href="%(home)s#radios">المحطات</a><a href="%(articles)s">المقالات</a><a href="%(about)s">من نحن</a><a href="%(contact)s">اتصل بنا</a><a href="%(privacy)s">الخصوصية</a><a href="%(terms)s">شروط الاستخدام</a><a href="%(disc)s">إخلاء المسؤولية</a><a href="%(cookies)s">الكوكيز</a></nav>
</div>
<div class="foot-links" style="margin-top:14px">%(foot_articles)s</div>
<div class="copy">© 2026 %(site)s. الأسماء والشعارات ملك لأصحابها وتُعرض للتعريف فقط.</div>
</div></footer>
%(player)s
<div class="cookie" id="cookieBar" role="dialog" aria-label="إشعار ملفات تعريف الارتباط"><p>نستعمل التخزين المحلي (لحفظ مفضلتك) وقد نعرض إعلانات من أطراف ثالثة تستعمل ملفات تعريف الارتباط. اطّلع على <a href="%(cookies)s">سياسة الكوكيز</a> و<a href="%(privacy)s">الخصوصية</a>.</p><button id="cookieOk" type="button">موافق</button></div>
<div class="toast" id="toast" role="status" aria-live="polite"></div>
<script src="%(js)s" defer></script>
</body>
</html>
""" % dict(
        title=esc(title), desc=esc(desc), canonical=canonical, robots=robots, site=SITE_NAME, og_type=og_type,
        og_image=url("/assets/og-image.png"), og_extra=og_extra, css=href("/assets/style.css"), js=href("/assets/app.js"),
        favicon=href("/assets/favicon.svg"), icon192=href("/assets/icon-192.png"), apple=href("/assets/apple-touch-icon.png"),
        ads=ads, ld=ld, promo=promo, home=href("/"), logo=('<img src="%s" alt="" width="44" height="44">' % href("/assets/app-icon-96.png")),
        nav=nav, body=body, tagline=SITE_TAGLINE, articles=href("/articles/"), about=href("/about/"), contact=href("/contact/"),
        privacy=href("/privacy/"), terms=href("/terms/"), disc=href("/disclaimer/"), cookies=href("/cookies/"),
        foot_articles=foot_articles, player=player)


def write(path, content, binary=False):
    full = os.path.join(OUT, path.lstrip("/"))
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf8") as f:
        f.write(content)


# ------------------------------------------------------------------ pages
def build_home():
    cats = ["موسيقى", "أخبار", "وطنية", "جهوية", "دينية", "رياضة", "مجتمع"]
    chips = ['<button class="chip" type="button" data-filter="all" aria-pressed="true">الكل</button>']
    chips += ['<button class="chip" type="button" data-filter="cat:%s" aria-pressed="false">%s</button>' % (c, c) for c in cats]
    chips += ['<button class="chip" type="button" data-filter="lang:فرنسية" aria-pressed="false">بالفرنسية</button>',
              '<button class="chip" type="button" data-filter="fav" aria-pressed="false">⭐ المفضلة</button>']
    cards = "".join(station_card(s) for s in stations)
    acards = "".join(article_card(a) for a in articles)
    faq = [
        ("كيف أستمع إلى إذاعة مغربية مباشرة؟", "ابحث عن المحطة بالاسم أو اختر تصنيفاً من الأعلى، ثم اضغط «استمع». يظهر المشغّل أسفل الصفحة وتستطيع إيقاف البث أو إغلاقه في أي لحظة. لا تحتاج إلى حساب أو تسجيل."),
        ("هل الاستماع مجاني؟", "نعم، الدليل مجاني بالكامل. يأتي البث من خوادم المحطات نفسها، وتستهلك فقط بيانات الإنترنت الخاصة بك، ويُقدَّر ذلك بين 14 و58 ميغابايت في الساعة بحسب جودة البث."),
        ("لماذا يتوقف البث أو لا يعمل أحياناً؟", "يعتمد البث على خادم كل محطة وعلى جودة اتصالك. جرّب محطة أخرى للتحقق، وأعد تحميل الصفحة، وإن استمر الخلل فأخبرنا ليتم إصلاح الرابط. وفي مقال الاستماع عبر الإنترنت حلول لأغلب المشاكل."),
        ("هل يمكنني الاستماع من خارج المغرب؟", "نعم في الغالب. معظم المحطات تبث للعالم، وقد تقيّد قلة منها البث جغرافياً لأسباب تتعلق بالحقوق."),
        ("كيف أحفظ محطاتي المفضلة؟", "اضغط أيقونة الحفظ في بطاقة المحطة. تُحفظ المفضلة على جهازك فقط داخل المتصفح، وتجدها في تصنيف «المفضلة»."),
        ("كيف أقترح محطة أو أبلغ عن رابط معطل؟", "راسلنا عبر صفحة الاتصال بذكر اسم المحطة ومدينتها ورابطها، وسنتحقق منها قبل الإضافة أو الإصلاح."),
    ]
    faq_html = "".join('<details class="faq"><summary>%s</summary><p>%s</p></details>' % (esc(q), esc(a)) for q, a in faq)
    body = """
<section class="wrap hero" aria-labelledby="h1">
<div class="hero-copy"><span class="kicker"><span class="dot"></span> دليل الإذاعات المغربية</span>
<h1 id="h1">استمع إلى الإذاعات المغربية <strong>مباشرة</strong> من هاتفك</h1>
<p>ميدي 1، هيت راديو، راديو مارس، شذى FM وعشرات المحطات الأخرى في مكان واحد: أخبار وموسيقى ورياضة وقرآن وأمازيغية. اضغط «استمع» وابدأ.</p>
<div class="hero-actions"><button class="btn btn-ivory" id="heroPlay" type="button">استمع الآن ▶</button><a class="btn btn-ghost" href="#radios">تصفح المحطات ↓</a></div></div>
<div class="hero-art" aria-hidden="true"><svg viewBox="0 0 520 324" fill="none"><rect x="40" y="40" width="440" height="244" rx="16" fill="#2c141a" stroke="#6c2d35" stroke-width="1.5"/><rect x="60" y="60" width="400" height="204" rx="10" fill="#1f0d12"/><circle cx="120" cy="130" r="40" stroke="#a84b52" stroke-width="1.5"/><circle cx="120" cy="130" r="20" stroke="#a84b52" stroke-width="1.5"/><circle cx="120" cy="130" r="6" fill="#e5a18f"/><text x="300" y="140" fill="#e5a18f" font-family="monospace" font-size="28" letter-spacing="4">88.9</text><text x="300" y="170" fill="#a84b52" font-family="monospace" font-size="12" letter-spacing="2">MHz</text><line x1="60" y1="200" x2="460" y2="200" stroke="#4a2a30"/><rect x="60" y="230" width="400" height="8" rx="4" fill="#4a2a30"/><rect x="60" y="230" width="180" height="8" rx="4" fill="#e5a18f"/></svg></div>
</section>

<section id="radios" class="wrap sec" aria-labelledby="dir-h">
<div class="head"><div><div class="eyebrow">STATION DIRECTORY</div><h2 class="sec-title" id="dir-h">دليل المحطات <span class="count" id="countTxt">%(n)d</span></h2></div>
<label class="search"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#6b6966" stroke-width="2" aria-hidden="true"><circle cx="11" cy="11" r="8"/><path d="M21 21l-4.35-4.35"/></svg><input id="mainSearch" type="search" placeholder="ابحث عن محطة أو مدينة…" aria-label="ابحث عن محطة"></label></div>
<p class="intro">يضم الدليل %(n)d محطة وقناة: إذاعات وطنية وخاصة، وقنوات موسيقية متخصصة، وإذاعات جهوية ودينية وأمازيغية. اختر تصنيفاً أو ابحث بالاسم، ثم اضغط «استمع». تعرّف أكثر على محطات مناسبة لك في <a href="%(best)s">أفضل 10 إذاعات مغربية في 2026</a>.</p>
<div class="filters" role="group" aria-label="تصفية المحطات">%(chips)s</div>
<div class="grid" id="stationGrid">%(cards)s</div>
<div class="empty" id="emptyBox" hidden>لا توجد محطات مطابقة. جرّب كلمة أخرى أو <a href="%(contact)s">اقترح محطة</a>.</div>
</section>

<section class="wrap sec" aria-labelledby="art-h">
<div class="head"><div><div class="eyebrow">LISTENING GUIDES</div><h2 class="sec-title" id="art-h">دليل المستمع</h2></div><a href="%(articles)s" style="font-weight:700">كل المقالات ←</a></div>
<p class="intro">مقالات كتبناها لنساعدك على اختيار الإذاعة المناسبة، وفهم تاريخ الإذاعة المغربية، والاستماع إليها عبر الإنترنت دون مشاكل.</p>
<div class="agrid">%(acards)s</div>
</section>

<div class="wrap"><div class="app-card">%(icon)s<div><b>تجربة أفضل على هاتفك مع تطبيق راديو المغرب</b><small>استماع مباشر أسرع وواجهة مصممة للهاتف، مجاناً على Google Play.</small></div><a class="btn" href="%(app)s" target="_blank" rel="noopener">تحميل التطبيق</a></div></div>

<section class="wrap box" aria-labelledby="about-h">
<h2 id="about-h">عن راديو المغرب</h2>
<p>«راديو المغرب» دليل تحريري مستقل يجمع الإذاعات المغربية في مكان واحد: موسيقى شعبية وعصرية، أخبار ورياضة، ثقافة وحوار، وبرامج دينية وقرآن كريم وإذاعات أمازيغية. لا نتبع أي محطة، ونكتب أدلتنا بأنفسنا لنفيد المستمع. اقرأ المزيد في صفحة <a href="%(about)s">من نحن</a>.</p>
<h3>أسئلة شائعة</h3>
%(faq)s
</section>
""" % dict(n=len(stations), chips="".join(chips), cards=cards, acards=acards, icon=app_icon(64), app=APP_URL, faq=faq_html,
           best=href("/articles/best-moroccan-radio-stations-2026/"), contact=href("/contact/"), articles=href("/articles/"), about=href("/about/"))
    stations_json = json.dumps([{k: s[k] for k in ("id", "name", "init", "stream", "logo")} for s in stations], ensure_ascii=False, separators=(",", ":"))
    body += '<script type="application/json" id="stations-data">%s</script>' % stations_json.replace("</", "<\\/")
    title = "راديو المغرب | استمع إلى الإذاعات المغربية مباشرة"
    desc = "دليل الإذاعات المغربية: استمع مباشرة إلى ميدي 1 وهيت راديو وراديو مارس وشذى FM وأكثر من 40 محطة، مع أدلة ومقالات تساعدك على الاختيار."
    ld = jsonld(
        {"@context": "https://schema.org", "@graph": [
            {"@type": "WebSite", "@id": SITE_URL + "/#website", "url": SITE_URL + "/", "name": SITE_NAME, "description": desc, "inLanguage": "ar", "publisher": {"@id": SITE_URL + "/#org"}},
            ORG,
            {"@type": "ItemList", "name": "دليل المقالات", "itemListElement": [
                {"@type": "ListItem", "position": i + 1, "url": url("/articles/%s/" % a["slug"]), "name": a["meta"]["title"]} for i, a in enumerate(articles)]},
        ]})
    write("index.html", shell(title=title, desc=desc, path="/", body=body, ld=ld, current="home", is_home=True))


def build_articles_hub():
    body = """
<div class="wrap page" style="max-width:1200px">
<nav class="crumbs" aria-label="مسار التنقل"><a href="%(home)s">الرئيسية</a> › المقالات</nav>
<h1>مقالات وأدلة الاستماع</h1>
<p class="intro">أدلة عملية عن الإذاعات المغربية: كيف تختار محطتك، وكيف نشأت الإذاعة في المغرب، وكيف تستمع إليها في سيارتك وهاتفك وعبر الإنترنت.</p>
<div class="agrid">%(cards)s</div>
</div>""" % dict(home=href("/"), cards="".join(article_card(a) for a in articles))
    title = "مقالات وأدلة الإذاعات المغربية | راديو المغرب"
    desc = "أدلة ومقالات عن الإذاعات المغربية: أفضل المحطات، تاريخ الإذاعة، الإذاعات الجهوية، الاستماع في السيارة والهاتف وعبر الإنترنت."
    ld = jsonld({"@context": "https://schema.org", "@type": "CollectionPage", "name": "مقالات وأدلة الإذاعات المغربية", "url": url("/articles/"), "inLanguage": "ar", "isPartOf": {"@id": SITE_URL + "/#website"}},
                breadcrumb([("الرئيسية", url("/")), ("المقالات", url("/articles/"))]))
    write("articles/index.html", shell(title=title, desc=desc, path="/articles/", body=body, ld=ld, current="articles"))


def add_ids(html):
    heads = []

    def sub(m):
        i = len(heads) + 1
        heads.append((i, re.sub(r"<[^>]+>", "", m.group(1))))
        return '<h2 id="s%d">%s</h2>' % (i, m.group(1))
    return re.sub(r"<h2>(.*?)</h2>", sub, html, flags=re.S), heads


def build_article(i, a):
    meta, slug = a["meta"], a["slug"]
    path = "/articles/%s/" % slug
    body_html, heads = add_ids(a["body"])
    toc = '<nav class="toc" aria-label="محتويات المقال"><b>محتويات المقال</b><ol>%s</ol></nav>' % "".join('<li><a href="#s%d">%s</a></li>' % (n, esc(t)) for n, t in heads)
    related = [articles[(i + k) % len(articles)] for k in (1, 2, 3)]
    body = """
<article class="wrap page" itemscope itemtype="https://schema.org/Article">
<nav class="crumbs" aria-label="مسار التنقل"><a href="%(home)s">الرئيسية</a> › <a href="%(hub)s">المقالات</a> › %(cat)s</nav>
<span class="pill">%(cat)s</span>
<h1 itemprop="headline">%(title)s</h1>
<div class="byline"><span>بقلم: فريق تحرير راديو المغرب</span><span>نُشر: <time datetime="%(pub)s">%(pubar)s</time></span><span>آخر تحديث: <time datetime="%(mod)s">%(modar)s</time></span><span>القراءة: %(min)d دقائق</span></div>
%(toc)s
<div class="prose">%(body)s</div>
<div class="cta"><div><b>جاهز للاستماع؟</b><span>اختر محطتك من الدليل واضغط «استمع».</span></div><a class="btn btn-ivory" href="%(dir)s">افتح دليل المحطات ←</a></div>
<div class="authorbox"><img src="%(logo)s" alt="" width="52" height="52" style="border-radius:22%%"><p><b>فريق تحرير راديو المغرب</b><br>نكتب هذه الأدلة بأنفسنا ونراجعها دورياً. وجدت خطأً أو لديك اقتراح؟ <a href="%(contact)s">راسلنا</a>، وانظر <a href="%(about)s">منهجنا التحريري</a>.</p></div>
<section class="related" aria-labelledby="rel-h"><h2 id="rel-h">مقالات ذات صلة</h2><div class="agrid">%(rel)s</div></section>
</article>""" % dict(home=href("/"), hub=href("/articles/"), cat=esc(meta["category"]), title=esc(meta["title"]), pub=PUBLISHED, pubar=ar_date(PUBLISHED),
                      mod=MODIFIED, modar=ar_date(MODIFIED), min=a["minutes"], toc=toc, body=body_html, dir=href("/#radios"), logo=href("/assets/app-icon-96.png"),
                      contact=href("/contact/"), about=href("/about/"), rel="".join(article_card(r) for r in related))
    kws = [meta["primary"]] + [k.strip() for k in meta["secondary"].split(",")]
    ld = jsonld(
        {"@context": "https://schema.org", "@type": "Article", "headline": meta["title"], "description": meta["description"], "inLanguage": "ar",
         "datePublished": PUBLISHED, "dateModified": MODIFIED, "wordCount": a["words"], "keywords": ", ".join(kws),
         "image": [url("/assets/og-image.png")], "mainEntityOfPage": {"@type": "WebPage", "@id": url(path)},
         "author": {"@type": "Organization", "name": "فريق تحرير " + SITE_NAME, "url": url("/about/")},
         "publisher": ORG, "isPartOf": {"@id": SITE_URL + "/#website"}},
        breadcrumb([("الرئيسية", url("/")), ("المقالات", url("/articles/")), (meta["title"], url(path))]))
    extra = ('<meta property="article:published_time" content="%sT08:00:00+01:00">\n<meta property="article:modified_time" content="%sT08:00:00+01:00">\n'
             '<meta property="article:section" content="%s">\n' % (PUBLISHED, MODIFIED, esc(meta["category"])))
    write(path + "index.html", shell(title=meta["seo_title"], desc=meta["description"], path=path, body=body, og_type="article", ld=ld, current="articles", og_extra=extra))


def build_page(slug):
    p = pages[slug]
    path = "/%s/" % slug
    meta = p["meta"]
    body = """
<div class="wrap page">
<nav class="crumbs" aria-label="مسار التنقل"><a href="%s">الرئيسية</a> › %s</nav>
<h1>%s</h1>
<div class="prose">%s</div>
</div>""" % (href("/"), esc(meta["title"]), esc(meta["title"]), p["body"])
    ld = jsonld({"@context": "https://schema.org", "@type": PAGE_TYPES.get(slug, "WebPage"), "name": meta["title"], "url": url(path), "inLanguage": "ar",
                 "description": meta["description"], "isPartOf": {"@id": SITE_URL + "/#website"}},
                breadcrumb([("الرئيسية", url("/")), (meta["title"], url(path))]))
    write(path + "index.html", shell(title=meta["seo_title"], desc=meta["description"], path=path, body=body, ld=ld, current=slug))


def build_404():
    body = """
<div class="wrap page" style="text-align:center;padding-block:70px">
<h1>الصفحة غير موجودة</h1>
<p>ربما تغيّر الرابط أو حُذفت الصفحة. يمكنك العودة إلى <a href="%s">دليل المحطات</a> أو تصفح <a href="%s">المقالات</a>.</p>
</div>""" % (href("/"), href("/articles/"))
    write("404.html", shell(title="الصفحة غير موجودة | راديو المغرب", desc="الصفحة المطلوبة غير موجودة.", path="/404.html", body=body, noindex=True))


def build_static_files():
    urls = [("/", "1.0"), ("/articles/", "0.9")]
    urls += [("/articles/%s/" % a["slug"], "0.8") for a in articles]
    urls += [("/%s/" % s, "0.5" if s in ("about", "contact") else "0.3") for s in PAGE_ORDER]
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for p, pr in urls:
        sm.append("<url><loc>%s</loc><lastmod>%s</lastmod><priority>%s</priority></url>" % (url(p), MODIFIED, pr))
    sm.append("</urlset>")
    write("sitemap.xml", "\n".join(sm) + "\n")
    write("robots.txt", "User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n" % SITE_URL)
    if ADSENSE:
        pub = ADSENSE.replace("ca-", "")
        write("ads.txt", "google.com, %s, DIRECT, f08c47fec0942fa0\n" % pub)
    write("assets/favicon.svg", '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><rect width="24" height="24" rx="5" fill="#b63539"/><g fill="none" stroke="#fff" stroke-width="1.6" stroke-linecap="round"><path d="M7.5 7.5a6.4 6.4 0 000 9M16.5 7.5a6.4 6.4 0 010 9M4.8 4.8a10.2 10.2 0 000 14.4M19.2 4.8a10.2 10.2 0 010 14.4"/></g><circle cx="12" cy="12" r="2.2" fill="#fff"/></svg>')
    write(".nojekyll", "")


# ------------------------------------------------------------------ run
if os.path.isdir(OUT):
    shutil.rmtree(OUT)
os.makedirs(OUT)
for f in os.listdir(os.path.join(ROOT, "assets")):
    os.makedirs(os.path.join(OUT, "assets"), exist_ok=True)
    shutil.copy(os.path.join(ROOT, "assets", f), os.path.join(OUT, "assets", f))
build_home()
build_articles_hub()
for i, a in enumerate(articles):
    build_article(i, a)
for s in PAGE_ORDER:
    build_page(s)
build_404()
build_static_files()

print("Built %d pages into %s" % (1 + 1 + len(articles) + len(PAGE_ORDER) + 1, OUT))
print("SITE_URL=%s  BASE='%s'" % (SITE_URL, BASE))
for a in articles:
    print("  %-38s %5d words  title=%2d chars  desc=%3d chars" % (a["slug"], a["words"], len(a["meta"]["seo_title"]), len(a["meta"]["description"])))
if "example" in EMAIL:
    print("WARNING: using placeholder email %s -> pass --email your@real-address" % EMAIL)
if BASE and ".github.io" in SITE_URL:
    print("NOTE: robots.txt/sitemap at a github.io sub-path are not read by crawlers from the domain root; use a custom domain.")
