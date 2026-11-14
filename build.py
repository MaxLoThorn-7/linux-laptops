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
 dict(slug="dell-xps-14-panther-lake",name="Dell XPS 14 (Panther Lake)",distro="Omarchy 3.6",overall="Mixed (crash reports)",
  wifi=U,suspend=U,camera=U,audio=U,display="Works (incl. Studio Display, per post title)",battery="Owner says good",
  summary="Several owners say Omarchy runs well on the new XPS 14: one installed it right out of the box, one ran World of Warcraft at 60 fps on medium settings, and one says fan noise is his only gripe. But one owner of a days-old XPS 14 reports two crashes in one morning and points to a Dell community thread about abrupt crashes and shutdowns on battery on the 2026 XPS 14 and 16. He doesn't say which Linux distro he runs (his earlier post mentions Ubuntu), and no fix has been reported here yet. Worth watching before you buy.",
  reports=[("r/omarchy post","https://www.reddit.com/r/omarchy/comments/1sy0svs/dell_xps_14_panther_lake_studio_display_omarchy_36/",
   "Post titled \u201cDell XPS 14 Panther Lake + Studio Display + Omarchy 3.6\u201d: \u201cimmediately installed Omarchy 3.6 out of the box\u2026 a powerhouse in terms of battery and performance\u2026 seems to be working perfectly for what I\u2019ve thrown at [it]\u201d (excerpt as returned by search; partially truncated)."),
   ("Neil Chudleigh (@neilsuperduper) on X, 2026-11-08","https://x.com/neilsuperduper/status/2119565482902638794",
   "\u201cWoW Forever runs great on omarchy\u2026 this machine is pretty basic (dell xps 14)\u2026 worked out of the box got 60 fps with the new graphics on medium\u201d (excerpt; he also posted an unboxing-and-install video on 2026-11-04)"),
   ("Omar (@omarmsimon) on X, 2026-11-04","https://x.com/omarmsimon/status/2118120687940587708",
   "\u201cJumped from a lifetime Mac user to an XPS 14 on omarchy. Still can\u2019t get used to the fan noise\u2026.only gripe. Otherwise no looking back to MacOS\u201d"),
   ("Mark Maunder (@mmaunder) on X, 2026-11-09","https://x.com/mmaunder/status/2119798344990286051",
   "\u201cSecond crash this morning for me on a brand new XPS 14 only days old. Here\u2019s an Omarchy Linux thread reporting the same thing.\u201d (distro not stated in this post; his quoted post says \u201cRandom shutdown under ubuntu Linux\u201d)"),
   ("Dell Community thread (linked by @mmaunder)","https://www.dell.com/community/en/conversations/xps/xps-1416-2026-abrupt-crashshutdown-while-on-battery-da14260-da16260/6a41380230ba7b5c1c724a29?page=1",
   "Thread titled \u201cXPS 14/16 2026 abrupt crash/shutdown while on battery (DA14260, DA16260)\u201d; @mmaunder describes it as having six pages of reports. Not read in full here.")]),
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
 dict(slug="asus-expertbook-b9",name="ASUS ExpertBook B9 (generation not stated)",distro="Omarchy",overall="Works",
  wifi=U,suspend=U,camera=U,audio=U,display=U,battery=U,
  summary="One owner on X says their ASUS B9, a laptop they had written off and handed to their kids, is still good to use once it runs Omarchy. They call it \u201cAsus B9\u201d without naming the generation (the B9 line is sold as the ExpertBook B9), and they don't say which components they checked, so every item below is still unknown.",
  reports=[("Dmytro Gladkyi (@gladimdim) on X, 2026-10-24","https://x.com/gladimdim/status/2113969530917539963",
   "\u201cMy Asus B9 laptop was sentenced and given to kids to jump on it. Turns out it is still good if Omarchy is running it. Omarchy is truly a miracle\u201d")]),
 dict(slug="lenovo-thinkpad-t490s",name="Lenovo ThinkPad T490s",distro="Omarchy",overall="Works",
  wifi=U,suspend=U,camera=U,audio=U,display=U,battery=U,
  summary="One owner on X says Omarchy runs great on their ThinkPad T490s (Core i7-8665U, 32GB RAM, 512GB NVMe SSD), which they bought used for $150. They note the battery was at 90% health, which describes the battery's wear rather than battery life under Linux. They find the build feels worse than a MacBook and point out it isn't modular, but like that it's slim. They don't say which components they checked, so every item below is still unknown.",
  reports=[("Alejandro (@doomcheeks666) on X, 2026-10-26","https://x.com/doomcheeks666/status/2114819445843771736",
   "\u201cThinkPad T490s / i7 8665u @ 4.8 GHz / 512 ssd nvme / 32gb drr4 ram. Got this for $150! It\u2019s like new, the ssd health is 100%, the battery is at 90% health. The feel is kinda ass compared to macbook, but the specs are nice. It is not modular, but it is slim! Omarchy runs great on it \U0001f60e\u201d")]),
dict(slug="surface-laptop-1st-gen",name="Microsoft Surface Laptop (1st Gen)",distro="Omarchy",overall="Works",
  wifi=U,suspend=U,camera=U,audio=U,display=U,battery=U,
  summary="One owner on X says they're still using their first-generation Surface Laptop and that it now runs Omarchy, because the machine doesn't support Windows 11. They don't say which CPU variant they have or which components they checked, so every item below is still unknown.",
  reports=[("Eric Winnington (@ThrowATwit) on X, 2026-10-27","https://x.com/ThrowATwit/status/2115160421242196136",
   "\u201cStill rocking my Surface Laptop (1st Gen) - It's running Omarchy now since it doesn't support Win11.\u201d (reply to @surface)")]),
dict(slug="lenovo-thinkpad-x200",name="Lenovo ThinkPad X200 (2008)",distro="Omarchy 4.5 rc2 (pre-release)",overall="Experimental",
  wifi=U,suspend=U,camera=U,audio=U,display=U,battery=U,
  summary="One owner on X installed the Omarchy 4.5 release candidate on an 18-year-old ThinkPad X200 (Core 2 Duo P8400, Intel GMA 4500MHD graphics, 6GB RAM, 128GB SSD) and says the install took 2 minutes 32 seconds. That's a report that it installs, not that everything works: they don't say how it runs day to day or which components they checked, so every item below is still unknown. It's marked experimental because it was a pre-release build on very old hardware.",
  reports=[("Jonny Heggheim (@jonnyheggheim) on X, 2026-10-28","https://x.com/jonnyheggheim/status/2115482194097414165",
   "\u201c@Omarchy 4.5rc2 on a ThinkPad X200 from 2008: installed in 2m 32s. Core 2 Duo P8400, GMA 4500MHD, 6 GB RAM, 128 GB SSD. Not bad for an 18-year-old laptop!\u201d")]),
