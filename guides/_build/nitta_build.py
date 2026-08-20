# -*- coding: utf-8 -*-
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import nitta_content as B   # scenes, faq, glossary, timing, colors, audience
OUT=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','nitta-guide.html')

# ============================================================
#  多言語ヘルパー：EN/FR/繁中/日本語 の4スパンを出力。
#  未指定(空)の言語はJSフォールバックでEN表示される。
#  英語はアメリカ英語（color 等）で統一。
# ============================================================
def t(en, fr='', tw='', ja=''):
    return ('<span class="en">%s</span><span class="fr">%s</span>'
            '<span class="tw">%s</span><span class="ja">%s</span>'
            % (en, fr, tw, ja))

# ---- ビジター向け：物語（4言語・写真付き）----
# (photo, reverse, (en,fr,tw,ja) title, (en,fr,tw,ja) body)
story=[
 ("images/shot-02.jpg", False,
  ("A Samurai Family, Weaving for Five Generations",
   "Une famille de samouraïs, cinq générations de tissage",
   "武士家族，五代織藝傳承",
   "武士の家系、五代つづく織り"),
  ("For over 140 years, the Nitta family has woven silk in Yonezawa. Founded in 1884, we were originally a samurai family who turned to textiles when the age of the sword ended. This house, built in 1925, is over 100 years old — and the 4th and 5th generations still weave here today.",
   "Depuis plus de 140 ans, la famille Nitta tisse la soie à Yonezawa. Fondée en 1884, notre famille était à l'origine une famille de samouraïs qui se tourna vers le textile à la fin de l'ère du sabre. Cette maison, bâtie en 1925, a plus de 100 ans — et les 4e et 5e générations y tissent encore aujourd'hui.",
   "一百四十多年來，新田家族在米澤織就絲綢。我們1884年創業，原是武士家族，於刀劍時代結束後轉投紡織。這棟宅邸建於1925年，已逾百年——第四代與第五代至今仍在此織布。",
   "新田家は140年以上、米沢で絹を織ってきました。1884年（明治17年）創業。もとは武士の家系で、刀の時代の終わりとともに織物へと転じました。1925年建築のこの家は築100年を超え、いまも4代目・5代目がここで織り続けています。")),
 ("images/shot-09.jpg", True,
  ("The Lord Who Turned Poverty into Craft",
   "Le seigneur qui fit de la pauvreté un art",
   "化貧困為工藝的藩主",
   "貧しさをものづくりに変えた藩主"),
  ("Yonezawa was once a poor domain. Its 9th lord, Yozan Uesugi, encouraged his samurai to take up crafts — weaving, dyeing, papermaking — that could be done at home. Silk weaving became the town's soul, and 250 years later that spirit still lives here.",
   "Yonezawa fut jadis un domaine pauvre. Son 9e seigneur, Yozan Uesugi, encouragea ses samouraïs à pratiquer des métiers — tissage, teinture, papier — réalisables à la maison. Le tissage de la soie devint l'âme de la ville, et 250 ans plus tard cet esprit demeure.",
   "米澤昔為貧困之藩。第九代藩主上杉鷹山鼓勵武士從事可在家中進行的工藝——織布、染色、造紙。絲織遂成城市之魂，二百五十年後，這份精神依然長存。",
   "米沢はかつて貧しい藩でした。9代藩主・上杉鷹山は、家の中でできる織り・染め・紙漉きといった手仕事を武士に奨励します。絹織物は町の魂となり、250年を経たいまも、その精神が息づいています。")),
 ("images/shot-04.jpg", False,
  ("Benibana — The Red of Yamagata",
   "Benibana — le rouge de Yamagata",
   "紅花——山形之紅",
   "紅花 — 山形の赤"),
  ("Our signature is benibana (safflower) dyeing — a red once as valuable as gold. Revived by the family in the 1960s, it is dyed only in winter, when the cold brings out the most beautiful red. From one flower we draw red and yellow, and with other plants, green and purple.",
   "Notre signature est la teinture au benibana (carthame) — un rouge jadis aussi précieux que l'or. Ressuscitée dans les années 1960, elle ne se teint qu'en hiver, quand le froid révèle le plus beau rouge. D'une seule fleur naissent le rouge et le jaune, et avec d'autres plantes, le vert et le violet.",
   "我們的招牌是紅花染——一種曾與黃金等值的紅。家族於1960年代復興此技，僅於冬季染製，愈寒冷，紅色愈美。一朵花可取紅與黃，並與其他植物調出綠與紫。",
   "私たちの真骨頂は紅花染め。かつて金と同じ価値をもった赤です。1960年代に家族が復興し、寒さが最も美しい赤を生む冬にだけ染めます。一輪の花から赤と黄を、ほかの植物と合わせれば緑や紫も生まれます。")),
]

# ---- 登場人物（人物カード）----
# (gen(en,fr,tw,ja), name(en,tw,ja), role(en,fr,tw,ja), desc(en,fr,tw,ja))
people=[
 (("3rd Generation","3e génération","第三代","3代目"),
  ("Shuji &amp; Tomiko Nitta","新田 秀治・富子","新田 秀治・富子"),
  ("Revived benibana dyeing","Renaissance du benibana","復興紅花染","紅花染めを復興"),
  ("Rediscovered the lost safflower-dyeing technique through years of research in the 1960s.",
   "Ont redécouvert la teinture au carthame, perdue, après des années de recherche dans les années 1960.",
   "於1960年代歷經多年研究，復興一度失傳的紅花染技法。",
   "1960年代、失われた紅花染めの技法を、幾年もの研究の末によみがえらせた。")),
 (("4th Generation","4e génération","第四代","4代目"),
  ("Hideyuki Nitta","新田 英行","新田 英行"),
  ("Chairman &amp; your host","Président &amp; votre hôte","會長・主人","会長・当主"),
  ("Established the in-house dyeing-and-weaving workshop and welcomes guests to the house.",
   "A établi l'atelier intégré de teinture et tissage, et accueille les visiteurs.",
   "確立染織一貫工房，親自迎接來訪賓客。",
   "染めと織りの一貫工房を確立し、この家で来客を迎える。")),
 (("5th Generation","5e génération","第五代","5代目"),
  ("Gentaro Nitta","新田 源太郎","新田 源太郎"),
  ("President &amp; maker","Président &amp; artisan","社長・作家","社長・作り手"),
  ("Today's weaver; co-created the pillar-less tea room with media artist Yoichi Ochiai.",
   "Tisserand d'aujourd'hui ; a co-créé le salon de thé sans pilier avec l'artiste Yoichi Ochiai.",
   "當代織者；與媒體藝術家落合陽一共創無柱茶室。",
   "現役の織り手。メディアアーティスト落合陽一と、柱のない茶室を共作。")),
 (("Edo Period","Époque d'Edo","江戶時代","江戸時代"),
  ("Lord Yozan Uesugi","上杉 鷹山","上杉 鷹山"),
  ("9th lord of Yonezawa","9e seigneur de Yonezawa","米澤第九代藩主","米沢藩9代藩主"),
  ("The reformer who, 250 years ago, turned a struggling domain toward craft and silk.",
   "Le réformateur qui, il y a 250 ans, orienta un domaine en difficulté vers l'artisanat et la soie.",
   "二百五十年前引領困頓之藩轉向工藝與絲織的中興名君。",
   "250年前、傾いた藩をものづくりと絹へと導いた名君。")),
]

