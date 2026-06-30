# -*- coding: utf-8 -*-
"""
PLAT YONEZAWA — Trade Tariff PDF source generator.
Generates print-ready HTML (EN / FR / ZH-Hant) for each product, faithful to the
existing 3-page editorial design. Content is sourced from the Notion 商品タリフDB
(structured properties = source of truth). Render to PDF with headless Chrome:

    python build.py            # writes print_<PID>_<lang>.html for all products/langs

Then (PowerShell) render each with:
    chrome --headless=new --no-pdf-header-footer --print-to-pdf=out.pdf file:///.../print_<PID>_<lang>.html
(see render.ps1)
"""
import os, io

HERE = os.path.dirname(os.path.abspath(__file__))
EMAIL = "info1@plat-yonezawa.jp"

# ---------------------------------------------------------------- CSS
ROOT_LATIN = """
  --serif:'Cormorant Garamond','Times New Roman',serif;
  --ui:'Inter','Helvetica Neue',sans-serif;
  --cjk:'Cormorant Garamond',serif;
"""
ROOT_ZH = """
  --serif:'Cormorant Garamond','Noto Serif TC','Times New Roman',serif;
  --ui:'Inter','Noto Serif TC','Helvetica Neue',sans-serif;
  --cjk:'Noto Serif TC',serif;
"""

CSS_BODY = """
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
"""

# CJK: serif/italic display looks poor for Han; force upright Noto Serif TC for prose-ish elements.
CSS_ZH_OVERRIDES = """
.cover .sub,.cover .tag,.cover .host,.exp .lead,.prog .d,.terms .price-sub,
.terms .appt,.spec .cell .v,.incl li,.terms .enq .note{ font-family:var(--cjk); font-style:normal; }
.exp .lead{ line-height:1.95; }
.incl li{ line-height:2.0; }
.cover .tag{ line-height:1.7; }
"""

FONT_LINK_LATIN = '<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&family=Inter:wght@300;400;500&display=swap" rel="stylesheet">'
FONT_LINK_ZH = '<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&family=Noto+Serif+TC:wght@400;500;600&family=Inter:wght@300;400;500&display=swap" rel="stylesheet">'

def css(lang):
    root = ROOT_ZH if lang == "zh" else ROOT_LATIN
    out = ":root{" + root + CSS_BODY
    if lang == "zh":
        out += CSS_ZH_OVERRIDES
    return out

# ---------------------------------------------------------------- per-language UI labels
LABELS = {
    "en": dict(lang_attr="en", exp="II · The Experience", prog="Programme", terms="III · Terms",
               dur="Duration", cap="Capacity", langs="Languages", venue="Venue", incl="What is included"),
    "fr": dict(lang_attr="fr", exp="II · L'Expérience", prog="Programme", terms="III · Modalités",
               dur="Durée", cap="Capacité", langs="Langues", venue="Lieu", incl="Ce qui est inclus"),
    "zh": dict(lang_attr="zh-Hant", exp="II · 體驗", prog="流程", terms="III · 條款",
               dur="時長", cap="人數", langs="語言", venue="地點", incl="費用包含"),
}
COLL_WORD = {"en": "Collection", "fr": "Collection", "zh": "Collection"}
ZH_SERIES = {"I": "第一系列", "II": "第二系列", "III": "第三系列"}

def coll_label(lang, roman):
    base = "Collection " + roman
    return (ZH_SERIES[roman] + " · " + base) if lang == "zh" else base

# ---------------------------------------------------------------- DATA (source: 商品タリフDB)
DATA = {}