dict(slug="macbook-pro-2016-touch-bar",name="Apple MacBook Pro 15\" with Touch Bar (2016, Intel)",distro="Omarchy",overall="Works (minor fix)",
  wifi=U,suspend=U,camera=U,audio="Needed fix (T1 chip firmware + speaker channel)",display="Owner says panel is excellent; runs at 4K",battery=U,
  summary="One owner (posting in Italian) installed Omarchy on a 15-inch Touch Bar MacBook Pro they believe is from 2016 and had it up and running in about five minutes. Sound needed a fix: they say a firmware piece for Apple's T1 chip was missing and the speaker channel had to be enabled, which an AI coding agent sorted out for them. They praise the screen, and say it runs a little warm with everything maxed at 4K, which they suspect is dust inside. They also warn that they skipped the step of keeping Apple's EFI partition, so read the install notes first. A second owner says Omarchy made their 2016 MacBook Pro usable again, without naming the screen size. Wi-Fi, suspend, camera and battery are still unreported.",
  reports=[("\U0001d676\U0001d676 (@ggcripto) on X, 2026-10-29 (Italian; our translation)","https://x.com/ggcripto/status/2115907647245578318",
   "\u201cI forgot I had an old 15\" MacBook Pro, one with the Touch Bar, I think it's from 2016. Dead for macOS by now, so I'm installing Omarchy. Up and running in 5 minutes. But since I'm the hasty type, I hadn't read about keeping Apple's EFI partition.\u201d"),
   ("@ggcripto follow-up replies on X, 2026-10-29 (Italian; our translation)","https://x.com/ggcripto/status/2115939700082868337",
   "\u201c\u2026codex solved it: a firmware piece for the damned T1 chip was missing, plus enabling the speaker channel.\u201d Earlier in the thread: \u201cThe panel on this MacBook is stratospheric. It runs a bit warm, but I suspect it's dirty inside\u201d and \u201cI'm at 4K with everything maxed and it warms up a little.\u201d (excerpts)"),
   ("Bjorn Dunkel (@bjorndunkel) on X, 2026-10-29","https://x.com/bjorndunkel/status/2115919534255440038",
   "\u201cOmarchy made my 2016 MacBook Pro work again. As I could not install the latest python to the ole intel Mac I switch to @omarchy\u201d (screen size not stated; post goes on to ask for TeamViewer help)")]),
dict(slug="asus-chromebook-c523n",name="ASUS Chromebook C523N",distro="Omarchy (installed after Debian, to fix partitions)",overall="Works (minor fix)",
  wifi=U,suspend=U,camera=U,audio="Needed setup (done by an AI agent over SSH; details not given)",display=U,battery=U,
  summary="One owner on X brought an old ASUS C523N Chromebook (8GB RAM) back to life with Omarchy. The Omarchy installer first failed with a \u201cno space\u201d error, so they installed Debian to sort out the disk partitions and then installed Omarchy over it. Audio needed configuring, which they had the Codex AI agent handle over SSH, and they don't say what the fix was. They also don't say whether they had to replace the Chromebook's firmware to boot Linux, which many Chromebooks need, so check that before you start. Wi-Fi, suspend, camera, display and battery are still unreported.",
  reports=[("Erdepfel (@Erdepfel) on X, 2026-10-30","https://x.com/Erdepfel/status/2116289435088343392",
   "\u201cHey @omarchy, my old ASUS C523N Chromebook is alive again! The installer reported \u2018no space,\u2019 so I installed Debian first to fix the partitions, then Omarchy. Codex handled the remaining setup and audio configuration over SSH. Now running Linux and Codex CLI on 8GB RAM.\u201d")]),
dict(slug="surface-pro-3",name="Microsoft Surface Pro 3 (2014)",distro="Omarchy",overall="Works",
  wifi=U,suspend=U,camera=U,audio=U,display="Works (owner says the touchscreen works with no setup)",battery=U,
  summary="One owner on X dug a 2014 Surface Pro 3 out of a cabinet and installed Omarchy on it. They call it a straightforward install with no blockers, and say the touchscreen just works: tapping through panels and switching workspaces with a finger, with no configuration. They describe it as smooth and also say location (GPS) works. Their one complaint was software, not hardware: Synology Drive has no on-demand sync on Linux. They said battery testing was next and haven't reported on it yet. Wi-Fi, suspend, camera, audio, the Type Cover keyboard and the pen are all still unreported.",
  reports=[("kurito.exe (@KuritoL) on X, 2026-10-31","https://x.com/KuritoL/status/2116520088970944891",
   "\u201c@omarchy is alive on my 2014 Surface Pro 3. The touchscreen just works. Tapping through panels, switching workspaces with my finger, no config at all. And everything feels smooth, GPS also works. The shortcuts are just there out of the box.\u201d \u2026 \u201cNext I will test how the battery holds up in normal use.\u201d (excerpts; emoji removed)"),
   ("@KuritoL follow-up reply on X, 2026-10-31","https://x.com/KuritoL/status/2116523341423206894",
   "\u201cWell, it was a pretty straightforward install. No blockers at all. I could have finished even sooner if I did not have personal stuff to deal with.\u201d")]),
dict(slug="lenovo-thinkpad-t470s",name="Lenovo ThinkPad T470s",distro="Omarchy",overall="Works (few details)",
  wifi=U,suspend=U,camera=U,audio=U,display=U,battery=U,
  summary="One owner on X (a consulting firm's account) pulled an old ThinkPad T470s with 16 GB of RAM and 1 TB of storage out of a drawer, installed Omarchy on it, and now uses it as their travel laptop for building applications. They report it in daily use but don't mention any specific hardware, so Wi-Fi, suspend, camera, audio, display, battery and the keyboard/trackpad are all still unreported. The rest of their thread is about Omarchy's built-in AI agent feature, not this laptop's hardware.",
  reports=[("Survis Consulting (@Survis_com) on X, 2026-10-30","https://x.com/Survis_com/status/2115987058741166535",
   "\u201cMy old Lenovo T470s was sitting in a drawer. 16 GB of RAM, 1 TB of storage, nothing to do. This week I installed Omarchy on it, an Arch Linux desktop from David Heinemeier Hansson built on Hyprland. Now it is my travel laptop for building applications.\u201d")]),
