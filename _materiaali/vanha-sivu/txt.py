import sys,re,html
from html.parser import HTMLParser
class P(HTMLParser):
    def __init__(s): super().__init__(); s.out=[]; s.skip=0
    def handle_starttag(s,t,a):
        if t in('script','style','noscript'): s.skip+=1
        if t in('p','div','h1','h2','h3','h4','li','br'): s.out.append('\n')
        if t=='img':
            d=dict(a); s.out.append(f"\n[IMG {d.get('alt','')} {d.get('src') or d.get('data-src','')}]\n")
    def handle_endtag(s,t):
        if t in('script','style','noscript'): s.skip-=1
    def handle_data(s,d):
        if not s.skip: s.out.append(d)
for f in sys.argv[1:]:
    p=P(); p.feed(open(f,encoding='utf-8').read())
    t=re.sub(r'\n\s*\n+','\n',''.join(p.out))
    print('=====',f); print(t)