# ---- 訪問の流れ（タイムライン）----
# (step, title(en,fr,tw,ja), desc(en,fr,tw,ja))
visitflow=[
 ("01",("Entrance &amp; welcome","Entrée &amp; accueil","玄關・迎賓","玄関・お出迎え"),
  ("Step through the gate into a house built in 1925.","Franchissez le portail d'une maison de 1925.","踏入建於1925年的宅邸。","門をくぐり、1925年築の家へ。")),
 ("02",("Gallery","Galerie","展廊","ギャラリー"),
  ("The story of Lord Yozan and Yonezawa silk.","L'histoire du seigneur Yozan et de la soie de Yonezawa.","上杉鷹山與米澤絲綢的故事。","上杉鷹山と米沢の絹の物語。")),
 ("03",("Tea room","Salon de thé","茶室","お茶室"),
  ("Matcha and wagashi in a pillar-less tea room.","Matcha et wagashi dans un salon de thé sans pilier.","於無柱茶室品抹茶與和菓子。","柱のない茶室で抹茶と和菓子を。")),
 ("04",("Four-season garden","Jardin des quatre saisons","四季庭園","四季の庭"),
  ("The seasons framed by 100-year-old glass.","Les saisons vues à travers un verre centenaire.","透過百年玻璃眺望四季。","百年のガラス越しに映る四季。")),
 ("05",("Dye your own handkerchief","Teignez votre mouchoir","親手染手帕","紅花染め体験"),
  ("Fold, tie and dip in living safflower red.","Pliez, nouez et plongez dans le rouge du carthame.","摺、綁、浸入鮮活的紅花紅。","畳んで、結んで、紅花の赤に浸す。")),
 ("06",("The workshop","L'atelier","工房","工房"),
  ("A century-old Jacquard loom, still running.","Un métier Jacquard centenaire, toujours en marche.","仍在運轉的百年提花織機。","今も動く、百年もののジャガード織機。")),
 ("07",("Showroom","Showroom","展示間","ショールーム"),
  ("Kimono, obi, and the meaning of colors.","Kimonos, obis et la signification des couleurs.","和服、腰帶與色彩的寓意。","着物・帯、そして色に込めた意味。")),
 ("08",("Farewell","Au revoir","送別","お見送り"),
  ("Carry home your handkerchief — one of a kind.","Repartez avec votre mouchoir, unique au monde.","帶走世上僅此一件的手帕。","世界に一枚のハンカチを持ち帰って。")),
]

# ---- ハイライト（写真スポット）----
# (photo, emoji, name(en,fr,tw,ja), desc(en,fr,tw,ja))
highlights=[
 ("images/shot-03.jpg","🍵",
  ("The tea room “Null-Beni-An”","Le salon de thé « Null-Beni-An »","茶室「紅無庵」","茶室「ヌベルニ庵」"),
  ("A pillar-less, movable tea room of safflower-dyed silk, co-created with artist Yoichi Ochiai.",
   "Un salon de thé mobile et sans pilier, en soie teinte au carthame, co-créé avec Yoichi Ochiai.",
   "以紅花染絲打造、可移動的無柱茶室，與落合陽一共創。",
   "紅花染めの絹でつくる、柱のない移動式の茶室。落合陽一との共作。")),
 ("images/shot-04.jpg","🌺",
  ("Dye your own handkerchief","Teignez votre propre mouchoir","親手染製手帕","自分だけのハンカチを染める"),
  ("Fold, tie and dip — open it to reveal a pattern that is yours alone.",
   "Pliez, nouez, plongez — dépliez pour révéler un motif rien qu'à vous.",
   "摺、綁、浸——展開即見專屬您的圖案。",
   "畳んで、結んで、浸す——広げれば、あなただけの模様。")),
 ("images/shot-05.jpg","🧵",
  ("A century-old Jacquard loom","Un métier Jacquard centenaire","百年提花織機","百年のジャガード織機"),
  ("Punch-card patterns and polished steel needles, maintained and running for over 100 years.",
   "Cartes perforées et aiguilles d'acier polies, entretenues et en marche depuis plus d'un siècle.",
   "紋紙與磨亮的鋼針，維護運轉逾百年。",
   "紋紙と磨き上げた鋼の針。100年以上、手入れしながら動かし続ける。")),
 ("images/shot-06.jpg","🎴",
  ("Silk in seasonal color","La soie aux couleurs de saison","四季色絲織","四季を映す絹"),
  ("Kimono and obi, each made to measure — no two designs are ever the same.",
   "Kimonos et obis, faits sur mesure — jamais deux motifs identiques.",
   "和服與腰帶皆量身訂製，圖案絕無雷同。",
   "着物も帯も、すべてお誂え。同じ柄は二つとありません。")),
]

# ---- 色の意味（カード）----
# (swatch hex, name(en,fr,tw,ja), meaning(en,fr,tw,ja))
colorcards=[
 ("#a83a2b",("Red","Rouge","紅","赤"),
  ("Protection, health, family safety","Protection, santé, sécurité de la famille","避邪、健康、闔家平安","魔除け・健康・家族の安全")),
 ("#d9a441",("Yellow","Jaune","黃","黄"),
  ("Wealth, hope, energy","Richesse, espoir, énergie","財運、希望、活力","金運・希望・活力")),
 ("#c9772f",("Orange","Orange","橙","橙"),
  ("Shields you from bad energy","Vous protège des mauvaises énergies","抵禦負面能量","悪い気から守る")),
 ("#3f6d8c",("Blue","Bleu","藍","青"),
  ("Study, talent, business luck","Études, talent, chance en affaires","學業、才華、商運","学問・才能・商売運")),
 ("#2b2622",("Black","Noir","黑","黒"),
  ("Long-lasting business success","Réussite durable en affaires","生意長久興隆","商売繁盛が長く続く")),
]