dict(slug="surface-go-2018",name="Microsoft Surface Go (2018)",distro="Omarchy",overall="Works",
  wifi=U,suspend=U,camera=U,audio=U,display=U,battery=U,
  summary="One owner on X installed Omarchy on a 2018 Surface Go that could barely run Windows, and says the install took five minutes and everything just worked. They now use it as a front end for AI agents (Claude, ChatGPT) with Tailscale to heavier machines. They don't say which CPU/storage variant they have or which components they checked, so every item below is still unknown. The Type Cover keyboard and the pen are also unreported.",
  reports=[("Mark Relph (@mrelph) on X, 2026-11-02","https://x.com/mrelph/status/2117394175125750119",
   "\u201cThis 2018 Surface Go barely ran Windows. Now it\u2019s a front end for AI agents. Omarchy installed in five minutes and everything just worked. Claude, ChatGPT and my agents, with Tailscale to the machines doing the heavy lifting. Saved from e-waste.\u201d")]),
dict(slug="surface-laptop-3",name="Microsoft Surface Laptop 3 (2019)",distro="Omarchy",overall="Works (minor fix)",
  wifi=U,suspend=U,camera=U,audio="Needed fix (startup; with linux-surface kernel, per one owner)",display=U,battery=U,
  summary="Two owners report Omarchy on a 2019 Surface Laptop 3. One on X says it runs perfectly fine, without naming which components they checked. Another on Reddit says it works well after installing the linux-surface kernel and applying a few tweaks so audio starts with the OS; they don't spell out those tweaks. A third Reddit commenter (same thread) says their 8GB Surface Laptop 3 runs great without the linux-surface kernel for anything they use, and they haven't tested the camera. Wi-Fi, suspend, camera, display, battery, Type Cover and pen are still unreported in detail; experiences with the Surface kernel appear to vary by owner.",
  reports=[("ymanyen3 (@ymanyen3) on X, 2026-08-19","https://x.com/ymanyen3/status/2090070452203061343",
   "\u201cAbsolutely agree. Omarchy is running perfectly fine on Surface Laptop 3 from 2019.\u201d (reply to DHH)"),
   ("r/omarchy comment by u/Alfrai, 2026-09-24","https://www.reddit.com/r/omarchy/comments/1wpaf6b/omarchy_on_surface_laptop/",
   "\u201cI have omarchy on my surface laptop 3, works like a charm after installing the Linux surface kernel and a few tweaks to make the audio start at the start of the OS\u201d"),
   ("r/omarchy comment by u/OligarchyAmbulance, 2026-09-25","https://www.reddit.com/r/omarchy/comments/1wpaf6b/omarchy_on_surface_laptop/",
   "\u201cI have an old 8GB Surface Laptop 3, absolutely, completely unusable on Windows. I installed Fedora and Omarchy and it runs great, no linux-surface kernel needed for anything I've run into (I haven't tested the camera but don't care about that. It totally brought the computer back to life.\u201d")]),
dict(slug="lenovo-thinkpad-t480",name="Lenovo ThinkPad T480 (2018)",distro="Omarchy",overall="Works (minor fix)",
  wifi=U,suspend=U,camera=U,audio=U,display=U,battery="Needed fix (dual-battery panel showed only one; owner had an AI agent rewrite the panel)",
  summary="Three owners on X report Omarchy on a ThinkPad T480. One calls it their portable compute / control-plane laptop and asks who has a better Omarchy machine. Another runs it as a home server. A third says the dual internal batteries only showed as one in Omarchy until they asked an AI agent to rewrite the battery panel, which took about five minutes and gave them a bar icon per battery. Wi-Fi, suspend, camera, audio and display are still unreported in detail.",
  reports=[("CompilingThings (@Compilethings) on X, 2026-10-30","https://x.com/Compilethings/status/2116222826080276868",
   "\u201cTell me a better laptop than a T480 running Omarchy. I'll wait.\u201d"),
   ("Karthik Raju (@karthikraju391) on X, 2026-10-15","https://x.com/karthikraju391/status/2110597761125261629",
   "\u201cMy agentmaxxing setup: - thinkpad t480 running omarchy as the home server\u2026\u201d (excerpt; post continues with other tools)"),
   ("Ruth Kant (@Ruth_Kant_) on X, 2026-10-31","https://x.com/Ruth_Kant_/status/2116582360812867659",
   "\u201cMy T480 has two batteries, Omarchy only showed one. I justz told it to rewrite the battery panel to include more than one battry. Five minutes later, it was done, and I even had an individual bar icon for each battery.\u201d")]),
dict(slug="dell-xps-13-2026",name="Dell XPS 13 (2026)",distro="Omarchy",overall="Works",
  wifi=U,suspend="Owner says power states work (one owner, no detail)",camera=U,audio=U,display=U,battery=U,
  summary="Three owners on X say Omarchy runs well on a newly released Dell XPS 13. One names the 2026 Wildcat Lake model with 16GB of RAM and calls it really nice. Another says everything, including the power states, just works and uses it as a light client laptop. A third runs it next to a desktop and says the XPS 13 is so snappy they barely want the desktop. None of them say which components they tested, so Wi-Fi, camera, audio, display and battery life are still unreported in detail. Only one post names the Wildcat Lake chip, so the other two are assumed to be the same new XPS 13 but don't say so.",
  reports=[("Oliver Allpress (@OliverAllpress) on X, 2026-11-05","https://x.com/OliverAllpress/status/2118463678735585597",
   "\u201cI have the 2026 Wildcat lake Dell XPS13 16GB and its really nice with Omarchy.\u201d (reply)"),
   ("Jason Milldrum (@NT7S_Jason) on X, 2026-11-05","https://x.com/NT7S_Jason/status/2118451582497075668",
   "\u201cI got the XPS13 thanks to DHH's recommendation to run Omarchy and it's primo, highly recommended light client laptop. Heavy work relegated to a shed PC on my Tailnet. Big ups to Dell for supporting Omarchy on this hardware. Everything, including the power states, just work.\u201d"),
   ("Yael Ossowski (@YaelOss) on X, 2026-11-05","https://x.com/YaelOss/status/2118442514025722165",
   "\u201ci run omarchy on an old Ryzen desktop computer with 32GB RAM and have another instance on a brand-new xps 13 with 16GB RAM. the XPS 13 is so snappy I really don't even want the desktop anymore (apart from massive HDD space). Dell makes great products, and @omarchy just works\u201d")]),