DATA["C-NTA-01"] = dict(
    roman="I", brand="The Colors of the Snow Country", title="The Philosophy",
    img=("shot-01", "shot-02", "shot-06"), minutes={"en": "120 minutes", "fr": "120 minutes", "zh": "120 分鐘"},
    price="JPY 30,000",
    en=dict(subtitle="Weaving the Breath of Nature",
        tagline="An exclusive afternoon with the master of a 140-year-old silk house.",
        host="Hosted by Nitta Textile Arts Inc. — Est. 1884",
        prose="In Yonezawa, seasons are not four, but twenty-four. While the modern world rushes by, the Nitta family has spent generations capturing the subtle breath of nature. This exclusive session opens the family’s private residence, hosted by Chairman Nitta and his family. Witness the alchemy of natural dyeing — silk dyed with Japan red (safflower) — and the craftsmanship behind colours that have defined Yonezawa for generations. Through a tea ritual, dialogue, and a hands-on dyeing experience, you touch the essence of careful living.",
        prog=[("2:00 p.m", "Welcome &amp; the ritual — matcha &amp; wagashi service in the private welcome space."),
              ("2:45 p.m", "The crafting session (atelier) — dyeing the silk scarf with Japan red (safflower)."),
              ("3:25 p.m", "The factory walk — a guided walkthrough of the production floor with the Chairman."),
              ("3:50 p.m", "Unveiling — presentation of your finished silk scarf."),
              ("4:00 p.m", "End of tour.")],
        price_sub="per person · inclusive of consumption tax",
        appt="By appointment only · minimum two guests",
        dur="2 hours · 120 minutes", cap="2 — 8 guests", langs="English · French",
        venue="Nitta Textile Atelier · Yonezawa, Yamagata",
        incl=["Full attendance by Chairman Nitta and his family",
              "Silk scarf dyed with Japan red (safflower), to take home",
              "Matcha and seasonal confectionery", "Exclusive access to the atelier",
              "Comprehensive insurance"],
        enq="To enquire about availability, net rates, or familiarisation visits."),
    fr=dict(subtitle="Tisser le souffle de la nature",
        tagline="Un après-midi privilégié auprès du maître d’une maison de soie de 140 ans.",
        host="Sur l’invitation de Nitta Textile Arts Inc. — Fondée en 1884",
        prose="À Yonezawa, les saisons ne sont pas quatre, mais vingt-quatre. Tandis que le monde moderne s’emballe, la famille Nitta capture depuis des générations le souffle subtil de la nature. Cette séance exclusive ouvre la résidence privée de la famille, reçue par le président Nitta et les siens. Assistez à l’alchimie de la teinture naturelle — la soie teinte au rouge du Japon (carthame) — et au savoir-faire derrière les couleurs qui définissent Yonezawa depuis des générations. À travers un rituel du thé, le dialogue et une expérience de teinture à la main, vous touchez l’essence d’une vie attentive.",
        prog=[("2:00 p.m", "Accueil &amp; rituel — service de matcha et de wagashi dans l’espace d’accueil privé."),
              ("2:45 p.m", "La séance de teinture (atelier) — teinture de l’écharpe de soie au rouge du Japon (carthame)."),
              ("3:25 p.m", "La visite de la fabrique — parcours guidé de l’atelier de production avec le président."),
              ("3:50 p.m", "Dévoilement — présentation de votre écharpe de soie achevée."),
              ("4:00 p.m", "Fin de la visite.")],
        price_sub="par personne · taxe à la consommation incluse",
        appt="Sur rendez-vous uniquement · minimum deux personnes",
        dur="2 heures · 120 minutes", cap="2 — 8 personnes", langs="Anglais · Français",
        venue="Nitta Textile Atelier · Yonezawa, Yamagata",
        incl=["Présence complète du président Nitta et de sa famille",
              "Écharpe de soie teinte au rouge du Japon (carthame), à emporter",
              "Matcha et confiseries de saison", "Accès exclusif à l’atelier",
              "Assurance complète"],
        enq="Pour toute demande de disponibilité, de tarifs nets ou de visites de familiarisation."),
    zh=dict(subtitle="織就自然的氣息",
        tagline="與擁有 140 年歷史的絲織世家主人共度的專屬午後。",
        host="由 NITTA TEXTILE ARTS INC. 主理 — 創立於 1884 年",
        prose="在米澤，季節並非四季，而是二十四節氣。當現代世界匆匆前行，新田家數代以來始終捕捉著自然細微的氣息。這場專屬體驗將開啟新田家的私人宅邸，由會長新田先生及其家族親自接待。親眼見證天然染色的錄金術——以日本紅（紅花）染製的絲綢——以及數代守護、定義米澤色彩的職人技藝。透過茶之儀、對話與親手染製的體驗，您將觸及「用心生活」的本質。",
        prog=[("2:00 p.m", "迎賓與茶之儀——於私人迎賓空間奉上抹茶與和菓子。"),
              ("2:45 p.m", "染製環節（工坊）——以日本紅（紅花）染製絲巾。"),
              ("3:25 p.m", "工坊參觀——由會長親自引領參觀製造現場。"),
              ("3:50 p.m", "揭曉——呈獻您完成的絲巾。"),
              ("4:00 p.m", "行程結束。")],
        price_sub="每位 · 含消費稅",
        appt="僅限預約 · 最少兩位",
        dur="2 小時 · 120 分鐘", cap="2 — 8 位", langs="英語 · 法語",
        venue="新田織物工坊 · 山形縣米澤",
        incl=["會長新田先生及其家族全程接待",
              "以日本紅（紅花）染製的絲巾，可帶回家",
              "抹茶與當季點心", "工坊專屬參觀", "完整保險"],
        enq="如需查詢檔期、淨價或考察行程，敬請與我們聯繫。"),
)