# ---- 訪問前に（Good to know）(en,fr,tw,ja) ----
goodtoknow=[
 ("Duration is about 60–90 minutes, by reservation.","Durée d'environ 60 à 90 minutes, sur réservation.","體驗約60〜90分鐘，採預約制。","所要時間は約60〜90分、予約制です。"),
 ("Handkerchief dyeing is available year-round (making the dye itself is winter-only).","La teinture de mouchoir est proposée toute l'année (la fabrication du colorant, seulement en hiver).","手帕染色全年皆可（製作染料則僅限冬季）。","ハンカチ染め体験は通年（染料づくり自体は冬季限定）。"),
 ("Kimono and obi are made to measure; lead time and price vary.","Kimonos et obis sont faits sur mesure ; délai et prix variables.","和服與腰帶為量身訂製，工期與價格因品項而異。","着物・帯はお誂え。納期と価格は品により異なります。"),
 ("Each September, Yonezawa opens its workshops for the “Open Factory” event.","Chaque septembre, Yonezawa ouvre ses ateliers lors de l'« Open Factory ».","每年九月，米澤舉辦「Open Factory」開放工坊活動。","毎年9月、米沢では「オープンファクトリー」で工房を公開します。"),
 ("Overseas shipping: handkerchiefs and small items yes; obi and kimono on request.","Expédition internationale : mouchoirs et petits articles oui ; obis et kimonos sur demande.","海外寄送：手帕與小物可寄；腰帶、和服可洽詢。","海外発送：ハンカチ・小物は可。帯・着物はご相談ください。"),
]

# ---- ビジター向けFAQ (Q(en,fr,tw,ja), A(en,fr,tw,ja)) ----
vfaq=[
 (("Is the silk produced here?","La soie est-elle produite ici ?","絲綢是在此生產的嗎？","絹はここで作っているのですか？"),
  ("Historically, yes. Today most silk is imported (about 90%), with roughly 10% from Japan.",
   "Historiquement, oui. Aujourd'hui, la majeure partie est importée (environ 90 %), 10 % venant du Japon.",
   "昔日如此。如今約九成為進口，約一成產自日本。",
   "かつては、はい。今は約9割が輸入で、日本産は約1割です。")),
 (("Can I try dyeing at any time of year?","Peut-on teindre à n'importe quelle saison ?","任何季節都能體驗染色嗎？","染め体験は一年中できますか？"),
  ("Handkerchief dyeing is available year-round; making the safflower dye itself is done only in winter.",
   "La teinture de mouchoir est proposée toute l'année ; la fabrication du colorant se fait uniquement en hiver.",
   "手帕染色全年皆可；紅花染料的製作則僅在冬季進行。",
   "ハンカチ染めは通年。紅花の染料づくりは冬にだけ行います。")),
 (("Can I order a kimono or obi?","Peut-on commander un kimono ou un obi ?","可以訂製和服或腰帶嗎？","着物や帯は注文できますか？"),
  ("Yes — they are made to measure. Lead time and price depend on the piece.",
   "Oui — ils sont faits sur mesure. Le délai et le prix dépendent de la pièce.",
   "可以，皆為量身訂製，工期與價格視品項而定。",
   "はい、お誂えです。納期と価格は品によります。")),
 (("Do you ship overseas?","Livrez-vous à l'étranger ?","可以寄送海外嗎？","海外へ送れますか？"),
  ("Handkerchiefs and small items can be shipped abroad; obi and kimono on request.",
   "Mouchoirs et petits articles peuvent être expédiés ; obis et kimonos sur demande.",
   "手帕與小物可寄送海外；腰帶與和服可洽詢。",
   "ハンカチ・小物は海外発送可。帯・着物はご相談ください。")),
]

phrases=[
 ("ようこそ／歓迎","Welcome to Nitta.","Bienvenue chez Nitta.","歡迎光臨新田。"),
 ("遠路のお礼","Thank you for coming all the way to Yonezawa.","Merci d'être venus jusqu'à Yonezawa.","感謝您遠道而來米澤。"),
 ("ごゆっくり","Please take your time.","Prenez votre temps.","請慢慢參觀。"),
 ("これは紅花です","This is benibana — safflower.","Ceci est du benibana — du carthame.","這是紅花。"),
 ("金と同じ価値","Once as valuable as gold.","Jadis aussi précieux que l'or.","曾與黃金等值。"),
 ("世界に1枚","One of a kind in the world.","Unique au monde.","世上僅此一件。"),
 ("またどうぞ","Please come again anytime.","Revenez quand vous voulez.","歡迎再度光臨。"),
]

def paras(lst): return "\n".join("<p>%s</p>"%p for p in lst)

# ============================================================
#  ビジター向けHTML生成
# ============================================================
def vchapter(kicker_t, h2_t, body):
    return ('<section class="vchapter">'
            '<div class="kicker">%s</div>'
            '<h2>%s</h2>%s</section>') % (kicker_t, h2_t, body)

# 導入（ブランド動画）
intro_sec=vchapter(
  t("Welcome","Bienvenue","歡迎","ようこそ"),
  t("A Living Workshop","Un atelier vivant","一座活著的工房","生きている工房"),
  '<p class="lead">%s</p>'
  '<div class="video-wrap"><video src="images/brand-world.mp4" controls muted playsinline preload="metadata" poster="images/shot-10.jpg"></video>'
  '<div class="video-cap">%s</div></div>'
  % (t("A private visit into a 140-year-old silk atelier in Yonezawa, where dye, thread and loom are still worked by hand. Take a breath, and step inside.",
       "Une visite privée dans un atelier de soie de 140 ans à Yonezawa, où teinture, fil et métier sont encore travaillés à la main. Respirez, et entrez.",
       "走進米澤一座擁有140年歷史的絲織工房，染、線、機仍以手工進行。深吸一口氣，請進。",
       "米沢で140年、染めも糸も機（はた）も、いまなお手仕事で続く絹の工房へ。ひと呼吸おいて、どうぞ中へ。"),
     t("Nitta Textile — the brand world (with sound).","Nitta Textile — l'univers de la marque (avec le son).","新田織物——品牌世界（含聲音）。","新田織物 — ブランドの世界（音が出ます）。")))

# 物語
story_html=[]
for img,rev,(et,ft,tt,jt),(eb,fb,tb,jb) in story:
    story_html.append(
      '<div class="story%s">'
      '<img src="%s" alt="" loading="lazy">'
      '<div class="stext"><h3>%s</h3><p>%s</p></div></div>'
      % (' rev' if rev else '', img, t(et,ft,tt,jt), t(eb,fb,tb,jb)))
