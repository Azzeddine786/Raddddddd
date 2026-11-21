# -*- coding: utf-8 -*-
"""Radio Maroc site generator.
Usage:  python3 tools/build.py [SRC_DIR] [OUT_DIR]
Reads the existing Arabic site (SRC), writes the trilingual site (OUT):
 - Arabic stays at the root, French in /fr/, English in /en/
 - station pages, guides, hubs, home pages, static pages, sitemap, feed, manifest
Edit data/frequencies.json (verified FM numbers) and re-run to refresh the frequency tables."""
import os, re, sys, json, html, shutil
from urllib.parse import quote
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from i18n_data import *
from content_stations import STATIONS
from content_guides import GUIDES
from content_legal import LEGAL, EMAIL

SRC = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/site/Raddddddd-main'
OUT = sys.argv[2] if len(sys.argv) > 2 else '/home/claude/out/radiomaroc-site'
TODAY = '2026-11-20'
CSSV = '?v=20261120'
PLAY_URL = 'https://play.google.com/store/apps/details?id=com.maradioazdhj.radiomoroccoandab'

def rd(p): return open(p, encoding='utf8').read()
def wr(p, s):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, 'w', encoding='utf8').write(s)
def esc(s): return html.escape(s, quote=True)
def fmt(s, **kw):
    for k, v in kw.items(): s = s.replace('{' + k + '}', v)
    return s

# ------------------------------------------------------------------ copy source
if os.path.exists(OUT): shutil.rmtree(OUT)
shutil.copytree(SRC, OUT)

# ------------------------------------------------------------------ stations
ar_index = rd(os.path.join(SRC, 'index.html'))
raw = re.search(r'id="stations-data"[^>]*>(.*?)</script>', ar_index, re.S).group(1).strip()
sdata = json.JSONDecoder().raw_decode(raw)[0]
cards = re.findall(r'<article class="station" data-id="(\d+)" data-cat="([^"]*)" data-lang="([^"]*)".*?<p class="meta">([^<]*)</p>', ar_index, re.S)
meta = {int(i): (c, l, m) for i, c, l, m in cards}
STN = {}
for s in sdata:
    c, l, m = meta[s['id']]
    STN[s['id']] = dict(id=s['id'], name=s['name'], init=s['init'], stream=s['stream'], logo=s.get('logo', ''),
                        cat=html.unescape(c), lang=html.unescape(l), city=html.unescape(m.split(' • ')[0]))
N_ST = len(STN)
ST_KEY = {v['id']: k for k, v in STATIONS.items()}

def sname(lang, sid):
    if lang == 'ar': return AR_NAME.get(sid, STN[sid]['name'])
    if lang == 'fr': return FR_NAME.get(sid, STN[sid]['name'])
    return EN_NAME.get(sid, STN[sid]['name'])

def join_and(lang, items):
    w = {'ar': ' و', 'fr': ' et ', 'en': ' and '}[lang]
    if len(items) <= 1: return ''.join(items)
    return ', '.join(items[:-1]) + w + items[-1] if lang != 'ar' else '، '.join(items[:-1]) + w + items[-1]

def lang_words(lang, sid):
    return [LANGWORD.get(x.strip(), {}).get(lang, x.strip()) for x in STN[sid]['lang'].split('/')]

# ------------------------------------------------------------------ page registry
STATIC = {
 'articles': dict(ar='articles', fr='articles', en='articles'),
 'about': dict(ar='about', fr='a-propos', en='about'),
 'contact': dict(ar='contact', fr='contact', en='contact'),
 'privacy': dict(ar='privacy', fr='confidentialite', en='privacy'),
 'terms': dict(ar='terms', fr='conditions-utilisation', en='terms'),
 'disclaimer': dict(ar='disclaimer', fr='avertissement', en='disclaimer'),
 'cookies': dict(ar='cookies', fr='cookies', en='cookies'),
}
AR_ONLY_KEYS = {'fix': 'radio-stream-not-working-fixes', 'car': 'choose-radio-car-phone-morocco', 'abroad': 'listen-moroccan-radio-abroad',
                'music': 'moroccan-music-on-radio', 'news': 'best-moroccan-news-radio', 'sports': 'sports-radio-morocco',
                'regional': 'regional-moroccan-radio-guide', 'ramadan': 'ramadan-radio-morocco', 'best': 'best-moroccan-radio-stations-2026',
                'history': 'history-of-moroccan-radio', 'amazigh': 'amazigh-radio-morocco'}

def url(key, lang):
    if key == 'home': return PREFIX[lang] + '/'
    if key in STATIC: return PREFIX[lang] + '/' + STATIC[key][lang]
    if key in GUIDES: return PREFIX[lang] + '/' + GUIDES[key]['slug'][lang]
    if key in STATIONS: return PREFIX[lang] + '/' + STATIONS[key]['slug'][lang]
    if key in AR_ONLY_KEYS: return '/' + AR_ONLY_KEYS[key]
    raise KeyError(key)

def abs_url(path): return SITE + path

def resolve(text, lang):
    def rep(m): return url(m.group(1), lang)
    text = re.sub(r'\{link:([a-z0-9\-]+)\}', rep, text)
    for tok, key in [('medi1ch', 'medi1-channels'), ('mrktng', 'marrakech-tangier'), ('frradio', 'french-radio'),
                     ('sports', 'sports'), ('news', 'news'), ('music', 'music'), ('ramadan', 'ramadan'), ('regional', 'regional')]:
        text = text.replace('{' + tok + '}', url(key, lang))
    for k in STATIC:
        text = text.replace('{' + k + '}', url(k, lang))
    return text.replace('{email}', EMAIL)

# ------------------------------------------------------------------ frequencies
FREQ_PATH = os.path.join(os.path.dirname(HERE), 'data', 'frequencies.json')
if not os.path.exists(FREQ_PATH): FREQ_PATH = os.path.join(SRC, 'data', 'frequencies.json')
FREQ = {'entries': []}
if os.path.exists(FREQ_PATH):
    try: FREQ = json.load(open(FREQ_PATH, encoding='utf8'))
    except Exception: pass

def freq_html(lang, sid=None):
    u = UI[lang]
    rows = [e for e in FREQ.get('entries', []) if e.get('mhz') and (sid is None or e.get('station') == sid)]
    if not rows:
        return '<div class="note-box">' + u['freq_none'] + '</div>'
    out = ['<table class="freq"><thead><tr>']
    if sid is None: out.append('<th>' + {'ar': 'المحطة', 'fr': 'Station', 'en': 'Station'}[lang] + '</th>')
    out.append('<th>' + u['freq_city'] + '</th><th>' + u['freq_mhz'] + '</th><th>' + u['freq_verified'] + '</th></tr></thead><tbody>')
    for e in rows:
        out.append('<tr>')
        if sid is None: out.append('<td>' + esc(sname(lang, e['station'])) + '</td>')
        city = CITY.get(e.get('city', ''), {}).get(lang, e.get('city', ''))
        out.append('<td>' + esc(city) + '</td><td dir="ltr">' + esc(str(e['mhz'])) + '</td><td dir="ltr">' + esc(e.get('verified', FREQ.get('last_verified', ''))) + '</td></tr>')
    out.append('</tbody></table>')
    return ''.join(out)

# ------------------------------------------------------------------ station lists
def stlist(flt, lang):
    u = UI[lang]
    kind, _, val = flt.partition(':')
    ids = []
    for sid, s in STN.items():
        if kind == 'prefix' and s['name'].startswith(val): ids.append(sid)
        elif kind == 'city' and s['city'] in val.split('|'): ids.append(sid)
        elif kind == 'lang' and val in s['lang'] and s['city'] in MOROCCAN_CITIES: ids.append(sid)
    if kind == 'ids': ids = [int(x) for x in val.split(',')]
    return stlist_ids(ids, lang)

