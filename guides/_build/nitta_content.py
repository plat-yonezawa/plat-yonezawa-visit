# -*- coding: utf-8 -*-
import os as _os
# 新田織物 コンテンツガイド（ガイド育成用）ページ生成
OUT=_os.path.join(_os.path.dirname(_os.path.abspath(__file__)),'_nitta_single_preview.html')

def esc(s): return s

# scenes: (n, title, std, hl, note(html or None), jp(list), en(list), tip(html or None))
scenes = [
(1,"玄関・ご挨拶","3分","2分",
 "玄関で靴を脱いでいただく（スリッパ）。「足のままで大丈夫ですか？」と一声。ご年配には腰掛けを用意。",
 ["新田です。本日は遠いところ、ようこそお越しくださいました。私、<b>新田英行</b>と申します。会社では会長を務めております。",
  "このお家は<b>1925年（大正14年）</b>に建てられたもので、<b>今年でちょうど築101年</b>になります。私で<b>4代目</b>、いま大阪に出ております息子の<b>源太郎</b>が<b>5代目</b>の社長として後を継いでくれています。",
  "もともと、うちは<b>侍の家系</b>です。約120年前、明治政府が「武士はもう要らない」と決めたときに、この織物ビジネスに完全に切り替えました。会社としては<b>明治17年（1884年）創業</b>、それ以来ずっとこの場所で織物を続けています。",
  "今日は、米沢の織物の歴史と、うちで守っている<b>紅花染め</b>という技術をご紹介します。ゆっくり見ていってください。"],
 ["Welcome to Nitta. Thank you so much for coming all the way to Yonezawa. My name is <b>Hideyuki Nitta</b>, the <b>4th-generation Chairman</b>.",
  "This house was built in <b>1925 — exactly 101 years old this year</b>. My son <b>Gentaro Nitta</b>, currently based in Osaka, is the <b>5th-generation President</b>, carrying on the business.",
  "Our family was originally a <b>samurai family</b>. About 120 years ago, when the Meiji government decided Japan no longer needed samurai, our family switched completely to this textile business. The company was officially founded in <b>1884 (Meiji 17)</b>, and we have been weaving in this place ever since.",
  "Today, I'd like to share the history of Yonezawa textiles and the natural dyeing technique called <b>benibana-zome (safflower dyeing)</b> that our family has preserved. Please take your time."],
 "「サムライ家系」は欧米客に必ず刺さるので最初に言う。明治政府＝1868年、廃刀令＝1876年（120年前ストーリーの根拠）。"),
(2,"ギャラリー — 上杉鷹山の物語","8分","4分",
 "鷹山公の肖像・展示物の前へ。養蚕の繭・生糸・綿状シルクをトレイで提示。袴のミニチュア/実物も。",
 ["こちらが米沢藩9代藩主、<b>上杉鷹山公</b>です。この方を知っていただくと、米沢のものづくりがすべてつながります。",
  "米沢藩は江戸時代、非常に貧しい藩でした。16世紀末の大きな内戦で上杉家は「<b>負け組</b>」に入り、徳川幕府に領地を大きく減らされた。税収は減ったのに家臣の数は多い、という苦しい状態でした。",
  "そこで鷹山公は武士に「<b>刀以外の仕事</b>」を奨励しました。<b>織物・農業・漆器・和紙・刃物</b>——家の中でやれる仕事だから、奥さんや家族も手伝える。武士のプライドを傷つけずに副業ができるようにした。これが米沢のものづくりの原点です。",
  "特に力を入れたのが<b>養蚕と織物</b>。〔繭・生糸を見せる〕これが「<b>おかいこさん</b>」と呼ばれる蚕の繭で、ここから糸を取り、綿状にして絹糸に引き伸ばします。桑を植え、蚕を飼い、糸を取り、織物にする——という一連の産業を米沢に根付かせました。",
  "<b>250年経った今</b>も、鷹山公が始めた多くの産業がこの街に残っています。私たちはそのいちばん端っこにいる、というわけです。"],
 ["This is <b>Lord Yozan Uesugi</b>, the 9th-generation lord of the Yonezawa domain. If you understand this one person, everything about Yonezawa craftsmanship makes sense.",
  "During the Edo period, Yonezawa was a very poor domain. After a major civil war at the end of the 16th century, the Uesugi clan ended up on the <b>losing side</b>. The shogunate cut our land sharply, so tax income dropped — but the number of samurai we had to feed stayed the same. The domain was almost bankrupt.",
  "So Lord Yozan encouraged his samurai to take up <b>work other than the sword</b>: weaving, agriculture, lacquerware, paper-making, knife-making — anything that could be done <b>inside the house</b>, so the family could help. It let them earn a living without losing samurai pride. This is the origin of craftsmanship in Yonezawa.",
  "He focused on <b>silk farming and weaving</b>. 〔Show cocoons / raw silk〕 These are silkworm cocoons — we call them “okaikosan.” We unravel the cocoon, fluff it like cotton, and pull it into silk thread. Lord Yozan built the entire silk industry from the ground up.",
  "<b>250 years later</b>, many of the industries he started are still alive in this town. Our family is one of the last pieces of that puzzle."],
 "“Lord Yozan Uesugi” と必ず \"Lord\" を付ける。「負け組」\"losing side\" は笑いを取れる定番。"),
(3,"米沢織のヒット商品「かみしも生地」","7分","3分",
 "〔本物の袴／機械織りと手織りのサンプル〕を提示。縦糸と横糸を別の色で示せると尚良し。",
 ["これが武士の履いた<b>袴（はかま）</b>です。〔袴を広げる〕米沢で大ヒットしたのは、この袴に使う「<b>かみしも生地</b>」でした。",
  "もともと、かみしもの生地は<b>縦も横も麻</b>で、ゴワゴワして着づらかった。鷹山公が絹を奨励した時、うちの初代が「<b>縦糸を絹に変えてみたら？</b>」と考えたんです。",
  "すると<b>縦は絹、横は麻</b>の組み合わせがピタッとはまった。絹のしなやかさと麻の腰が両立して着やすい袴になり、これが大ヒット。「<b>かみしもの生地といえば米沢</b>」と全国に知られました。",
  "うちの初代は、まさにそのかみしもを織って、この家を建てたんです。〔家を見回す〕〔機械織りと手織りを比べる〕こちらが<b>機械織り</b>、こちらが<b>手織り</b>。手織りは今、私の息子が織っています。"],
 ["This is a <b>hakama</b>, the formal trouser-skirt samurai wore. 〔Show hakama〕 The textile that made Yonezawa famous nationally was the fabric for these hakama, called <b>“kamishimo-jiji.”</b>",
  "Originally kamishimo used <b>hemp for both warp and weft</b> — stiff and scratchy. When Lord Yozan promoted silk, our <b>1st-generation ancestor</b> had an idea: <i>“What if we replace the vertical thread with silk?”</i>",
  "<b>Silk for the warp, hemp for the weft</b> — the result was magic. Softness of silk plus the firm body of hemp. It became a huge hit; “kamishimo from Yonezawa” became the gold standard nationwide.",
  "Our 1st-generation ancestor built <b>this very house</b> with that income. 〔Gesture around〕 〔Compare samples〕 This is <b>machine-woven</b>; this one is <b>hand-woven</b> — by my son."],
 None),
(4,"絹の現在 — どこから来るのか？","3分","スキップ",
 None,
 ["よく聞かれます——「絹は今もここで作っているんですか？」と。昔は米沢でも養蚕していましたが、今はほとんど輸入です。",
  "内訳は概ね：<b>中国 約80%</b>／ブラジル（「ブラジルタックス」）数%／インド（<b>野蚕＝オーガニックシルク</b>）一部／タイ 一部／<b>日本産はわずか10%程度</b>。",
  "中国産が圧倒的。ブラジルは高品質。インドの<b>野蚕（やさん）</b>は自然の中で育つ蚕の糸でオーガニックシルクとして珍重されます。日本産は1割ほど。寂しいですが、これが現実です。"],
 ["A common question: <i>“Is the silk still produced here?”</i> We used to raise silkworms in Yonezawa; today most silk is imported.",
  "Roughly: <b>China ~80%</b> / Brazil (“Brazil-tax”) a few % / India (<b>wild silk = organic</b>) small share / Thailand small share / <b>Japan only ~10%</b>.",
  "China dominates; Brazilian silk is high quality. From India comes <b>wild silk (yasan)</b>, harvested in nature and prized as organic silk. Japanese silk is only about 10% today — a bit sad, but that's the reality."],
 "インドネシア等のお客様には「御国にも野蚕がありますか？」と振ると会話が弾む。"),
(5,"江戸の手仕事から明治の工場へ","5分","2分",
 None,
 ["米沢の面白さは、<b>侍の奥さんや娘さんがものづくりをした</b>点です。家の中で機を織っていた。これが米沢の特徴です。",
  "工場形式に変わったのは<b>明治時代</b>——だいたい150年前。最初は手織りの工場、今は<b>モーター付きの機械</b>です。うちの工場は<b>明治17年（141年前）</b>に正式スタート。皆で織機を持ち寄り本格的な工場にしました。",
  "〔工場を指して〕後ほど2階をお見せします。今日はお休みで機械の音はしませんが、珍しい<b>「静かな工場」</b>を見ていただけます。"],
 ["What is unique about Yonezawa is that <b>the wives and daughters of samurai families</b> were the actual makers, weaving inside the house.",
  "It shifted to a <b>factory format in the Meiji era</b> — about 150 years ago. First hand-looms, today motorized looms. Our factory officially started in <b>Meiji 17 (141 years ago)</b>, when people gathered their looms into a proper factory.",
  "〔Point to workshop〕 I'll show you the 2nd floor later. Today it's on holiday, so no machine noise — but you'll see something rare: a <b>silent factory</b>."],
 "平日訪問なら「動いている音をお聞きください」に差し替え。"),
(6,"お茶室で一服","8分","スキップ／5分",
 "抹茶と和菓子を準備。座布団（紅花染めの絹）を指差せる位置に。",
 ["こちらで一服しましょう。これは「<b>和菓子</b>」、中身は「<b>あんこ</b>」（豆のペースト）。少し甘く、抹茶とよく合います。",
  "〔座布団を指す〕この座布団も<b>紅花で染めた絹</b>、緑の紐も紅花染めです。紅花からは赤だけでなく<b>黄</b>、他の植物と合わせて<b>緑や紫</b>も作れます。",
  "そしてこの<b>茶室</b>は、メディアアーティスト<b>落合陽一さん</b>（筑波大学准教授・「デジタルネイチャー」提唱）と5代目<b>源太郎</b>のコラボ作品「<b>ヌベルニ庵（Null-Beni-An / Nouvelle Néant）</b>」。「Craft × Tech 東北プロジェクト 2024」の一環で生まれました。",
  "この茶室は<b>柱がない</b>のが特徴。中央の天然木と四隅の<b>紅花染めの紐</b>の張力で全体を支える「<b>テンセグリティ構造</b>」。<b>置賜紬</b>の紅花染め生地でできた<b>移動式の茶室</b>で、うちの織物の見本にもなっています。"],
 ["Let's take a short break with tea. This is <b>wagashi</b>, a traditional sweet; the filling is <b>anko</b> (sweet red bean paste), mildly sweet and balancing matcha well.",
  "〔Point at cushions〕 These cushions are <b>silk dyed with benibana (safflower)</b>; the green cord too. From safflower we get not only <b>red</b> but <b>yellow</b>, and combined with other plants, <b>green and purple</b>.",
  "This <b>tea room</b> is a collaboration between media artist <b>Yoichi Ochiai</b> (Assoc. Prof., University of Tsukuba; “Digital Nature”) and my son <b>Gentaro</b>, titled <b>“Null-Beni-An / Nouvelle Néant”</b> — from the <b>Craft × Tech Tohoku Project 2024</b>.",
  "It has <b>no pillars</b>: one central wooden piece plus four <b>benibana-dyed cords</b> hold it entirely by <b>tensegrity</b>. Made of <b>Oitama-tsumugi</b> dyed with safflower, it can be disassembled and moved — a living showroom of our textiles."],
 "落合陽一は欧米・アジアの美術/テック界隈で通る。\"Yoichi Ochiai\" \"Digital Nature\" \"Tsukuba\" を覚えておく。"),
(7,"お庭 — 四季を表現した日本庭園","10分","3分",
 "縁側/応接間のガラス越しに池の見える場所へ。大正ガラスを指し示せる位置で。",
 ["建物はちょうど<b>築100年</b>。窓を見てください。少し歪んで見えるでしょう？これは「<b>大正ガラス（流し込みガラス）</b>」、当時の技法の<b>手作りガラス</b>です。子どもには「この辺で遊んじゃダメ」と言っています。",
  "このお庭は<b>日本の四季</b>を一つの空間で表現。〔池〕<b>海・湖</b>を表し、底から<b>井戸水</b>が湧き冬も水温一定で鯉が快適。〔大きな石〕<b>山石</b>＝山。〔別の石〕<b>川石</b>。松・もみじ・盆栽も意味があり、秋はもみじが真っ赤に。",
  "〔紅花の木〕これが<b>紅花の木</b>——<b>山形県の保護木</b>。普通は寺社の木が選ばれるので、民家の庭の木の指定は非常に珍しい。",
  "冬は雪が<b>1メートル30センチ</b>ほど。毎年雪囲いで守り、松は<b>職人が7月に手で</b>カットします。"],
 ["This building is exactly <b>100 years old</b>. The window glass is a bit wavy, isn't it? This is <b>Taisho glass (poured glass)</b> — handmade glass of that era. I always tell the children not to play near it.",
  "This garden expresses <b>all four seasons in one space</b>. 〔Pond〕 represents the <b>sea/lake</b>; underground spring water keeps it stable so the koi winter comfortably. 〔Large stone〕 a <b>mountain stone</b>; 〔another〕 a <b>river stone</b>. Pine, maple, bonsai all carry meaning; the maple turns deep red in autumn.",
  "〔Safflower tree〕 This is the <b>safflower tree</b>, designated a <b>protected tree by Yamagata Prefecture</b> — very rare for a private garden.",
  "Winter brings about <b>1.3 m of snow</b>; we wrap the trees yearly, and a craftsman prunes the pines <b>by hand in July</b>."],
 "紅花の保護木は新田家のユニークセリングポイント。繰り返し言ってよい。"),
(8,"紅花染め体験 — 山形の赤","20分","10分",
 "染料作りの工程は冬限定（寒いほど赤が綺麗）。ハンカチ染め体験は通年可。参加者の名前を聞きハンカチに書く。",
 ["<b>【紅花とは】</b>これが<b>紅花（べにばな／safflower）</b>を乾燥させたもので、<b>赤の原料</b>。江戸時代から山形で盛んに栽培され、今も<b>日本一の産地</b>。当時は<b>京都</b>へ運ばれ、職人が<b>口紅</b>や「<b>玉虫色</b>」の高級な紅に仕上げました。紅花の赤は当時<b>金と同じくらい価値</b>があった。3代目<b>秀治・富子</b>夫妻が昭和38年（1963年）頃から再興し、1966年「<b>紅花紬</b>」として世に。今は4代目英行・5代目源太郎が継承。",
  "<b>【なぜ冬に染めるか】</b><b>冬にしか染めない</b>。<b>寒いほど赤がきれいに発色</b>し、夏は染めません。",
  "<b>【pHのマジック】</b>色素を定着させるにはpH調整が要。①<b>アルカリ性</b>に（〔灰〕アカザを燃やした灰）②紅花を漬ける③<b>酸</b>を加える（〔米酢〕）④中和に近づくと<b>赤</b>が出る。紅花染めは「pHを操る化学」——すべて<b>自然のものだけ</b>。",
  "<b>【ハンカチを染める】</b>絹は吸い込みが早いので今日は<b>綿のハンカチ</b>。<b>扇子畳み</b>（屏風状にジグザグ）→三角形に折り直し→<b>輪ゴム</b>で数カ所縛る。縛った所は染まらず<b>白い模様</b>に。開くまでのお楽しみ。",
  "<b>【多彩な色】</b>紅花＝赤・黄／藍＝青／紅花+藍＝紫／赤+黄＝緑／栗のイガ・くるみの皮(+鉄媒染)＝茶。<b>鉄媒染</b>は鉄分で色を留める重要工程。",
  "<b>【紅花餅と京都】</b>〔花餅〕摘んだ紅花を<b>足で踏んで</b>団子状に固め、発酵・乾燥させた「<b>紅花餅</b>」。この形で京都へ運び、京都の職人が口紅や玉虫色に仕上げました。"],
 ["<b>[What is benibana]</b> Dried <b>benibana — safflower</b>, the raw material for <b>red dye</b>. Cultivated in Yamagata since the Edo period; still Japan's <b>number-one producer</b>. It was carried to <b>Kyoto</b>, where artisans made <b>lipstick</b> and a premium red called <b>“tamamushi-iro.”</b> Back then this red was <b>as valuable as gold</b>. My parents, the <b>3rd-generation Shuji & Tomiko</b>, revived the technique from ~1963, releasing <b>“Benibana-tsumugi”</b> in 1966; my son and I continue it.",
  "<b>[Why dye in winter]</b> We <b>only dye in winter</b> — the <b>colder it is, the more beautiful the red</b>. Never in summer.",
  "<b>[The pH magic]</b> To fix the pigment, pH control is essential: ① make it <b>alkaline</b> (〔ash〕 from the plant “akaza”) ② soak the safflower ③ add <b>acid</b> (〔rice vinegar〕) ④ near neutral, the <b>red emerges</b>. It's <b>chemistry</b> — using <b>only natural ingredients</b>.",
  "<b>[Dye a handkerchief]</b> Silk absorbs fast, so today we use <b>cotton</b>. <b>Fan-fold (ougi-datami)</b> → fold into a triangle → tie with <b>rubber bands</b>. Tied parts resist dye and stay <b>white</b> — the design is a surprise until you open it.",
  "<b>[A palette of colors]</b> safflower = red/yellow; indigo = blue; safflower+indigo = purple; red+yellow = green; chestnut burr / walnut husk (+iron mordant) = brown. <b>Iron mordanting</b> fixes the color.",
  "<b>[Benibana-mochi & Kyoto]</b> 〔flower cake〕 Picked safflower is <b>stamped by foot</b> into a fermented, dried cake — <b>benibana-mochi</b> — easy to carry to Kyoto, where only Kyoto artisans finished it into lipstick and tamamushi-iro."],
 "pH（化学）の説明は英語で難解。図示 or シンプルに \"alkali first, then acid, then red comes out\" に切替えると◎。「酢の匂い」と言われたら「天然の証拠です」と笑顔で。"),
(9,"2階工場 — 染色記録と糸繰り","7分","3分",
 None,
 ["2階の工場をご案内します。〔染色機の前で〕こちらが<b>染色機</b>。手作業と機械の両方で染料を煮出して染めます。",
  "〔染色記録ノート〕これが大事な<b>染色記録ノート</b>。<b>いつ・どんな材料で・どんな手順で</b>染めたかを全て記録。お客様に「以前のあの色をもう一度」と言われた時、これを見れば再現できる。<b>色を再現可能にするレシピ集</b>です。",
  "〔糸巻き機〕下で染めた糸を<b>ボビン</b>に巻き、<b>縦糸</b>として使えるように並べます。この機械の原型は<b>トヨタ佐吉</b>——お母さんの手織りを楽にしようと発明したもので、10年後に米沢へ入ってきました。"],
 ["Let me take you upstairs. 〔At the dyeing equipment〕 This is our <b>dyeing equipment</b> — we dye by hand and by machine, simmering plants and materials.",
  "〔Show dyeing log〕 This is important: our <b>dyeing log</b>. Every job records <b>the date, materials, exact procedure</b>. When a customer says <i>“make that color again,”</i> we reproduce it exactly. It's our <b>recipe book</b> for repeatable color.",
  "〔At the winding machine〕 This winds dyed thread onto <b>bobbins</b>, aligned as <b>warp</b>. This machine was originally invented by <b>Sakichi Toyoda</b> — founder of what became <b>Toyota</b> — to ease his mother's hand-weaving. It reached Yonezawa about 10 years later."],
 "\"Toyota = the car company\" は欧米客に鉄板。"),
(10,"ジャガード織機と紋紙の歴史","8分","5分",
 None,
 ["これが<b>ジャガード織機</b>。〔上〕この「<b>紋紙（もんがみ）</b>」という穴あき厚紙の<b>穴の配置で柄が決まる</b>。今は紅花の柄。〔針〕<b>金属の針</b>が穴に応じて上下し、<b>縦糸</b>が持ち上がり、隙間に<b>シャトル</b>が<b>横糸</b>を通す。針は磨いておかないと縦糸を傷つけます。",
  "〔紋紙→レコード→フロッピー→USB〕<b>紋紙の進化</b>が面白い：①紙の紋紙②レコード盤型③フロッピー④今は<b>USB</b>。新しい技術は導入しつつ<b>古いものも使えるように維持</b>する——これがうちのやり方。",
  "〔別の織機〕この織機は<b>100年前にアメリカ・マサチューセッツ州ウースター市</b>へ渡りました。明治末の博覧会で職人が現地で実演。<b>分解できる</b>んです。",
  "〔足踏み織機〕足で交互に踏むと開き、<b>平織り・綾織り</b>など踏み方で変わる。良い運動です。今、息子がこれで織っています。いつか<b>UNESCO無形文化遺産</b>に登録される日が来れば、と思っています。"],
 ["This is our <b>Jacquard loom</b>. 〔Top〕 A punched card called <b>“mongami”</b> — <b>the holes determine the design</b> (a safflower pattern now). 〔Needles〕 <b>Metal needles</b> rise/fall per the holes, lifting the <b>warp</b> so a <b>shuttle</b> carries the <b>weft</b>. Needles must be polished or they damage the warp.",
  "〔mongami → record → floppy → USB〕 The evolution is fascinating: ① paper mongami ② record-disk ③ floppy ④ today <b>USB</b>. We adopt the new but <b>maintain the old</b> — our philosophy.",
  "〔Another loom〕 This loom <b>traveled to Worcester, Massachusetts, USA</b> about 100 years ago, assembled before an American audience at a Meiji-era exhibition. It <b>disassembles</b>.",
  "〔Foot-pedal loom〕 Different pedaling makes <b>plain weave, twill</b>, and more — great exercise. My son weaves on it today. One day I hope these become <b>UNESCO Intangible Cultural Heritage</b>."],
 "紋紙→USB は世代別アナロジー（コンピュータ史）で響く。\"Worcester\" は「ウースター」。"),
(11,"帯のデザイン — 1本5.5m、5本まとめて織る","4分","2分",
 None,
 ["織りかけの<b>帯（おび）</b>です。帯は1本約<b>5.5メートル</b>。1本ずつではなく<b>5本分</b>をまとめて織り、1本終わると次は別の柄——と続けて織れる設計（<b>約27.5m</b>を1セット）。",
  "〔白い部分〕ここが<b>デザインパターン</b>。緑・赤・黄の下色の上に、デザイナーの図案を一目ずつ拾って追う。〔針〕<b>針の打ち方</b>で柄が決まるので、幅を変えたければ<b>針を全部打ち替える</b>——大変な作業です。"],
 ["An <b>obi (kimono sash)</b> in mid-weaving. One obi is about <b>5.5 m</b>. We weave <b>five back-to-back</b>, each with a different pattern (one set ~<b>27.5 m</b>).",
  "〔White sections〕 the <b>design pattern</b>, followed stitch by stitch over the base color. 〔Needles〕 their arrangement sets the design; widening the obi means <b>replacing every needle</b>."],
 None),
(12,"ショールーム — 商品と海外展開","10分","5分",
 "商品を見せながら。色の意味は後半のカラーミーニング表を参照。",
 ["ショールームへどうぞ。〔夏の着物〕日本の着物は<b>寸法を測りオーダーメイド</b>。〔帯〕先ほどの<b>帯</b>は<b>1本ずつ柄が違い</b>、同じものは2つとありません。〔紅花染めの帯〕うちの代表作の一つ。",
  "〔20年前のヒット商品〕私の代でヒットした商品。〔パリEXPO〕昨年<b>パリ「JAPAN EXPO」</b>で紹介した商品——糸も織りも縫製も<b>すべてこの工場で仕上げ</b>ました。〔鯉のぼり〕男の子のお祝いに。",
  "そして——<b>色にはそれぞれ意味</b>があります（下表）。"],
 ["Welcome to the showroom. 〔Summer kimono〕 Japanese kimono are <b>made-to-measure</b>. 〔Obi〕 <b>Every obi differs</b> — no two alike. 〔Benibana obi〕 one of our signature pieces.",
  "〔20-year-old design〕 a hit from my generation. 〔Paris EXPO〕 shown last year at <b>JAPAN EXPO in Paris</b> — thread, weaving, sewing all <b>done in this workshop</b>. 〔Koinobori〕 a carp streamer, to celebrate boys.",
  "And — <b>each color carries a meaning</b> (see the table below)."],
 "東南アジア・台湾のお客様には縁起色（黒・赤）が刺さる。仏・南欧客には「ストーリーのある商品」を推す。"),
(13,"オープンファクトリーと業界の今","3分","スキップ",
 None,
 ["最後に業界の現状を少し。米沢では毎年<b>9月に「オープンファクトリー」</b>を開催し、普段閉じている工場を数社が一斉開放します。再訪なら9月もおすすめ。",
  "最近は<b>専門のメンテナンス屋さんが減り</b>、古いジャガード織機を直せる人が少ない。だからうちは<b>メンテナンスも自分たちで</b>——技術を残すとはそういうことだと思っています。",
  "<b>トヨタの方たち</b>が業務改善の<b>研修で工場見学</b>にいらっしゃることも。100年の鉄の機械が今も正確に動く様子を見に来られます。"],
 ["A quick word on the industry. Each <b>September, Yonezawa hosts an “Open Factory”</b> — several usually-closed factories open together. If you return, <b>September is recommended</b>.",
  "These days <b>specialized maintenance shops are disappearing</b>; few can repair old Jacquard looms. So we do <b>all maintenance in-house</b> — preserving the technique means preserving the machines.",
  "Sometimes <b>Toyota team members</b> visit for <b>business-improvement training</b>, to see how 100-year-old iron machines still run with such precision."],
 "9月オープンファクトリーは強い再訪フック。連絡先・公式SNSを案内すると効果的。"),
(14,"お見送り","2分","2分",
 None,
 ["本日は遠いところ、ありがとうございました。最初にお話しした<b>上杉鷹山公</b>が250年前に始めた文化・産業が、今も米沢に残っています。私たちはその一端を守るに過ぎませんが、海外の方に見ていただけることが何よりの励みです。",
  "染めていただいたハンカチは<b>世界に1枚だけ</b>。お国で米沢を少し思い出していただけたら嬉しいです。またいつでもいらしてください。お元気で。"],
 ["Thank you so much for coming all the way to Yonezawa. The culture and industry <b>Lord Yozan Uesugi</b> began 250 years ago still lives here. We are only a small part of that legacy, but visitors like you are our greatest encouragement.",
  "The handkerchief you dyed is <b>one-of-a-kind in the world</b>. We hope it helps you remember Yonezawa. Please come back anytime — take care and safe travels."],
 None),
]