story_sec=vchapter(
  t("The Story","L'histoire","故事","物語"),
  t("Silk, Safflower &amp; a Samurai House","Soie, carthame &amp; maison de samouraïs","絲綢、紅花與武士之家","絹と紅花、そして武士の家"),
  "".join(story_html))

# 人物
people_html=[]
for (ge,gf,gw,gj),(nm_en,nm_tw,nm_ja),(re,rf,rw,rj),(de,df,dw,dj) in people:
    people_html.append(
      '<div class="figure-card"><div class="gen">%s</div>'
      '<div class="nm">%s</div><div class="role">%s</div>'
      '<div class="fdesc">%s</div></div>'
      % (t(ge,gf,gw,gj), t(nm_en,'',nm_tw,nm_ja), t(re,rf,rw,rj), t(de,df,dw,dj)))
people_sec=vchapter(
  t("The People","Les personnes","織家與人物","人"),
  t("Meet the Family","Rencontrez la famille","認識織家","織家の人々"),
  '<div class="figure-grid">%s</div>' % "".join(people_html))

# 訪問の流れ
flow_html=[]
for step,(te,tf,tw_,tj),(de,df,dw,dj) in visitflow:
    flow_html.append(
      '<div class="tl"><div class="step">STEP %s</div>'
      '<div class="tt">%s</div><div class="td">%s</div></div>'
      % (step, t(te,tf,tw_,tj), t(de,df,dw,dj)))
flow_sec=vchapter(
  t("Your Visit · about 60–90 min","Votre visite · env. 60–90 min","造訪流程 · 約60–90分","ご案内 · 約60〜90分"),
  t("What Happens, Step by Step","Le déroulé, étape par étape","逐步體驗","当日の流れ"),
  '<div class="timeline">%s</div>' % "".join(flow_html))

# ハイライト
hl_html=[]
for img,emo,(ne,nf,nw,nj),(de,df,dw,dj) in highlights:
    hl_html.append(
      '<div class="spot"><img src="%s" alt="" loading="lazy">'
      '<div class="sb"><span class="emoji">%s</span>'
      '<div class="sn">%s</div><div class="sd">%s</div></div></div>'
      % (img, emo, t(ne,nf,nw,nj), t(de,df,dw,dj)))
hl_sec=vchapter(
  t("Highlights","Points forts","亮點","見どころ"),
  t("What You'll Experience","Ce que vous vivrez","您將體驗的","体験できること"),
  '<div class="spots">%s</div>' % "".join(hl_html))

# 色の意味
cc_html=[]
for hexv,(ne,nf,nw,nj),(me,mf,mw,mj) in colorcards:
    cc_html.append(
      '<div class="ccard"><div class="swatch" style="background:%s"></div>'
      '<div class="cb"><div class="cn">%s</div><div class="cm">%s</div></div></div>'
      % (hexv, t(ne,nf,nw,nj), t(me,mf,mw,mj)))
color_sec=vchapter(
  t("Colors &amp; Meaning","Couleurs &amp; sens","色彩與寓意","色と意味"),
  t("A Color for Every Wish","Une couleur pour chaque vœu","每種願望，皆有其色","どの願いにも、ふさわしい色を"),
  '<p class="lead">%s</p><div class="colorgrid">%s</div>' % (
     t("In Japan, each color carries a wish. A dyed silk is not only beautiful — it is a small blessing you can carry.",
       "Au Japon, chaque couleur porte un vœu. Une soie teinte n'est pas seulement belle — c'est une petite bénédiction à emporter.",
       "在日本，每種顏色都承載一份祝願。染就的絲綢不僅美麗，更是可隨身攜帶的小小祝福。",
       "日本では、色それぞれに願いが込められています。染めた絹は美しいだけでなく、持ち歩ける小さなお守りでもあるのです。"),
     "".join(cc_html)))

# 訪問前に
gtk_html="".join('<li>%s</li>'%t(e,f,w,j) for e,f,w,j in goodtoknow)
faq_html="".join('<div class="qa"><div class="q">%s</div><div class="a">%s</div></div>'
                 % (t(qe,qf,qw,qj), t(ae,af,aw,aj)) for (qe,qf,qw,qj),(ae,af,aw,aj) in vfaq)
plan_sec=vchapter(
  t("Plan Your Visit","Préparez votre visite","行前須知","訪問の準備"),
  t("Good to Know","Bon à savoir","實用資訊","知っておきたいこと"),
  '<ul class="notice">%s</ul>'
  '<div class="callout"><div class="ct">%s</div>%s</div>%s'
  % (gtk_html,
     t("BEFORE YOU COME","AVANT DE VENIR","來訪前","お越しになる前に"),
     t("Visits are by reservation and hosted personally by the Nitta family. Please arrange through your travel partner.",
       "Les visites se font sur réservation et sont accueillies par la famille Nitta. Merci de passer par votre partenaire de voyage.",
       "採預約制，由新田家親自接待，請透過您的旅遊夥伴安排。",
       "見学は予約制で、新田家がじきじきにご案内します。旅行会社を通じてお申し込みください。"),
     faq_html))

visitor_block="\n".join([intro_sec, story_sec, people_sec, flow_sec, hl_sec, color_sec, plan_sec])

# CTA（trade・4言語）
cta_eyebrow=t("For the travel trade","Pour les professionnels du voyage","旅遊業者專用","旅行業の皆さまへ")
cta_title=t("Bring this experience to your clients","Offrez cette expérience à vos clients","為您的客戶帶來這場體驗","この体験を、お客さまへ")
cta_link=t("View the tariff →","Voir le tarif →","查看報價 →","タリフを見る →")

# ============================================================
#  ガイド向け（Staff Only）：従来どおり
# ============================================================
scene_html=[]
for n,title,std,hl,note,jp,en,tip in B.scenes:
    note_html='<div class="note"><span class="lbl">動線・準備</span>%s</div>'%note if note else ""
    tip_html='<div class="tip"><span class="lbl">💡 ガイドTips</span>%s</div>'%tip if tip else ""
    scene_html.append('''<section class="scene" id="s{n}">
  <div class="scene-head"><span class="snum">{n:02d}</span><h3>{title}</h3><span class="mins">標準 {std} ／ ハイライト {hl}</span></div>
  {note}
  <div class="cols">
    <div class="col j"><div class="flag">🇯🇵 日本語（新田さん）</div>{jp}</div>
    <div class="col e"><div class="flag">🇺🇸 English (guide)</div>{en}</div>
  </div>
  {tip}
</section>'''.format(n=n,title=title,std=std,hl=hl,note=note_html,jp=paras(jp),en=paras(en),tip=tip_html))