DATA["S-TKO-01"] = dict(
    roman="II", brand="The Soul of the Snow Country", title="The Legacy &amp; The Master",
    img=("shot-01", "shot-03", "shot-06"), minutes={"en": "120–150 minutes", "fr": "120–150 minutes", "zh": "120–150 分鐘"},
    price="JPY 30,000",
    en=dict(subtitle="A Private Dialogue with the Brewer",
        tagline="A private audience with the 24th-generation master of a four-century sake house.",
        host="Hosted by Toko Brewery (Kojima Sohonten) — four centuries of brewing",
        prose="In Yonezawa, sake brewing is the heartbeat of the community. This is the ultimate sake experience — a private audience with the brewery owner. Just as one might visit a historic Champagne maison to converse with its owner, you explore the brewing museum with the current Chairman, “Yazaemon Kojima,” the 24th-generation head of the house. Hear the history of brewing and the spiritual tales of the storehouse — the branch shrine of “Omiwa Myojin” and the legend of the “Daikoku-sama in a yellow kimono.” The experience culminates in an exclusive lunch at the historic “Jodan-no-Ma” (the Upper Room), usually reserved for dignitaries, featuring local Yonezawa cuisine prepared by the chairman’s family and paired with the finest brews.",
        prog=[("11:00 a.m", "Arrival at the Toko Brewing Museum."),
              ("11:10 a.m", "[Private tour] Walking the brewing museum and historical areas with the Chairman and his family — the bond between brewery, community, and the spirits."),
              ("0:00 p.m", "[Gastronomy] Special pairing lunch at the “Jodan-no-Ma” — cuisine prepared by the chairman’s family, with deep conversation with the host."),
              ("1:30 p.m", "End of tour.")],
        price_sub="per person · inclusive of consumption tax",
        appt="By appointment only · minimum two guests · ages 20+",
        dur="2–2.5 hours · 120–150 minutes", cap="2 — 8 guests", langs="English · French",
        venue="Toko Brewery · Yonezawa, Yamagata",
        incl=["Private guide by the Chairman", "Special lunch course by the chairman’s family",
              "Premium sake pairing", "Private room charge"],
        enq="To enquire about availability, net rates, or familiarisation visits."),
    fr=dict(subtitle="Un dialogue privé avec le maître brasseur",
        tagline="Une audience privée avec le maître de la 24ᵉ génération d’une maison de saké de quatre siècles.",
        host="Sur l’invitation de Toko Brewery (Kojima Sohonten) — quatre siècles de brassage",
        prose="À Yonezawa, le brassage du saké est le cœur battant de la communauté. Voici l’expérience ultime du saké — une audience privée avec le propriétaire de la brasserie. Comme on visiterait une maison de Champagne historique pour s’entretenir avec son propriétaire, vous explorez le musée du brassage avec l’actuel président, « Yazaemon Kojima », chef de la maison à la 24ᵉ génération. Découvrez l’histoire du brassage et les récits spirituels de la maison — le sanctuaire d’« Omiwa Myojin » et la légende du « Daikoku-sama au kimono jaune ». L’expérience s’achève par un déjeuner exclusif dans la salle historique « Jodan-no-Ma » (la salle haute), habituellement réservée aux dignitaires, mettant à l’honneur la cuisine de Yonezawa préparée par la famille du président et accordée aux meilleurs crus.",
        prog=[("11:00 a.m", "Arrivée au musée du brassage Toko."),
              ("11:10 a.m", "[Visite privée] Parcours du musée du brassage et des espaces historiques avec le président et sa famille — le lien entre la brasserie, la communauté et les divinités."),
              ("0:00 p.m", "[Gastronomie] Déjeuner d’accords au « Jodan-no-Ma » — cuisine préparée par la famille du président, ponctuée d’un échange privilégié avec l’hôte."),
              ("1:30 p.m", "Fin de la visite.")],
        price_sub="par personne · taxe à la consommation incluse",
        appt="Sur rendez-vous · minimum deux personnes · 20 ans et plus",
        dur="2–2,5 heures · 120–150 minutes", cap="2 — 8 personnes", langs="Anglais · Français",
        venue="Toko Brewery · Yonezawa, Yamagata",
        incl=["Visite privée guidée par le président", "Déjeuner spécial préparé par la famille du président",
              "Accord avec des sakés premium", "Frais de salon privé"],
        enq="Pour toute demande de disponibilité, de tarifs nets ou de visites de familiarisation."),
    zh=dict(subtitle="與杜氏的私密對話",
        tagline="與傳承二十四代、歷經四百年的酒造當主的私密會面。",
        host="由 TOKO BREWERY（小嶋總本店）主理 — 四百餘年釀造",
        prose="在米澤，釀酒是社群躍動的心跳。這是極致的清酒體驗——與酒造當主的私密會面。一如造訪歷史悠久的香檳莊園與莊主對談，您將與現任會長「弥左衛門 小嶋」（藏元第二十四代）一同走訪酒造博物館。聆聽釀造的歷史，以及酒藏的靈性傳說——酒神「大神大明神」的分社，與「身著黃衣的大黑天」的傳奇。體驗最終於歷史悠久、平日僅接待貴賓的「上段之間」迎來尊榮午宴，由當主家族親手烹製的米澤在地料理，佐以頂級銘酒。",
        prog=[("11:00 a.m", "抵達東光酒造博物館。"),
              ("11:10 a.m", "〔私人導覽〕由會長與其家族引領參觀酒造博物館與歷史區域——酒藏、社群與神祇之間的羈絆。"),
              ("0:00 p.m", "〔餐饊〕於「上段之間」享用搭配午宴——當主家族親製，並與主人深入對談。"),
              ("1:30 p.m", "行程結束。")],
        price_sub="每位 · 含消費稅",
        appt="僅限預約 · 最少兩位 · 限 20 歲以上",
        dur="2–2.5 小時 · 120–150 分鐘", cap="2 — 8 位", langs="英語 · 法語",
        venue="東光酒造 · 山形縣米澤",
        incl=["由當主親自導覽", "當主家族手製的特別午宴",
              "頂級日本酒搭配", "私人包廂費用"],
        enq="如需查詢檔期、淨價或考察行程，敬請與我們聯繫。"),
)