dict(slug="macbook-pro-m1-2020",name="Apple MacBook Pro 13\" (M1, 2020)",distro="Omarchy 4.5 (native M1)",overall="Works (minor fix)",
  wifi="Works (owner reports plane Wi-Fi)",suspend=U,camera=U,audio="Speakers work; mic needed fix (apple_sep driver, per one owner)",display="Works (Studio Display, per one owner)",battery=U,
  summary="Four owners on X report Omarchy on an M1 MacBook Pro (the 2020 13-inch with Touch Bar). One, an ex-Apple employee, says Wi-Fi (including on a plane), speakers, Apple Music and AirDrop all work, calls it super fast, and earlier showed Touch ID working after some patching; they also say a Studio Display works and that Omarchy makes the Touch Bar useful. Another owner fixed the built-in mic, which showed up but recorded silence until they loaded the apple_sep driver in read-only mode so the Secure Enclave could pass audio. A third installed Omarchy 4.5 after native M1 support landed: the installer still had a few bugs but finished, and a fourth says an older M1 MacBook Pro runs very nicely. Suspend, camera and battery life are still unreported in detail. Screen size is taken from the 2020 M1 MacBook Pro line (13-inch with Touch Bar); owners say \"M1 MacBook Pro\" without always naming inches.",
  reports=[("Todd Dailey (@twid) on X, 2026-11-06","https://x.com/twid/status/2118757257370644839",
   "\u201cAfter 22 years of working for Apple and always traveling with a Mac laptop, this weekend I brought a Mac but not macOS. My M1 MacBook Pro is running Omarchy Linux. Everything works! WiFi on the plane, Apple Music, speakers, airdrop. It\u2019s super fast\u2026\u201d (excerpt from longer post)"),
   ("Todd Dailey (@twid) on X, 2026-11-03","https://x.com/twid/status/2117425191685124541",
   "\u201cTouchID on Omarchy on M1 MacBook Pro! Everything works now, speakers, Studio Display, Airdrop! Really great Omarchy system- if you can find one with 16GB on eBay and don\u2019t mind patching a few things it\u2019s awesome!\u201d"),
   ("Stonekeep4ever (@Stonekeep458291) on X, 2026-11-02","https://x.com/Stonekeep458291/status/2117268641561432173",
   "\u201cFixed my M1 MacBook Pro's built-in mic on Omarchy today. The mic showed up but recorded pure silence. The cause: the Secure Enclave chip sits in the mic's signal path and has to be switched on first. Fix: load the apple_sep driver in read-only mode. Works!\u201d"),
   ("Gleydson (@g13ydson) on X, 2026-11-06","https://x.com/g13ydson/status/2118737506124370417",
   "\u201cOmarchy 4.5 dropped yesterday with native M1 support, so I gave it a shot on my MacBook. It took a bit to get going and the installer still has a few bugs, but it worked in the end. Now I\u2019ve got Omarchy Linux running on my M1 MacBook PRO :)\u201d"),
   ("John Engates (@jengates) on X, 2026-11-07","https://x.com/jengates/status/2118904627907482096",
   "\u201cI installed Omarchy Linux on my old M1 Macbook Pro and it's very nice. Will be my weekend project to master this thing. Thanks @dhh\u201d")]),
dict(slug="macbook-air-m1-2020",name="Apple MacBook Air (M1, 2020)",distro="Omarchy 4.5 (native M1)",overall="Works",
  wifi=U,suspend=U,camera=U,audio="Mixed (one owner says audio works perfectly; another says the internal mic showed no input on 4.5)",display="Works (USB-C to HDMI external monitor, per one owner)",battery=U,
  summary="Five owners on X report Omarchy on an M1 MacBook Air (the 2020 13-inch). One says installing it made the laptop feel like new again and calls it blazing fast. Another did a clean install of Omarchy 4.5 with the project's native macOS installer app after running an earlier Quattro alpha, and called the 4.5 install very polished; the same owner later said the internal microphone was selected but showed no input (including with Superwhisper), and they confirmed the mic still works in macOS. A third says a DMG install ran flawless out of the box, including audio, was super snappy, and is set up to dual-boot. A fourth says their M1 Air has a new life and calls Omarchy ridiculously smooth. A fifth says it's really cool on an MBA M1 and that connecting a USB-C to HDMI monitor (via something they call aurora) works. Wi-Fi, suspend, camera and battery life are still unreported in detail. The M1 MacBook Air was only sold as a 13-inch; owners say \"M1 MacBook Air\" without always naming inches.",
  reports=[("Dan Eriksson (@erikssondan) on X, 2026-11-06","https://x.com/erikssondan/status/2118771371090096285",
   "\u201cFinally! @omarchy installed on my MacBook Air M1. It feels like new again. Blazing fast. And I don't have to use MacOS anymore. Thank you!\u201d"),
   ("theRealDarkHorse (@jeffreydsauer) on X, 2026-11-06","https://x.com/jeffreydsauer/status/2118743680228147543",
   "\u201cCongrats to @OmarchyMac team for releasing the new native macOS Installer app! I was running an earlier Quattro alpha version, and just finished a clean install of macOS, and install of Omarchy 4.5 on my 2020 M1 Macbook Air. Wow! Very polished!\u201d"),
   ("@jeffreydsauer follow-up replies on X, 2026-11-06","https://x.com/jeffreydsauer/status/2118755981551378573",
   "\u201cDoes the M1 Macbook Air microphone work on Omarchy 4.5 with Superwhisper? I have it selected, but I do not see any input happening\u201d Then: \u201cSo... I booted into macOS to verify the internal Macbook Air mic works, and it does. Back in omarchy now, having an agent try to diagnose why I can no audio from the internal mic...\u201d"),
   ("flyonthewall (@flyonthewa87725) on X, 2026-11-04","https://x.com/flyonthewa87725/status/2118105787398766642",
   "\u201cI ran a easy DMG install on my macbook air m1. Runs flawless right out the box everything including audio works perfectly. Super snappy. Its set up to dual boot but im sure i wont be using Macos\u201d"),
   ("Peter Skaronis (@skaronis) on X, 2026-11-05","https://x.com/skaronis/status/2118436081796534506",
   "\u201cMy M1 MacBook Air has a new life. Awesome work @dhh Omarchy has tamed Linux. Ridiculously smooth. We can truly fix everything.\u201d"),
   ("Ayush Sanj (@AyushSanj) on X, 2026-10-20","https://x.com/AyushSanj/status/2112496916898656384",
   "\u201c@omarchy in mba m1, its really cool. tried aurora to connect usb c to hdmi monitor, works.\u201d")]),
