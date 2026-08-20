# -*- coding: utf-8 -*-
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import nitta_content as B   # scenes, faq, glossary, timing, colors, audience
OUT=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','nitta-guide.html')

# ---- ビジター向け（公開・EN/FR/繁中）----
visitor=[
 ("A Samurai Family, Weaving for Five Generations","Une famille de samouraïs, cinq générations de tissage","武士家族，五代織藝傳承",
  "For over 140 years, the Nitta family has woven silk in Yonezawa. Founded in 1884, we were originally a samurai family who turned to textiles when the age of the sword ended. This house, built in 1925, is over 100 years old — and the 4th and 5th generations still weave here today.",
  "Depuis plus de 140 ans, la famille Nitta tisse la soie à Yonezawa. Fondée en 1884, notre famille était à l'origine une famille de samouraïs qui se tourna vers le textile à la fin de l'ère du sabre. Cette maison, bâtie en 1925, a plus de 100 ans — et les 4e et 5e générations y tissent encore aujourd'hui.",
  "一百四十多年來，新田家族在米澤織就絲綢。我們1884年創業，原是武士家族，於刀劍時代結束後轉投紡織。這棟宅邸建於1925年，已逾百年——第四代與第五代至今仍在此織布。"),
 ("The Lord Who Turned Poverty into Craft","Le seigneur qui fit de la pauvreté un art","化貧困為工藝的藩主",
  "Yonezawa was once a poor domain. Its 9th lord, Yozan Uesugi, encouraged his samurai to take up crafts — weaving, dyeing, papermaking — that could be done at home. Silk weaving became the town's soul, and 250 years later that spirit still lives here.",
  "Yonezawa fut jadis un domaine pauvre. Son 9e seigneur, Yozan Uesugi, encouragea ses samouraïs à pratiquer des métiers — tissage, teinture, papier — réalisables à la maison. Le tissage de la soie devint l'âme de la ville, et 250 ans plus tard cet esprit demeure.",
  "米澤昔為貧困之藩。第九代藩主上杉鷹山鼓勵武士從事可在家中進行的工藝——織布、染色、造紙。絲織遂成城市之魂，二百五十年後，這份精神依然長存。"),
 ("Benibana — The Red of Yamagata","Benibana — le rouge de Yamagata","紅花——山形之紅",
  "Our signature is benibana (safflower) dyeing — a red once as valuable as gold. Revived by the family in the 1960s, it is dyed only in winter, when the cold brings out the most beautiful red. From one flower we draw red and yellow, and with other plants, green and purple.",
  "Notre signature est la teinture au benibana (carthame) — un rouge jadis aussi précieux que l'or. Ressuscitée dans les années 1960, elle ne se teint qu'en hiver, quand le froid révèle le plus beau rouge. D'une seule fleur naissent le rouge et le jaune, et avec d'autres plantes, le vert et le violet.",
  "我們的招牌是紅花染——一種曾與黃金等值的紅。家族於1960年代復興此技，僅於冬季染製，愈寒冷，紅色愈美。一朵花可取紅與黃，並與其他植物調出綠與紫。"),
 ("What You'll Experience","Ce que vous vivrez","您將體驗的",
  "A private visit into a living workshop: a four-season garden seen through 100-year-old glass; a pillar-less tea room co-created with media artist Yoichi Ochiai; a century-old Jacquard loom still running; and dyeing your own safflower handkerchief — one of a kind in the world.",
  "Une visite privée au cœur d'un atelier vivant : un jardin aux quatre saisons vu à travers un verre centenaire ; un salon de thé sans pilier, co-créé avec l'artiste Yoichi Ochiai ; un métier Jacquard centenaire toujours en marche ; et la teinture de votre propre mouchoir au carthame — unique au monde.",
  "一場走進活工坊的私人造訪：透過百年玻璃眺望的四季庭園；與媒體藝術家落合陽一共創的無柱茶室；仍在運轉的百年提花織機；並親手染製專屬您的紅花手帕——世上僅此一件。"),
 ("Good to Know","Bon à savoir","實用資訊",
  "Duration about 60–90 minutes. Handkerchief dyeing is available year-round. Kimono and obi are made to measure. Each September, Yonezawa opens its workshops for the “Open Factory” event.",
  "Durée : environ 60 à 90 minutes. La teinture de mouchoir est proposée toute l'année. Kimonos et obis sont faits sur mesure. Chaque septembre, Yonezawa ouvre ses ateliers lors de l'« Open Factory ».",
  "體驗約60〜90分鐘。手帕染色全年皆可。和服與腰帶皆為量身訂製。每年九月，米澤舉辦「Open Factory」開放工坊活動。"),
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

# guide scenes (ja/en) reuse
scene_html=[]
for n,title,std,hl,note,jp,en,tip in B.scenes:
    note_html='<div class="note"><span class="lbl">動線・準備</span>%s</div>'%note if note else ""
    tip_html='<div class="tip"><span class="lbl">💡 ガイドTips</span>%s</div>'%tip if tip else ""
    scene_html.append('''<section class="scene" id="s{n}">
  <div class="scene-head"><span class="snum">{n:02d}</span><h3>{title}</h3><span class="mins">標準 {std} ／ ハイライト {hl}</span></div>
  {note}
  <div class="cols">
    <div class="col j"><div class="flag">🇯🇵 日本語（新田さん）</div>{jp}</div>
    <div class="col e"><div class="flag">🇬🇧 English (guide)</div>{en}</div>
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

vis_html=[]
for en_t,fr_t,tw_t,en,fr,tw in visitor:
    vis_html.append('''<section class="vsec">
  <h3><span class="en">{et}</span><span class="fr">{ft}</span><span class="tw">{tt}</span></h3>
  <p><span class="en">{e}</span><span class="fr">{f}</span><span class="tw">{t}</span></p>
</section>'''.format(et=en_t,ft=fr_t,tt=tw_t,e=en,f=fr,t=tw))

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
.en,.fr,.tw,.j,.e{}
.fr,.tw{display:none}
body.lang-fr .fr{display:initial}body.lang-fr .en{display:none}
body.lang-tw .tw{display:initial}body.lang-tw .en{display:none}
body.lang-tw{font-family:var(--f-tw)}
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
.hero h1.en,.hero h1.fr{font-family:var(--f-en)} .hero h1.tw{font-family:var(--f-tw)}
.hero .sub{font-family:var(--f-en);font-style:italic;color:var(--gold-soft);font-size:18px}
/* visitor */
.vsec{background:#fff;border:1px solid var(--line);border-radius:12px;padding:22px 26px;margin:16px 0}
.vsec h3{font-family:var(--f-en);font-size:23px;color:var(--deep);margin-bottom:8px}
body.lang-tw .vsec h3{font-family:var(--f-tw)}
.vsec p{font-family:var(--f-en);font-size:16.5px}
body.lang-tw .vsec p{font-family:var(--f-tw)}
.vcta{background:var(--deep);color:#f3e9dd;border-radius:12px;padding:26px;margin:18px 0;text-align:center}
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
    <button data-lang="ja" data-modes="guide">🇯🇵 日本語</button>
    <button data-lang="en" data-modes="visitor,guide" class="active">🇬🇧 English</button>
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
  <h1 class="en">Nitta Textile</h1><h1 class="fr">Nitta Textile</h1><h1 class="tw">新田織物</h1>
  <div class="sub">Silk &amp; Safflower — a samurai family, weaving for five generations</div>
</div></header>

<div class="wrap">

  <!-- ===== VISITOR (public) ===== -->
  <div class="visitor-only">
    {visitor}
    <div class="vcta">
      <div style="font-family:var(--f-ui);font-size:11px;letter-spacing:.2em;text-transform:uppercase;color:var(--gold-soft)">For the travel trade</div>
      <div style="font-family:var(--f-en);font-size:22px;margin:6px 0 2px">Bring this experience to your clients</div>
      <a href="/tariff/tariff_C-NTA-01.html"><span class="en">View the tariff →</span><span class="fr">Voir le tarif →</span><span class="tw">查看報價 →</span></a>
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
    // 未訳spanはEN表示（fr/tw選択時）
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
for k,v in {'{visitor}':"\n".join(vis_html),'{phrases}':phrase_rows,'{nav}':nav_html,'{scenes}':"\n".join(scene_html),
            '{faq}':faq_rows,'{colors}':color_rows,'{gloss}':gloss_rows,'{timing}':timing_rows,'{aud}':aud_rows}.items():
    HTML=HTML.replace(k,v)
open(OUT,'w',encoding='utf-8').write(HTML)
print('written',OUT,'bytes',len(HTML))