faq=[
 ("シルクは今もご自分で養蚕を？","今は約90%が輸入（中国80%等）、日本産は約10%。米沢でも昔は養蚕していた。","Is the silk still produced here?","~90% imported (China ~80%), only ~10% Japanese. Yonezawa used to raise silkworms."),
 ("紅花染めはいつでも体験できる？","染料作りは<b>冬限定</b>（寒いほど赤が綺麗）。<b>ハンカチ染め体験は通年</b>可。","Can I always try safflower dyeing?","Dye-making is <b>winter-only</b>; the <b>handkerchief experience is year-round</b>."),
 ("工場は何人で？","職人数名。1人で機械2台、ベテランで3台。標準は1人2台。","How many people run the factory?","A few artisans. One person runs 2 looms (veterans 3)."),
 ("着物のオーダーは可能？","はい、寸法を取りオーダーメイド。納期・価格は商品による。","Can I order a kimono?","Yes — made-to-measure; lead time and price vary."),
 ("海外発送は？","ハンカチ・小物は可能。帯・着物は要相談。","Overseas shipping?","Small items yes; obi/kimono on request."),
 ("この織機は何年前のもの？","トヨタ佐吉発明→約10年後に米沢へ。<b>100年以上</b>現役の機械あり。","How old is this loom?","Invented by Sakichi Toyoda; some run <b>100+ years</b>."),
 ("なぜ「侍の家」が織物を？","江戸期の財政難で武士に副業奨励。「家の中で出来る仕事」＝織物でプライドを保ち家計を支えた。","Why did a samurai family start weaving?","Edo-era hardship; weaving could be done at home, preserving pride while supporting the household."),
 ("UNESCO登録は？","いつか登録される日を願う。技術と道具の両方を守るのが先決。","UNESCO registration?","We hope so one day; preserving both technique and tools comes first."),
]