dict(slug="acer-swift-3",name="Acer Swift 3 (14-inch, SF314 series)",distro="Omarchy (3.0.2 for one owner; version not stated by the other)",overall="Works (few details)",
  wifi=U,suspend=U,camera=U,audio=U,display=U,battery=U,
  summary="Two owners report Omarchy installed and running on an Acer Swift 3, but they have different generations of it. One dug out a 2020 Acer Swift 3 after their M4 MacBook crashed repeatedly and now uses the Swift 3 with Omarchy to run AI agents, local CI and code reviews, saying it handled 20+ merged PRs and 2 releases in a day. The other installed Omarchy 3.0.2 on a Swift 3 SF314-71 with 16GB of RAM; their USB stick's built-in UEFI check flagged two missing EFI files, but they went ahead and called the install smooth and successful, and DHH replied that with a matching checksum it looked like a false alarm. Neither owner says how Wi-Fi, suspend, the camera, audio, the display or battery life behave, so those are unknown. The 2020 owner doesn't give the exact model number or chip, so it may not be the same hardware as the SF314-71.",
  reports=[("Abel Ayalew (@nabroleonx) on X, 2026-11-06","https://x.com/nabroleonx/status/2118755997988601888",
   "\u201cmy M4 crashed 5+ times in one day trying to run agents + local CI so I dug out my 2020 Acer Swift 3 and put Omarchy on it. it's now running our agents, CI and code reviews: 20+ PRs merged and 2 releases shipped today\u201d"),
   ("@kvidaxl on GitHub (basecamp/omarchy issue #2255), 2025-10-06","https://github.com/basecamp/omarchy/issues/2255",
   "Acer Swift 3 (SF314-71, 16GB RAM), omarchy-3.0.2.iso written with Rufus: the USB's UEFI media check reported 2 missing EFI files, but \u201cDespite the failed tests, I proceeded with the installation, which was smooth and successful.\u201d DHH replied: \u201cIf you have the right sha, and the installation works, that seems like a false alarm to me from that tool.\u201d")]),
dict(slug="dell-latitude-7440",name="Dell Latitude 7440 (2023)",distro="Omarchy (4.0.0-1 for one owner; version not stated by the other)",overall="Works (Bluetooth quirk)",
  wifi=U,suspend=U,camera=U,audio=U,display=U,battery=U,
  summary="Two owners report Omarchy running on a Dell Latitude 7440. One installed it on his 82-year-old dad's 7440 as a birthday gift, saying the install was \u201creally smooth\u201d, and about a week later called Omarchy \u201csmooth as butter\u201d on the old Latitude he set up for his dad (that later post doesn't repeat the model). The other, on Omarchy 4.0.0-1 with an Intel AX211 wireless card, found one real gotcha: turning Bluetooth off from the Omarchy panel removes the Bluetooth radio completely, and neither the panel toggle nor rfkill unblock brings it back; only a suspend/resume or a reboot does. That GitHub issue is now closed, but we haven't confirmed whether this Dell-specific case is fixed. Nobody here reports on suspend in general, the camera, audio, the display or battery life, so those are unknown.",
  reports=[("Dragos Roua (@dragosroua) on X, 2026-10-31","https://x.com/dragosroua/status/2116467421426971049",
   "\u201cJoining the crowd and installing @omarchy by @dhh on my dad\u2019s Dell Latitude 7440\u2026 He also uses a laptop, for chess and searching stuff online, every single day.\u201d (excerpt); in a reply the same morning: \u201cIt was really smooth the install.\u201d"),
   ("Dragos Roua (@dragosroua) on X, 2026-11-06","https://x.com/dragosroua/status/2118608152161587706",
   "\u201c@omarchy is an absolute beast, I installed it for my dad on an old Dell Latitude. Smooth as butter.\u201d (model not repeated in this post)"),
   ("@oren on GitHub (basecamp/omarchy issue #6956), 2026-08-19","https://github.com/basecamp/omarchy/issues/6956#issuecomment-5340352331",
   "\u201cDell Latitude 7440, Omarchy 4.0.0-1, kernel 7.1.8-arch1-3, Intel AX211\u2026 Neither `rfkill unblock bluetooth` nor `omarchy-bluetooth-power on` recovers it\u2026 Only a suspend/resume or reboot brings the radio back.\u201d (excerpt)")]),
 dict(slug="lenovo-thinkpad-p14s",name="Lenovo ThinkPad P14s (Gen 2 and other generations)",distro="Omarchy (version not stated)",overall="Works (wake quirk)",
  wifi=U,suspend="Mixed (one Gen 2 owner reports unpredictable wake-up)",camera=U,audio=U,display="Works with external displays (one Gen 2 owner)",battery="One owner says excellent (generation not stated)",
  summary="Several owners on X run Omarchy on a ThinkPad P14s. The most detailed is a Gen 2 owner who uses it full time with external displays, though in September he listed \u201cunpredictable wake-up\u201d as something he still needed to fix; he doesn't say whether his is the Intel or AMD version. Another owner of an AMD P14s (generation not stated) says the install was straightforward once Secure Boot was turned off, and that setting up the fingerprint reader let him skip typing his password. A third says battery and performance are excellent, and a fourth, who traded in a MacBook Air M3 for a P14s, says a few days in he could move his development work back onto the laptop. One Ryzen P14s owner reports one app-specific problem: YouTube live streams inside VRChat freeze after about 10 seconds. Wi-Fi, camera and audio aren't mentioned by anyone. Not an owner report, but useful: NixOS's hardware config for the Gen 2 AMD model says to set the firmware's Sleep State to \u201cLinux\u201d for suspend to work, which may be worth checking if wake-up misbehaves.",
  reports=[("JjP (@DoppioJP) on X, 2026-11-07","https://x.com/DoppioJP/status/2119134237874172000",
   "\u201cI\u2019ve been using full time ThinkPad P14s Gen 2 with Omarchy, external displays, with a mouse and Lofree keyboard\u2026\u201d (excerpt; Intel or AMD not stated)"),
   ("JjP (@DoppioJP) on X, 2026-09-21","https://x.com/DoppioJP/status/2102176813170512007",
   "Listed among fixes awaiting attention: \u201cunpredictable wake-up of Omarchy on ThinkPad P14s Gen 2\u201d (no further details given)"),
   ("RT (@hardrocktan) on X, 2026-09-04","https://x.com/hardrocktan/status/2095716930632266238",
   "\u201cGot a Thinkpad P14s AMD. Set Secure Boot Off. Flash the latest ISO of Omarchy. Install. Setup finger print (this enable you skip entering the password for everything)\u201d (generation not stated)"),
   ("Stephen Edginton (@StephenEdginton) on X, 2026-08-12","https://x.com/StephenEdginton/status/2087643358537617773",
   "\u201c\u2026the battery and performance on thinkpad p14s is excellent on Omarchy\u201d (excerpt; generation not stated)"),
   ("TIE (@kurtszt) on X, 2026-09-02","https://x.com/kurtszt/status/2095148863464280435",
   "Posted in Chinese; our translation: traded in a MacBook Air M3 for a ThinkPad P14s, installed Omarchy and used it for a few days, and feels he can move his development back onto the laptop instead of always SSHing into his desktop. (Generation not stated.)"),
   ("@DrKai_Lab on X, 2026-07-25","https://x.com/DrKai_Lab/status/2080829483159089273",
   "Posted in Japanese; our translation: on a ThinkPad P14s (Ryzen) running Omarchy, YouTube live streams played through iwaSync in VRChat freeze after about 10 seconds, and changing options didn't fix it. (Generation not stated.)"),
   ("NixOS hardware config for P14s Gen 2 AMD (context, not an owner report)","https://github.com/NixOS/nixos-hardware/blob/master/lenovo/thinkpad/p14s/amd/gen2/default.nix",
   "Code comment: \u201cFor suspending to RAM, set Config -> Power -> Sleep State to \u2018Linux\u2019 in EFI.\u201d")]),
