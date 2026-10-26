# Plain-Python static generator. Edit DATA, run `python3 build.py`.
import html, os
U="unknown"
DATA=[
 dict(slug="lenovo-x9-15p",name="Lenovo X9-15p",distro="Omarchy",overall="Works (minor fix)",
  wifi=U,suspend=U,camera="Needed fix",audio=U,display=U,battery=U,
  summary="One owner reports Omarchy works out of the box except the camera, which they fixed quickly.",
  reports=[("Antonio Cangiano on X, 2026-10-16","https://x.com/acangiano/status/2111320896468406312",
   "\u201cThe Lenovo X9-15p is likely the nicest laptop I've ever had. Omarchy works out of the box, except for the camera, which the agent fixed in two minutes.\u201d")]),
 dict(slug="framework-13-amd",name="Framework Laptop 13 (AMD)",distro="Omarchy",overall="Works",
  wifi=U,suspend=U,camera=U,audio=U,display=U,battery="Owner reports ~6h (Ryzen 5 7640U, older battery)",
  summary="Two owners report it works well. One says only personal-preference configuration was needed; another, on a Ryzen 5 7640U model with an older battery, reports about six hours of battery life on Omarchy.",
  reports=[("r/omarchy comment, 2026-02-06","https://www.reddit.com/r/omarchy/comments/1qxj4fo/linux_laptop_omarchy_suggestions/",
   "\u201cI have a framework 13 amd and it works great, only configuration I needed was personal preference. everything else worked out of the box.\u201d"),
   ("Cynthia Toporowski (@ItsCynnamoroll) on X, 2026-10-24","https://x.com/ItsCynnamoroll/status/2113832857722642495",
   "\u201cI don't know what I was expecting when I installed @omarchy earlier today\u2026 Nope. No BS. Framework 13 7640u old battery, 6h battery life\u201d (excerpt)")]),
 dict(slug="dell-xps-14-panther-lake",name="Dell XPS 14 (Panther Lake)",distro="Omarchy 3.6",overall="Works",
  wifi=U,suspend=U,camera=U,audio=U,display="Works (incl. Studio Display, per post title)",battery="Owner says good",
  summary="An owner installed Omarchy 3.6 and reports it working well, including good battery and performance.",
  reports=[("r/omarchy post","https://www.reddit.com/r/omarchy/comments/1sy0svs/dell_xps_14_panther_lake_studio_display_omarchy_36/",
   "Post titled \u201cDell XPS 14 Panther Lake + Studio Display + Omarchy 3.6\u201d: \u201cimmediately installed Omarchy 3.6 out of the box\u2026 a powerhouse in terms of battery and performance\u2026 seems to be working perfectly for what I\u2019ve thrown at [it]\u201d (excerpt as returned by search; partially truncated).")]),
 dict(slug="lenovo-thinkpad-t450",name="Lenovo ThinkPad T450",distro="Omarchy",overall="Works",
  wifi=U,suspend=U,camera=U,audio=U,display=U,battery=U,
  summary="One tester reports everything works out of the box.",
  reports=[("r/omarchy comment by u/porfiriopaiz, 2025-10-14","https://www.reddit.com/r/omarchy/comments/1o66zj1/hardware_suggestions_for_omarchy/",
   "\u201cJust tested it on Lenovo ThinkPad T450, everything works out of the box.\u201d")]),
 dict(slug="surface-laptop-7-snapdragon",name="Microsoft Surface Laptop 7 13.8\" (Snapdragon X Plus)",distro="Omarchy aarch64 (Dragon, in development)",overall="Experimental",
  wifi=U,suspend=U,camera="Face unlock (IR) works",audio=U,display=U,battery=U,
  summary="A developer is bringing up an Omarchy ARM build; face unlock via the IR camera is reported working. Everything else is unreported.",
  reports=[("Chris McLaughlin on X, 2026-10-09","https://x.com/qBitnaut/status/2108350982627233807",
   "\u201cI've been working on getting an Omarchy aarch64 Dragon build up on the Surface Laptop 7 (13.8\", Snapdragon X Plus X1P-64-100). What works - Face unlock (lock screen + sudo) with the built-in IR camera and emitter\u2026\u201d"),
   ("Omarchy Dragon announcement (context), DHH on X","https://x.com/dhh/status/2100833589042491769",
   "\u201cOmarchy Dragon is our new official team for working on making Omarchy run beautifully on @Qualcomm Snapdragon computers\u201d")]),
 dict(slug="macbook-pro-2015",name="Apple MacBook Pro (2015, Intel)",distro="Omarchy",overall="Works",
  wifi=U,suspend=U,camera=U,audio=U,display=U,battery=U,
  summary="Two owners on X say Omarchy runs well on a 2015 Intel MacBook Pro. Neither says which components they checked, so every item below is still unknown. One report is the 13-inch model; the other doesn't say the screen size.",
  reports=[("Marian Gabriel (@vladmariang) on X, 2026-10-08","https://x.com/vladmariang/status/2108285563728240957",
   "\u201cAlso on Macbook Pro 13\" 2015 works like I bought the laptop yesterday.....\u201d (reply to DHH; same post also says Omarchy installed straight away on an HP Omen, model not specified)"),
   ("Bj\u00f6rn (@teddybear_lost) on X, 2026-10-07","https://x.com/teddybear_lost/status/2107891169464074290",
   "\u201cI installed omarchy on my MacBook Pro from 2015 and it works great \U0001f642\U0001f44d\u201d (screen size not stated)")]),
 dict(slug="asus-rog-strix-g15-g512lv",name="ASUS ROG Strix G15 (G512LV)",distro="Omarchy",overall="Works (minor fix)",
  wifi=U,suspend=U,camera=U,audio=U,display=U,battery=U,
  summary="One owner installed Omarchy on this older ASUS gaming laptop in about seven minutes and says everything worked smoothly. The only issue they mention was loud fans, which they quieted by switching the power profile to quiet. They don't say which components they checked, so each item below is still unknown, including how the discrete NVIDIA GPU behaves.",
  reports=[("Aurelien Navarre (@anavarre) on X, 2026-10-16","https://x.com/anavarre/status/2111194211601272999",
   "\u201cInstalled Omarchy on an old ASUS ROG Strix G15 (G512LV) gaming laptop tonight. Took 7 minutes. Fan got a little crazy, which I fixed with: powerprofilesctl set quiet. Apart from that everything worked smoothly \U0001f44c\u201d")]),
 dict(slug="lenovo-thinkpad-t14s-gen-3",name="Lenovo ThinkPad T14s Gen 3",distro="Omarchy",overall="Works",
  wifi=U,suspend=U,camera=U,audio=U,display=U,battery=U,
  summary="One owner on X says Omarchy runs very fast on a ThinkPad T14s Gen 3, and notes the laptop can be bought used for a couple of hundred pounds. They don't say whether theirs is the Intel or AMD version, or which components they checked, so every item below is still unknown.",
  reports=[("Frank Cheung (@fcuk112) on X, 2026-10-20","https://x.com/fcuk112/status/2112690323398791443",
   "\u201c@omarchy is a joy to play around with - i got it running on a thinkpad T14s gen 3 (which can be had for a couple of hundred \u00a3) and it absolutely flies!\u201d (excerpt; post continues)")]),
 dict(slug="lenovo-thinkpad-t14-gen-2-intel",name="Lenovo ThinkPad T14 Gen 2 (Intel)",distro="Omarchy",overall="Works",
  wifi=U,suspend=U,camera=U,audio=U,display=U,battery=U,
  summary="One owner on X says Omarchy made their Intel ThinkPad T14 Gen 2 a \u201cdream laptop\u201d and calls these machines great little workhorses. Their only complaint is that the screen is hard to see in bright outdoor light, which is about the panel itself rather than Linux support. They don't say which components they checked, so every item below is still unknown.",
  reports=[("Nick (@maietta) on X, 2026-10-24","https://x.com/maietta/status/2114089169165455740",
   "\u201cI'm running a Second Gen Intel version of the T14. Omarchy made this a dream laptop. The only thing I wish now is ability to see the screen when it's bright out. Other than that these are great little workhorses.\u201d")]),
]
COLS=[("wifi","Wi-Fi"),("suspend","Suspend"),("camera","Camera"),("audio","Audio"),("display","Display"),("battery","Battery")]
CSS="""*{box-sizing:border-box}body{font:16px/1.5 system-ui,sans-serif;margin:0;color:#1a1a1a;background:#fafafa}
header,main,footer{max-width:960px;margin:auto;padding:1rem}header{display:flex;gap:1rem;align-items:baseline;flex-wrap:wrap}
header a{color:#333}h1 a{text-decoration:none;color:inherit}table{width:100%;border-collapse:collapse;background:#fff;font-size:.92rem}
th,td{border:1px solid #ddd;padding:.45rem;text-align:left;vertical-align:top}th{background:#f0f0f0}
.u{color:#888;font-style:italic}.ok{color:#11702f;font-weight:600}.warn{color:#9a5b00;font-weight:600}
blockquote{border-left:4px solid #ccc;margin:.5rem 0;padding:.25rem .75rem;background:#fff}
.filters{display:flex;gap:.75rem;flex-wrap:wrap;margin:.75rem 0}input,select{padding:.35rem;font:inherit}
footer{font-size:.85rem;color:#666}@media(prefers-color-scheme:dark){body{background:#121212;color:#e6e6e6}table,blockquote{background:#1d1d1d}th{background:#262626}th,td{border-color:#333}header a{color:#ccc}}"""
def cls(v): return "u" if v==U else ("ok" if v.startswith("Works") else "warn")
def cell(v): return f'<span class="{cls(v)}">{html.escape(v)}</span>'
def page(title,body,depth=0):
    p="../"*depth
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)} · Linux laptops, verified by owners</title><meta name="description" content="Owner-reported Linux and Omarchy laptop compatibility, with sources."><link rel="stylesheet" href="{p}style.css"></head><body>
<header><h1><a href="{p}index.html">Linux laptops, verified by owners</a></h1><nav><a href="{p}index.html">Table</a> · <a href="{p}about.html">About &amp; method</a> · <a href="{p}submit.html">Submit a report</a></nav></header>
<main>{body}</main><footer>Every claim links to a public owner report. “unknown” means no report found yet, not “broken”.</footer><script defer src='https://static.cloudflareinsights.com/beacon.min.js' data-cf-beacon='{{"token": "a672c8bbb0704c30b4d89dbf8ba579fe"}}'></script></body></html>"""
os.makedirs("laptops",exist_ok=True)
open("style.css","w").write(CSS)
rows=""
for d in DATA:
    rows+=f'<tr data-distro="{html.escape(d["distro"].lower())}" data-text="{html.escape((d["name"]+" "+d["overall"]).lower())}"><td><a href="laptops/{d["slug"]}.html">{html.escape(d["name"])}</a></td><td>{html.escape(d["distro"])}</td><td>{cell(d["overall"])}</td>'+"".join(f"<td>{cell(d[k])}</td>" for k,_ in COLS)+f'<td>{len(d["reports"])}</td></tr>\n'
home=f"""<p>Owner reports of how specific laptops run <strong>Omarchy</strong> and other Linux setups. Each row links to its sources. Small and early: {len(DATA)} models so far.</p>
<div class="filters"><label>Search <input id="q" placeholder="e.g. lenovo"></label>
<label>Setup <select id="d"><option value="">All</option><option value="omarchy" selected>Omarchy (any)</option></select></label>
<label>Status <select id="s"><option value="">All</option><option value="works">Works</option><option value="experimental">Experimental</option></select></label></div>
<div style="overflow-x:auto"><table id="t"><thead><tr><th>Model</th><th>Setup</th><th>Overall</th>{"".join(f"<th>{n}</th>" for _,n in COLS)}<th>Reports</th></tr></thead><tbody>
{rows}</tbody></table></div><p id="n"></p>
<script>const q=document.getElementById('q'),d=document.getElementById('d'),s=document.getElementById('s');
function f(){{let c=0;for(const r of document.querySelectorAll('#t tbody tr')){{const ok=r.dataset.text.includes(q.value.toLowerCase())&&r.dataset.distro.includes(d.value)&&r.dataset.text.includes(s.value);r.hidden=!ok;c+=ok}}document.getElementById('n').textContent=c+' model(s) shown';}}
[q,d,s].forEach(e=>e.addEventListener('input',f));f();</script>"""
open("index.html","w").write(page("Compatibility table",home))
for d in DATA:
    rep="".join(f'<h3><a href="{u}">{html.escape(t)}</a></h3><blockquote>{html.escape(q)}</blockquote>' for t,u,q in d["reports"])
    tbl="".join(f"<tr><th>{n}</th><td>{cell(d[k])}</td></tr>" for k,n in COLS)
    body=f"""<h2>{html.escape(d["name"])}</h2><p><strong>Setup:</strong> {html.escape(d["distro"])} · <strong>Overall:</strong> {cell(d["overall"])}</p><p>{html.escape(d["summary"])}</p>