nav_html="".join('<a href="#s{n}">{n:02d} {t}</a>'.format(n=n,t=title) for n,title,_,_,_,_,_,_ in B.scenes)
faq_rows="".join('<tr><td class="q"><b>Q.</b> {jq}<div class="en2">{eq}</div></td><td>{ja}<div class="en2">{ea}</div></td></tr>'.format(jq=q,eq=eq,ja=a,ea=ea) for q,a,eq,ea in B.faq)
gloss_rows="".join('<tr><td>{a}</td><td>{b}</td><td class="sub">{c}</td></tr>'.format(a=a,b=b,c=c) for a,b,c in B.glossary)
timing_rows="".join('<tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{d}</td></tr>'.format(a=a,b=b,c=c,d=d) for a,b,c,d in B.timing)
color_rows="".join('<tr><td>{a}</td><td>{b}</td><td class="sub">{c}</td></tr>'.format(a=a,b=b,c=c) for a,b,c in B.colors)
aud_rows="".join('<tr><td><b>{a}</b></td><td>{b}</td></tr>'.format(a=a,b=b) for a,b in B.audience)
phrase_rows="".join('<tr><td>{a}</td><td class="e2">{b}</td><td class="e2">{c}</td><td class="e2">{d}</td></tr>'.format(a=a,b=b,c=c,d=d) for a,b,c,d in phrases)