dict(slug="dell-latitude-7350-detachable",name="Dell Latitude 7350 Detachable (Intel, 2-in-1 tablet)",distro="Omarchy (version not stated) plus the owner's published fix repos",overall="Works (needs fixes)",
  wifi=U,suspend="Works with the owner's audio fixes; it adds lock-then-sleep and timed hibernation",camera="Partial (needs fixes; not exposed through PipeWire)",audio="Works after fixes (no sound out of the box for this owner)",display="Works (owner sets the 2880x1920 panel to 2x; Chromium shows faint artifacts, unresolved)",battery=U,
  summary="One owner, Greg Yeutter, runs Omarchy on a Dell Latitude 7350 Detachable, a Surface-style Intel tablet with a keyboard cover, and he has published two public repos with everything he had to change. The biggest problem was sound: with the camera package Omarchy installs, the audio system stalled on the camera's raw devices and there was no sound at all until he disabled PipeWire's camera monitor, which means apps that go through PipeWire can't see the cameras (apps that open the camera directly still work). The built-in microphone could also lock up the sound card after suspend/resume; he fixed that by swapping in a newer kernel driver, which then passed his recording and suspend/resume tests. He also tamed volume buttons that jumped several steps per tap, set the high-resolution screen to exactly 2x, added finer low-brightness steps, and made the on-screen keyboard detect when the keyboard cover is attached. His separate tablet repo adds the on-screen keyboard, touch window moving and resizing, screen rotation, and a lock-screen PIN pad. Still open on his list: faint display artifacts in Chromium and an infrared camera that only works with an experimental driver. He doesn't say how Wi-Fi or battery life are, so those are unknown. This is more of a tinkerer's machine than a plug-and-play one, but every fix is written down.",
  reports=[("Greg Yeutter (@GregYeutter) on X, 2026-10-14","https://x.com/GregYeutter/status/2110366489329246448",
   "\u201cPicked up a Dell 7350 detachable. A little less complex due to being on Intel, but I've been working on some tablet optimizations\u2026 and device-specific optimizations\u201d (excerpt; links to his two repos below)"),
   ("Greg Yeutter (@GregYeutter) on X, 2026-10-15","https://x.com/GregYeutter/status/2110875843635683680",
   "\u201cI've got Omarchy on a Dell Latitude 7350 Detachable (Surface-style device with Intel Chip). Trying to make Omarchy work well with touch\u201d"),
   ("yeutterg/omarchy-dell-latitude-7350-detachable on GitHub (owner's fix repo)","https://github.com/yeutterg/omarchy-dell-latitude-7350-detachable",
   "README: \u201cWorking sound: camera monitor disabled, stable upstream microphone driver\u201d; CHANGES.md: with the camera package, WirePlumber \u201cstalls its event queue on the ~48 raw IPU6 camera nodes\u2026 so there is no sound\u201d; known issues list Chromium display artifacts (\u201cThe issue remains unresolved\u201d) and an infrared camera running on an experimental driver. (excerpts)"),
   ("yeutterg/omarchy-tablet on GitHub (owner's tablet repo)","https://github.com/yeutterg/omarchy-tablet",
   "Generic tablet layer for Omarchy: on-screen keyboard that pops up when the cover is detached, Stay Awake with the cover closed, lock-screen PIN pad, touch move/resize of windows, and screen rotation from the accelerometer. (summary)")]),
