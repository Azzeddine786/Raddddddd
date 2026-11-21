import os,re,sys,json,html,collections
OUT=sys.argv[1]
pages={}
for r,d,fs in os.walk(OUT):
    for f in fs:
        if f.endswith('.html'):
            p=os.path.join(r,f); rel='/'+os.path.relpath(p,OUT).replace('\\','/')
            pages[rel]=open(p,encoding='utf8').read()
def target(href):
    href=href.split('#')[0].split('?')[0]
    if not href: return True
    if href.startswith(('http','mailto:','tel:','javascript:','data:')): return True
    if not href.startswith('/'): return True
    if href.endswith('/'): return os.path.exists(OUT+href+'index.html')
    return os.path.exists(OUT+href) or os.path.exists(OUT+href+'.html')
bad=collections.defaultdict(set)
titles=collections.defaultdict(list); descs=collections.defaultdict(list)
for rel,s in pages.items():
    for h in re.findall(r'(?:href|src)="([^"]*)"',s):
        if not target(h): bad[rel].add(h)
    t=re.search(r'<title>(.*?)</title>',s,re.S); d=re.search(r'<meta name="description" content="(.*?)">',s,re.S)
    if t: titles[html.unescape(t.group(1))].append(rel)
    if d: descs[html.unescape(d.group(1))].append(rel)
    for m in re.findall(r'<script type="application/ld\+json">(.*?)</script>',s,re.S):
        try: json.loads(m)
        except Exception as e: print('BAD JSON-LD',rel,e)
    ids=re.findall(r'\sid="([^"]+)"',s)
    dup=[i for i,c in collections.Counter(ids).items() if c>1]
    if dup: print('DUP IDS',rel,dup)
    if s.count('<main')!=1 and rel!='/404.html': print('main count',rel,s.count('<main'))
print('pages',len(pages))
print('BROKEN LINKS:',{k:sorted(v) for k,v in bad.items()})
print('dup titles:',[(t,v) for t,v in titles.items() if len(v)>1])
print('dup descs:',[(t[:50],v) for t,v in descs.items() if len(v)>1])
# hreflang reciprocity
for rel,s in pages.items():
    alts=re.findall(r'<link rel="alternate" hreflang="([a-z\-]+)" href="https://radiomaroc.live([^"]*)">',s)
    for l,h in alts:
        if l=='x-default': continue
        tp=h if h.endswith('/') is False else h+'index.html'
        tp=(h+'index.html') if h.endswith('/') else (h+'.html')
        if tp not in pages: print('hreflang target missing',rel,l,h)
        else:
            back=re.findall(r'hreflang="([a-z\-]+)" href="https://radiomaroc.live([^"]*)"',pages[tp])
            me=rel[:-5] if not rel.endswith('index.html') else rel[:-10]
            me=me or '/'
            if not any(x==me or x==me+'/' for _,x in back): print('no backlink',rel,'<-',tp)
# length checks
for rel,s in pages.items():
    t=html.unescape(re.search(r'<title>(.*?)</title>',s,re.S).group(1))
    d=re.search(r'<meta name="description" content="(.*?)">',s,re.S)
    d=html.unescape(d.group(1)) if d else ''
    if len(t)>70 or len(d)>175: print('LEN',rel,len(t),len(d))