DATA["O-STY-01"] = dict(
    roman="III", brand="The Other Side of the Mountain", title="Gastronomy with Magari",
    img=("shot-01", "shot-03", "shot-06"), minutes={"en": "150 minutes", "fr": "150 minutes", "zh": "150 分鐘"},
    price="JPY 15,000",
    en=dict(subtitle="An Italian Table in the Living Forest",
        tagline="An Italian table set in a living Satoyama forest, read through the 24 solar terms.",
        host="Hosted by Satoyama Sommelier × Yamazato Magari",
        prose="Begin with a guided walk through a private Satoyama forest, read through the lens of the 24 solar terms. Then Florence-trained Chef Takahiro Takasu of Yamazato Magari brings his kitchen into the forest for an exclusive collaboration with Satoyama Sommelier Mika Kuroda. Drawing on the “Katemono” philosophy and Yonezawa’s seasonal harvest, each course is paired by the resident sommelier with Italian and Yamagata wines — a single journey, from walking the forest to tasting its bounty.",
        prog=[("11:00 a.m", "Meet at JR Yonezawa Station (taxi transfer) or direct arrival."),
              ("11:30 a.m", "[Nature] “24 solar terms” forest walk (approx. 60 min)."),
              ("0:30 p.m", "[Lunch] “Katemono × Magari” Italian full course with sommelier wine pairing."),
              ("1:30 p.m", "Relaxing time."),
              ("1:50 p.m", "End of tour.")],
        price_sub="per person · inclusive of consumption tax",
        appt="By appointment only · minimum 15 guests · ages 20+",
        dur="2.5 hours · 150 minutes", cap="15 — 40 guests", langs="English · French",
        venue="Private Satoyama · Yonezawa, Yamagata",
        incl=["Private venue access", "Host &amp; guide fee", "Forest walking tour",
              "Chef out-catering", "Full Italian course meal", "Sommelier wine pairing",
              "Comprehensive insurance"],
        enq="To enquire about availability, net rates, or familiarisation visits."),
    fr=dict(subtitle="Une table italienne dans la forêt vivante",
        tagline="Une table italienne dressée dans une forêt satoyama vivante, au rythme des 24 micro-saisons.",
        host="Sur l’invitation de Satoyama Sommelier × Yamazato Magari",
        prose="Commencez par une promenade guidée dans une forêt satoyama privée, lue à travers le prisme des 24 micro-saisons. Puis le chef Takahiro Takasu, formé à Florence, du Yamazato Magari installe sa cuisine en forêt pour une collaboration exclusive avec la sommelière du satoyama, Mika Kuroda. Inspiré de la philosophie « Katemono » et des récoltes de saison de Yonezawa, chaque plat est accordé par le sommelier maison à des vins italiens et de Yamagata — un même voyage, de la marche en forêt à la dégustation de ses fruits.",
        prog=[("11:00 a.m", "Rendez-vous à la gare JR de Yonezawa (transfert en taxi) ou arrivée directe."),
              ("11:30 a.m", "[Nature] Promenade en forêt « 24 micro-saisons » (env. 60 min)."),
              ("0:30 p.m", "[Déjeuner] Menu italien complet « Katemono × Magari », accords mets-vins du sommelier."),
              ("1:30 p.m", "Temps de détente."),
              ("1:50 p.m", "Fin de la visite.")],
        price_sub="par personne · taxe à la consommation incluse",
        appt="Sur rendez-vous · minimum 15 personnes · 20 ans et plus",
        dur="2,5 heures · 150 minutes", cap="15 — 40 personnes", langs="Anglais · Français",
        venue="Satoyama privé · Yonezawa, Yamagata",
        incl=["Accès privatif au site", "Honoraires d’hôte et de guide", "Promenade en forêt guidée",
              "Traiteur du chef sur place", "Menu italien complet", "Accord mets-vins par le sommelier",
              "Assurance complète"],
        enq="Pour toute demande de disponibilité, de tarifs nets ou de visites de familiarisation."),
    zh=dict(subtitle="活森林中的義式餐桌",
        tagline="在生機盎然的里山森林中，依循二十四節氣而設的義式餐桌。",
        host="由 Satoyama Sommelier × Yamazato Magari 主理",
        prose="首先在私人里山森林中展開導覽散策，以二十四節氣的視角閱讀自然。隨後，曾於佛羅倫斯研修的「山里まがり」主廄高須崇大將廄房帶進森林，與里山侍酒師 Mika Kuroda（三佳）展開專屬聯名。以「かてもの」哲學與米澤當季食材為靈感，每道菜餒皆由駐店侍酒師搭配義大利與山形葡萄酒——從漫步森林到品味其恩澤，一气呀成的旅程。",
        prog=[("11:00 a.m", "於 JR 米澤站集合（計程車接駁）或現地直接抵達。"),
              ("11:30 a.m", "〔自然〕「二十四節氣」森林散策（約 60 分鐘）。"),
              ("0:30 p.m", "〔午宴〕「かてもの × Magari」義式全套餐，佐侍酒師選酒搭配。"),
              ("1:30 p.m", "悠閒時光。"),
              ("1:50 p.m", "行程結束。")],
        price_sub="每位 · 含消費稅",
        appt="僅限預約 · 最少 15 位 · 限 20 歲以上",
        dur="2.5 小時 · 150 分鐘", cap="15 — 40 位", langs="英語 · 法語",
        venue="私人里山 · 山形縣米澤",
        incl=["場地專屬使用", "主持與導覽費", "森林散策導覽",
              "主廄到場外燴", "完整義式套餐", "侍酒師選酒搭配", "完整保險"],
        enq="如需查詢檔期、淨價或考察行程，敬請與我們聯繫。"),
)