dict(slug="macbook-air-m3",name="Apple MacBook Air (M3, 2024)",distro="Omarchy 4.5 (native Apple Silicon; one owner used 4.5 RC3)",overall="Works (minor fixes)",
  wifi=U,suspend="Mixed (one owner: unreliable and power-hungry; another got reliable sleep after his own fixes)",camera=U,audio=U,display="Works on the built-in screen; external USB-C monitor not working for two owners; brightness keys broken on one stock install",battery="Mixed (higher drain during sleep than macOS for one owner; no runtime figures given)",
  summary="Omarchy 4.5 added native support for M-series MacBooks, and several M3 MacBook Air owners posted about it on X in early November 2026. Installs went smoothly for most of them: one owner says it \u201cwent really smoothly,\u201d another says it runs well and the Mesa graphics driver works, though it lacks the polish of macOS. The two problems that came up more than once are external monitors and sleep. Two owners could not get an external monitor working over USB-C, and one owner on the 4.5 RC3 pre-release found sleep unreliable, sometimes not kicking in at all, and draining more power than macOS. A different owner says he got reliable sleep, AirDrop and AirPlay working with some AI-assisted fixes (for AirPlay he rebuilt a menu-bar plugin for ARM). A fourth owner reports that on the stock install of an M3 Air (model identifier Mac15,13) the brightness keys don't work because the display driver can't find the backlight; a custom kernel build fixes it but has to be rebuilt after every kernel update. No one in these reports said how Wi-Fi, the webcam, speakers or battery runtime compare, so those are unknown. Good for a tinkerer who mainly uses the built-in screen; check external-monitor status before relying on it.",
  reports=[("kaimi (@kaimi_local) on X, 2026-11-04","https://x.com/kaimi_local/status/2118080538627977252",
   "\u201cInstalled Omarchy 4.5 RC3 on my M3 MacBook Air today! It worked!\u2026 Sleep/suspend mode is unreliable, consumes much more power than on macOS, and sometimes doesn\u2019t kick in at all\u2026 External monitor is not working\u201d"),
   ("Karl (@ClockerMountain) on X, 2026-11-05","https://x.com/ClockerMountain/status/2118317064767017049",
   "\u201cAnd now I'm writing from my m3 macbook air. It went really smoothly.\u201d"),
   ("Omer Muneer Qazi (@omermuneer) on X, 2026-11-05","https://x.com/omermuneer/status/2118437118469124236",
   "\u201cBrightness keys don't work on the stock install (M3 Air, Mac15,13)\u2026 Your custom build fixes it, but it has to be rebuilt after every kernel update.\u201d (excerpt)"),
   ("john omar (@johnomarkid) on X, 2026-11-07","https://x.com/johnomarkid/status/2118860424376652136",
   "\u201cI got Omarchy running on my M3 Macbook Air. Everything is working except connecting to my external Dell monitor via the usb-c port.\u201d"),
   ("SC (@sierracharlie24) on X, 2026-11-07","https://x.com/sierracharlie24/status/2118881484711100681",
   "\u201cAirplay installed in the menu bar but didn't work. AI rebuilt Doubletake from x86 to arm\u2026 Now I can airplay to other macs and apple tv's\u201d (excerpt)"),
   ("SC (@sierracharlie24) on X, 2026-11-08","https://x.com/sierracharlie24/status/2119488566585860455",
   "\u201cI can confirm Omarchy running smoothly an M3 MacBook Air. And with some AI we have reliable sleep, airdrop, and airplay working.\u201d"),
   ("RGW (@RGWorldz) on X, 2026-11-09","https://x.com/RGWorldz/status/2119744344198705609",
   "\u201cOmarchy runs well on the Macbook Air M3, Mesa driver works, though it still lacks the polish and fluidity of MacOS.\u201d")]),
]
COLS=[("wifi","Wi-Fi"),("suspend","Suspend"),("camera","Camera"),("audio","Audio"),("display","Display"),("battery","Battery")]
CSS="""*{box-sizing:border-box}body{font:16px/1.5 system-ui,sans-serif;margin:0;color:#1a1a1a;background:#fafafa}
header,main,footer{max-width:960px;margin:auto;padding:1rem}header{display:flex;gap:1rem;align-items:baseline;flex-wrap:wrap}
header a{color:#333}h1 a{text-decoration:none;color:inherit}table{width:100%;border-collapse:collapse;background:#fff;font-size:.92rem}
th,td{border:1px solid #ddd;padding:.45rem;text-align:left;vertical-align:top}th{background:#f0f0f0}
.u{color:#888;font-style:italic}.ok{color:#11702f;font-weight:600}.warn{color:#9a5b00;font-weight:600}
blockquote{border-left:4px solid #ccc;margin:.5rem 0;padding:.25rem .75rem;background:#fff}
.filters{display:flex;gap:.75rem;flex-wrap:wrap;margin:.75rem 0}input,select{padding:.35rem;font:inherit}
footer{font-size:.85rem;color:#666}.buy{border:1px solid #ccc;padding:.5rem .75rem;margin:1rem 0}@media(prefers-color-scheme:dark){body{background:#121212;color:#e6e6e6}table,blockquote{background:#1d1d1d}th{background:#262626}th,td{border-color:#333}header a{color:#ccc}}"""
def cls(v): return "u" if v==U else ("ok" if v.startswith("Works") else "warn")
def cell(v): return f'<span class="{cls(v)}">{html.escape(v)}</span>'
BASE="https://maxlothorn-7.github.io/linux-laptops/"
SITE="Linux laptops: owner reports"
def clip(t,n=155):
    t=" ".join(t.split())
    if len(t)<=n: return t
    return t[:n-1].rsplit(" ",1)[0].rstrip(",;:. ")+"\u2026"
def page(title,body,depth=0,desc="Owner-reported Linux and Omarchy laptop compatibility, with sources.",path="",full_title=None):
    p="../"*depth
    ft=full_title or f"{title} \u00b7 {SITE}"
    et=html.escape(ft); ed=html.escape(desc,quote=True); eu=html.escape(BASE+path,quote=True)
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="google-site-verification" content="TjpcVWFtCRT0HTAodlyFz_t3EosdQ0vKlujXUvH4IUM" /><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{et}</title><meta name="description" content="{ed}"><link rel="canonical" href="{eu}"><meta property="og:type" content="website"><meta property="og:site_name" content="{SITE}"><meta property="og:title" content="{html.escape(ft,quote=True)}"><meta property="og:description" content="{ed}"><meta property="og:url" content="{eu}"><meta name="twitter:card" content="summary"><meta name="twitter:title" content="{html.escape(ft,quote=True)}"><meta name="twitter:description" content="{ed}"><link rel="stylesheet" href="{p}style.css"></head><body>
<header><h1><a href="{p}index.html">{SITE}</a></h1><nav><a href="{p}index.html">Table</a> \u00b7 <a href="{p}guides/index.html">Buyer guides</a> \u00b7 <a href="{p}about.html">About &amp; method</a> \u00b7 <a href="{p}submit.html">Submit a report</a></nav></header>
<main>{body}</main><footer>Every claim links to a public owner report. \u201cunknown\u201d means no report found yet, not \u201cbroken\u201d.</footer><script defer src='https://static.cloudflareinsights.com/beacon.min.js' data-cf-beacon='{{"token": "a672c8bbb0704c30b4d89dbf8ba579fe"}}'></script></body></html>"""
import json
from guides import GUIDES
DISCLOSURE="As an eBay Partner Network affiliate, I may earn a commission from qualifying purchases."
AFF={}
if os.path.exists("affiliate_links.json"):
    for s,v in json.load(open("affiliate_links.json")).items():
        u=v.get("url","")
        if u.startswith("https://") and any(u.split("/")[2].endswith(h) for h in ("ebay.com","ebay.us")): AFF[s]=v
def guidelink(d):
    g=[x for x in GUIDES if any(d["slug"].startswith(r) for r in x["related"])]
    return "".join(f'<p>See also: <a href="../guides/{x["slug"]}.html">{html.escape(x["title"])}</a></p>' for x in g)
def buybox(d):
    v=AFF.get(d["slug"])
    if not v or d["overall"].startswith("Experimental"): return ""
    return f'<div class="buy"><p><a href="{html.escape(v["url"],quote=True)}" rel="sponsored nofollow noopener">{html.escape(v.get("label","Search used listings on eBay"))}</a></p><p><small>{DISCLOSURE} We don\'t check listings; confirm the exact model and variant before buying. Affiliate links never change a compatibility status.</small></p></div>'
os.makedirs("laptops",exist_ok=True)
os.makedirs("guides",exist_ok=True)
open("style.css","w").write(CSS)
rows=""
for d in DATA:
    rows+=f'<tr data-distro="{html.escape(d["distro"].lower())}" data-text="{html.escape((d["name"]+" "+d["overall"]).lower())}"><td><a href="laptops/{d["slug"]}.html">{html.escape(d["name"])}</a></td><td>{html.escape(d["distro"])}</td><td>{cell(d["overall"])}</td>'+"".join(f"<td>{cell(d[k])}</td>" for k,_ in COLS)+f'<td>{len(d["reports"])}</td></tr>\n'
home=f"""<p>Owner reports of how specific laptops run <strong>Omarchy</strong> and other Linux setups. Each row links to its sources. Small and early: {len(DATA)} models so far, collected from owners, not tested by us. <a href="guides/index.html">Buyer guides</a>: used ThinkPads, Intel MacBooks, Surface.</p>
<div class="filters"><label>Search <input id="q" placeholder="e.g. lenovo"></label>
<label>Setup <select id="d"><option value="">All</option><option value="omarchy" selected>Omarchy (any)</option></select></label>
<label>Status <select id="s"><option value="">All</option><option value="works">Works</option><option value="experimental">Experimental</option></select></label></div>
<div style="overflow-x:auto"><table id="t"><thead><tr><th>Model</th><th>Setup</th><th>Overall</th>{"".join(f"<th>{n}</th>" for _,n in COLS)}<th>Reports</th></tr></thead><tbody>
{rows}</tbody></table></div><p id="n"></p>
<script>const q=document.getElementById('q'),d=document.getElementById('d'),s=document.getElementById('s');
function f(){{let c=0;for(const r of document.querySelectorAll('#t tbody tr')){{const ok=r.dataset.text.includes(q.value.toLowerCase())&&r.dataset.distro.includes(d.value)&&r.dataset.text.includes(s.value);r.hidden=!ok;c+=ok}}document.getElementById('n').textContent=c+' model(s) shown';}}
[q,d,s].forEach(e=>e.addEventListener('input',f));f();</script>"""
open("index.html","w").write(page("Compatibility table",home,full_title="Linux laptop compatibility table: owner reports for Omarchy and Linux",
  desc=f"Owner-reported compatibility for {len(DATA)} laptops running Omarchy and other Linux setups. Wi-Fi, suspend, audio and more, each row linked to a public source.",path=""))
for d in DATA:
    rep="".join(f'<h3><a href="{u}">{html.escape(t)}</a></h3><blockquote>{html.escape(q)}</blockquote>' for t,u,q in d["reports"])
    tbl="".join(f"<tr><th>{n}</th><td>{cell(d[k])}</td></tr>" for k,n in COLS)
    body=f"""<h2>{html.escape(d["name"])}</h2><p><strong>Setup:</strong> {html.escape(d["distro"])} · <strong>Overall:</strong> {cell(d["overall"])}</p><p>{html.escape(d["summary"])}</p>