glossary=[
 ("紅花","safflower / benibana","山形県の県花"),
 ("紅花餅","safflower cake / benibana-mochi","京都へ運ぶ形態"),
 ("玉虫色","tamamushi-iro","金色がかった緑を含む赤"),
 ("染色記録","dyeing log / recipe book","再現性の要"),
 ("紋紙","mongami / punched card","ジャガードのデータ"),
 ("ジャガード織機","Jacquard loom","紋紙で柄を制御"),
 ("シャトル","shuttle","横糸を運ぶ道具"),
 ("縦糸 / 横糸","warp / weft","機の糸 / シャトルで通す糸"),
 ("鉄媒染","iron mordanting","茶色などを定着"),
 ("灰汁","lye / ash extract","アルカリ源（アカザ灰）"),
 ("かみしも生地","kamishimo fabric","縦＝絹／横＝麻"),
 ("養蚕","sericulture","蚕を飼い絹を作る"),
 ("上杉鷹山","Lord Yozan Uesugi","米沢藩9代藩主"),
 ("平織り / 綾織り","plain weave / twill","基本 / 斜めの織り目"),
]

timing=[("1","玄関・ご挨拶","3分","2分"),("2","ギャラリー／上杉鷹山","8分","4分"),("3","かみしも生地","7分","3分"),("4","絹の現在","3分","スキップ"),("5","江戸→明治の工場化","5分","2分"),("6","お茶室","8分","スキップ／5分"),("7","庭園・四季","10分","3分"),("8","紅花染め体験","20分","10分"),("9","2階・染色記録","7分","3分"),("10","ジャガード織機","8分","5分"),("11","帯のデザイン","4分","2分"),("12","ショールーム＆色","10分","5分"),("13","オープンファクトリー","3分","スキップ"),("14","お見送り","2分","2分"),("","合計","約98分","約46分")]