DATA["O-STY-02"] = dict(
    roman="III", brand="The Other Side of the Mountain", title="Katemono Afternoon Tea",
    img=("shot-01", "shot-03", "shot-06"), minutes={"en": "120 minutes", "fr": "120 minutes", "zh": "120 分鐘"},
    price="JPY 8,000",
    en=dict(subtitle="An Afternoon of Wild Wisdom",
        tagline="An afternoon of wild Yonezawa wisdom, served as a Katemono tea.",
        host="Hosted by Satoyama Sommelier — Mika Kuroda",
        prose="A relaxed afternoon hosted by Satoyama Sommelier Mika Kuroda. The wild food wisdom of Yonezawa — foraged plants, nuts, and fermented preserves — is reimagined as a “Katemono Afternoon Tea”: a tiered stand of sweet and savoury small plates paired with herbal and Japanese teas. In a quiet reception room, guests touch the Japanese aesthetic of “Ma” (negative space) while Mika shares stories of the half-samurai, half-farmer life and the 24 solar terms. A lighter, shorter counterpart to the full-course lunch.",
        prog=[("2:00 p.m", "Meet at the Satoyama entrance / reception room."),
              ("2:15 p.m", "[Tea] “Katemono” afternoon tea — a tiered stand of sweet &amp; savoury plates with tea / herbal pairing and the host’s narration."),
              ("3:30 p.m", "Short forest stroll or relaxing time (optional)."),
              ("4:00 p.m", "End of experience.")],
        price_sub="per person · inclusive of consumption tax",
        appt="By appointment only · from 1 guest (minimum charge applies)",
        dur="2 hours · 120 minutes", cap="1 — 20 guests", langs="English · French",
        venue="Private Satoyama · Yonezawa, Yamagata",
        incl=["Private venue access", "Host fee (Mika Kuroda)", "Katemono tea set", "Drinks",
              "Comprehensive insurance"],
        enq="To enquire about availability, net rates, or familiarisation visits."),
    fr=dict(subtitle="Un après-midi de sagesse sauvage",
        tagline="Un après-midi de sagesse sauvage de Yonezawa, servi en thé Katemono.",
        host="Sur l’invitation de la Satoyama Sommelier — Mika Kuroda",
        prose="Un après-midi détendu en compagnie de la sommelière du satoyama, Mika Kuroda. La sagesse alimentaire sauvage de Yonezawa — plantes cueillies, noix et conserves fermentées — est réinventée en un « thé de l’après-midi Katemono » : un présentoir à étages de petites assiettes sucrées et salées, accordées à des thés japonais et infusions. Dans un salon paisible, les hôtes effleurent l’esthétique japonaise du « Ma » (l’espace vide) tandis que Mika partage les récits de la vie mi-samouraï, mi-paysanne et des 24 micro-saisons. Une version plus légère et plus courte du déjeuner gastronomique.",
        prog=[("2:00 p.m", "Accueil à l’entrée du satoyama / salon de réception."),
              ("2:15 p.m", "[Thé] Thé de l’après-midi « Katemono » — présentoir à étages d’assiettes sucrées et salées, accords thé / infusions et récit de l’hôte."),
              ("3:30 p.m", "Courte promenade en forêt ou temps libre (facultatif)."),
              ("4:00 p.m", "Fin de l’expérience.")],
        price_sub="par personne · taxe à la consommation incluse",
        appt="Sur rendez-vous · à partir d’1 personne (forfait minimum)",
        dur="2 heures · 120 minutes", cap="1 — 20 personnes", langs="Anglais · Français",
        venue="Satoyama privé · Yonezawa, Yamagata",
        incl=["Accès privatif au site", "Honoraires d’hôte (Mika Kuroda)", "Service de thé Katemono",
              "Boissons", "Assurance complète"],
        enq="Pour toute demande de disponibilité, de tarifs nets ou de visites de familiarisation."),
    zh=dict(subtitle="野之智慧的午後",
        tagline="以「かてもの」茶席呈現的米澤野生智慧午後。",
        host="由 Satoyama Sommelier — Mika Kuroda 主理",
        prose="由里山侍酒師 Mika Kuroda（三佳）主持的悠閒午後。米澤的野生飲食智慧——採集的野草、堅果與發酵保存食——被重新詮釋為「かてもの下午茶」：層層疊起的鹹甜小點，佐以日本茶與花草茶。在靜謐的迎賓室裡，賓客在三佳娓娓道來半士半農的生活與二十四節氣之際，觸碰日本「間」（留白）的美學。這是全套午宴之外，更輕盈、更簡短的姊妹體驗。",
        prog=[("2:00 p.m", "於里山入口／迎賓室集合。"),
              ("2:15 p.m", "〔茶席〕「かてもの」下午茶——層疊的鹹甜小點，佐日本茶／花草茶與主人解說。"),
              ("3:30 p.m", "短暫森林散步或自由時光（任選）。"),
              ("4:00 p.m", "體驗結束。")],
        price_sub="每位 · 含消費稅",
        appt="僅限預約 · 1 位起（適用最低消費）",
        dur="2 小時 · 120 分鐘", cap="1 — 20 位", langs="英語 · 法語",
        venue="私人里山 · 山形縣米澤",
        incl=["場地專屬使用", "主持費（Mika Kuroda）", "かてもの茶席", "飲品",
              "完整保險"],
        enq="如需查詢檔期、淨價或考察行程，敬請與我們聯繫。"),
)