def stlist_ids(ids, lang):
    u = UI[lang]
    out = ['<ul class="stn-list">']
    for sid in ids:
        s = STN[sid]
        n = esc(sname(lang, sid))
        link = url(ST_KEY[sid], lang) if sid in ST_KEY else None
        nm = '<a href="' + link + '">' + n + '</a>' if link else n
        cat = CAT.get(s['cat'], {}).get(lang, s['cat'])
        city = CITY.get(s['city'], {}).get(lang, s['city'])
        meta_ = ' · '.join([city, cat, join_and(lang, lang_words(lang, sid))]) if lang != 'ar' else ' · '.join([city, cat, '، '.join(lang_words(lang, sid))])
        out.append('<li><div class="sl-main"><b>' + nm + '</b><span class="sl-meta">' + esc(meta_) + '</span></div>'
                   '<button class="btn btn-red btn-sm" type="button" data-play="' + str(sid) + '" aria-label="' + esc(fmt(u['listen_to'], name=sname(lang, sid))) + '">▶ ' + u['listen'] + '</button></li>')
    out.append('</ul>')
    return ''.join(out)

def expand(body, lang):
    body = re.sub(r'\{\{STLIST:([^}]+)\}\}', lambda m: stlist(m.group(1), lang), body)
    body = body.replace('{{FREQ}}', freq_html(lang))
    return resolve(body, lang)

# ------------------------------------------------------------------ shared shell pieces
def grab(pat, s):
    m = re.search(pat, s, re.S)
    return m.group(0) if m else ''
GTM_HEAD = grab(r'<!-- ============ Google Tag Manager ============ -->.*?<!-- ============ End Google Tag Manager ============ -->', ar_index)
GA_HEAD = grab(r'<!-- ============ Google Analytics ============ -->.*?<!-- ============ End Google Analytics ============ -->', ar_index)
GTM_NS = grab(r'<!-- ============ Google Tag Manager \(noscript\) ============ -->.*?<!-- ============ End Google Tag Manager \(noscript\) ============ -->', ar_index)
WPADM = grab(r'<!-- ============ wpadmngr Ad Manager ============ -->.*?<!-- ============ End wpadmngr ============ -->', ar_index)
SWREG = grab(r'<!-- ============ Service Worker ============ -->.*?<!-- ============ End Service Worker ============ -->', ar_index)
BANNER = grab(r'<!-- ============ بانر إعلاني ============ -->.*?<!-- ============ نهاية البانر ============ -->', ar_index)

def alt_links(alts):
    if not alts: return ''
    out = ''.join('<link rel="alternate" hreflang="%s" href="%s">' % (l, abs_url(p)) for l, p in alts.items())
    return out + '<link rel="alternate" hreflang="x-default" href="%s">' % abs_url(alts.get('ar', list(alts.values())[0]))

def head(lang, title, desc, path, image, og_type, alts, jsonld, home=False, extra=''):
    u = UI[lang]
    img = abs_url('/' + image)
    canon = abs_url(path)
    parts = ['<!DOCTYPE html>\n<html lang="%s" dir="%s">\n<head>\n' % (HTML_LANG[lang], DIR[lang])]
    if home: parts.append(GTM_HEAD + '\n')
    parts.append('<meta charset="utf-8">\n<meta name="viewport" content="width=device-width,initial-scale=1">\n')
    parts.append('<title>%s</title>\n<meta name="description" content="%s">\n<link rel="canonical" href="%s">\n' % (esc(title), esc(desc), canon))
    parts.append(alt_links(alts) + '\n')
    parts.append('<meta name="robots" content="index,follow,max-image-preview:large">\n<meta name="theme-color" content="#b63539">\n')
    parts.append('<link rel="icon" href="/favicon.svg" type="image/svg+xml">\n<link rel="icon" href="/icon-192.png" sizes="192x192" type="image/png">\n<link rel="apple-touch-icon" href="/apple-touch-icon.png">\n')
    parts.append('<meta property="og:site_name" content="%s">\n<meta property="og:locale" content="%s">\n<meta property="og:type" content="%s">\n' % (esc(u['brand_plain']), OG_LOCALE[lang], og_type))
    parts.append('<meta property="og:title" content="%s">\n<meta property="og:description" content="%s">\n<meta property="og:url" content="%s">\n<meta property="og:image" content="%s">\n' % (esc(title), esc(desc), canon, img))
    parts.append('<meta property="og:image:width" content="1200">\n<meta property="og:image:height" content="630">\n<meta property="og:image:alt" content="%s">\n' % esc(u['brand_plain'] + ' - ' + u['dir_title']))
    for l in LANGS:
        if l != lang and alts and l in alts: parts.append('<meta property="og:locale:alternate" content="%s">\n' % OG_LOCALE[l])
    if og_type == 'article':
        parts.append('<meta property="article:published_time" content="%sT08:00:00+01:00">\n<meta property="article:modified_time" content="%sT08:00:00+01:00">\n' % (TODAY, TODAY))
    parts.append('<meta name="twitter:card" content="summary_large_image">\n<meta name="twitter:title" content="%s">\n<meta name="twitter:description" content="%s">\n<meta name="twitter:image" content="%s">\n' % (esc(title), esc(desc), img))
    parts.append('<link rel="preconnect" href="https://fonts.googleapis.com">\n<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n')
    font = 'https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Arabic:wght@400;500;600;700&amp;display=swap'
    parts.append('<link rel="preload" as="style" href="%s" onload="this.onload=null;this.rel=\'stylesheet\'">\n<noscript><link rel="stylesheet" href="%s"></noscript>\n' % (font, font))
    parts.append('<link rel="manifest" href="/manifest.webmanifest">\n<link rel="alternate" type="application/rss+xml" title="%s" href="/feed.xml">\n<link rel="stylesheet" href="/style.css%s">\n' % (esc(u['brand_plain']), CSSV))
    for j in jsonld:
        parts.append('<script type="application/ld+json">' + json.dumps(j, ensure_ascii=False, separators=(',', ':')) + '</script>\n')
    if home: parts.append(GA_HEAD + '\n')
    parts.append(extra + '</head>\n')
    return ''.join(parts)

def lang_switcher(lang, alts):
    out = ['<div class="langsw" role="group" aria-label="%s">' % esc(UI[lang]['lang_label'])]
    for l in LANGS:
        href = alts.get(l, PREFIX[l] + '/') if alts else PREFIX[l] + '/'
        cur = ' aria-current="true"' if l == lang else ''
        out.append('<a href="%s" hreflang="%s" lang="%s" title="%s"%s>%s</a>' % (href, l, l, LANG_NAME[l], cur, l.upper()))
    out.append('</div>')
    return ''.join(out)

def header(lang, alts, current=''):
    u = UI[lang]
    home = url('home', lang)
    def a(href, label, key):
        cur = ' aria-current="page"' if current == key else ''
        return '<a href="%s"%s>%s</a>' % (href, cur, label)
    nav = a(home + '#radios', u['stations'], 'home') + a(url('articles', lang), u['articles'], 'articles') + a(url('about', lang), u['about'], 'about') + a(url('contact', lang), u['contact'], 'contact')
    brand_sub = '<span class="brand-sub">%s</span>' % u['brand_sub']
    return ('<a class="skip" href="#main">%s</a>\n<header class="top"><div class="wrap top-inner">\n'
            '<a class="brand" href="%s" aria-label="%s"><img src="/app-icon-96.png" alt="" width="44" height="44"><span><span class="brand-name">%s</span>%s</span></a>\n'
            '<nav class="nav" id="mainNav" aria-label="%s">%s</nav>\n'
            '<div class="tools"><time class="clock" id="clock" aria-hidden="true"></time>%s<button class="menu-btn" id="menuBtn" type="button" aria-expanded="false" aria-controls="mainNav">%s</button></div>\n'
            '</div></header>\n') % (u['skip'], home, esc(u['brand_plain'] + ' - ' + u['home']), u['brand_html'], brand_sub, u['nav_label'], nav, lang_switcher(lang, alts), u['menu'])

def footer(lang):
    u = UI[lang]
    links = ''.join('<a href="%s">%s</a>' % (url(k, lang) if k != 'home' else url('home', lang) + '#radios', u[l]) for k, l in
                    [('home', 'stations'), ('articles', 'articles'), ('about', 'about'), ('contact', 'contact'), ('privacy', 'privacy'), ('terms', 'terms'), ('disclaimer', 'disclaimer'), ('cookies', 'cookies')])
    st = ''.join('<a href="%s">%s</a>' % (url(k, lang), esc(sname(lang, v['id']))) for k, v in STATIONS.items())
    langs = ''.join('<a href="%s" hreflang="%s" lang="%s">%s</a>' % (PREFIX[l] + '/', l, l, LANG_NAME[l]) for l in LANGS)
    return ('<footer class="foot"><div class="wrap">\n<div class="foot-in">\n<div><b>%s</b><p>%s</p></div>\n<nav class="foot-links" aria-label="%s">%s</nav>\n</div>\n'
            '<div class="foot-links" style="margin-top:14px"><b>%s:</b>%s</div>\n<div class="foot-links" style="margin-top:10px">%s</div>\n<div class="copy">%s</div>\n</div></footer>\n') % (
            u['brand_plain'], u['foot_tag'], u['footer_links'], links, u['foot_stations'], st, langs, u['copy'])