<table>{tbl}</table><h2>Owner reports</h2>{rep}<p>Own this laptop? <a href="../submit.html">Add your report</a>, especially for anything marked unknown.</p>"""
    open(f"laptops/{d['slug']}.html","w").write(page(d["name"],body,1))
about="""<h2>About &amp; methodology</h2><p>This site collects <em>public, first-hand owner reports</em> of how laptops run Omarchy and other Linux setups.</p>
<ul><li>Every compatibility claim links to its source. We don't test hardware ourselves (yet).</li><li>“Unknown” means nobody has reported on it yet. It doesn't mean the feature is broken.</li>
<li>Overall status follows the report: <em>Works</em>, <em>Works (minor fix)</em>, <em>Experimental</em>, or <em>Problems</em>.</li><li>Quotes are copied word for word. Reports are dated, and newer kernels and Omarchy releases can change results.</li>
<li>Corrections are welcome via the <a href="submit.html">submit page</a>.</li></ul>
<h2>Affiliate disclosure</h2><p><strong>[Placeholder]</strong> This site currently has no affiliate links. If we add them later (for example to laptop makers' stores), we will mark them clearly and say so here. Affiliate links will never change a compatibility status.</p>
<p>Not affiliated with Omarchy, Basecamp, or any laptop manufacturer.</p>"""
open("about.html","w").write(page("About",about))
submit="""<h2>Submit your report</h2><p>Own a laptop running Omarchy or another Linux setup? Send us:</p><ol>
<li>Exact model (and CPU/GPU variant)</li><li>Distro and version (e.g. Omarchy 3.6), kernel if known</li>
<li>For each item, say works / needed a fix / broken / not tested: Wi-Fi, Bluetooth, suspend/resume, camera, audio, internal display, external displays, battery life, fingerprint</li>
<li>Any fixes you applied</li><li>Optionally, a public link (X post, Reddit, blog) we can cite</li></ol>
<p><strong>Email:</strong> <a href="mailto:REPLACE_ME@example.com?subject=Laptop%20report">REPLACE_ME@example.com</a> (placeholder)<br><strong>GitHub issues:</strong> coming soon (placeholder)</p>
<p>We only publish what you report. Anything you don't mention stays “unknown”.</p>"""
open("submit.html","w").write(page("Submit a report",submit))
print("built",len(DATA))