DATA["O-STY-03"] = dict(
    roman="III", brand="The Other Side of the Mountain", title="Forest Bathing with Mika",
    img=("shot-01", "shot-03", "shot-06"), minutes={"en": "120 minutes", "fr": "120 minutes", "zh": "120 分鐘"},
    price="JPY 5,000",
    en=dict(subtitle="A Forest Immersion with the Satoyama Sommelier",
        tagline="A two-hour forest immersion with the Satoyama Sommelier.",
        host="Hosted by Satoyama Sommelier — Mika Kuroda",
        prose="A two-hour guided forest immersion led by Mika Kuroda — Satoyama Sommelier, NHK World contributor, and author of “Mori to Katemono” (The Forest and Katemono). Mika lives in the very Satoyama forest where samurai-farmers once cultivated the land in the spirit of han-shi han-no. Walk among the 24 solar terms through the eyes of someone who has spent years rediscovering the wild food wisdom of Yonezawa — the most accessible way to enter “The Other Side of the Mountain.”",
        prog=[("2:00 p.m", "Meet at the Satoyama entrance."),
              ("2:10 p.m", "[Forest walk] Guided immersion with Mika Kuroda — seasonal signs, wild plants, and the philosophy of “Teire” (care). Approx. 2 hours."),
              ("4:00 p.m", "End of experience.")],
        price_sub="per person · inclusive of consumption tax",
        appt="By appointment only · from 1 guest",
        dur="2 hours · 120 minutes", cap="From 1 guest", langs="English · French",
        venue="Private Satoyama · Yonezawa, Yamagata",
        incl=["Host &amp; guide fee (Mika Kuroda)", "Forest walking tour", "Comprehensive insurance"],
        enq="To enquire about availability, net rates, or familiarisation visits."),
    fr=dict(subtitle="Une immersion forestière avec la sommelière du satoyama",
        tagline="Une immersion forestière de deux heures avec la sommelière du satoyama.",
        host="Sur l’invitation de la Satoyama Sommelier — Mika Kuroda",
        prose="Une immersion forestière guidée de deux heures, menée par Mika Kuroda — sommelière du satoyama, intervenante sur NHK World et autrice de « Mori to Katemono » (La forêt et le Katemono). Mika vit dans cette forêt satoyama même où les samouraïs-paysans cultivaient jadis la terre dans l’esprit du han-shi han-no. Marchez au fil des 24 micro-saisons à travers le regard de celle qui a passé des années à redécouvrir la sagesse alimentaire sauvage de Yonezawa — la manière la plus accessible d’entrer dans « L’Autre Versant de la Montagne ».",
        prog=[("2:00 p.m", "Accueil à l’entrée du satoyama."),
              ("2:10 p.m", "[Marche en forêt] Immersion guidée avec Mika Kuroda — signes de saison, plantes sauvages et philosophie du « Teire » (le soin). Env. 2 heures."),
              ("4:00 p.m", "Fin de l’expérience.")],
        price_sub="par personne · taxe à la consommation incluse",
        appt="Sur rendez-vous · à partir d’1 personne",
        dur="2 heures · 120 minutes", cap="À partir d’1 personne", langs="Anglais · Français",
        venue="Satoyama privé · Yonezawa, Yamagata",
        incl=["Honoraires d’hôte et de guide (Mika Kuroda)", "Promenade en forêt guidée", "Assurance complète"],
        enq="Pour toute demande de disponibilité, de tarifs nets ou de visites de familiarisation."),
    zh=dict(subtitle="與里山侍酒師的森林沉浸",
        tagline="與里山侍酒師共度的兩小時森林沉浸。",
        host="由 Satoyama Sommelier — Mika Kuroda 主理",
        prose="由 Mika Kuroda（三佳）親自帶領的兩小時森林沉浸——她是里山侍酒師、NHK World 的出演者，也是《森與かてもの》的作者。三佳就居住在這片里山森林，昔日武士曾以「半士半農」的精神在此耕作。透過一位多年來不斷重新發掘米澤野生飲食智慧者的眼睛，漫步於二十四節氣之間——這是進入「山的另一側」最平易近人的方式。",
        prog=[("2:00 p.m", "於里山入口集合。"),
              ("2:10 p.m", "〔森林散策〕由 Mika Kuroda（三佳）帶領的沉浸導覽——季節徵兆、野生植物，以及「手入れ」（照料）的哲學。約 2 小時。"),
              ("4:00 p.m", "體驗結束。")],
        price_sub="每位 · 含消費稅",
        appt="僅限預約 · 1 位起",
        dur="2 小時 · 120 分鐘", cap="1 位起", langs="英語 · 法語",
        venue="私人里山 · 山形縣米澤",
        incl=["主持與導覽費（Mika Kuroda）", "森林散策導覽", "完整保險"],
        enq="如需查詢檔期、淨價或考察行程，敬請與我們聯繫。"),
)

