#!/usr/bin/perl
# PLAT YONEZAWA — Trade Tariff PDF source generator (Perl port of build.py).
# Generates print_<PID>_<lang>.html (en/fr/zh) faithful to the 3-page design.
# Content source: Notion 商品タリフDB (structured properties = source of truth).
# Run:  perl build.pl     (Git Bash)   then render with render.ps1 (headless Chrome).
use strict; use warnings; use utf8;
use FindBin; use File::Spec;
binmode STDOUT, ':encoding(UTF-8)';

my $EMAIL = 'info1@plat-yonezawa.jp';

# ---------- CSS (literal heredocs: no interpolation; @page / braces safe) ----------
my $ROOT_LATIN = <<'CSS';
  --serif:'Cormorant Garamond','Times New Roman',serif;
  --ui:'Inter','Helvetica Neue',sans-serif;
  --cjk:'Cormorant Garamond',serif;
CSS

my $ROOT_ZH = <<'CSS';
  --serif:'Cormorant Garamond','Noto Serif TC','Times New Roman',serif;
  --ui:'Inter','Noto Serif TC','Helvetica Neue',sans-serif;
  --cjk:'Noto Serif TC',serif;
CSS

my $CSS_BODY = <<'CSS';
  --ink:#2a2622; --soft:#5b534c; --muted:#9a9289; --faint:#c9c1b6;
  --gold:#a8893a; --gold-deep:#6b5418; --accent:#9f3f2f;
  --line:#e4ddd1; --paper:#ffffff;
}
*{box-sizing:border-box;margin:0;padding:0;}
@page{ size:A4; margin:0; }
html,body{ background:#fff; color:var(--ink); font-family:var(--serif); -webkit-print-color-adjust:exact; print-color-adjust:exact; }
.page{ position:relative; width:210mm; height:297mm; padding:18mm 22mm 16mm; overflow:hidden;
  page-break-after:always; display:flex; flex-direction:column; background:var(--paper); }
.page:last-child{ page-break-after:auto; }
.rh{ display:flex; justify-content:space-between; align-items:flex-end; font-family:var(--ui);
  font-size:7.5pt; letter-spacing:.28em; color:var(--muted); text-transform:uppercase;
  padding-bottom:7px; border-bottom:1px solid var(--line); }
.rh .l{ color:var(--ink); letter-spacing:.34em; }
.rf{ position:absolute; left:22mm; right:22mm; bottom:14mm; display:flex; justify-content:space-between;
  align-items:center; font-family:var(--ui); font-size:7.5pt; letter-spacing:.24em; color:var(--muted);
  text-transform:uppercase; padding-top:8px; border-top:1px solid var(--line); }
.rf .num{ font-family:var(--serif); font-style:italic; font-size:10pt; letter-spacing:.05em; color:var(--gold); }
.eyebrow{ font-family:var(--ui); font-size:8.5pt; letter-spacing:.30em; text-transform:uppercase; color:var(--gold); }
.eyebrow.dim{ color:var(--muted); letter-spacing:.28em; }
.vrule{ width:1px; height:34px; background:var(--gold); opacity:.8; margin:18px auto; }
.cover-inner{ flex:1; display:flex; flex-direction:column; }
.cover .hero{ width:100%; height:88mm; background-size:cover; background-position:center; border-radius:2px; }
.cover .meta{ text-align:center; margin-top:auto; margin-bottom:auto; }
.cover .coll{ margin-bottom:6px; }
.cover .brandline{ font-family:var(--ui); font-size:8.5pt; letter-spacing:.28em; text-transform:uppercase; color:var(--muted); }
.cover h1{ font-family:var(--serif); font-weight:500; font-size:46pt; line-height:1.04; letter-spacing:.01em; }
.cover .sub{ font-size:17pt; color:var(--soft); margin-top:6px; }
.cover .tag{ font-size:13pt; color:var(--ink); max-width:128mm; margin:0 auto; line-height:1.55; }
.cover .host{ font-family:var(--ui); font-size:8.5pt; letter-spacing:.20em; text-transform:uppercase; color:var(--muted); margin-top:26px; }
.exp-grid{ flex:1; display:grid; grid-template-columns:64mm 1fr; gap:14mm; margin-top:14mm; }
.exp-grid .imgcol{ background-size:cover; background-position:center; border-radius:2px; min-height:150mm; }
.exp .lead{ font-size:13.5pt; line-height:1.62; color:var(--ink); margin-top:14px; }
.exp .div{ width:54px; height:1px; background:var(--faint); margin:26px 0 20px; }
.prog{ margin-top:6px; }
.prog .row{ display:grid; grid-template-columns:26mm 1fr; gap:10px; padding:9px 0; border-bottom:1px solid var(--line); align-items:baseline; }
.prog .row:last-child{ border-bottom:none; }
.prog .t{ font-family:var(--serif); font-style:italic; font-size:11.5pt; color:var(--gold-deep); white-space:nowrap; }
.prog .d{ font-size:11pt; line-height:1.4; color:var(--soft); }
.terms{ flex:1; display:flex; flex-direction:column; }
.terms .topimg{ width:100%; height:74mm; background-size:cover; background-position:center; border-radius:2px; }
.terms .price-wrap{ text-align:center; margin:22px 0 8px; }
.terms .price{ font-family:var(--serif); font-size:40pt; font-weight:500; letter-spacing:.01em; }
.terms .price-sub{ font-size:11.5pt; color:var(--soft); margin-top:4px; }
.terms .appt{ font-size:11pt; color:var(--accent); margin-top:10px; }
.terms .hr{ width:60%; height:1px; background:var(--line); margin:20px auto; }
.spec{ display:grid; grid-template-columns:1fr 1fr; gap:14px 24px; max-width:152mm; margin:0 auto; }
.spec .cell .l{ font-family:var(--ui); font-size:8pt; letter-spacing:.22em; text-transform:uppercase; color:var(--muted); }
.spec .cell .v{ font-size:12.5pt; color:var(--ink); margin-top:3px; }
.incl{ text-align:center; margin-top:24px; }
.incl .h{ font-family:var(--ui); font-size:8.5pt; letter-spacing:.28em; text-transform:uppercase; color:var(--gold); }
.incl ul{ list-style:none; margin-top:12px; }
.incl li{ font-size:11.5pt; color:var(--soft); line-height:1.9; }
.terms .enq{ text-align:center; margin-top:auto; margin-bottom:12mm; }
.terms .enq .note{ font-size:11pt; color:var(--muted); }
.terms .enq .mail{ font-weight:600; font-size:13.5pt; color:var(--ink); margin-top:6px; }
CSS

my $CSS_ZH_OVERRIDES = <<'CSS';
.cover .sub,.cover .tag,.cover .host,.exp .lead,.prog .d,.terms .price-sub,
.terms .appt,.spec .cell .v,.incl li,.terms .enq .note{ font-family:var(--cjk); font-style:normal; }
.exp .lead{ line-height:1.95; }
.incl li{ line-height:2.0; }
.cover .tag{ line-height:1.7; }
CSS

my $FONT_LATIN = q{<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&family=Inter:wght@300;400;500&display=swap" rel="stylesheet">};
my $FONT_ZH    = q{<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&family=Noto+Serif+TC:wght@400;500;600&family=Inter:wght@300;400;500&display=swap" rel="stylesheet">};

sub css {
    my ($lang) = @_;
    my $root = $lang eq 'zh' ? $ROOT_ZH : $ROOT_LATIN;
    my $out = ":root{" . $root . $CSS_BODY;
    $out .= $CSS_ZH_OVERRIDES if $lang eq 'zh';
    return $out;
}

# ---------- labels ----------
my %LABELS = (
  en => { attr=>'en',      exp=>q{II · The Experience}, prog=>q{Programme}, terms=>q{III · Terms},
          dur=>q{Duration}, cap=>q{Capacity}, langs=>q{Languages}, venue=>q{Venue}, incl=>q{What is included} },
  fr => { attr=>'fr',      exp=>q{II · L'Expérience},   prog=>q{Programme}, terms=>q{III · Modalités},
          dur=>q{Durée},    cap=>q{Capacité}, langs=>q{Langues}, venue=>q{Lieu}, incl=>q{Ce qui est inclus} },
  zh => { attr=>'zh-Hant', exp=>q{II · 體驗},           prog=>q{流程},     terms=>q{III · 條款},
          dur=>q{時長},     cap=>q{人數},     langs=>q{語言},     venue=>q{地點}, incl=>q{費用包含} },
);
my %ZH_SERIES = ( I=>q{第一系列}, II=>q{第二系列}, III=>q{第三系列} );
sub coll_label { my ($lang,$r)=@_; my $b="Collection ".$r; return $lang eq 'zh' ? $ZH_SERIES{$r}." · ".$b : $b; }

# ---------- DATA (商品タリフDB) ----------
my %DATA;

$DATA{'C-NTA-01'} = {
  roman=>'I', brand=>q{The Colors of the Snow Country}, title=>q{The Philosophy},
  img=>['shot-01','shot-02','shot-06'], minutes=>{en=>q{120 minutes},fr=>q{120 minutes},zh=>q{120 分鐘}}, price=>q{JPY 33,000},
  en=>{ subtitle=>q{Weaving the Breath of Nature},
    tagline=>q{An exclusive afternoon with the master of a 140-year-old silk house.},
    host=>q{Hosted by Nitta Textile Arts Inc. — Est. 1884},
    prose=>q{In Yonezawa, seasons are not four, but twenty-four. While the modern world rushes by, the Nitta family has spent generations capturing the subtle breath of nature. This exclusive session opens the family’s private residence, hosted by Chairman Nitta and his family. Witness the alchemy of natural dyeing — silk dyed with Japan red (safflower) — and the craftsmanship behind colours that have defined Yonezawa for generations. Through a tea ritual, dialogue, and a hands-on dyeing experience, you touch the essence of careful living.},
    prog=>[['2:00 p.m',q{Welcome &amp; the ritual — matcha &amp; wagashi service in the private welcome space.}],
           ['2:45 p.m',q{The crafting session (atelier) — dyeing the silk scarf with Japan red (safflower).}],
           ['3:25 p.m',q{The factory walk — a guided walkthrough of the production floor with the Chairman.}],
           ['3:50 p.m',q{Unveiling — presentation of your finished silk scarf.}],
           ['4:00 p.m',q{End of tour.}]],
    price_sub=>q{per person · inclusive of consumption tax}, appt=>q{By appointment only · minimum two guests},
    dur=>q{2 hours · 120 minutes}, cap=>q{2 — 8 guests}, langs=>q{English · French},
    venue=>q{Nitta Textile Atelier · Yonezawa, Yamagata},
    incl=>[q{Full attendance by Chairman Nitta and his family},q{Silk scarf dyed with Japan red (safflower), to take home},q{Matcha and seasonal confectionery},q{Exclusive access to the atelier},q{Comprehensive insurance}],
    enq=>q{To enquire about availability, net rates, or familiarisation visits.} },
  fr=>{ subtitle=>q{Tisser le souffle de la nature},
    tagline=>q{Un après-midi privilégié auprès du maître d’une maison de soie de 140 ans.},
    host=>q{Sur l’invitation de Nitta Textile Arts Inc. — Fondée en 1884},
    prose=>q{À Yonezawa, les saisons ne sont pas quatre, mais vingt-quatre. Tandis que le monde moderne s’emballe, la famille Nitta capture depuis des générations le souffle subtil de la nature. Cette séance exclusive ouvre la résidence privée de la famille, reçue par le président Nitta et les siens. Assistez à l’alchimie de la teinture naturelle — la soie teinte au rouge du Japon (carthame) — et au savoir-faire derrière les couleurs qui définissent Yonezawa depuis des générations. À travers un rituel du thé, le dialogue et une expérience de teinture à la main, vous touchez l’essence d’une vie attentive.},
    prog=>[['2:00 p.m',q{Accueil &amp; rituel — service de matcha et de wagashi dans l’espace d’accueil privé.}],
           ['2:45 p.m',q{La séance de teinture (atelier) — teinture de l’écharpe de soie au rouge du Japon (carthame).}],
           ['3:25 p.m',q{La visite de la fabrique — parcours guidé de l’atelier de production avec le président.}],
           ['3:50 p.m',q{Dévoilement — présentation de votre écharpe de soie achevée.}],
           ['4:00 p.m',q{Fin de la visite.}]],
    price_sub=>q{par personne · taxe à la consommation incluse}, appt=>q{Sur rendez-vous uniquement · minimum deux personnes},
    dur=>q{2 heures · 120 minutes}, cap=>q{2 — 8 personnes}, langs=>q{Anglais · Français},
    venue=>q{Nitta Textile Atelier · Yonezawa, Yamagata},
    incl=>[q{Présence complète du président Nitta et de sa famille},q{Écharpe de soie teinte au rouge du Japon (carthame), à emporter},q{Matcha et confiseries de saison},q{Accès exclusif à l’atelier},q{Assurance complète}],
    enq=>q{Pour toute demande de disponibilité, de tarifs nets ou de visites de familiarisation.} },
  zh=>{ subtitle=>q{織就自然的氣息},
    tagline=>q{與擁有 140 年歷史的絲織世家主人共度的專屬午後。},
    host=>q{由 NITTA TEXTILE ARTS INC. 主理 — 創立於 1884 年},
    prose=>q{在米澤，季節並非四季，而是二十四節氣。當現代世界匆匆前行，新田家數代以來始終捕捉著自然細微的氣息。這場專屬體驗將開啟新田家的私人宅邸，由會長新田先生及其家族親自接待。親眼見證天然染色的鍊金術——以日本紅（紅花）染製的絲綢——以及數代守護、定義米澤色彩的職人技藝。透過茶之儀、對話與親手染製的體驗，您將觸及「用心生活」的本質。},
    prog=>[['2:00 p.m',q{迎賓與茶之儀——於私人迎賓空間奉上抹茶與和菓子。}],
           ['2:45 p.m',q{染製環節（工坊）——以日本紅（紅花）染製絲巾。}],
           ['3:25 p.m',q{工坊參觀——由會長親自引領參觀製造現場。}],
           ['3:50 p.m',q{揭曉——呈獻您完成的絲巾。}],
           ['4:00 p.m',q{行程結束。}]],
    price_sub=>q{每位 · 含消費稅}, appt=>q{僅限預約 · 最少兩位},
    dur=>q{2 小時 · 120 分鐘}, cap=>q{2 — 8 位}, langs=>q{英語 · 法語},
    venue=>q{新田織物工坊 · 山形縣米澤},
    incl=>[q{會長新田先生及其家族全程接待},q{以日本紅（紅花）染製的絲巾，可帶回家},q{抹茶與當季點心},q{工坊專屬參觀},q{完整保險}],
    enq=>q{如需查詢檔期、淨價或考察行程，敬請與我們聯繫。} },
};

$DATA{'S-TKO-01'} = {
  roman=>'II', brand=>q{The Soul of the Snow Country}, title=>q{The Legacy &amp; The Master},
  img=>['shot-01','shot-03','shot-06'], minutes=>{en=>q{120–150 minutes},fr=>q{120–150 minutes},zh=>q{120–150 分鐘}}, price=>q{JPY 33,000},
  en=>{ subtitle=>q{A Private Dialogue with the Brewer},
    tagline=>q{A private audience with the 24th-generation master of a four-century sake house.},
    host=>q{Hosted by Toko Brewery (Kojima Sohonten) — four centuries of brewing},
    prose=>q{In Yonezawa, sake brewing is the heartbeat of the community. This is the ultimate sake experience — a private audience with the brewery owner. Just as one might visit a historic Champagne maison to converse with its owner, you explore the brewing museum with the current Chairman, “Yazaemon Kojima,” the 24th-generation head of the house. Hear the history of brewing and the spiritual tales of the storehouse — the branch shrine of “Omiwa Myojin” and the legend of the “Daikoku-sama in a yellow kimono.” The experience culminates in an exclusive lunch at the historic “Jodan-no-Ma” (the Upper Room), usually reserved for dignitaries, featuring local Yonezawa cuisine prepared by the chairman’s family and paired with the finest brews.},
    prog=>[['11:00 a.m',q{Arrival at the Toko Brewing Museum.}],
           ['11:10 a.m',q{[Private tour] Walking the brewing museum and historical areas with the Chairman and his family — the bond between brewery, community, and the spirits.}],
           ['0:00 p.m',q{[Gastronomy] Special pairing lunch at the “Jodan-no-Ma” — cuisine prepared by the chairman’s family, with deep conversation with the host.}],
           ['1:30 p.m',q{End of tour.}]],
    price_sub=>q{per person · inclusive of consumption tax}, appt=>q{By appointment only · minimum two guests · ages 20+},
    dur=>q{2–2.5 hours · 120–150 minutes}, cap=>q{2 — 8 guests}, langs=>q{English · French},
    venue=>q{Toko Brewery · Yonezawa, Yamagata},
    incl=>[q{Private guide by the Chairman},q{Special lunch course by the chairman’s family},q{Premium sake pairing},q{Private room charge}],
    enq=>q{To enquire about availability, net rates, or familiarisation visits.} },
  fr=>{ subtitle=>q{Un dialogue privé avec le maître brasseur},
    tagline=>q{Une audience privée avec le maître de la 24ᵉ génération d’une maison de saké de quatre siècles.},
    host=>q{Sur l’invitation de Toko Brewery (Kojima Sohonten) — quatre siècles de brassage},
    prose=>q{À Yonezawa, le brassage du saké est le cœur battant de la communauté. Voici l’expérience ultime du saké — une audience privée avec le propriétaire de la brasserie. Comme on visiterait une maison de Champagne historique pour s’entretenir avec son propriétaire, vous explorez le musée du brassage avec l’actuel président, « Yazaemon Kojima », chef de la maison à la 24ᵉ génération. Découvrez l’histoire du brassage et les récits spirituels de la maison — le sanctuaire d’« Omiwa Myojin » et la légende du « Daikoku-sama au kimono jaune ». L’expérience s’achève par un déjeuner exclusif dans la salle historique « Jodan-no-Ma » (la salle haute), habituellement réservée aux dignitaires, mettant à l’honneur la cuisine de Yonezawa préparée par la famille du président et accordée aux meilleurs crus.},
    prog=>[['11:00 a.m',q{Arrivée au musée du brassage Toko.}],
           ['11:10 a.m',q{[Visite privée] Parcours du musée du brassage et des espaces historiques avec le président et sa famille — le lien entre la brasserie, la communauté et les divinités.}],
           ['0:00 p.m',q{[Gastronomie] Déjeuner d’accords au « Jodan-no-Ma » — cuisine préparée par la famille du président, ponctuée d’un échange privilégié avec l’hôte.}],
           ['1:30 p.m',q{Fin de la visite.}]],
    price_sub=>q{par personne · taxe à la consommation incluse}, appt=>q{Sur rendez-vous · minimum deux personnes · 20 ans et plus},
    dur=>q{2–2,5 heures · 120–150 minutes}, cap=>q{2 — 8 personnes}, langs=>q{Anglais · Français},
    venue=>q{Toko Brewery · Yonezawa, Yamagata},
    incl=>[q{Visite privée guidée par le président},q{Déjeuner spécial préparé par la famille du président},q{Accord avec des sakés premium},q{Frais de salon privé}],
    enq=>q{Pour toute demande de disponibilité, de tarifs nets ou de visites de familiarisation.} },
  zh=>{ subtitle=>q{與杜氏的私密對話},
    tagline=>q{與傳承二十四代、歷經四百年的酒造當主的私密會面。},
    host=>q{由 TOKO BREWERY（小嶋總本店）主理 — 四百餘年釀造},
    prose=>q{在米澤，釀酒是社群躍動的心跳。這是極致的清酒體驗——與酒造當主的私密會面。一如造訪歷史悠久的香檳莊園與莊主對談，您將與現任會長「弥左衛門 小嶋」（藏元第二十四代）一同走訪酒造博物館。聆聽釀造的歷史，以及酒藏的靈性傳說——酒神「大神大明神」的分社，與「身著黃衣的大黑天」的傳奇。體驗最終於歷史悠久、平日僅接待貴賓的「上段之間」迎來尊榮午宴，由當主家族親手烹製的米澤在地料理，佐以頂級銘酒。},
    prog=>[['11:00 a.m',q{抵達東光酒造博物館。}],
           ['11:10 a.m',q{〔私人導覽〕由會長與其家族引領參觀酒造博物館與歷史區域——酒藏、社群與神祇之間的羈絆。}],
           ['0:00 p.m',q{〔餐饗〕於「上段之間」享用搭配午宴——當主家族親製，並與主人深入對談。}],
           ['1:30 p.m',q{行程結束。}]],
    price_sub=>q{每位 · 含消費稅}, appt=>q{僅限預約 · 最少兩位 · 限 20 歲以上},
    dur=>q{2–2.5 小時 · 120–150 分鐘}, cap=>q{2 — 8 位}, langs=>q{英語 · 法語},
    venue=>q{東光酒造 · 山形縣米澤},
    incl=>[q{由當主親自導覽},q{當主家族手製的特別午宴},q{頂級日本酒搭配},q{私人包廂費用}],
    enq=>q{如需查詢檔期、淨價或考察行程，敬請與我們聯繫。} },
};

$DATA{'O-STY-01'} = {
  roman=>'III', brand=>q{The Other Side of the Mountain}, title=>q{Gastronomy with Magari},
  img=>['shot-01','shot-03','shot-06'], minutes=>{en=>q{150 minutes},fr=>q{150 minutes},zh=>q{150 分鐘}}, price=>q{JPY 15,000},
  en=>{ subtitle=>q{An Italian Table in the Living Forest},
    tagline=>q{An Italian table set in a living Satoyama forest, read through the 24 solar terms.},
    host=>q{Hosted by Satoyama Sommelier × Yamazato Magari},
    prose=>q{Begin with a guided walk through a private Satoyama forest, read through the lens of the 24 solar terms. Then Florence-trained Chef Takahiro Takasu of Yamazato Magari brings his kitchen into the forest for an exclusive collaboration with Satoyama Sommelier Mika Kuroda. Drawing on the “Katemono” philosophy and Yonezawa’s seasonal harvest, each course is paired by the resident sommelier with Italian and Yamagata wines — a single journey, from walking the forest to tasting its bounty.},
    prog=>[['11:00 a.m',q{Meet at JR Yonezawa Station (taxi transfer) or direct arrival.}],
           ['11:30 a.m',q{[Nature] “24 solar terms” forest walk (approx. 60 min).}],
           ['0:30 p.m',q{[Lunch] “Katemono × Magari” Italian full course with sommelier wine pairing.}],
           ['1:30 p.m',q{Relaxing time.}],
           ['1:50 p.m',q{End of tour.}]],
    price_sub=>q{per person · inclusive of consumption tax}, appt=>q{By appointment only · minimum 15 guests · ages 20+},
    dur=>q{2.5 hours · 150 minutes}, cap=>q{15 — 40 guests}, langs=>q{English · French},
    venue=>q{Private Satoyama · Yonezawa, Yamagata},
    incl=>[q{Private venue access},q{Host &amp; guide fee},q{Forest walking tour},q{Chef out-catering},q{Full Italian course meal},q{Sommelier wine pairing},q{Comprehensive insurance}],
    enq=>q{To enquire about availability, net rates, or familiarisation visits.} },
  fr=>{ subtitle=>q{Une table italienne dans la forêt vivante},
    tagline=>q{Une table italienne dressée dans une forêt satoyama vivante, au rythme des 24 micro-saisons.},
    host=>q{Sur l’invitation de Satoyama Sommelier × Yamazato Magari},
    prose=>q{Commencez par une promenade guidée dans une forêt satoyama privée, lue à travers le prisme des 24 micro-saisons. Puis le chef Takahiro Takasu, formé à Florence, du Yamazato Magari installe sa cuisine en forêt pour une collaboration exclusive avec la sommelière du satoyama, Mika Kuroda. Inspiré de la philosophie « Katemono » et des récoltes de saison de Yonezawa, chaque plat est accordé par le sommelier maison à des vins italiens et de Yamagata — un même voyage, de la marche en forêt à la dégustation de ses fruits.},
    prog=>[['11:00 a.m',q{Rendez-vous à la gare JR de Yonezawa (transfert en taxi) ou arrivée directe.}],
           ['11:30 a.m',q{[Nature] Promenade en forêt « 24 micro-saisons » (env. 60 min).}],
           ['0:30 p.m',q{[Déjeuner] Menu italien complet « Katemono × Magari », accords mets-vins du sommelier.}],
           ['1:30 p.m',q{Temps de détente.}],
           ['1:50 p.m',q{Fin de la visite.}]],
    price_sub=>q{par personne · taxe à la consommation incluse}, appt=>q{Sur rendez-vous · minimum 15 personnes · 20 ans et plus},
    dur=>q{2,5 heures · 150 minutes}, cap=>q{15 — 40 personnes}, langs=>q{Anglais · Français},
    venue=>q{Satoyama privé · Yonezawa, Yamagata},
    incl=>[q{Accès privatif au site},q{Honoraires d’hôte et de guide},q{Promenade en forêt guidée},q{Traiteur du chef sur place},q{Menu italien complet},q{Accord mets-vins par le sommelier},q{Assurance complète}],
    enq=>q{Pour toute demande de disponibilité, de tarifs nets ou de visites de familiarisation.} },
  zh=>{ subtitle=>q{活森林中的義式餐桌},
    tagline=>q{在生機盎然的里山森林中，依循二十四節氣而設的義式餐桌。},
    host=>q{由 Satoyama Sommelier × Yamazato Magari 主理},
    prose=>q{首先在私人里山森林中展開導覽散策，以二十四節氣的視角閱讀自然。隨後，曾於佛羅倫斯研修的「山里まがり」主廚高須崇大將廚房帶進森林，與里山侍酒師 Mika Kuroda（三佳）展開專屬聯名。以「かてもの」哲學與米澤當季食材為靈感，每道菜餚皆由駐店侍酒師搭配義大利與山形葡萄酒——從漫步森林到品味其恩澤，一氣呵成的旅程。},
    prog=>[['11:00 a.m',q{於 JR 米澤站集合（計程車接駁）或現地直接抵達。}],
           ['11:30 a.m',q{〔自然〕「二十四節氣」森林散策（約 60 分鐘）。}],
           ['0:30 p.m',q{〔午宴〕「かてもの × Magari」義式全套餐，佐侍酒師選酒搭配。}],
           ['1:30 p.m',q{悠閒時光。}],
           ['1:50 p.m',q{行程結束。}]],
    price_sub=>q{每位 · 含消費稅}, appt=>q{僅限預約 · 最少 15 位 · 限 20 歲以上},
    dur=>q{2.5 小時 · 150 分鐘}, cap=>q{15 — 40 位}, langs=>q{英語 · 法語},
    venue=>q{私人里山 · 山形縣米澤},
    incl=>[q{場地專屬使用},q{主持與導覽費},q{森林散策導覽},q{主廚到場外燴},q{完整義式套餐},q{侍酒師選酒搭配},q{完整保險}],
    enq=>q{如需查詢檔期、淨價或考察行程，敬請與我們聯繫。} },
};

$DATA{'O-STY-02'} = {
  roman=>'III', brand=>q{The Other Side of the Mountain}, title=>q{Katemono Afternoon Tea},
  img=>['shot-01','shot-03','shot-06'], minutes=>{en=>q{120 minutes},fr=>q{120 minutes},zh=>q{120 分鐘}}, price=>q{JPY 12,000},
  en=>{ subtitle=>q{An Afternoon of Wild Wisdom},
    tagline=>q{An afternoon of wild Yonezawa wisdom, served as a Katemono tea.},
    host=>q{Hosted by Satoyama Sommelier — Mika Kuroda},
    prose=>q{A relaxed afternoon hosted by Satoyama Sommelier Mika Kuroda. The wild food wisdom of Yonezawa — foraged plants, nuts, and fermented preserves — is reimagined as a “Katemono Afternoon Tea”: a tiered stand of sweet and savoury small plates paired with herbal and Japanese teas. In a quiet reception room, guests touch the Japanese aesthetic of “Ma” (negative space) while Mika shares stories of the half-samurai, half-farmer life and the 24 solar terms. A lighter, shorter counterpart to the full-course lunch.},
    prog=>[['2:00 p.m',q{Meet at the Satoyama entrance / reception room.}],
           ['2:15 p.m',q{[Tea] “Katemono” afternoon tea — a tiered stand of sweet &amp; savoury plates with tea / herbal pairing and the host’s narration.}],
           ['3:30 p.m',q{Short forest stroll or relaxing time (optional).}],
           ['4:00 p.m',q{End of experience.}]],
    price_sub=>q{per person · inclusive of consumption tax}, appt=>q{By appointment only · from 1 guest (minimum charge applies)},
    dur=>q{2 hours · 120 minutes}, cap=>q{1 — 20 guests}, langs=>q{English · French},
    venue=>q{Private Satoyama · Yonezawa, Yamagata},
    incl=>[q{Private venue access},q{Host fee (Mika Kuroda)},q{Katemono tea set},q{Drinks},q{Comprehensive insurance}],
    enq=>q{To enquire about availability, net rates, or familiarisation visits.} },
  fr=>{ subtitle=>q{Un après-midi de sagesse sauvage},
    tagline=>q{Un après-midi de sagesse sauvage de Yonezawa, servi en thé Katemono.},
    host=>q{Sur l’invitation de la Satoyama Sommelier — Mika Kuroda},
    prose=>q{Un après-midi détendu en compagnie de la sommelière du satoyama, Mika Kuroda. La sagesse alimentaire sauvage de Yonezawa — plantes cueillies, noix et conserves fermentées — est réinventée en un « thé de l’après-midi Katemono » : un présentoir à étages de petites assiettes sucrées et salées, accordées à des thés japonais et infusions. Dans un salon paisible, les hôtes effleurent l’esthétique japonaise du « Ma » (l’espace vide) tandis que Mika partage les récits de la vie mi-samouraï, mi-paysanne et des 24 micro-saisons. Une version plus légère et plus courte du déjeuner gastronomique.},
    prog=>[['2:00 p.m',q{Accueil à l’entrée du satoyama / salon de réception.}],
           ['2:15 p.m',q{[Thé] Thé de l’après-midi « Katemono » — présentoir à étages d’assiettes sucrées et salées, accords thé / infusions et récit de l’hôte.}],
           ['3:30 p.m',q{Courte promenade en forêt ou temps libre (facultatif).}],
           ['4:00 p.m',q{Fin de l’expérience.}]],
    price_sub=>q{par personne · taxe à la consommation incluse}, appt=>q{Sur rendez-vous · à partir d’1 personne (forfait minimum)},
    dur=>q{2 heures · 120 minutes}, cap=>q{1 — 20 personnes}, langs=>q{Anglais · Français},
    venue=>q{Satoyama privé · Yonezawa, Yamagata},
    incl=>[q{Accès privatif au site},q{Honoraires d’hôte (Mika Kuroda)},q{Service de thé Katemono},q{Boissons},q{Assurance complète}],
    enq=>q{Pour toute demande de disponibilité, de tarifs nets ou de visites de familiarisation.} },
  zh=>{ subtitle=>q{野之智慧的午後},
    tagline=>q{以「かてもの」茶席呈現的米澤野生智慧午後。},
    host=>q{由 Satoyama Sommelier — Mika Kuroda 主理},
    prose=>q{由里山侍酒師 Mika Kuroda（三佳）主持的悠閒午後。米澤的野生飲食智慧——採集的野草、堅果與發酵保存食——被重新詮釋為「かてもの下午茶」：層層疊起的鹹甜小點，佐以日本茶與花草茶。在靜謐的迎賓室裡，賓客在三佳娓娓道來半士半農的生活與二十四節氣之際，觸碰日本「間」（留白）的美學。這是全套午宴之外，更輕盈、更簡短的姊妹體驗。},
    prog=>[['2:00 p.m',q{於里山入口／迎賓室集合。}],
           ['2:15 p.m',q{〔茶席〕「かてもの」下午茶——層疊的鹹甜小點，佐日本茶／花草茶與主人解說。}],
           ['3:30 p.m',q{短暫森林散步或自由時光（任選）。}],
           ['4:00 p.m',q{體驗結束。}]],
    price_sub=>q{每位 · 含消費稅}, appt=>q{僅限預約 · 1 位起（適用最低消費）},
    dur=>q{2 小時 · 120 分鐘}, cap=>q{1 — 20 位}, langs=>q{英語 · 法語},
    venue=>q{私人里山 · 山形縣米澤},
    incl=>[q{場地專屬使用},q{主持費（Mika Kuroda）},q{かてもの茶席},q{飲品},q{完整保險}],
    enq=>q{如需查詢檔期、淨價或考察行程，敬請與我們聯繫。} },
};

$DATA{'O-STY-03'} = {
  roman=>'III', brand=>q{The Other Side of the Mountain}, title=>q{Forest Bathing with Mika},
  img=>['shot-01','shot-03','shot-06'], minutes=>{en=>q{120 minutes},fr=>q{120 minutes},zh=>q{120 分鐘}}, price=>q{JPY 5,000},
  en=>{ subtitle=>q{A Forest Immersion with the Satoyama Sommelier},
    tagline=>q{A two-hour forest immersion with the Satoyama Sommelier.},
    host=>q{Hosted by Satoyama Sommelier — Mika Kuroda},
    prose=>q{A two-hour guided forest immersion led by Mika Kuroda — Satoyama Sommelier, NHK World contributor, and author of “Mori to Katemono” (The Forest and Katemono). Mika lives in the very Satoyama forest where samurai-farmers once cultivated the land in the spirit of han-shi han-no. Walk among the 24 solar terms through the eyes of someone who has spent years rediscovering the wild food wisdom of Yonezawa — the most accessible way to enter “The Other Side of the Mountain.”},
    prog=>[['2:00 p.m',q{Meet at the Satoyama entrance.}],
           ['2:10 p.m',q{[Forest walk] Guided immersion with Mika Kuroda — seasonal signs, wild plants, and the philosophy of “Teire” (care). Approx. 2 hours.}],
           ['4:00 p.m',q{End of experience.}]],
    price_sub=>q{per person · inclusive of consumption tax}, appt=>q{By appointment only · from 1 guest},
    dur=>q{2 hours · 120 minutes}, cap=>q{From 1 guest}, langs=>q{English · French},
    venue=>q{Private Satoyama · Yonezawa, Yamagata},
    incl=>[q{Host &amp; guide fee (Mika Kuroda)},q{Forest walking tour},q{Comprehensive insurance}],
    enq=>q{To enquire about availability, net rates, or familiarisation visits.} },
  fr=>{ subtitle=>q{Une immersion forestière avec la sommelière du satoyama},
    tagline=>q{Une immersion forestière de deux heures avec la sommelière du satoyama.},
    host=>q{Sur l’invitation de la Satoyama Sommelier — Mika Kuroda},
    prose=>q{Une immersion forestière guidée de deux heures, menée par Mika Kuroda — sommelière du satoyama, intervenante sur NHK World et autrice de « Mori to Katemono » (La forêt et le Katemono). Mika vit dans cette forêt satoyama même où les samouraïs-paysans cultivaient jadis la terre dans l’esprit du han-shi han-no. Marchez au fil des 24 micro-saisons à travers le regard de celle qui a passé des années à redécouvrir la sagesse alimentaire sauvage de Yonezawa — la manière la plus accessible d’entrer dans « L’Autre Versant de la Montagne ».},
    prog=>[['2:00 p.m',q{Accueil à l’entrée du satoyama.}],
           ['2:10 p.m',q{[Marche en forêt] Immersion guidée avec Mika Kuroda — signes de saison, plantes sauvages et philosophie du « Teire » (le soin). Env. 2 heures.}],
           ['4:00 p.m',q{Fin de l’expérience.}]],
    price_sub=>q{par personne · taxe à la consommation incluse}, appt=>q{Sur rendez-vous · à partir d’1 personne},
    dur=>q{2 heures · 120 minutes}, cap=>q{À partir d’1 personne}, langs=>q{Anglais · Français},
    venue=>q{Satoyama privé · Yonezawa, Yamagata},
    incl=>[q{Honoraires d’hôte et de guide (Mika Kuroda)},q{Promenade en forêt guidée},q{Assurance complète}],
    enq=>q{Pour toute demande de disponibilité, de tarifs nets ou de visites de familiarisation.} },
  zh=>{ subtitle=>q{與里山侍酒師的森林沉浸},
    tagline=>q{與里山侍酒師共度的兩小時森林沉浸。},
    host=>q{由 Satoyama Sommelier — Mika Kuroda 主理},
    prose=>q{由 Mika Kuroda（三佳）親自帶領的兩小時森林沉浸——她是里山侍酒師、NHK World 的出演者，也是《森與かてもの》的作者。三佳就居住在這片里山森林，昔日武士曾以「半士半農」的精神在此耕作。透過一位多年來不斷重新發掘米澤野生飲食智慧者的眼睛，漫步於二十四節氣之間——這是進入「山的另一側」最平易近人的方式。},
    prog=>[['2:00 p.m',q{於里山入口集合。}],
           ['2:10 p.m',q{〔森林散策〕由 Mika Kuroda（三佳）帶領的沉浸導覽——季節徵兆、野生植物，以及「手入れ」（照料）的哲學。約 2 小時。}],
           ['4:00 p.m',q{體驗結束。}]],
    price_sub=>q{每位 · 含消費稅}, appt=>q{僅限預約 · 1 位起},
    dur=>q{2 小時 · 120 分鐘}, cap=>q{1 位起}, langs=>q{英語 · 法語},
    venue=>q{私人里山 · 山形縣米澤},
    incl=>[q{主持與導覽費（Mika Kuroda）},q{森林散策導覽},q{完整保險}],
    enq=>q{如需查詢檔期、淨價或考察行程，敬請與我們聯繫。} },
};

# ---------- render ----------
my @ORDER = ('C-NTA-01','S-TKO-01','O-STY-01','O-STY-02','O-STY-03');

sub render {
    my ($pid,$lang)=@_;
    my $d=$DATA{$pid}; my $c=$d->{$lang}; my $L=$LABELS{$lang};
    my $pl=lc $pid; my $idir="../images/".$pl;
    my $cover=$idir."/".$d->{img}[0].".jpg";
    my $eimg =$idir."/".$d->{img}[1].".jpg";
    my $timg =$idir."/".$d->{img}[2].".jpg";
    my $rows=join("\n", map { '        <div class="row"><span class="t">'.$_->[0].'</span><span class="d">'.$_->[1].'</span></div>' } @{$c->{prog}});
    my $items=join("\n", map { '      <li>— '.$_.' —</li>' } @{$c->{incl}});
    my $font = $lang eq 'zh' ? $FONT_ZH : $FONT_LATIN;
    my $proglabel = $L->{prog}." · ".$d->{minutes}{$lang};
    my $coll = coll_label($lang,$d->{roman});
    my $css = css($lang);
    my $attr=$L->{attr};
    my $title=$d->{title}; my $brand=$d->{brand};

    my $head = '<!DOCTYPE html>'."\n".'<html lang="'.$attr.'">'."\n".'<head>'."\n".'<meta charset="UTF-8">'."\n"
      .'<title>'.$pid.' — '.$title.' | PLAT YONEZAWA Trade Tariff</title>'."\n"
      .'<link rel="preconnect" href="https://fonts.googleapis.com">'."\n"
      .'<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'."\n".$font."\n"
      .'<style>'."\n".$css."\n".'</style>'."\n".'</head>'."\n".'<body>'."\n";

    my $sub=$c->{subtitle}; my $tag=$c->{tagline}; my $host=$c->{host}; my $prose=$c->{prose};
    my $lexp=$L->{exp}; my $lterms=$L->{terms}; my $price=$d->{price}; my $psub=$c->{price_sub};
    my $appt=$c->{appt}; my $ldur=$L->{dur}; my $dur=$c->{dur}; my $lcap=$L->{cap}; my $cap=$c->{cap};
    my $llang=$L->{langs}; my $langs=$c->{langs}; my $lven=$L->{venue}; my $ven=$c->{venue};
    my $lincl=$L->{incl}; my $enq=$c->{enq}; my $email=$EMAIL;

    my $body = <<"BODY";
<section class="page cover">
  <div class="rh"><span class="l">PLAT YONEZAWA</span><span>PLAT YONEZAWA · MMXXVI</span></div>
  <div class="cover-inner">
    <div class="hero" style="background-image:url('$cover')"></div>
    <div class="meta">
      <div class="coll eyebrow">$coll</div>
      <div class="brandline">$brand</div>
      <div class="vrule"></div>
      <h1>$title</h1>
      <div class="sub">$sub</div>
      <div class="vrule"></div>
      <p class="tag">$tag</p>
      <div class="host">$host</div>
    </div>
  </div>
  <div class="rf"><span>$pid</span><span class="num">I</span><span>$email</span></div>
</section>

<section class="page exp">
  <div class="rh"><span class="l">PLAT YONEZAWA</span><span>PLAT YONEZAWA · MMXXVI</span></div>
  <div class="exp-grid">
    <div class="imgcol" style="background-image:url('$eimg')"></div>
    <div>
      <div class="eyebrow">$lexp</div>
      <p class="lead">$prose</p>
      <div class="div"></div>
      <div class="eyebrow">$proglabel</div>
      <div class="prog">
$rows
      </div>
    </div>
  </div>
  <div class="rf"><span>$pid</span><span class="num">II</span><span>$email</span></div>
</section>

<section class="page terms">
  <div class="rh"><span class="l">PLAT YONEZAWA</span><span>PLAT YONEZAWA · MMXXVI</span></div>
  <div class="topimg" style="background-image:url('$timg')"></div>
  <div class="eyebrow dim" style="text-align:center;margin-top:20px;">$lterms</div>
  <div class="price-wrap">
    <div class="price">$price</div>
    <div class="price-sub">$psub</div>
    <div class="appt">$appt</div>
  </div>
  <div class="hr"></div>
  <div class="spec">
    <div class="cell"><div class="l">$ldur</div><div class="v">$dur</div></div>
    <div class="cell"><div class="l">$lcap</div><div class="v">$cap</div></div>
    <div class="cell"><div class="l">$llang</div><div class="v">$langs</div></div>
    <div class="cell"><div class="l">$lven</div><div class="v">$ven</div></div>
  </div>
  <div class="incl">
    <div class="h">$lincl</div>
    <ul>
$items
    </ul>
  </div>
  <div class="enq">
    <p class="note">$enq</p>
    <p class="mail">$email</p>
  </div>
  <div class="rf"><span>$pid</span><span class="num">III</span><span>$email</span></div>
</section>

</body>
</html>
BODY
    return $head.$body;
}

my $n=0;
for my $pid (@ORDER) {
    for my $lang ('en','fr','zh') {
        my $html=render($pid,$lang);
        my $path=File::Spec->catfile($FindBin::Bin, "print_${pid}_${lang}.html");
        open(my $fh, '>:encoding(UTF-8)', $path) or die "open $path: $!";
        print $fh $html;
        close $fh;
        print "wrote print_${pid}_${lang}.html\n";
        $n++;
    }
}
print "done: $n files\n";