colors=[("🔴 赤","魔除け・健康・家族の安全","Protection from evil, health, family safety"),
 ("🟡 黄","金運・希望・健康・エネルギー","Wealth, hope, health, energy"),
 ("🟠 オレンジ","悪いエネルギーから守る","Shields from bad energy"),
 ("🔵 青","学問運・才能開花・商売運","Study, talent, business luck"),
 ("⚫ 黒","商売繁盛・長く続くビジネス","Long-lasting business success")]

audience=[("欧米・北米","マサチューセッツに渡った織機／トヨタ佐吉の原型機／UNESCO候補級技術／紅花染め（pHのサイエンス）"),
 ("フランス・南欧","パリJAPAN EXPO出展／家族4代・紅花復活のストーリー／大正ガラス・四季の庭の美学"),
 ("アジア（台・香・新・泰・尼・馬）","色の意味（縁起の黒・赤）／オーダーメイド着物・帯／商売繁盛モチーフ／鯉のぼり"),
 ("視察団・業界関係者","工場メンテ自社対応／紋紙→USBの系譜／染色記録＝再現性／オープンファクトリー（9月）")]

# ---------- build HTML ----------
def paras(lst): return "\n".join("<p>%s</p>"%p for p in lst)

scene_html=[]
for n,title,std,hl,note,jp,en,tip in scenes:
    note_html='<div class="note"><span class="lbl">動線・準備</span>%s</div>'%note if note else ""
    tip_html='<div class="tip"><span class="lbl">💡 ガイドTips</span>%s</div>'%tip if tip else ""
    scene_html.append('''
<section class="scene" id="s{n}">
  <div class="scene-head"><span class="snum">{n:02d}</span><h2>{title}</h2><span class="mins">標準 {std} ／ ハイライト {hl}</span></div>
  {note}
  <div class="cols">
    <div class="col blk-ja"><div class="flag">🇯🇵 日本語（新田さん）</div>{jp}</div>
    <div class="col blk-en"><div class="flag">🇬🇧 English (guide)</div>{en}</div>
  </div>
  {tip}
</section>'''.format(n=n,title=title,std=std,hl=hl,note=note_html,jp=paras(jp),en=paras(en),tip=tip_html))