def player_block(lang):
    u = UI[lang]
    return ('<div class="player" id="playerBar" role="region" aria-label="%s"><div class="wrap player-in"><div class="logo" id="pLogo">RM</div><div class="pid"><b id="pName">%s</b>'
            '<div class="pstat"><span class="dot" id="pDot" style="background:#777"></span><span id="pStatus" aria-live="polite">%s</span></div></div>'
            '<button class="pbtn" id="playBtn" type="button" aria-label="%s"><svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg></button>'
            '<button class="pstop" id="stopBtn" type="button" aria-label="%s"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 6L6 18M6 6l12 12"/></svg></button></div></div>\n') % (
            u['player_aria'], u['p_choose'], u['p_ready'], u['p_toggle'], u['p_close'])

def tail(lang, with_player=True, home=False):
    u = UI[lang]
    i18n = dict(u['js']); i18n['brand'] = u['brand_plain']
    cookie = ('<div class="cookie" id="cookieBar" role="dialog" aria-label="%s"><p>%s</p><button id="cookieOk" type="button">%s</button></div>\n') % (
        u['cookie_aria'], fmt(u['cookie_msg'], cookies=url('cookies', lang), privacy=url('privacy', lang)), u['cookie_ok'])
    s = ''
    if with_player:
        s += player_block(lang)
        s += '<script type="application/json" id="stations-data">' + json.dumps(
            [dict(id=v['id'], name=(sname(lang, v['id']) if (v['id'] in ST_KEY and not home) else v['name']), init=v['init'], stream=v['stream'], logo=v['logo']) for v in STN.values()],
            ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/') + '</script>\n'
    s += cookie + '<div class="toast" id="toast" role="status" aria-live="polite"></div>\n'
    s += '<script>window.RM_LANG="%s";window.RM_I18N=%s;</script>\n' % (lang, json.dumps(i18n, ensure_ascii=False))
    s += '<script src="/app.js%s" defer></script>\n' % CSSV
    if home: s += '\n' + WPADM + '\n'
    return s + '</body>\n</html>\n'

def body_open(home=False):
    return '<body>\n' + (GTM_NS + '\n' if home else '')

def fmt_date(lang, d=TODAY):
    y, m, dd = d.split('-'); mi = int(m) - 1; dd = str(int(dd))
    M = {'ar': ['يناير', 'فبراير', 'مارس', 'أبريل', 'ماي', 'يونيو', 'يوليوز', 'غشت', 'شتنبر', 'أكتوبر', 'نونبر', 'دجنبر'],
         'fr': ['janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet', 'août', 'septembre', 'octobre', 'novembre', 'décembre'],
         'en': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']}
    if lang == 'en': return '%s %s, %s' % (M['en'][mi], dd, y)
    return '%s %s %s' % (dd, M[lang][mi], y)

# ------------------------------------------------------------------ metadata of all new pages (two-pass)
ART_OG = {'art-online.svg': 'og-listen-radio-online-morocco.jpg', 'art-music.svg': 'og-moroccan-music-on-radio.jpg',
          'art-regional.svg': 'og-regional-moroccan-radio-guide.jpg', 'art-car.svg': 'og-choose-radio-car-phone-morocco.jpg',
          'art-stations.svg': 'og-home.jpg'}
META = {l: {} for l in LANGS}

def station_texts(lang, key):
    st = STATIONS[key]; sid = st['id']; s = STN[sid]
    n = sname(lang, sid)
    cat = CAT.get(s['cat'], {}).get(lang, s['cat'])
    city = CITY.get(s['city'], {}).get(lang, s['city'])
    langs = join_and(lang, lang_words(lang, sid))
    if lang == 'ar':
        return st['ar_h1'], st['ar_mt'], st['ar_md']
    if lang == 'fr':
        mt = n + ' en direct : fréquence et programmes | Radio Maroc'
        if len(mt) > 65: mt = n + ' en direct | Radio Maroc'
        return (n + ' en direct : fréquence, programmes et écoute gratuite', mt,
                'Écoutez %s en direct : station %s basée à %s, en %s. Fréquence FM, programmes et écoute gratuite sur mobile.' % (n, cat.lower(), city, langs))
    return (n + ' Live: Listen Online, FM Frequency and Programs', n + ' live: frequency and programs | Radio Maroc',
            'Listen to %s live: a %s station based in %s broadcasting in %s. FM frequency info, programs and free online listening.' % (n, cat.lower(), city, langs))

for lang in LANGS:
    for key, g in GUIDES.items():
        t = g[lang]
        META[lang][key] = dict(title=t['title'], mt=t['mt'], desc=t['desc'], img=g['img'], pill=g['pill'], kind='guide')
    for key in STATIONS:
        h1, mt, md = station_texts(lang, key)
        META[lang][key] = dict(title=h1, mt=mt, desc=md, img='art-stations.svg', pill='pill_station', kind='station')

def card(lang, key, eager=False):
    m = META[lang][key]; u = UI[lang]
    return ('<a class="acard" href="%s"><div class="thumb"><img src="/%s" alt="" width="1200" height="630" decoding="async" loading="lazy"></div>'
            '<div class="body"><span class="pill">%s</span><h3>%s</h3><p>%s</p><span class="more">%s</span></div></a>') % (
            url(key, lang), m['img'], u[m['pill']], esc(m['title']), esc(m['desc']), u['read_more'])

def card_ar_only(lang, akey):
    img, pill, tr = AR_ONLY[AR_ONLY_KEYS[akey]] if False else AR_ONLY[AR_ONLY_KEYS[akey]]
    t, d = tr[lang]
    u = UI[lang]
    return ('<a class="acard" href="/%s" hreflang="ar"><div class="thumb"><img src="/%s" alt="" width="1200" height="630" decoding="async" loading="lazy"></div>'
            '<div class="body"><span class="pill">%s · AR</span><h3>%s</h3><p>%s</p><span class="more">%s</span></div></a>') % (
            AR_ONLY_KEYS[akey], img, u[pill], esc(t), esc(d), u['read_more'])

# ------------------------------------------------------------------ alternates
def alts_for(key):
    if key == 'home' or key in STATIC or key in GUIDES or key in STATIONS:
        return {l: url(key, l) for l in LANGS}
    return None

# ------------------------------------------------------------------ article / station page rendering
REL = {'listen-online': ['smart-speaker', 'fm-frequencies', 'medi1-channels'], 'medi1-channels': ['chaabi', 'medi-1-radio', 'listen-online'],
       'fm-frequencies': ['casablanca', 'marrakech-tangier', 'listen-online'], 'french-radio': ['medi-1-radio', 'atlantic-radio', 'casablanca'],
       'casablanca': ['radio-mars', 'hit-radio-maroc', 'fm-frequencies'], 'smart-speaker': ['listen-online', 'fm-frequencies', 'medi1-channels'],
       'chaabi': ['medi1-channels', 'chada-fm', 'medina-fm'], 'marrakech-tangier': ['medina-fm', 'cap-radio', 'fm-frequencies']}
STATION_CITY_GUIDE = {'الدار البيضاء': 'casablanca', 'طنجة': 'marrakech-tangier', 'مراكش': 'marrakech-tangier', 'الرباط': 'fm-frequencies'}

def add_ids(body):
    toc = []
    def rep(m):
        i = len(toc) + 1
        toc.append((i, re.sub(r'<[^>]+>', '', m.group(1))))
        return '<h2 id="s%d">%s</h2>' % (i, m.group(1))
    body = re.sub(r'<h2>(.*?)</h2>', rep, body, flags=re.S)
    return body, toc

def faq_ld(body):
    qa = re.findall(r'<details class="faq"><summary>(.*?)</summary><p>(.*?)</p></details>', body, re.S)
    if not qa: return None
    strip = lambda s: html.unescape(re.sub(r'<[^>]+>', '', s))
    return {'@context': 'https://schema.org', '@type': 'FAQPage', 'mainEntity': [
        {'@type': 'Question', 'name': strip(q), 'acceptedAnswer': {'@type': 'Answer', 'text': strip(a)}} for q, a in qa]}

def station_body(lang, key):
    u = UI[lang]; st = STATIONS[key]; sid = st['id']; s = STN[sid]; tx = st[lang]
    n = sname(lang, sid)
    cat = CAT.get(s['cat'], {}).get(lang, s['cat'])
    city = CITY.get(s['city'], {}).get(lang, s['city'])
    langs = join_and(lang, lang_words(lang, sid))
    logo = ('<img src="%s" alt="%s" width="78" height="78" loading="lazy" decoding="async" referrerpolicy="no-referrer" onerror="this.remove()">' % (esc(s['logo']), esc(fmt(u['logo_alt'], name=n)))) if s['logo'] else ''
    hero = ('<div class="stn-hero"><div class="stn-logo"><span>%s</span>%s</div><dl class="stn-facts"><div><dt>%s</dt><dd>%s</dd></div><div><dt>%s</dt><dd>%s</dd></div>'
            '<div><dt>%s</dt><dd>%s</dd></div><div><dt>%s</dt><dd>%s</dd></div></dl>'
            '<button class="btn btn-red" type="button" data-play="%d">%s</button></div>') % (
            esc(s['init']), logo, u['st_city'], esc(city), u['st_cat'], esc(cat), u['st_lang'], esc(langs), u['st_free'], u['st_free_v'], sid, u['listen_now'])
    fq = {
     'ar': [('كيف أستمع إلى %s مباشرة؟' % n, 'اضغط زر «استمع» في أعلى هذه الصفحة فيبدأ البث من متصفحك دون حساب أو تسجيل. وإن لم يعمل فأعد تحميل الصفحة أو راجع <a href="%s">دليل حلول انقطاع البث</a>.' % url('fix', lang)),
            ('ما تردد %s على موجة FM؟' % n, 'تختلف الترددات من مدينة إلى أخرى وقد تتغير، ولذلك لا ننشر رقماً قبل التحقق منه من مصدر رسمي. راجع الموقع الرسمي للمحطة أو <a href="%s">دليل الترددات حسب المدينة</a>. أما الاستماع عبر الإنترنت فلا يحتاج إلى تردد.' % url('fm-frequencies', lang)),
            ('بأي لغة تبث %s؟' % n, '%s محطة مقرها %s وتبث بـ%s، وهي مصنفة في دليلنا ضمن فئة «%s».' % (n, city, langs, cat))],
     'fr': [('Comment écouter %s en direct ?' % n, 'Appuyez sur « Écouter » en haut de cette page : le flux démarre dans votre navigateur, sans compte ni inscription. S\'il ne démarre pas, rechargez la page ou consultez le <a href="%s">guide des coupures de flux</a> (en arabe).' % url('fix', lang)),
            ('Quelle est la fréquence FM de %s ?' % n, 'Les fréquences varient d\'une ville à l\'autre et peuvent changer ; nous ne publions donc un chiffre qu\'après vérification auprès d\'une source officielle. Consultez le site officiel de la station ou notre <a href="%s">guide des fréquences par ville</a>. L\'écoute en ligne ne demande aucune fréquence.' % url('fm-frequencies', lang)),
            ('En quelles langues %s émet-elle ?' % n, '%s est une station basée à %s qui émet en %s ; notre guide la classe dans la catégorie « %s ».' % (n, city, langs, cat))],
     'en': [('How do I listen to %s live?' % n, 'Press “Listen” at the top of this page and the stream starts in your browser, with no account or sign-up. If it does not start, reload the page or see the <a href="%s">guide to stream cut-outs</a> (in Arabic).' % url('fix', lang)),
            ('What is the FM frequency of %s?' % n, 'Frequencies vary from city to city and can change, so we only publish a number once it is verified with an official source. Check the station’s official website or our <a href="%s">guide to frequencies by city</a>. Listening online needs no frequency.' % url('fm-frequencies', lang)),
            ('Which languages does %s broadcast in?' % n, '%s is a station based in %s that broadcasts in %s; our directory files it under “%s”.' % (n, city, langs, cat))]}[lang]
    faq = ''.join('<details class="faq"><summary>%s</summary><p>%s</p></details>' % (q, a) for q, a in fq)
    how = {'ar': '<ul><li><strong>من الهاتف أو الحاسوب:</strong> اضغط «استمع» أعلاه، ولا حاجة إلى حساب.</li><li><strong>في السيارة:</strong> اقرنه بالبلوتوث أو استعمل كابل AUX، أو ابحث عن التردد في مدينتك من <a href="%s">دليل الترددات</a>.</li><li><strong>من خارج المغرب:</strong> معظم المحطات تبث للعالم؛ التفاصيل في <a href="%s">دليل الاستماع أونلاين</a>.</li></ul>',
           'fr': '<ul><li><strong>Sur téléphone ou ordinateur :</strong> appuyez sur « Écouter » ci-dessus, sans compte.</li><li><strong>En voiture :</strong> associez-le en Bluetooth ou utilisez un câble AUX, ou cherchez la fréquence dans votre ville avec le <a href="%s">guide des fréquences</a>.</li><li><strong>Depuis l\'étranger :</strong> la plupart des stations diffusent dans le monde entier ; détails dans le <a href="%s">guide pour écouter en ligne</a>.</li></ul>',
           'en': '<ul><li><strong>On a phone or computer:</strong> press “Listen” above, no account needed.</li><li><strong>In the car:</strong> pair it by Bluetooth or use an AUX cable, or look up the frequency in your city in the <a href="%s">frequency guide</a>.</li><li><strong>From abroad:</strong> most stations broadcast worldwide; details in the <a href="%s">guide to listening online</a>.</li></ul>'}[lang] % (url('fm-frequencies', lang), url('listen-online', lang))
    sim = stlist_ids(st['sim'], lang)
    body = (hero + '<p>' + tx['intro'] + '</p>' + '<h2>' + u['st_h_hear'] + '</h2><p>' + tx['hear'] + '</p><p><strong>' + u['st_best'] + ':</strong> ' + tx['best'] + '</p>'
            + '<h2>' + u['st_h_freq'] + '</h2>' + freq_html(lang, sid) + '<h2>' + u['st_h_how'] + '</h2>' + how
            + '<h2>' + u['st_h_faq'] + '</h2>' + faq + '<h2>' + u['st_h_sim'] + '</h2>' + sim)
    return resolve(body, lang)

def render_page(lang, key):
    u = UI[lang]; m = META[lang][key]
    path = url(key, lang)
    is_station = m['kind'] == 'station'
    if is_station:
        raw_body = station_body(lang, key)
        read = 3
        kw = STATIONS[key]['kw'][lang] if lang in STATIONS[key]['kw'] else ''
    else:
        g = GUIDES[key]
        raw_body = expand(g[lang]['body'], lang)
        read = g['read']
        kw = g[lang]['kw']
    body, toc = add_ids(raw_body)
    toc_html = '<ol>' + ''.join('<li><a href="#s%d">%s</a></li>' % (i, t) for i, t in toc) + '</ol>'
    alts = alts_for(key)
    image = ART_OG.get(m['img'], 'og-home.jpg')
    words = len(re.sub(r'<[^>]+>', ' ', body).split())
    org = {'@type': 'Organization', '@id': SITE + '/#org', 'name': u['brand_plain'], 'url': SITE + '/', 'logo': {'@type': 'ImageObject', 'url': SITE + '/app-icon.png', 'width': 512, 'height': 512}}
    art = {'@context': 'https://schema.org', '@type': 'Article', 'headline': m['title'], 'description': m['desc'], 'inLanguage': lang, 'datePublished': TODAY, 'dateModified': TODAY,
           'wordCount': words, 'keywords': kw, 'articleSection': u[m['pill']], 'image': [abs_url('/' + image)], 'mainEntityOfPage': {'@type': 'WebPage', '@id': abs_url(path)},
           'author': {'@type': 'Organization', 'name': u['author_b'], 'url': abs_url(url('about', lang))}, 'publisher': org, 'isPartOf': {'@id': SITE + '/#website'}}
    crumbs = {'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': [
        {'@type': 'ListItem', 'position': 1, 'name': u['home'], 'item': abs_url(url('home', lang))},
        {'@type': 'ListItem', 'position': 2, 'name': u['articles'], 'item': abs_url(url('articles', lang))},
        {'@type': 'ListItem', 'position': 3, 'name': m['title'], 'item': abs_url(path)}]}
    ld = [art, crumbs]
    if is_station:
        sid = STATIONS[key]['id']; s = STN[sid]
        ld.append({'@context': 'https://schema.org', '@type': 'BroadcastService', 'name': sname(lang, sid), 'broadcastDisplayName': sname(lang, sid), 'description': m['desc'],
                   'inLanguage': [LANGWORD.get(x.strip(), {}).get('en', x.strip()) for x in s['lang'].split('/')], 'areaServed': 'MA', 'url': abs_url(path), 'provider': {'@id': SITE + '/#org'}})
    f = faq_ld(body)
    if f: ld.append(f)
    # related
    if is_station:
        city_guide = STATION_CITY_GUIDE.get(STN[STATIONS[key]['id']]['city'], 'fm-frequencies')
        rel_keys = [city_guide, 'fm-frequencies', 'listen-online']
        rel_keys = list(dict.fromkeys(rel_keys))[:3]
    else:
        rel_keys = REL[key]
    related = '<section class="related" aria-labelledby="rel-h"><h2 id="rel-h">%s</h2><div class="agrid">%s</div></section>' % (u['related'], ''.join(card(lang, k) for k in rel_keys))
    full = url_abs = abs_url(path)
    share = ('<div class="share"><a href="https://wa.me/?text=%s" target="_blank" rel="noopener">%s</a><a href="https://www.facebook.com/sharer/sharer.php?u=%s" target="_blank" rel="noopener">Facebook</a>'
             '<a href="https://twitter.com/intent/tweet?url=%s" target="_blank" rel="noopener">X</a><button type="button" data-copy="%s">%s</button></div>') % (
             quote(m['title'] + ' ' + full, safe=''), u['share_whatsapp'], esc(full), esc(full), esc(full), u['copy_link'])
    cta = '<div class="cta"><div><b>%s</b><span>%s</span></div><a class="btn btn-ivory" href="%s#radios">%s</a></div>' % (u['cta_b'], u['cta_s'], url('home', lang), u['cta_btn'])
    author = '<div class="authorbox"><img src="/app-icon-96.png" alt="" width="52" height="52" style="border-radius:22%%"><p><b>%s</b><br>%s</p></div>' % (u['author_b'], fmt(u['author_p'], contact=url('contact', lang), about=url('about', lang)))
    hero_img = '' if is_station else '<figure class="hero-img"><img src="/%s" alt="%s" width="1200" height="630" decoding="async" fetchpriority="high"></figure>' % (m['img'], esc(m['title']))
    mins = '%d %s' % (read, u['minutes'])
    byline = '<div class="byline"><span>%s</span><span>%s: <time datetime="%s">%s</time></span><span>%s: <time datetime="%s">%s</time></span><span>%s: %s</span></div>' % (
        u['byline_by'], u['published'], TODAY, fmt_date(lang), u['updated'], TODAY, fmt_date(lang), u['reading'], mins)
    crumb_html = '<nav class="crumbs" aria-label="%s"><a href="%s">%s</a> › <a href="%s">%s</a> › %s</nav>' % (u['crumbs_label'], url('home', lang), u['home'], url('articles', lang), u['articles'], u[m['pill']])
    aside = '<aside class="art-side" aria-label="%s"><nav class="toc side-toc" aria-label="%s"><b>%s</b>%s</nav><a class="side-cta" href="%s#radios"><b>%s</b><span>%s</span></a></aside>' % (
        u['toc'], u['toc'], u['toc'], toc_html, url('home', lang), u['side_cta_b'], fmt(u['side_cta_s'], n=str(N_ST)))
    main = ('<main id="main">\n\n<div class="progress" id="progress" aria-hidden="true"></div>\n<div class="wrap art-layout">\n<article class="art-main">\n' + crumb_html
            + '<span class="pill">%s</span>\n<h1>%s</h1>\n' % (u[m['pill']], esc(m['title'])) + byline + hero_img
            + '<nav class="toc toc-inline" aria-label="%s"><b>%s</b>%s</nav>\n' % (u['toc'], u['toc'], toc_html)
            + '<div class="prose">' + body + '</div>\n' + share + cta + author + related + '</article>\n' + aside + '\n</div>\n</main>\n')
    page = head(lang, m['mt'], m['desc'], path, image, 'article', alts, ld) + body_open() + header(lang, alts, 'articles') + main + footer(lang) + tail(lang)
    wr(os.path.join(OUT, path.lstrip('/') + '.html'), page)
    return path

# ------------------------------------------------------------------ simple static pages (FR / EN)
def render_static(lang, key):
    u = UI[lang]
    title, desc, body = LEGAL[key][lang]
    body = resolve(body, lang)
    path = url(key, lang)
    alts = alts_for(key)
    body_html = '<div class="prose">' + body + '</div>'
    main = ('<main id="main">\n\n<div class="wrap page">\n<nav class="crumbs" aria-label="%s"><a href="%s">%s</a> › %s</nav>\n<h1>%s</h1>\n%s\n</div>\n</main>\n') % (
        u['crumbs_label'], url('home', lang), u['home'], esc(title), esc(title), body_html)
    mt = title + ' | ' + u['brand_plain']
    ld = [{'@context': 'https://schema.org', '@type': 'WebPage', 'name': title, 'description': desc, 'inLanguage': lang, 'url': abs_url(path), 'isPartOf': {'@id': SITE + '/#website'}}]
    page = head(lang, mt, desc, path, 'og-home.jpg', 'website', alts, ld) + body_open() + header(lang, alts, key if key in ('about', 'contact') else '') + main + footer(lang) + tail(lang, with_player=False)
    wr(os.path.join(OUT, path.lstrip('/') + '.html'), page)

# ------------------------------------------------------------------ hubs
def render_hub(lang):
    u = UI[lang]
    path = url('articles', lang)
    alts = alts_for('articles')
    if lang == 'ar':
        n_total = 12 + len(GUIDES) - 1 + len(STATIONS)
        s = rd(os.path.join(OUT, 'articles.html'))
        s = re.sub(r'<p class="intro">.*?</p>', '<p class="intro">' + fmt(u['hub_intro'], n=str(n_total)) + '</p>', s, count=1, flags=re.S)
        new_guides = [k for k in GUIDES if k != 'listen-online']
        add = ('<section class="sec" aria-labelledby="gn1"><h2 class="sec-title" id="gn1">%s</h2><div class="agrid">%s</div></section>'
               '<section class="sec" aria-labelledby="gn2"><h2 class="sec-title" id="gn2">%s</h2><div class="agrid">%s</div></section>') % (
               u['hub_g_cities'], ''.join(card('ar', k) for k in new_guides), u['hub_g_stations'], ''.join(card('ar', k) for k in STATIONS))
        i = s.rfind('</section>') + len('</section>')
        s = s[:i] + add + s[i:]
        # head patches
        s = s.replace('<link rel="canonical" href="%s">' % abs_url('/articles'), '<link rel="canonical" href="%s">' % abs_url('/articles') + alt_links(alts))
        wr(os.path.join(OUT, 'articles.html'), s)
        return
    n_total = len(GUIDES) + len(STATIONS)
    others = ['best', 'news', 'regional', 'sports', 'car', 'music', 'ramadan', 'amazigh', 'abroad', 'fix', 'history']
    groups = [(u['hub_g_guides'], ['listen-online', 'smart-speaker', 'fm-frequencies']),
              (u['hub_g_cities'], ['french-radio', 'casablanca', 'marrakech-tangier', 'medi1-channels', 'chaabi']),
              (u['hub_g_stations'], list(STATIONS.keys()))]
    secs = ''.join('<section class="sec" aria-labelledby="g%d"><h2 class="sec-title" id="g%d">%s</h2><div class="agrid">%s</div></section>' % (
        i, i, t, ''.join(card(lang, k) for k in ks)) for i, (t, ks) in enumerate(groups))
    secs += '<section class="sec" aria-labelledby="g9"><h2 class="sec-title" id="g9">%s</h2><div class="agrid">%s</div></section>' % (u['hub_g_more'], ''.join(card_ar_only(lang, k) for k in others))
    main = ('<main id="main">\n\n<div class="wrap page-wide">\n<nav class="crumbs" aria-label="%s"><a href="%s">%s</a> › %s</nav>\n<h1>%s</h1>\n<p class="intro">%s</p>\n%s\n</div>\n</main>\n') % (
        u['crumbs_label'], url('home', lang), u['home'], u['articles'], u['hub_h1'], fmt(u['hub_intro'], n=str(n_total)), secs)
    ld = [{'@context': 'https://schema.org', '@type': 'CollectionPage', 'name': u['hub_h1'], 'inLanguage': lang, 'url': abs_url(path), 'isPartOf': {'@id': SITE + '/#website'}}]
    page = head(lang, u['hub_h1'] + ' | ' + u['brand_plain'], fmt(u['hub_intro'], n=str(n_total)), path, 'og-home.jpg', 'website', alts, ld) + body_open() + header(lang, alts, 'articles') + main + footer(lang) + tail(lang)
    wr(os.path.join(OUT, path.lstrip('/') + '.html'), page)

# ------------------------------------------------------------------ home pages
def station_card(lang, sid):
    u = UI[lang]; s = STN[sid]
    nm = esc(s['name'])
    city = CITY.get(s['city'], {}).get(lang, s['city'])
    cat = CAT.get(s['cat'], {}).get(lang, s['cat'])
    langs = ' / '.join(lang_words(lang, sid))
    search = ' '.join([s['name'], s['cat'], cat, s['city'], city, s['lang'], langs]).lower()
    logo = ('<img src="%s" alt="%s" width="62" height="62" loading="lazy" decoding="async" referrerpolicy="no-referrer" onerror="this.remove()">' % (esc(s['logo']), esc(fmt(u['logo_alt'], name=s['name'])))) if s['logo'] else ''
    title = '<a href="%s">%s</a>' % (url(ST_KEY[sid], lang), nm) if sid in ST_KEY else nm
    return ('<article class="station" data-id="%d" data-cat="%s" data-lang="%s" data-search="%s"><div class="tile-top"><div class="logo"><span>%s</span>%s</div>'
            '<button class="fav" type="button" data-fav="%d" aria-pressed="false" aria-label="%s"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" aria-hidden="true"><path d="M19 21l-7-5-7 5V5a2 2 0 012-2h10a2 2 0 012 2z"/></svg></button></div>'
            '<h3>%s</h3><p class="meta">%s • %s</p><div class="tile-foot"><button class="play" type="button" data-play="%d" aria-label="%s"><span class="disc"><svg width="13" height="13" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M8 5v14l11-7z"/></svg></span><span class="play-label">%s</span></button><span class="tag">%s</span></div></article>') % (
            sid, esc(s['cat']), esc(s['lang']), esc(search), esc(s['init']), logo, sid, esc(fmt(u['fav_save'], name=s['name'])), title, esc(city), esc(langs), sid, esc(fmt(u['listen_to'], name=s['name'])), u['listen'], esc(cat))

def render_home(lang):
    u = UI[lang]; path = url('home', lang); alts = alts_for('home')
    best_t = {'ar': 'best'}.get(lang, 'best')
    dir_intro = fmt(u['dir_intro'], n=str(N_ST), best=url('best', lang))
    if lang == 'fr': dir_intro = dir_intro.replace('2026</a>.', '2026</a> (guide en arabe).')
    if lang == 'en': dir_intro = dir_intro.replace('2026</a>.', '2026</a> (guide in Arabic).')
    chips = [('all', u['all'])] + [('cat:' + k, CAT[k][lang]) for k in ['موسيقى', 'أخبار', 'وطنية', 'جهوية', 'دينية', 'رياضة', 'مجتمع']] + [('lang:فرنسية', u['f_fr']), ('lang:أمازيغية', u['f_am']), ('fav', u['fav_chip'])]
    chip_html = ''.join('<button class="chip" type="button" data-filter="%s" aria-pressed="%s">%s</button>' % (f, 'true' if f == 'all' else 'false', l) for f, l in chips)
    grid = ''.join(station_card(lang, sid) for sid in STN)
    tl = u['topic_labels']
    if lang == 'ar':
        tmap = [('news', url('news', 'ar')), ('sports', url('sports', 'ar')), ('music', url('music', 'ar')), ('ramadan', url('ramadan', 'ar')),
                ('amazigh', url('amazigh', 'ar')), ('abroad', url('abroad', 'ar')), ('car', url('car', 'ar')), ('fix', url('fix', 'ar'))]
    else:
        tmap = [('news', url('medi-1-radio', lang)), ('sports', url('radio-mars', lang)), ('music', url('medi1-channels', lang)), ('ramadan', url('radio-quran', lang) if 'radio-quran' in STATIONS else url('quran', lang)),
                ('amazigh', url('amazigh', lang)), ('abroad', url('listen-online', lang)), ('car', url('smart-speaker', lang)), ('fix', url('fix', lang))]
    topics = ''.join('<a class="topic" href="%s"%s><span>%s</span></a>' % (h, ' hreflang="ar"' if h.startswith('/') and not h.startswith('/fr/') and not h.startswith('/en/') and lang != 'ar' else '', tl[k]) for k, h in tmap)
    st_pages = ''.join('<a class="topic" href="%s"><span>%s</span></a>' % (url(k, lang), esc(sname(lang, v['id']))) for k, v in STATIONS.items())
    recent = ['fm-frequencies', 'medi1-channels', 'listen-online', 'smart-speaker', 'casablanca', 'french-radio']
    cards_html = ''.join(card(lang, k) for k in recent)
    n_total = (12 + len(GUIDES) - 1 + len(STATIONS)) if lang == 'ar' else (len(GUIDES) + len(STATIONS))
    faq_html = ''.join('<details class="faq"><summary>%s</summary><p>%s</p></details>' % (q, a) for q, a in u['faq'])
    faq_ld_ = {'@context': 'https://schema.org', '@type': 'FAQPage', 'mainEntity': [{'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in u['faq']]}
    title = {'ar': 'راديو المغرب | استمع إلى الإذاعات المغربية مباشرة', 'fr': 'Radio Maroc | Écoutez les radios marocaines en direct', 'en': 'Radio Maroc | Listen to Moroccan Radio Stations Live'}[lang]
    desc = {'ar': 'دليل الإذاعات المغربية: استمع مباشرة إلى ميدي 1 وهيت راديو وراديو مارس وشذى FM وأكثر من 40 محطة، مع أدلة ومقالات تساعدك على الاختيار.',
            'fr': 'Guide des radios marocaines : écoutez en direct Medi 1, Hit Radio, Radio Mars, Chada FM et plus de 40 stations, avec des guides pour bien choisir.',
            'en': 'Guide to Moroccan radio: listen live to Medi 1, Hit Radio, Radio Mars, Chada FM and more than 40 stations, with guides to help you choose.'}[lang]
    org = {'@type': 'Organization', '@id': SITE + '/#org', 'name': 'Radio Maroc', 'url': SITE + '/', 'logo': {'@type': 'ImageObject', 'url': SITE + '/app-icon.png', 'width': 512, 'height': 512}}
    site = {'@type': 'WebSite', '@id': SITE + '/#website', 'url': SITE + '/', 'name': u['brand_plain'], 'description': desc, 'inLanguage': ['ar', 'fr', 'en'], 'publisher': {'@id': SITE + '/#org'}}
    il = {'@type': 'ItemList', 'name': u['guides_title'], 'itemListElement': [{'@type': 'ListItem', 'position': i + 1, 'url': abs_url(url(k, lang)), 'name': META[lang][k]['title']} for i, k in enumerate(recent)]}
    ld = [{'@context': 'https://schema.org', '@graph': [site, org, il]}, faq_ld_]
    promo = ('<div class="promo" id="promo" role="complementary"><span class="app-icon p-ico" style="width:40px;height:40px"><img src="/app-icon.png" alt="%s" width="40" height="40" decoding="async"></span>'
             '<div class="p-txt"><b>%s</b><small>%s</small></div><a class="p-btn" href="%s" target="_blank" rel="noopener">%s</a><button class="p-close" id="promoClose" type="button" aria-label="X">✕</button></div>\n') % (
             esc(u['app_alt']), u['promo_b'], u['promo_s'], PLAY_URL, u['promo_btn'])
    hero = ('<section class="wrap hero" aria-labelledby="h1">\n<div class="hero-copy"><span class="kicker"><span class="dot"></span> %s</span>\n<h1 id="h1">%s</h1>\n<p>%s</p>\n'
            '<div class="hero-actions"><button class="btn btn-ivory" id="heroPlay" type="button">%s</button><a class="btn btn-ghost" href="#radios">%s</a></div></div>\n'
            '<div class="hero-art"><img src="/art-stations.svg" alt="%s" width="1200" height="630" fetchpriority="high" decoding="async"></div>\n</section>\n') % (
            u['h_kicker'], u['h_h1'], u['h_p'], u['listen_now'], u['h_browse'], esc(u['hero_alt']))
    stats = '<div class="wrap"><ul class="stats" aria-label="%s">\n<li><b>%d</b><span>%s</span></li><li><b>%d</b><span>%s</span></li><li><b>0</b><span>%s</span></li><li><b>100%%</b><span>%s</span></li></ul></div>\n' % (
        u['stats_aria'], N_ST, u['s1'], n_total, u['s2'], u['s3'], u['s4'])
    dirsec = ('<section id="radios" class="wrap sec" aria-labelledby="dir-h">\n<div class="head"><div><div class="eyebrow">STATION DIRECTORY</div><h2 class="sec-title" id="dir-h">%s <span class="count" id="countTxt">%d</span></h2></div>\n'
              '<label class="search"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#6b6966" stroke-width="2" aria-hidden="true"><circle cx="11" cy="11" r="8"/><path d="M21 21l-4.35-4.35"/></svg><input id="mainSearch" type="search" placeholder="%s" aria-label="%s"></label></div>\n'
              '<p class="intro">%s</p>\n<div class="filters" role="group" aria-label="%s">%s</div>\n<div class="grid" id="stationGrid">%s</div>\n<div class="empty" id="emptyBox" hidden>%s</div>\n</section>\n') % (
              u['dir_title'], N_ST, esc(u['search_ph']), esc(u['search_aria']), dir_intro, esc(u['filters_aria']), chip_html, grid, fmt(u['empty'], contact=url('contact', lang)))
    topics_sec = '<section class="wrap sec" aria-labelledby="topics-h">\n<div class="head"><div><div class="eyebrow">EXPLORE BY NEED</div><h2 class="sec-title" id="topics-h">%s</h2></div></div>\n<div class="topics">%s</div>\n</section>\n' % (u['topics_title'], topics)
    pages_sec = '<section class="wrap sec" aria-labelledby="pg-h">\n<div class="head"><div><div class="eyebrow">STATION PAGES</div><h2 class="sec-title" id="pg-h">%s</h2></div></div>\n<p class="intro">%s</p>\n<div class="topics">%s</div>\n</section>\n' % (u['pages_title'], u['pages_intro'], st_pages)
    art_sec = ('<section class="wrap sec" aria-labelledby="art-h">\n<div class="head"><div><div class="eyebrow">LISTENING GUIDES</div><h2 class="sec-title" id="art-h">%s</h2></div><a href="%s" style="font-weight:700">%s</a></div>\n<p class="intro">%s</p>\n<div class="agrid">%s</div>\n</section>\n') % (
        u['guides_title'], url('articles', lang), fmt(u['all_articles'], n=str(n_total)), u['guides_intro'], cards_html)
    appcard = ('<div class="wrap"><div class="app-card"><span class="app-icon" style="width:64px;height:64px"><img src="/app-icon.png" alt="%s" width="64" height="64" decoding="async" loading="lazy"></span><div><b>%s</b><small>%s</small></div>'
               '<a class="btn" href="%s" target="_blank" rel="noopener">%s</a></div></div>\n') % (esc(u['app_alt']), u['app_b'], u['app_s'], PLAY_URL, u['app_btn'])
    about_sec = '<section class="wrap box" aria-labelledby="about-h">\n<h2 id="about-h">%s</h2>\n<p>%s</p>\n<h3>%s</h3>\n%s\n</section>\n' % (u['about_h'], fmt(u['about_p'], about=url('about', lang)), u['faq_h'], faq_html)
    main = '<main id="main">\n\n' + hero + stats + dirsec + '\n' + BANNER + '\n\n' + topics_sec + pages_sec + art_sec + '\n' + appcard + '\n' + about_sec + '\n' + SWREG + '\n</main>\n'
    page = head(lang, title, desc, path, 'og-home.jpg', 'website', alts, ld, home=True) + body_open(True) + header(lang, alts, 'home') + promo + main + footer(lang) + tail(lang, home=True)
    wr(os.path.join(OUT, 'index.html' if lang == 'ar' else path.lstrip('/') + 'index.html'), page)

# ------------------------------------------------------------------ run: generated pages
for lang in LANGS:
    for key in list(GUIDES) + list(STATIONS):
        render_page(lang, key)
for lang in ('fr', 'en'):
    for key in ('about', 'contact', 'privacy', 'terms', 'disclaimer', 'cookies'):
        render_static(lang, key)
for lang in LANGS:
    render_hub(lang)
    render_home(lang)

# ------------------------------------------------------------------ patch existing Arabic pages
SKIP = {'index.html', 'articles.html', '404.html'} | {v['slug']['ar'] + '.html' for v in GUIDES.values()} | {v['slug']['ar'] + '.html' for v in STATIONS.values()}
st_row = '<div class="foot-links" style="margin-top:14px"><b>%s:</b>%s</div>\n' % (UI['ar']['foot_stations'], ''.join('<a href="%s">%s</a>' % (url(k, 'ar'), esc(sname('ar', v['id']))) for k, v in STATIONS.items()))
for fn in sorted(os.listdir(OUT)):
    if not fn.endswith('.html') or fn in SKIP: continue
    p = os.path.join(OUT, fn); s = rd(p); slug = fn[:-5]
    key = next((k for k, v in STATIC.items() if v['ar'] == slug), None)
    alts = alts_for(key) if key else None
    s = s.replace('/style.css"', '/style.css%s"' % CSSV).replace('/app.js"', '/app.js%s"' % CSSV)
    if alts:
        canon = '<link rel="canonical" href="%s">' % abs_url('/' + slug)
        s = s.replace(canon, canon + alt_links(alts), 1)
    s = s.replace('<button class="menu-btn"', lang_switcher('ar', alts or {}) + '<button class="menu-btn"', 1)
    if '<div class="copy">' in s and st_row not in s:
        s = s.replace('<div class="copy">', st_row + '<div class="copy">', 1)
    s = s.replace('contact@radiomaroc.example', EMAIL)
    wr(p, s)
# 404 page: cache-busting + language switcher
p = os.path.join(OUT, '404.html'); s = rd(p)
s = s.replace('/style.css"', '/style.css%s"' % CSSV).replace('/app.js"', '/app.js%s"' % CSSV)
s = s.replace('<button class="menu-btn"', lang_switcher('ar', {}) + '<button class="menu-btn"', 1)
wr(p, s)
# patch hub head (cache bust)
p = os.path.join(OUT, 'articles.html'); s = rd(p)
s = s.replace('/style.css"', '/style.css%s"' % CSSV).replace('/app.js"', '/app.js%s"' % CSSV)
s = s.replace('<button class="menu-btn"', lang_switcher('ar', alts_for('articles')) + '<button class="menu-btn"', 1)
if st_row not in s: s = s.replace('<div class="copy">', st_row + '<div class="copy">', 1)
wr(p, s)

# ------------------------------------------------------------------ app.js (i18n + player on any page)
js = rd(os.path.join(SRC, 'app.js'))
js = js.replace("'use strict';", "'use strict';\n  var I = window.RM_I18N || {loading:'جاري التحميل…',live:'مباشر',paused:'متوقف مؤقتاً',unavail:'البث غير متوفر حالياً',fail:'تعذّر تشغيل هذا البث. جرّب محطة أخرى أو أعد المحاولة لاحقاً.',playing:'قيد التشغيل',listen:'استمع',fav_add:'أضيفت إلى المفضلة',fav_del:'أزيلت من المفضلة',copied:'تم نسخ الرابط',brand:'راديو المغرب'};", 1)
reps = [("toast('تم نسخ الرابط')", "toast(I.copied)"), ("toast(i === -1 ? 'أضيفت إلى المفضلة' : 'أزيلت من المفضلة')", "toast(i === -1 ? I.fav_add : I.fav_del)"),
        ("on ? 'قيد التشغيل' : 'استمع'", "on ? I.playing : I.listen"), ("pStatus.textContent = 'البث غير متوفر حالياً'", "pStatus.textContent = I.unavail"),
        ("toast('تعذّر تشغيل هذا البث. جرّب محطة أخرى أو أعد المحاولة لاحقاً.')", "toast(I.fail)"), ("pStatus.textContent = 'جاري التحميل…'", "pStatus.textContent = I.loading"),
        ("pStatus.textContent = 'مباشر'", "pStatus.textContent = I.live"), ("pStatus.textContent = 'متوقف مؤقتاً'", "pStatus.textContent = I.paused"),
        ("artist: 'راديو المغرب'", "artist: (I.brand || 'راديو المغرب')"),
        ("var grid = $('#stationGrid');\n  if (!grid) return;", "var grid = $('#stationGrid');\n  if (!grid && !$('#playerBar')) return;"),
        ("var cards = $$('.station', grid);", "var cards = grid ? $$('.station', grid) : [];"),
        ("grid.addEventListener('click'", "(grid || document).addEventListener('click'"), ("\n  applyFilter();\n})();", "\n  if (grid) applyFilter();\n})();")]
for a, b in reps:
    if a not in js: print('WARN app.js pattern missing:', a[:60])
    js = js.replace(a, b)
wr(os.path.join(OUT, 'app.js'), js)

# ------------------------------------------------------------------ CSS additions
css = rd(os.path.join(SRC, 'style.css'))
if '/* ===== i18n + station pages' not in css:
    css += '''
/* ===== i18n + station pages (2026-11-20) ===== */
.langsw{display:inline-flex;border:1px solid var(--line);border-radius:10px;overflow:hidden;background:#fff}
.langsw a{padding:6px 10px;font:700 12px var(--mono);color:#4d4a47;text-decoration:none;letter-spacing:.04em}
.langsw a:hover{background:#f6efe9;color:var(--red)}
.langsw a[aria-current="true"]{background:var(--red);color:#fff}
html[dir=ltr] .eyebrow{justify-content:flex-start}
html[dir=ltr] body{font-family:'IBM Plex Sans Arabic','Segoe UI',system-ui,Arial,sans-serif}
.station h3 a{color:inherit;text-decoration:none}.station h3 a:hover{color:var(--red)}
.stn-hero{display:flex;gap:18px;align-items:center;flex-wrap:wrap;background:var(--card);border:1px solid var(--line);border-radius:18px;padding:18px;margin:0 0 20px}
.stn-logo{width:78px;height:78px;border-radius:18px;background:#481d26;color:#fff;display:grid;place-items:center;font-weight:800;overflow:hidden;flex-shrink:0;position:relative}
.stn-logo img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;background:#fff}
.stn-facts{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:8px 20px;margin:0;flex:1;min-width:220px}
.stn-facts dt{font-size:12px;color:var(--dim)}.stn-facts dd{margin:0;font-weight:700}
.stn-list{list-style:none;margin:0 0 1rem;padding:0;display:grid;gap:8px}
.stn-list li{display:flex;align-items:center;justify-content:space-between;gap:10px;background:var(--card);border:1px solid var(--line);border-radius:12px;padding:10px 14px}
.stn-list .sl-main{display:flex;flex-direction:column;min-width:0}.stn-list .sl-main b{line-height:1.5}
.stn-list .sl-main a{color:var(--ink);text-decoration:none}.stn-list .sl-main a:hover{color:var(--red)}
.sl-meta{font-size:13px;color:var(--dim)}
.btn-sm{min-height:36px;padding:4px 14px;font-size:13px;flex-shrink:0}
.freq{width:100%;border-collapse:collapse;margin:0 0 1rem;font-size:15px}
.freq th,.freq td{border:1px solid var(--line);padding:8px 10px;text-align:start}.freq th{background:#f4f2eb}
.note-box{background:#f4f2eb;border:1px solid var(--line);border-radius:12px;padding:14px 16px;font-size:15.5px;line-height:1.9;margin:0 0 1rem}
@media(max-width:860px){.langsw{order:2}}
@media(max-width:560px){.langsw a{padding:5px 7px;font-size:11px}.top-inner{gap:8px}.tools{gap:6px}.clock{display:none}}
'''
    wr(os.path.join(OUT, 'style.css'), css)

# ------------------------------------------------------------------ manifest, data, sitemap, feed
man = json.loads(rd(os.path.join(SRC, 'manifest.webmanifest')))
man.update({'id': '/', 'start_url': '/', 'scope': '/'})
for ic in man.get('icons', []): ic['src'] = ic['src'].replace('/Raddddddd/', '/')
wr(os.path.join(OUT, 'manifest.webmanifest'), json.dumps(man, ensure_ascii=False, indent=1))

os.makedirs(os.path.join(OUT, 'data'), exist_ok=True)
if os.path.exists(FREQ_PATH):
    shutil.copy(FREQ_PATH, os.path.join(OUT, 'data', 'frequencies.json'))
if not os.path.exists(os.path.join(OUT, 'data', 'frequencies.json')):
    wr(os.path.join(OUT, 'data', 'frequencies.json'), json.dumps({
        '_help': 'Add verified FM frequencies here, then run: python3 tools/build.py . ./out . Each entry: station = directory id, city = Arabic city name as in the directory, mhz = number as text, verified = YYYY-MM-DD, source = URL of the official source (not shown on the page). Leave entries empty until a number is verified.',
        'last_verified': '', 'entries': []}, ensure_ascii=False, indent=1))

def sm_entry(path, lastmod, prio, alts=None):
    x = '<url><loc>%s</loc><lastmod>%s</lastmod><priority>%s</priority>' % (abs_url(path), lastmod, prio)
    if alts:
        for l, p in alts.items(): x += '<xhtml:link rel="alternate" hreflang="%s" href="%s"/>' % (l, abs_url(p))
        x += '<xhtml:link rel="alternate" hreflang="x-default" href="%s"/>' % abs_url(alts['ar'])
    return x + '</url>\n'
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
for l in LANGS: sm += sm_entry(url('home', l), TODAY, '1.0', alts_for('home'))
for l in LANGS: sm += sm_entry(url('articles', l), TODAY, '0.9', alts_for('articles'))
for key in list(GUIDES) + list(STATIONS):
    for l in LANGS: sm += sm_entry(url(key, l), TODAY, '0.8', alts_for(key))
for slug in AR_ONLY_KEYS.values(): sm += sm_entry('/' + slug, '2026-11-18', '0.8')
for key in ('about', 'contact'):
    for l in LANGS: sm += sm_entry(url(key, l), TODAY, '0.5', alts_for(key))
for key in ('privacy', 'terms', 'disclaimer', 'cookies'):
    for l in LANGS: sm += sm_entry(url(key, l), TODAY, '0.3', alts_for(key))
sm += '</urlset>\n'
wr(os.path.join(OUT, 'sitemap.xml'), sm)

feed = rd(os.path.join(SRC, 'feed.xml'))
items = ''
for key in list(GUIDES) + list(STATIONS):
    if key == 'listen-online': continue
    m = META['ar'][key]
    items += '<item><title>%s</title><link>%s</link><guid>%s</guid><pubDate>Fri, 20 Nov 2026 08:00:00 +0100</pubDate><description>%s</description></item>' % (
        html.escape(m['title']), abs_url(url(key, 'ar')), abs_url(url(key, 'ar')), html.escape(m['desc']))
m = META['ar']['listen-online']
feed = re.sub(r'(<item><title>)[^<]*(</title><link>%s</link>)' % re.escape(abs_url('/listen-radio-online-morocco')), r'\g<1>%s\g<2>' % html.escape(m['title']).replace('\\', ''), feed)
feed = feed.replace('<language>ar</language>', '<language>ar</language>' + items, 1) if False else feed.replace('</channel>', items + '</channel>')
wr(os.path.join(OUT, 'feed.xml'), feed)

print('OK. pages written under', OUT)
