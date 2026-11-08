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
BASE="https://maxlothorn-7.github.io/linux-laptops/"
SITE="Linux laptops, verified by owners"
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
<header><h1><a href="{p}index.html">{SITE}</a></h1><nav><a href="{p}index.html">Table</a> \u00b7 <a href="{p}about.html">About &amp; method</a> \u00b7 <a href="{p}submit.html">Submit a report</a></nav></header>
<main>{body}</main><footer>Every claim links to a public owner report. \u201cunknown\u201d means no report found yet, not \u201cbroken\u201d.</footer><script defer src='https://static.cloudflareinsights.com/beacon.min.js' data-cf-beacon='{{"token": "a672c8bbb0704c30b4d89dbf8ba579fe"}}'></script></body></html>"""
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
open("index.html","w").write(page("Compatibility table",home,full_title="Linux laptop compatibility table: owner reports for Omarchy and Linux",
  desc=f"Owner-reported compatibility for {len(DATA)} laptops running Omarchy and other Linux setups. Wi-Fi, suspend, audio and more, each row linked to a public source.",path=""))
for d in DATA:
    rep="".join(f'<h3><a href="{u}">{html.escape(t)}</a></h3><blockquote>{html.escape(q)}</blockquote>' for t,u,q in d["reports"])
    tbl="".join(f"<tr><th>{n}</th><td>{cell(d[k])}</td></tr>" for k,n in COLS)
    body=f"""<h2>{html.escape(d["name"])}</h2><p><strong>Setup:</strong> {html.escape(d["distro"])} · <strong>Overall:</strong> {cell(d["overall"])}</p><p>{html.escape(d["summary"])}</p>
<table>{tbl}</table><h2>Owner reports</h2>{rep}<p>Own this laptop? <a href="../submit.html">Add your report</a>, especially for anything marked unknown.</p>
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
<h2>Affiliate disclosure</h2><p><strong>[Placeholder]</strong> This site currently has no affiliate links. If we add them later (for example to laptop makers' stores), we will mark them clearly and say so here. Affiliate links will never change a compatibility status.</p>
<p>Not affiliated with Omarchy, Basecamp, or any laptop manufacturer.</p>"""
open("about.html","w").write(page("About",about,full_title="About and method: how this Linux laptop list is sourced",desc="How the list works: public first-hand owner reports only, every claim linked to its source, and unknown means nobody has reported yet.",path="about.html"))
submit="""<h2>Submit your report</h2><p>Own a laptop running Omarchy or another Linux setup? Send us:</p><ol>
<li>Exact model (and CPU/GPU variant)</li><li>Distro and version (e.g. Omarchy 3.6), kernel if known</li>
<li>For each item, say works / needed a fix / broken / not tested: Wi-Fi, Bluetooth, suspend/resume, camera, audio, internal display, external displays, battery life, fingerprint</li>
<li>Any fixes you applied</li><li>Optionally, a public link (X post, Reddit, blog) we can cite</li></ol>
<p><strong>Email:</strong> <a href="mailto:REPLACE_ME@example.com?subject=Laptop%20report">REPLACE_ME@example.com</a> (placeholder)<br><strong>GitHub issues:</strong> coming soon (placeholder)</p>
<p>We only publish what you report. Anything you don't mention stays “unknown”.</p>"""
open("submit.html","w").write(page("Submit a report",submit,full_title="Submit a Linux laptop report: what to include",desc="Own a laptop running Omarchy or another Linux setup? Here is what to send us: exact model, distro, and what works or needed a fix.",path="submit.html"))
print("built",len(DATA))

# sitemap
BASE="https://maxlothorn-7.github.io/linux-laptops/"
urls=["", "about.html", "submit.html"]+[f"laptops/{d['slug']}.html" for d in DATA]
open("sitemap.xml","w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+"".join(f"<url><loc>{BASE}{u}</loc></url>\n" for u in urls)+"</urlset>\n")