nav_html="".join('<a href="#s{n}">{n:02d} {t}</a>'.format(n=n,t=title) for n,title,_,_,_,_,_,_ in scenes)

faq_rows="".join('<tr><td class="q"><b>Q.</b> {jq}<div class="en2">{eq}</div></td><td class="a">{ja}<div class="en2">{ea}</div></td></tr>'.format(jq=q,eq=eq,ja=a,ea=ea) for q,a,eq,ea in faq)
gloss_rows="".join('<tr><td>{a}</td><td>{b}</td><td class="sub">{c}</td></tr>'.format(a=a,b=b,c=c) for a,b,c in glossary)
timing_rows="".join('<tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{d}</td></tr>'.format(a=a,b=b,c=c,d=d) for a,b,c,d in timing)
color_rows="".join('<tr><td>{a}</td><td>{b}</td><td class="sub">{c}</td></tr>'.format(a=a,b=b,c=c) for a,b,c in colors)
aud_rows="".join('<tr><td><b>{a}</b></td><td>{b}</td></tr>'.format(a=a,b=b) for a,b in audience)

HTML='''<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="robots" content="noindex,nofollow">
<title>新田織物 コンテンツガイド（ガイド専用）｜PLAT YONEZAWA</title>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600&family=Shippori+Mincho:wght@400;500;600;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<style>
:root{--bg:#fbf6f1;--paper:#f3ede2;--card:#fff;--ink:#2b201d;--muted:#7f7166;--deep:#2e1f1c;--gold:#a8893a;--gold-deep:#6b5418;--gold-soft:#d4c084;--line:#e4d8c8;--accent:#a83a2b;--crimson:#a83a2b;
--f-ja:'Shippori Mincho',serif;--f-en:'Cormorant Garamond','Shippori Mincho',serif;--f-ui:'Inter','Shippori Mincho',sans-serif;}
*{box-sizing:border-box;margin:0;padding:0}
body{background:var(--bg);color:var(--ink);font-family:var(--f-ja);line-height:1.85;font-size:16px;-webkit-font-smoothing:antialiased}
.wrap{max-width:1080px;margin:0 auto;padding:0 24px}
/* lang toggle */
body.lang-ja .blk-en{display:none}
body.lang-en .blk-ja{display:none}
/* topbar */
.topbar{position:sticky;top:0;z-index:50;background:rgba(251,246,241,.95);backdrop-filter:blur(8px);border-bottom:1px solid var(--line)}
.topbar .in{display:flex;align-items:center;gap:14px;max-width:1080px;margin:0 auto;padding:10px 24px}
.brand{font-family:var(--f-en);font-weight:600;letter-spacing:.2em;color:var(--deep);font-size:15px}
.badge{font-family:var(--f-ui);font-size:9.5px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:#fff;background:var(--crimson);padding:4px 9px;border-radius:999px}
.spacer{flex:1}
.langsw{display:flex;border:1px solid var(--line);border-radius:999px;overflow:hidden;background:#fff}
.langsw button{font-family:var(--f-ui);font-size:11px;font-weight:600;border:none;background:transparent;color:var(--muted);padding:7px 13px;cursor:pointer;border-left:1px solid var(--line)}
.langsw button:first-child{border-left:none}
.langsw button.active{background:var(--deep);color:var(--gold-soft)}
/* hero */
.hero{background:linear-gradient(160deg,#2e1f1c,#1c100e);color:#f3e9dd;padding:52px 0 46px}
.hero .eyebrow{font-family:var(--f-ui);letter-spacing:.28em;text-transform:uppercase;font-size:11px;color:var(--gold-soft)}
.hero h1{font-family:var(--f-ja);font-weight:700;font-size:34px;margin:12px 0 6px;color:#fff}
.hero .sub{font-family:var(--f-en);font-style:italic;color:var(--gold-soft);font-size:19px}
/* info box */
.info{background:var(--card);border:1px solid var(--line);border-left:4px solid var(--gold);border-radius:8px;padding:18px 22px;margin:26px 0;font-size:14.5px}
.info b{color:var(--deep)}
.info .row{margin:3px 0}
h2.sec{font-family:var(--f-ja);font-size:24px;color:var(--deep);margin:44px 0 14px;padding-bottom:8px;border-bottom:2px solid var(--gold-soft)}
table{width:100%;border-collapse:collapse;font-size:14px;background:#fff;border:1px solid var(--line);border-radius:8px;overflow:hidden;margin:10px 0}
th,td{text-align:left;padding:10px 12px;border-bottom:1px solid var(--line);vertical-align:top}
th{background:var(--paper);font-family:var(--f-ui);font-size:11px;letter-spacing:.06em;color:var(--muted);text-transform:uppercase}
td.sub,.en2{color:var(--muted);font-size:12.5px;font-family:var(--f-ui)}
.en2{margin-top:4px}
/* cast */
.cast td b{color:var(--deep)}
/* nav */
.scenenav{background:var(--paper);border:1px solid var(--line);border-radius:10px;padding:16px 18px;margin:18px 0}
.scenenav .t{font-family:var(--f-ui);font-size:11px;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);margin-bottom:8px}
.scenenav a{display:inline-block;font-family:var(--f-ui);font-size:12.5px;color:var(--deep);background:#fff;border:1px solid var(--line);border-radius:6px;padding:5px 10px;margin:3px 4px 3px 0;text-decoration:none}
.scenenav a:hover{background:var(--deep);color:var(--gold-soft);border-color:var(--deep)}
/* scenes */
.scene{background:#fff;border:1px solid var(--line);border-radius:12px;padding:24px 26px;margin:16px 0;scroll-margin-top:70px}
.scene-head{display:flex;align-items:baseline;gap:12px;flex-wrap:wrap;border-bottom:1px solid var(--line);padding-bottom:12px;margin-bottom:14px}
.snum{font-family:var(--f-en);font-size:30px;color:var(--gold);line-height:1}
.scene-head h2{font-family:var(--f-ja);font-size:21px;color:var(--deep);flex:1}
.mins{font-family:var(--f-ui);font-size:11.5px;color:var(--muted)}
.note{background:#f7f3ea;border:1px solid var(--line);border-radius:8px;padding:10px 14px;margin-bottom:14px;font-size:13.5px;color:var(--ink)}
.note .lbl,.tip .lbl{display:block;font-family:var(--f-ui);font-size:10.5px;font-weight:700;letter-spacing:.08em;color:var(--muted);margin-bottom:3px;text-transform:uppercase}
.cols{display:grid;grid-template-columns:1fr 1fr;gap:22px}
.col{min-width:0}
.col .flag{font-family:var(--f-ui);font-size:11px;font-weight:700;letter-spacing:.06em;color:var(--muted);margin-bottom:8px;border-bottom:1px dashed var(--line);padding-bottom:4px}
.blk-en{font-family:var(--f-en);font-size:15.5px}
.col p{margin-bottom:12px}
.tip{background:#fbf3dc;border:1px solid var(--gold-soft);border-radius:8px;padding:10px 14px;margin-top:14px;font-size:13px;color:var(--gold-deep)}
body.lang-ja .cols,body.lang-en .cols{grid-template-columns:1fr}
@media(max-width:820px){.cols{grid-template-columns:1fr}}
footer{background:var(--deep);color:rgba(243,233,221,.7);font-family:var(--f-ui);font-size:12px;text-align:center;padding:26px 24px;margin-top:40px}
</style>
</head>
<body class="lang-both">
<div class="topbar"><div class="in">
  <span class="brand">PLAT YONEZAWA</span><span class="badge">Guide-only 社内</span>
  <span class="spacer"></span>
  <div class="langsw">
    <button data-l="ja">日本語</button><button data-l="en">English</button><button data-l="both" class="active">両方</button>
  </div>
</div></div>

<header class="hero"><div class="wrap">
  <div class="eyebrow">Content Guide · ガイド育成コンテンツ</div>
  <h1>新田織物 コンテンツガイド</h1>
  <div class="sub">Nitta Textile — A Guide's Script for the Silk & Safflower Atelier</div>
</div></header>

<div class="wrap">
  <div class="info">
    <div class="row"><b>施設</b>：株式会社新田（米沢織・紅花染め工房／米沢市／明治17年〈1884年〉創業）</div>
    <div class="row"><b>想定時間</b>：約60〜90分（フル）／30分（ハイライト）</div>
    <div class="row"><b>想定客層</b>：海外個人旅行、欧米・アジアの文化観光客、視察団</div>
    <div class="row"><b>構成</b>：玄関 → ギャラリー → お茶室 → お庭 → 紅花染め体験 → 2階工場 → ショールーム → お見送り</div>
    <div class="row"><b>使い方</b>：日本語＝新田さん本人用／英語＝ガイド・通訳・スタッフ用。〔 〕内はステージディレクション。上部トグルで表示言語を切替。</div>
  </div>

  <h2 class="sec">👥 登場人物（新田家）</h2>
  <table class="cast"><tr><th>世代</th><th>お名前</th><th>役職</th><th>役割・トピック</th></tr>
  <tr><td>3代目</td><td><b>新田 秀治・富子</b>（夫妻）</td><td>故人／創業者の孫</td><td><b>紅花染め復興</b>（昭和38年頃〜）／紅花紬発表（1966年）</td></tr>
  <tr><td><b>4代目</b></td><td><b>新田 英行</b>（にった ひでゆき）</td><td><b>代表取締役会長</b></td><td>本ガイドの主たる語り手／染めと織りの一貫生産を確立</td></tr>
  <tr><td><b>5代目</b></td><td><b>新田 源太郎</b>（にった げんたろう）</td><td><b>代表取締役社長</b></td><td>現役の作り手／落合陽一氏とのコラボ「ヌベルニ庵」等</td></tr>
  </table>
  <div class="tip" style="margin-top:8px">海外客向け："Mr. Hideyuki Nitta — 4th-generation Chairman" / "Mr. Gentaro Nitta — 5th-generation President"</div>

  <h2 class="sec">🎯 ガイドのトーンの軸</h2>
  <table>
  <tr><td style="width:120px"><b>トーン</b></td><td>「米沢が貧しい藩だったからこそ、ものづくりが残った」逆境発の文化ストーリー</td></tr>
  <tr><td><b>主役</b></td><td>上杉鷹山公／4代目（父）＋5代目（息子）／紅花</td></tr>
  <tr><td><b>体験フック</b></td><td>① 紅花染めハンカチ ② 100年前のジャガード織機 ③ 大正ガラスの応接間と四季の庭</td></tr>
  <tr><td><b>海外強調点</b></td><td>UNESCO候補級の技術／パリJAPAN EXPO出展／100年前にマサチューセッツへ渡った織機</td></tr>
  </table>

  <div class="scenenav"><div class="t">シーン一覧（タップで移動）</div>{nav}</div>

  <h2 class="sec">🎬 シーン別スクリプト</h2>
  {scenes}

  <h2 class="sec">❓ 想定FAQ</h2>
  <table><tr><th style="width:44%">Q</th><th>A</th></tr>{faq}</table>

  <h2 class="sec">🎨 色の意味（カラーミーニング）</h2>
  <table><tr><th>色</th><th>意味</th><th>Meaning</th></tr>{colors}</table>

  <h2 class="sec">📚 用語集（日英）</h2>
  <table><tr><th>日本語</th><th>English</th><th>補足</th></tr>{gloss}</table>

  <h2 class="sec">⏱ シーン別タイミング表</h2>
  <table><tr><th>#</th><th>シーン</th><th>標準</th><th>ハイライト</th></tr>{timing}</table>

  <h2 class="sec">🌏 客層別おすすめハイライト</h2>
  <table><tr><th style="width:220px">客層</th><th>推し要素</th></tr>{aud}</table>
</div>

<footer>© 2026 PLAT YONEZAWA, Inc. ・ 新田織物 コンテンツガイド（ガイド専用・社外秘）<br>出典：Notion トークスクリプト（2026-05 録音ベース）／継続ブラッシュアップ</footer>

<script>
(function(){
  var body=document.body, btns=document.querySelectorAll('.langsw button');
  btns.forEach(function(b){b.addEventListener('click',function(){
    body.classList.remove('lang-ja','lang-en','lang-both');
    body.classList.add('lang-'+b.dataset.l);
    btns.forEach(function(x){x.classList.toggle('active',x===b)});
  });});
})();
</script>
</body>
</html>'''
HTML=(HTML.replace('{nav}',nav_html)
          .replace('{scenes}',"\n".join(scene_html))
          .replace('{faq}',faq_rows)
          .replace('{colors}',color_rows)
          .replace('{gloss}',gloss_rows)
          .replace('{timing}',timing_rows)
          .replace('{aud}',aud_rows))

if __name__=='__main__':
    open(OUT,'w',encoding='utf-8').write(HTML)
    print('single-mode preview:',OUT)
