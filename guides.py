# Buyer guides built from the owner reports in build.py DATA. Prose only restates sourced reports.
NOTE=('<p><em>These guides collect public owner reports. We haven\'t tested these machines ourselves. '
 '"Unknown" means nobody has reported on that part yet, not that it fails. A "works" report means one owner said it worked for them, '
 'not that every feature is confirmed. Reports are dated; newer releases can change results. Last reviewed: Nov 8, 2026.</em></p>')
def X(u,t="source"): return f'<a href="{u}">{t}</a>'
def L(slug,t): return f'<a href="../laptops/{slug}.html">{t}</a>'
GUIDES=[
dict(slug="used-thinkpads",title="Used ThinkPads on Omarchy: what owners report",
 desc="Owner reports of Omarchy on seven ThinkPad models (T480, T490s, T14s Gen 3, T14 Gen 2, T470s, T450, X200), with sources and what is still unreported.",
 related=["lenovo-thinkpad-"],
 body=f"""<h2>Used ThinkPads on Omarchy: what owners report</h2>{NOTE}
<p>We have owner reports for seven ThinkPad models. All but the T480 rest on a single owner. None of these reports itemizes Wi-Fi or suspend.</p>
<table><tr><th>Model</th><th>Reports</th><th>What owners said</th><th>Still unreported</th></tr>
<tr><td>{L("lenovo-thinkpad-t480","T480 (2018)")}</td><td>3</td><td>One owner: "Tell me a better laptop than a T480 running Omarchy" ({X("https://x.com/Compilethings/status/2116222826080276868")}). Another runs one as a home server ({X("https://x.com/karthikraju391/status/2110597761125261629")}). A third says its two batteries showed as one until they had the battery panel rewritten ({X("https://x.com/Ruth_Kant_/status/2116582360812867659")}).</td><td>Wi-Fi, suspend, camera, audio, display</td></tr>
<tr><td>{L("lenovo-thinkpad-t490s","T490s")}</td><td>1</td><td>i7-8665U, 32 GB; bought used for $150 (owner's price, Oct 2026). "Omarchy runs great"; says the feel is worse than a MacBook and it isn't modular ({X("https://x.com/doomcheeks666/status/2114819445843771736")}).</td><td>All itemized components</td></tr>
<tr><td>{L("lenovo-thinkpad-t14s-gen-3","T14s Gen 3")}</td><td>1</td><td>"Absolutely flies." Intel or AMD version not stated ({X("https://x.com/fcuk112/status/2112690323398791443")}).</td><td>All itemized components</td></tr>
<tr><td>{L("lenovo-thinkpad-t14-gen-2-intel","T14 Gen 2 (Intel)")}</td><td>1</td><td>"A dream laptop"; screen hard to see in bright light, a panel limitation ({X("https://x.com/maietta/status/2114089169165455740")}).</td><td>All itemized components</td></tr>
<tr><td>{L("lenovo-thinkpad-t470s","T470s")}</td><td>1</td><td>Daily travel/dev laptop (16 GB, 1 TB); no hardware details ({X("https://x.com/Survis_com/status/2115987058741166535")}).</td><td>All itemized components</td></tr>
<tr><td>{L("lenovo-thinkpad-t450","T450")}</td><td>1</td><td>"Everything works out of the box" ({X("https://www.reddit.com/r/omarchy/comments/1o66zj1/hardware_suggestions_for_omarchy/")}).</td><td>Nothing itemized</td></tr>
<tr><td>{L("lenovo-thinkpad-x200","X200 (2008)")}</td><td>1</td><td>A pre-release Omarchy build installed in 2m 32s. That is an install report, not a daily-use report ({X("https://x.com/jonnyheggheim/status/2115482194097414165")}).</td><td>All itemized components</td></tr></table>
<h3>Reading these reports</h3><ul>
<li>A report covers the exact model the owner named. A T480 and a T480s are different laptops, and the T14 and T14s generations come in Intel and AMD versions. We don't carry a report over to a model or version nobody has reported on.</li>
<li>The T480 has the most reports here (three) and one documented quirk with dual batteries. Its Wi-Fi and suspend are still unreported.</li>
<li>The X200 report is from a pre-release build on an 18-year-old machine, so we mark it experimental.</li></ul>
<h3>General used-laptop checks (general advice, not from these reports)</h3><ul>
<li>Ask the seller for the battery's health or wear figure. Battery wear differs from unit to unit; the T490s owner reported 90% on theirs.</li>
<li>Ask whether a BIOS/supervisor password is set. Former business laptops sometimes arrive locked.</li>
<li>Check that the listing names the exact model and CPU.</li></ul>"""),
dict(slug="intel-macbooks",title="Old Intel MacBooks on Omarchy: what owners report",
 desc="Owner reports of Omarchy on the 2015 Intel MacBook Pro and the 2016 15-inch Touch Bar MacBook Pro, with the reported T1 sound fix and sources.",
 related=["macbook-pro-2015","macbook-pro-2016-touch-bar"],
 body=f"""<h2>Old Intel MacBooks on Omarchy: what owners report</h2>{NOTE}
<p>Our owner reports cover two Intel MacBook Pro models so far.</p>
<table><tr><th>Model</th><th>Reports</th><th>What owners said</th><th>Reported issues</th></tr>
<tr><td>{L("macbook-pro-2015","MacBook Pro (2015, Intel)")}</td><td>2</td><td>A 13" owner: "works like I bought the laptop yesterday" ({X("https://x.com/vladmariang/status/2108285563728240957")}). A second owner (screen size not stated): "works great" ({X("https://x.com/teddybear_lost/status/2107891169464074290")}).</td><td>None reported; no component itemized</td></tr>
<tr><td>{L("macbook-pro-2016-touch-bar","MacBook Pro 15\" Touch Bar (2016, Intel)")}</td><td>2</td><td>Up and running in about five minutes; owner praises the panel and says it runs a little warm when pushed at 4K ({X("https://x.com/ggcripto/status/2115907647245578318")}). A second owner says Omarchy made their 2016 MacBook Pro work again, screen size not stated ({X("https://x.com/bjorndunkel/status/2115919534255440038")}).</td><td>Sound needed a fix: a missing T1 chip firmware piece plus enabling the speaker channel ({X("https://x.com/ggcripto/status/2115939700082868337")})</td></tr></table>
<h3>Reading these reports</h3><ul>
<li>The 2016 Touch Bar owner warns they skipped keeping Apple's EFI partition; read the install notes before wiping the drive.</li>
<li>We have no reports for other Intel years, including the 2017&ndash;2020 models. Nothing here covers them.</li>
<li>Apple silicon Macs are separate and use Omarchy's newer native support: see the {L("macbook-air-m1-2020","M1 MacBook Air")} and {L("macbook-pro-m1-2020","M1 MacBook Pro")} pages.</li></ul>
<h3>Checks before buying a used Intel Mac (Apple's documentation)</h3><ul>
<li>Ask whether a firmware password is set. On an Intel Mac it blocks starting up from any disk other than the chosen startup disk, and Apple removes a forgotten one only with proof of purchase (<a href="https://support.apple.com/en-us/102384">Apple: Set a firmware password on your Mac</a>).</li>
<li>Ask the seller to follow Apple's steps for preparing a Mac for sale, including signing out and erasing it (<a href="https://support.apple.com/en-us/102773">Apple: What to do before you sell your Mac</a>). Apple's Activation Lock applies to Macs with Apple silicon or the T2 chip (<a href="https://support.apple.com/en-us/102541">Apple: Activation Lock for Mac</a>).</li>
<li>Confirm the exact year and screen size from the model, not the listing title. One owner here wrote "I think it's from 2016."</li></ul>"""),
dict(slug="surface",title="Microsoft Surface on Omarchy: what owners report",
 desc="Owner reports of Omarchy on Surface Laptop 3, Surface Pro 3, Surface Go, Surface Laptop 1st Gen and the experimental Surface Laptop 7 Snapdragon, with sources.",
 related=["surface-"],
 body=f"""<h2>Microsoft Surface on Omarchy: what owners report</h2>{NOTE}
<p>Most Surface entries rest on one owner. Nobody in these reports has described the Type Cover keyboard or the pen.</p>
<table><tr><th>Device</th><th>Reports</th><th>What owners said</th><th>Notes</th></tr>
<tr><td>{L("surface-laptop-3","Surface Laptop 3 (2019)")}</td><td>3</td><td>One owner: "running perfectly fine" ({X("https://x.com/ymanyen3/status/2090070452203061343")}). In {X("https://www.reddit.com/r/omarchy/comments/1wpaf6b/omarchy_on_surface_laptop/","this Reddit thread")}, one owner needed the linux-surface kernel plus tweaks so audio starts with the system; another says theirs (8 GB) runs great without that kernel, camera untested.</td><td>Owners differ on audio and the kernel</td></tr>
<tr><td>{L("surface-pro-3","Surface Pro 3 (2014)")}</td><td>1</td><td>Straightforward install; touchscreen works with no setup; GPS works ({X("https://x.com/KuritoL/status/2116520088970944891")}, {X("https://x.com/KuritoL/status/2116523341423206894","follow-up")}).</td><td>Battery, Type Cover, pen unreported</td></tr>
<tr><td>{L("surface-go-2018","Surface Go (2018)")}</td><td>1</td><td>Installed in five minutes, "everything just worked" ({X("https://x.com/mrelph/status/2117394175125750119")}).</td><td>Variant and components not stated</td></tr>
<tr><td>{L("surface-laptop-1st-gen","Surface Laptop (1st Gen)")}</td><td>1</td><td>Now runs Omarchy because it can't run Windows 11 ({X("https://x.com/ThrowATwit/status/2115160421242196136")}).</td><td>No details</td></tr>
<tr><td>{L("surface-laptop-7-snapdragon","Surface Laptop 7 13.8\" (Snapdragon X Plus)")}</td><td>1</td><td>A developer's in-progress ARM build; only IR face unlock is reported working ({X("https://x.com/qBitnaut/status/2108350982627233807")}).</td><td>Experimental; everything else unreported</td></tr></table>
<h3>Reading these reports</h3><ul>
<li>If you need the Type Cover or pen, no report here covers them.</li>
<li>The Surface Laptop 7 entry describes an in-development build, not a ready install.</li>
<li>Reports don't carry over to other Surface models or CPU variants.</li></ul>
<h3>General used-device checks (general advice, not from these reports)</h3><ul>
<li>Confirm the exact model and CPU/memory variant.</li><li>Ask about battery condition and whether a working charger is included.</li>
<li>If you need a keyboard, confirm the Type Cover is included.</li></ul>"""),
]