# ---------------------------------------------------------------- render
def render(pid, lang):
    d = DATA[pid]; c = d[lang]; L = LABELS[lang]
    pid_lower = pid.lower()
    img_dir = "../images/" + pid_lower
    cover_img = img_dir + "/" + d["img"][0] + ".jpg"
    exp_img = img_dir + "/" + d["img"][1] + ".jpg"
    terms_img = img_dir + "/" + d["img"][2] + ".jpg"
    prog_rows = "\n".join(
        '        <div class="row"><span class="t">%s</span><span class="d">%s</span></div>' % (t, desc)
        for (t, desc) in c["prog"])
    incl_items = "\n".join('      <li>— %s —</li>' % it for it in c["incl"])
    font_link = FONT_LINK_ZH if lang == "zh" else FONT_LINK_LATIN
    prog_label = "%s · %s" % (L["prog"], d["minutes"][lang])

    head = (
        '<!DOCTYPE html>\n<html lang="%s">\n<head>\n<meta charset="UTF-8">\n'
        '<title>%s — %s | PLAT YONEZAWA Trade Tariff</title>\n'
        '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
        '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n%s\n'
        '<style>\n%s\n</style>\n</head>\n<body>\n'
    ) % (L["lang_attr"], pid, d["title"], font_link, css(lang))

    body = """
<section class="page cover">
  <div class="rh"><span class="l">PLAT YONEZAWA</span><span>PLAT YONEZAWA · MMXXVI</span></div>
  <div class="cover-inner">
    <div class="hero" style="background-image:url('{cover}')"></div>
    <div class="meta">
      <div class="coll eyebrow">{coll}</div>
      <div class="brandline">{brand}</div>
      <div class="vrule"></div>
      <h1>{title}</h1>
      <div class="sub">{subtitle}</div>
      <div class="vrule"></div>
      <p class="tag">{tagline}</p>
      <div class="host">{host}</div>
    </div>
  </div>
  <div class="rf"><span>{pid}</span><span class="num">I</span><span>{email}</span></div>
</section>

<section class="page exp">
  <div class="rh"><span class="l">PLAT YONEZAWA</span><span>PLAT YONEZAWA · MMXXVI</span></div>
  <div class="exp-grid">
    <div class="imgcol" style="background-image:url('{exp}')"></div>
    <div>
      <div class="eyebrow">{lbl_exp}</div>
      <p class="lead">{prose}</p>
      <div class="div"></div>
      <div class="eyebrow">{prog_label}</div>
      <div class="prog">
{prog_rows}
      </div>
    </div>
  </div>
  <div class="rf"><span>{pid}</span><span class="num">II</span><span>{email}</span></div>
</section>

<section class="page terms">
  <div class="rh"><span class="l">PLAT YONEZAWA</span><span>PLAT YONEZAWA · MMXXVI</span></div>
  <div class="topimg" style="background-image:url('{terms}')"></div>
  <div class="eyebrow dim" style="text-align:center;margin-top:20px;">{lbl_terms}</div>
  <div class="price-wrap">
    <div class="price">{price}</div>
    <div class="price-sub">{price_sub}</div>
    <div class="appt">{appt}</div>
  </div>
  <div class="hr"></div>
  <div class="spec">
    <div class="cell"><div class="l">{lbl_dur}</div><div class="v">{dur}</div></div>
    <div class="cell"><div class="l">{lbl_cap}</div><div class="v">{cap}</div></div>
    <div class="cell"><div class="l">{lbl_langs}</div><div class="v">{langs}</div></div>
    <div class="cell"><div class="l">{lbl_venue}</div><div class="v">{venue}</div></div>
  </div>
  <div class="incl">
    <div class="h">{lbl_incl}</div>
    <ul>
{incl_items}
    </ul>
  </div>
  <div class="enq">
    <p class="note">{enq}</p>
    <p class="mail">{email}</p>
  </div>
  <div class="rf"><span>{pid}</span><span class="num">III</span><span>{email}</span></div>
</section>

</body>
</html>
""".format(
        cover=cover_img, exp=exp_img, terms=terms_img,
        coll=coll_label(lang, d["roman"]), brand=d["brand"], title=d["title"],
        subtitle=c["subtitle"], tagline=c["tagline"], host=c["host"], pid=pid, email=EMAIL,
        lbl_exp=L["exp"], prose=c["prose"], prog_label=prog_label, prog_rows=prog_rows,
        lbl_terms=L["terms"], price=d["price"], price_sub=c["price_sub"], appt=c["appt"],
        lbl_dur=L["dur"], dur=c["dur"], lbl_cap=L["cap"], cap=c["cap"],
        lbl_langs=L["langs"], langs=c["langs"], lbl_venue=L["venue"], venue=c["venue"],
        lbl_incl=L["incl"], incl_items=incl_items, enq=c["enq"],
    )
    return head + body


def main():
    n = 0
    for pid in DATA:
        for lang in ("en", "fr", "zh"):
            html = render(pid, lang)
            path = os.path.join(HERE, "print_%s_%s.html" % (pid, lang))
            with io.open(path, "w", encoding="utf-8") as f:
                f.write(html)
            n += 1
            print("wrote", os.path.basename(path))
    print("done:", n, "files")


if __name__ == "__main__":
    main()