<table>{tbl}</table>{buybox(d)}{guidelink(d)}<h2>Owner reports</h2>{rep}<p>Own this laptop? <a href="../submit.html">Add your report</a>, especially for anything marked unknown.</p>
<h2>Other laptops on the list</h2><p>"""+" \u00b7 ".join(f'<a href="{o["slug"]}.html">{html.escape(o["name"])}</a>' for o in DATA if o["slug"]!=d["slug"])+"""</p>"""
    first=d["summary"].split(". ")[0].rstrip(".")+"."
    ds="Omarchy" if d["distro"].startswith("Omarchy") else d["distro"].split(" (")[0]
    ldesc=clip(f'{d["name"]} on {ds}: {d["overall"]}. {first}')
    open(f"laptops/{d['slug']}.html","w").write(page(d["name"],body,1,desc=ldesc,path=f"laptops/{d['slug']}.html",
      full_title=f'{d["name"]} on {ds}: owner reports'))
about="""<h2>About &amp; methodology</h2><p>This site collects <em>public, first-hand owner reports</em> of how laptops run Omarchy and other Linux setups.</p>
<ul><li>Every compatibility claim links to its source. We don't test hardware ourselves (yet).</li><li>“Unknown” means nobody has reported on it yet. It doesn't mean the feature is broken.</li>
<li>Overall status follows the report: <em>Works</em>, <em>Works (minor fix)</em>, <em>Experimental</em>, or <em>Problems</em>.</li><li>Quotes are copied word for word. Reports are dated, and newer kernels and Omarchy releases can change results.</li>
<li>Corrections are welcome via the <a href="submit.html">submit page</a>.</li></ul>
<h2>Affiliate disclosure</h2><p>"+DISCLOSURE+" Some laptop pages may include an eBay link marked with this notice. Owner reports stay free to read, and affiliate links never change a compatibility status.</p>
<p>Not affiliated with Omarchy, Basecamp, or any laptop manufacturer.</p>"""
open("about.html","w").write(page("About",about,full_title="About and method: how this Linux laptop list is sourced",desc="How the list works: public first-hand owner reports only, every claim linked to its source, and unknown means nobody has reported yet.",path="about.html"))
submit="""<h2>Submit your report</h2><p>Own a laptop running Omarchy or another Linux setup? Send us:</p><ol>
<li>Exact model (and CPU/GPU variant)</li><li>Distro and version (e.g. Omarchy 3.6), kernel if known</li>
<li>For each item, say works / needed a fix / broken / not tested: Wi-Fi, Bluetooth, suspend/resume, camera, audio, internal display, external displays, battery life, fingerprint</li>
<li>Any fixes you applied</li><li>Optionally, a public link (X post, Reddit, blog) we can cite</li></ol>
<p><strong>Email:</strong> <a href="mailto:REPLACE_ME@example.com?subject=Laptop%20report">REPLACE_ME@example.com</a> (placeholder)<br><strong>GitHub issues:</strong> coming soon (placeholder)</p>
<p>We only publish what you report. Anything you don't mention stays “unknown”.</p>"""
open("submit.html","w").write(page("Submit a report",submit,full_title="Submit a Linux laptop report: what to include",desc="Own a laptop running Omarchy or another Linux setup? Here is what to send us: exact model, distro, and what works or needed a fix.",path="submit.html"))
gi="<h2>Buyer guides</h2><p>Each guide collects the owner reports for one family of laptops, with sources. We haven't tested these machines.</p><ul>"+"".join(f'<li><a href="{g["slug"]}.html">{html.escape(g["title"])}</a>: {html.escape(g["desc"])}</li>' for g in GUIDES)+"</ul>"
open("guides/index.html","w").write(page("Buyer guides",gi,1,desc="Buyer guides built from public owner reports of Omarchy on used ThinkPads, Intel MacBooks and Microsoft Surface devices.",path="guides/index.html",full_title="Buyer guides: used laptops for Omarchy, from owner reports"))
for g in GUIDES:
    open(f"guides/{g['slug']}.html","w").write(page(g["title"],g["body"],1,desc=g["desc"],path=f"guides/{g['slug']}.html",full_title=g["title"]))
print("built",len(DATA),"guides",len(GUIDES),"aff",len(AFF))

# sitemap
BASE="https://maxlothorn-7.github.io/linux-laptops/"
urls=["", "about.html", "submit.html", "guides/index.html"]+[f"guides/{g['slug']}.html" for g in GUIDES]+[f"laptops/{d['slug']}.html" for d in DATA]
open("sitemap.xml","w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+"".join(f"<url><loc>{BASE}{u}</loc></url>\n" for u in urls)+"</urlset>\n")