HTML='''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="robots" content="noindex,nofollow">
<title>新田織物 コンテンツガイド｜PLAT YONEZAWA</title>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600&family=Shippori+Mincho:wght@400;500;600;700&family=Noto+Serif+TC:wght@500;600&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<style>
:root{--bg:#fbf6f1;--paper:#f3ede2;--card:#fff;--ink:#2b201d;--muted:#7f7166;--deep:#2e1f1c;--deep2:#3a2a24;--gold:#a8893a;--gold-deep:#6b5418;--gold-soft:#d4c084;--line:#e4d8c8;--accent:#a83a2b;
--f-ja:'Shippori Mincho',serif;--f-en:'Cormorant Garamond','Shippori Mincho',serif;--f-tw:'Noto Serif TC',serif;--f-ui:'Inter','Shippori Mincho',sans-serif;}
*{box-sizing:border-box;margin:0;padding:0}
body{background:var(--bg);color:var(--ink);font-family:var(--f-ja);line-height:1.85;font-size:16px}
.wrap{max-width:1040px;margin:0 auto;padding:0 24px}
/* language visibility (EN fallback via JS) */
.en,.fr,.tw,.ja,.j,.e{}
.fr,.tw,.ja{display:none}
body.lang-fr .fr{display:initial}body.lang-fr .en{display:none}
body.lang-tw .tw{display:initial}body.lang-tw .en{display:none}
body.lang-ja .ja{display:initial}body.lang-ja .en{display:none}
body.lang-tw{font-family:var(--f-tw)}
body.lang-ja{font-family:var(--f-ja)}
/* mode visibility */
body.mode-visitor .guide-only{display:none}
body.mode-guide .visitor-only{display:none}
/* switcher (image準拠・2段) */
.sw{position:sticky;top:0;z-index:50}
.sw .brandbar{background:var(--deep);display:flex;align-items:center;gap:12px;padding:8px 24px}
.sw .brand{font-family:var(--f-en);font-weight:600;letter-spacing:.2em;color:#f3e9dd;font-size:14px}
.sw .badge{font-family:var(--f-ui);font-size:9px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:#fff;background:var(--accent);padding:3px 8px;border-radius:999px}
.sw .row{display:flex;background:var(--deep2)}
.sw .row.langs{background:var(--deep)}
.sw button{flex:1;background:transparent;border:none;color:rgba(243,233,221,.7);font-family:var(--f-ui);font-size:14px;padding:13px 8px;cursor:pointer;border-bottom:3px solid transparent;letter-spacing:.04em}
.sw .row.langs button{border-bottom-color:transparent}
.sw button:hover{color:#fff}
.sw button.active{color:#fff;border-bottom-color:var(--gold-soft)}
.sw .row.modes button.active{border-bottom-color:var(--accent)}
.sw button.hide{display:none}
.sw .lock{font-size:12px;opacity:.85}
/* hero */
.hero{background:linear-gradient(160deg,#2e1f1c,#1c100e);color:#f3e9dd;padding:44px 0 40px}
.hero .eyebrow{font-family:var(--f-ui);letter-spacing:.28em;text-transform:uppercase;font-size:11px;color:var(--gold-soft)}
.hero h1{font-weight:600;font-size:32px;margin:10px 0 6px;color:#fff}
.hero h1.en,.hero h1.fr{font-family:var(--f-en)} .hero h1.tw{font-family:var(--f-tw)} .hero h1.ja{font-family:var(--f-ja)}
.hero .sub{font-family:var(--f-en);font-style:italic;color:var(--gold-soft);font-size:18px}
/* ===== visitor : rich components (上杉ガイド準拠・新田パレット) ===== */
.hero-photo{display:block;width:100%;height:min(46vw,420px);object-fit:cover;border-radius:14px;margin:22px 0 4px;border:1px solid var(--line);box-shadow:0 12px 34px rgba(46,31,28,.18)}
.hero-cap{font-family:var(--f-ui);font-size:11px;color:var(--muted);text-align:center;letter-spacing:.08em;margin:0 0 8px}
.vchapter{background:#fff;border:1px solid var(--line);border-radius:16px;padding:30px 32px;margin:22px 0;box-shadow:0 3px 20px rgba(46,31,28,.05);position:relative;overflow:hidden}
.vchapter::before{content:"";position:absolute;top:0;left:32px;right:32px;height:3px;background:linear-gradient(90deg,transparent,var(--gold-soft) 22%,var(--gold) 50%,var(--gold-soft) 78%,transparent)}
.vchapter .kicker{font-family:var(--f-ui);letter-spacing:.26em;text-transform:uppercase;font-size:10.5px;color:var(--gold-deep);margin-bottom:8px}
.vchapter h2{font-family:var(--f-en);font-size:27px;color:var(--deep);border-left:5px solid var(--accent);padding-left:15px;line-height:1.25;margin-bottom:4px}
.lead{font-family:var(--f-en);font-size:17px;color:var(--ink);margin:6px 0 16px;line-height:1.85}
/* brand video */
.video-wrap{margin:8px 0 2px;background:#000;border:1px solid var(--line);border-radius:14px;overflow:hidden;box-shadow:0 12px 30px rgba(46,31,28,.16)}
.video-wrap video{display:block;width:100%;height:auto}
.video-cap{background:var(--deep);color:rgba(243,233,221,.8);font-family:var(--f-ui);font-size:11px;letter-spacing:.06em;text-align:center;padding:9px 12px}
/* story rows */
.story{display:grid;grid-template-columns:0.95fr 1.05fr;gap:26px;align-items:center;margin:22px 0}
.story img{width:100%;height:270px;object-fit:cover;border-radius:12px;border:1px solid var(--line)}
.story.rev img{order:2}
.story h3{font-family:var(--f-en);font-size:22px;color:var(--deep);margin-bottom:8px}
.story p{font-family:var(--f-en);font-size:16px}
@media(max-width:800px){.story{grid-template-columns:1fr;gap:14px}.story.rev img{order:0}.story img{height:220px}}
/* figure cards */
.figure-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(210px,1fr));gap:14px;margin:16px 0 2px}
.figure-card{background:var(--paper);border:1px solid var(--line);border-radius:12px;padding:16px 18px}
.figure-card .gen{font-family:var(--f-ui);font-size:9.5px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:var(--gold-deep)}
.figure-card .nm{font-family:var(--f-en);font-size:19px;color:var(--deep);margin:3px 0 1px}
.figure-card .role{font-family:var(--f-ui);font-size:11.5px;color:var(--accent);font-weight:600}
.figure-card .fdesc{font-family:var(--f-en);font-size:14px;color:var(--ink);margin-top:8px;line-height:1.6}
/* timeline (your visit) */
.timeline{position:relative;margin:14px 0 2px;padding-left:28px;border-left:2.5px solid var(--gold-soft)}
.tl{position:relative;margin-bottom:20px}
.tl::before{content:"";position:absolute;left:-35px;top:5px;width:11px;height:11px;background:var(--accent);border-radius:50%;border:3px solid var(--bg);box-shadow:0 0 0 2px var(--accent)}
.tl .step{font-family:var(--f-ui);font-size:10px;font-weight:700;letter-spacing:.2em;color:var(--gold-deep)}
.tl .tt{font-family:var(--f-en);font-size:18px;color:var(--deep);font-weight:600;margin:1px 0 3px}
.tl .td{font-family:var(--f-en);font-size:14.5px;color:var(--muted)}
/* highlight spots */
.spots{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:16px;margin:16px 0 2px}
.spot{background:#fff;border:1px solid var(--line);border-radius:14px;overflow:hidden;box-shadow:0 2px 12px rgba(46,31,28,.06);transition:transform .2s,box-shadow .2s}
.spot:hover{transform:translateY(-3px);box-shadow:0 12px 28px rgba(46,31,28,.14)}
.spot img{display:block;width:100%;height:180px;object-fit:cover;border-bottom:1px solid var(--line)}
.spot .sb{padding:14px 16px 16px}
.spot .emoji{font-size:22px;line-height:1}
.spot .sn{font-family:var(--f-en);font-size:17px;color:var(--deep);font-weight:600;margin:5px 0 3px}
.spot .sd{font-family:var(--f-en);font-size:14px;color:var(--muted);line-height:1.6}
/* color cards */
.colorgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:12px;margin:14px 0 2px}
.ccard{border:1px solid var(--line);border-radius:12px;overflow:hidden;background:#fff}
.ccard .swatch{height:62px}
.ccard .cb{padding:11px 14px}
.ccard .cn{font-family:var(--f-en);font-weight:600;color:var(--deep);font-size:16px}
.ccard .cm{font-family:var(--f-en);font-size:12.5px;color:var(--muted);margin-top:3px;line-height:1.5}
/* callout / notice / qa */
.callout{background:linear-gradient(135deg,#fbf3dc,#f6ebc6);border-left:5px solid var(--gold);border-radius:0 10px 10px 0;padding:16px 20px;margin:18px 0;font-family:var(--f-en);font-size:15px}
.callout .ct{font-family:var(--f-ui);font-weight:700;font-size:12px;letter-spacing:.12em;color:var(--gold-deep);margin-bottom:5px}
.notice{list-style:none;margin:6px 0 2px}
.notice li{position:relative;padding:10px 0 10px 26px;border-bottom:1px dotted var(--line);font-family:var(--f-en);font-size:15px}
.notice li:last-child{border-bottom:none}
.notice li::before{content:"✦";position:absolute;left:3px;color:var(--gold);top:10px}
.qa{background:var(--paper);border-left:4px solid var(--deep);border-radius:0 10px 10px 0;padding:14px 20px;margin:12px 0}
.qa .q{font-family:var(--f-en);font-weight:600;color:var(--deep);font-size:15.5px}
.qa .q::before{content:"Q. ";color:var(--accent);font-weight:700}
.qa .a{font-family:var(--f-en);font-size:14.5px;color:var(--ink);margin-top:6px;padding-left:22px;position:relative}
.qa .a::before{content:"A.";position:absolute;left:0;color:var(--gold-deep);font-weight:700}
/* 繁中フォント上書き */
body.lang-tw .vchapter h2,body.lang-tw .lead,body.lang-tw .story h3,body.lang-tw .story p,body.lang-tw .figure-card .nm,body.lang-tw .figure-card .fdesc,body.lang-tw .tl .tt,body.lang-tw .tl .td,body.lang-tw .spot .sn,body.lang-tw .spot .sd,body.lang-tw .ccard .cn,body.lang-tw .ccard .cm,body.lang-tw .callout,body.lang-tw .notice li,body.lang-tw .qa .q,body.lang-tw .qa .a,body.lang-tw .video-cap,body.lang-tw .vcta-title{font-family:var(--f-tw)}
/* 日本語フォント上書き */
body.lang-ja .vchapter h2,body.lang-ja .lead,body.lang-ja .story h3,body.lang-ja .story p,body.lang-ja .figure-card .nm,body.lang-ja .figure-card .fdesc,body.lang-ja .tl .tt,body.lang-ja .tl .td,body.lang-ja .spot .sn,body.lang-ja .spot .sd,body.lang-ja .ccard .cn,body.lang-ja .ccard .cm,body.lang-ja .callout,body.lang-ja .notice li,body.lang-ja .qa .q,body.lang-ja .qa .a,body.lang-ja .video-cap,body.lang-ja .vcta-title{font-family:var(--f-ja)}
/* CTA */
.vcta{background:var(--deep);color:#f3e9dd;border-radius:14px;padding:28px;margin:22px 0;text-align:center}
.vcta-eyebrow{font-family:var(--f-ui);font-size:11px;letter-spacing:.2em;text-transform:uppercase;color:var(--gold-soft)}
.vcta-title{font-family:var(--f-en);font-size:22px;margin:6px 0 2px}
.vcta a{display:inline-block;margin-top:12px;font-family:var(--f-ui);font-size:13px;font-weight:600;background:var(--gold-deep);color:#fff;padding:13px 28px;border-radius:6px;text-decoration:none;min-height:48px;line-height:22px}
/* guide gate */
.gate{background:#fff;border:1px solid var(--line);border-radius:14px;padding:40px 30px;text-align:center;margin:26px 0;max-width:460px;margin-left:auto;margin-right:auto}
body.guide-unlocked .gate{display:none}
body:not(.guide-unlocked) .guide-body{display:none}
.gate .lockicon{font-size:40px}
.gate h2{font-family:var(--f-ja);font-size:20px;color:var(--deep);margin:8px 0 6px}
.gate p{font-size:13px;color:var(--muted);margin-bottom:18px}
.gate input{width:100%;font-family:var(--f-ui);font-size:16px;padding:12px 14px;border:1.5px solid var(--line);border-radius:8px;margin-bottom:12px}
.gate button{width:100%;font-family:var(--f-ui);font-size:14px;font-weight:700;background:var(--deep);color:var(--gold-soft);border:none;border-radius:8px;padding:13px;cursor:pointer;min-height:48px}
.gate .note{font-size:11px;color:#a89;margin-top:12px}
/* guide body */
h2.sec{font-family:var(--f-ja);font-size:23px;color:var(--deep);margin:40px 0 14px;padding-bottom:8px;border-bottom:2px solid var(--gold-soft)}
.info{background:var(--card);border:1px solid var(--line);border-left:4px solid var(--gold);border-radius:8px;padding:16px 20px;margin:22px 0;font-size:14px}
.info b{color:var(--deep)}
table{width:100%;border-collapse:collapse;font-size:13.5px;background:#fff;border:1px solid var(--line);border-radius:8px;overflow:hidden;margin:10px 0}
th,td{text-align:left;padding:9px 11px;border-bottom:1px solid var(--line);vertical-align:top}
th{background:var(--paper);font-family:var(--f-ui);font-size:11px;color:var(--muted);text-transform:uppercase}
td.sub,.en2{color:var(--muted);font-size:12px;font-family:var(--f-ui)} .en2{margin-top:3px} .e2{font-family:var(--f-ui);font-size:13px}
.scenenav{background:var(--paper);border:1px solid var(--line);border-radius:10px;padding:14px 16px;margin:16px 0}
.scenenav a{display:inline-block;font-family:var(--f-ui);font-size:12px;color:var(--deep);background:#fff;border:1px solid var(--line);border-radius:6px;padding:4px 9px;margin:3px 3px 0 0;text-decoration:none}
.scene{background:#fff;border:1px solid var(--line);border-radius:12px;padding:22px 24px;margin:14px 0;scroll-margin-top:120px}
.scene-head{display:flex;align-items:baseline;gap:10px;flex-wrap:wrap;border-bottom:1px solid var(--line);padding-bottom:10px;margin-bottom:12px}
.snum{font-family:var(--f-en);font-size:28px;color:var(--gold)}
.scene-head h3{font-family:var(--f-ja);font-size:19px;color:var(--deep);flex:1}
.mins{font-family:var(--f-ui);font-size:11px;color:var(--muted)}
.note{background:#f7f3ea;border:1px solid var(--line);border-radius:8px;padding:9px 13px;margin-bottom:12px;font-size:13px}
.note .lbl,.tip .lbl{display:block;font-family:var(--f-ui);font-size:10px;font-weight:700;color:var(--muted);margin-bottom:2px;text-transform:uppercase}
.cols{display:grid;grid-template-columns:1fr 1fr;gap:20px}
.col .flag{font-family:var(--f-ui);font-size:11px;font-weight:700;color:var(--muted);margin-bottom:6px;border-bottom:1px dashed var(--line);padding-bottom:3px}
.col.e{font-family:var(--f-en);font-size:15px} .col p{margin-bottom:11px}
.tip{background:#fbf3dc;border:1px solid var(--gold-soft);border-radius:8px;padding:9px 13px;margin-top:12px;font-size:12.5px;color:var(--gold-deep)}
@media(max-width:800px){.cols{grid-template-columns:1fr}}
footer{background:var(--deep);color:rgba(243,233,221,.7);font-family:var(--f-ui);font-size:12px;text-align:center;padding:24px;margin-top:38px}
</style>
<script src="/assets/site.js" defer></script>
</head>
<body class="mode-visitor lang-en">
<div class="sw">
  <div class="brandbar"><span class="brand">PLAT YONEZAWA</span><span class="badge">Nitta Textile</span></div>
  <div class="row langs">
    <button data-lang="ja" data-modes="visitor,guide">🇯🇵 日本語</button>
    <button data-lang="en" data-modes="visitor,guide" class="active">🇺🇸 English</button>
    <button data-lang="fr" data-modes="visitor">🇫🇷 Français</button>
    <button data-lang="tw" data-modes="visitor">🇹🇼 繁體中文</button>
  </div>
  <div class="row modes">
    <button data-mode="visitor" class="active">🧭 <span style="margin-left:4px">Visitors</span></button>
    <button data-mode="guide">🔑 <span style="margin-left:4px">Staff Only — Guide Team</span></button>
  </div>
</div>

<header class="hero"><div class="wrap">
  <div class="eyebrow">Nitta Textile · 米沢織・紅花染</div>
  <h1 class="en">Nitta Textile</h1><h1 class="fr">Nitta Textile</h1><h1 class="tw">新田織物</h1><h1 class="ja">新田織物</h1>
  <div class="sub">Silk &amp; Safflower — a samurai family, weaving for five generations</div>
</div></header>

<div class="wrap">

  <!-- ===== VISITOR (public) ===== -->
  <div class="visitor-only">
    <img class="hero-photo" src="images/shot-01.jpg" alt="Naturally-dyed silk threads at Nitta Textile" loading="lazy">
    <div class="hero-cap">{herocap}</div>

    {visitor}

    <div class="vcta">
      <div class="vcta-eyebrow">{cta_eyebrow}</div>
      <div class="vcta-title">{cta_title}</div>
      <a href="/tariff/tariff_C-NTA-01.html">{cta_link}</a>
    </div>
  </div>

  <!-- ===== GUIDE (auth) ===== -->
  <div class="guide-only">
    <!-- 暫定ゲート（クライアント側・叩き台）：本番は Cloudflare Access（メール認証）に置換 -->
    <div class="gate">
      <div class="lockicon">🔑</div>
      <h2>Staff Only — Guide Team</h2>
      <p>For guide-team members only. Register your email to view.<br><span style="font-size:12px">ガイドチーム専用です。メールアドレスを登録してご覧ください。</span></p>
      <form id="gateForm" autocomplete="off">
        <input id="gEmail" type="email" placeholder="you@example.com" required>
        <button type="submit">Access the guide →</button>
      </form>
      <div class="note">Interim gate (prototype): client-side registration for now. Production will be protected by <b>Cloudflare Access</b> (email login · 3-hour session · email logged to CRM).</div>
    </div>

    <div class="guide-body">
      <div class="info">
        <div><b>施設</b>：株式会社新田（米沢織・紅花染め工房／米沢市／明治17年〈1884年〉創業）</div>
        <div><b>想定時間</b>：約60〜90分（フル）／30分（ハイライト）　<b>構成</b>：玄関→ギャラリー→お茶室→お庭→紅花染め体験→2階工場→ショールーム→お見送り</div>
        <div><b>使い方</b>：日本語＝新田さん本人用／英語＝ガイド・通訳用。〔 〕＝ステージディレクション。仏・繁中は下部「現場フレーズ集」を参照。</div>
      </div>
      <h2 class="sec">👥 登場人物（新田家）</h2>
      <table><tr><th>世代</th><th>お名前</th><th>役職</th><th>役割</th></tr>
      <tr><td>3代目</td><td><b>新田 秀治・富子</b></td><td>創業者の孫</td><td>紅花染め復興／紅花紬発表(1966)</td></tr>
      <tr><td>4代目</td><td><b>新田 英行</b></td><td>代表取締役会長</td><td>本ガイドの語り手</td></tr>
      <tr><td>5代目</td><td><b>新田 源太郎</b></td><td>代表取締役社長</td><td>現役の作り手／落合陽一氏コラボ</td></tr></table>

      <h2 class="sec">🗣 現場フレーズ集（仏・繁中の言い回し）</h2>
      <table><tr><th>場面</th><th>English</th><th>Français</th><th>繁體中文</th></tr>{phrases}</table>

      <div class="scenenav">{nav}</div>
      <h2 class="sec">🎬 シーン別スクリプト</h2>
      {scenes}

      <h2 class="sec">❓ 想定FAQ</h2><table><tr><th style="width:44%">Q</th><th>A</th></tr>{faq}</table>
      <h2 class="sec">🎨 色の意味</h2><table><tr><th>色</th><th>意味</th><th>Meaning</th></tr>{colors}</table>
      <h2 class="sec">📚 用語集（日英）</h2><table><tr><th>日本語</th><th>English</th><th>補足</th></tr>{gloss}</table>
      <h2 class="sec">⏱ タイミング表</h2><table><tr><th>#</th><th>シーン</th><th>標準</th><th>ハイライト</th></tr>{timing}</table>
      <h2 class="sec">🌏 客層別ハイライト</h2><table><tr><th style="width:210px">客層</th><th>推し要素</th></tr>{aud}</table>
    </div>
  </div>

</div>
<footer>© 2026 PLAT YONEZAWA, Inc. ・ Nitta Textile Content Guide<br>Visitors = public ／ Staff Only = authenticated (interim gate; production via Cloudflare Access)</footer>

<script>
(function(){
  var body=document.body;
  var langBtns=document.querySelectorAll('.sw .langs button');
  var modeBtns=document.querySelectorAll('.sw .modes button');
  function applyFallback(){
    // 未訳spanはEN表示（fr/tw/ja選択時）
    var lang=(body.className.match(/lang-(\\w+)/)||[])[1];
    document.querySelectorAll('span.en').forEach(function(en){
      en.style.display='';
      if(lang==='en'||!lang)return;
      var p=en.parentNode; var act=p.querySelector(':scope > span.'+lang);
      if(!act || !act.textContent.trim()) en.style.display='initial';
    });
  }
  function setLang(l){
    body.className=body.className.replace(/lang-\\w+/,'').trim()+' lang-'+l;
    langBtns.forEach(function(b){b.classList.toggle('active',b.dataset.lang===l);});
    applyFallback();
  }
  function availLangs(mode){var r=[];langBtns.forEach(function(b){var ok=b.dataset.modes.split(',').indexOf(mode)>=0;b.classList.toggle('hide',!ok);if(ok)r.push(b.dataset.lang);});return r;}
  function setMode(m){
    body.className=body.className.replace(/mode-\\w+/,'').trim();
    body.classList.add('mode-'+m);
    modeBtns.forEach(function(b){b.classList.toggle('active',b.dataset.mode===m);});
    var av=availLangs(m);
    var cur=(body.className.match(/lang-(\\w+)/)||[])[1];
    if(av.indexOf(cur)<0) setLang(m==='guide'?'ja':'en'); else applyFallback();
  }
  langBtns.forEach(function(b){b.addEventListener('click',function(){setLang(b.dataset.lang);});});
  modeBtns.forEach(function(b){b.addEventListener('click',function(){setMode(b.dataset.mode);});});
  // 暫定ゲート
  var gf=document.getElementById('gateForm');
  if(gf){
    // 既登録なら解錠
    try{ if(localStorage.getItem('nitta_guide_email')) body.classList.add('guide-unlocked'); }catch(e){}
    gf.addEventListener('submit',function(e){
      e.preventDefault();
      var v=(document.getElementById('gEmail').value||'').trim();
      if(!/^[^@\\s]+@[^@\\s]+\\.[^@\\s]+$/.test(v)) return;
      try{ localStorage.setItem('nitta_guide_email', v); }catch(e){}
      body.classList.add('guide-unlocked');
      // TODO(本番): ここでメールをCRM(HubSpot)へ送信 or Cloudflare Accessに委譲
    });
  }
  setMode('visitor'); setLang('en');
})();
</script>
</body>
</html>'''

herocap=t("Threads dyed with safflower and other natural plants, Nitta Textile atelier.",
          "Fils teints au carthame et à d'autres plantes naturelles, atelier Nitta.",
          "以紅花及天然植物染成的絲線，新田織物工房。",
          "紅花などの自然の植物で染めた糸。新田織物の工房にて。")

for k,v in {'{herocap}':herocap,'{visitor}':visitor_block,
            '{cta_eyebrow}':cta_eyebrow,'{cta_title}':cta_title,'{cta_link}':cta_link,
            '{phrases}':phrase_rows,'{nav}':nav_html,'{scenes}':"\n".join(scene_html),
            '{faq}':faq_rows,'{colors}':color_rows,'{gloss}':gloss_rows,'{timing}':timing_rows,'{aud}':aud_rows}.items():
    HTML=HTML.replace(k,v)
open(OUT,'w',encoding='utf-8').write(HTML)
print('written',OUT,'bytes',len(HTML))
