# visit.plat-yonezawa.com 編集ガイド（共有ルール）

> このリポジトリを**クローンして編集する担当者は、必ず最初に読むこと**。
> ランオペ事業 B2Bトレード向け公開サイトの編集規約です。最終更新: 2026-06-12

---

## 0. サイトの全体像

B2B（旅行業界）向けの「ソフトローンチ」公開サイト（直URL共有・検索非公開）。

```
/  (index.html)                         … Coming Soon（公開中・index可）※下記ルール参照
/lp.html                                … LP＝ブランドの玄関（4言語・noindex）
/tariff/Yonezawa_Tariff_v1_GrossOnly.html … 商談タリフ「目次」（カード型・noindex）
/tariff/tariff_<PID>.html               … 個別 商談ページ ×5（noindex）
/tariff/pdf/<PID>.pdf                    … Gross PDF（資料請求で送付・未リンク）
/tariff/images/<pid>/ , /tariff/videos/ … 画像・動画（最適化済）
/images/brand/logo.svg                  … PLATロゴ
```

現ラインナップ（5商品）:
- `C-NTA-01` The Philosophy（絹・新田）
- `S-TKO-01` The Legacy & The Master（酒・東光）
- `O-STY-01` Gastronomy with Magari（里山）
- `O-STY-02` Katemono Afternoon Tea（里山）
- `O-STY-03` Forest Bathing with Mika（里山）

---

## 1. 【最重要】コンテンツの正本 = Notion「商品タリフDB」

タリフの**事実情報**（タイトル／サブタイトル／価格／所要時間／定員／対象年齢／対応言語／含有物／スケジュール／提供事業者）は、**Notion「商品タリフDB」が唯一の正本**です。

- HTMLに事実を直書きで“発明”しない。**必ずNotionの値に一致させる**。
- 価格や仕様を変えるときは、**先にNotionを更新 → その値をHTMLへ反映**。
- DB: `商品タリフDB`（collection: `3149db54-5efa-8004-9d7e-000b5116597c`）

---

## 2. 【最重要】AUTOマーカー — 触り方のルール

各タリフHTMLには、Notion由来の事実ブロックを囲む**マーカー**があります：

```html
<!--AUTO:price--><div class="value">¥15,000</div><!--/AUTO:price-->
```

対象: `title` / `subtitle` / `price` / `quickfacts` / `spec` / `included`

ルール:
- ✅ マーカー**内**を編集する場合は、**必ずNotionの値に合わせる**。
- ❌ マーカー（`<!--AUTO:x-->` / `<!--/AUTO:x-->`）を**削除しない**。将来の自動生成の差込口です。
- ✅ マーカー**外**（写真エッセイ本文・SHOT解説・あらすじ）は手作り編集OK。

---

## 3. 商品スロット / PID / ファイル名

- **ファイル名（`tariff_O-STY-01.html` 等）と表示PID（O-STY-01/02/03）は変えない**。リンク・共有URLが壊れます。
- 商品を差し替えるときは「スロットの中身」を入れ替える（ファイル名は維持）。
- ※Notion側のPIDはサイトのスロット番号とズレる場合あり（例: サイト O-STY-01 ＝ Notion O-STY-06 Magari）。**サイトはスロット番号で運用**。

---

## 4. 多言語（EN / JA / FR / 繁中）

文言は4スパンで持つ：

```html
<span class="en">English</span><span class="ja">日本語</span><span class="fr">Français</span><span class="zh">繁體中文</span>
```

- **`en` と `ja` は必須**。`fr` / `zh` が無い要素は**自動的にENにフォールバック**（空白にならない＝崩れない）。
- 言語切替のJS（`applyLang`）・CSS（`.en/.ja/.fr/.zh`）は**触らない**。

---

## 5. 公開ポリシー（noindex / robots）

- LP = `index,follow`（ただしソフトローンチ中は一時 `noindex` のことあり）。
- **タリフ各ページ = `noindex,nofollow`**（業界限定・直URL共有）。
- robots メタを**勝手に変えない**。本ローンチ時に別途切替。

---

## 6. 画像・動画（リポジトリ肥大化を防ぐ）

- **未最適化の大画像を入れない**。長辺 **2000px・JPEG品質80** 程度に最適化してから配置。
  - 例(macOS): `sips -Z 2000 -s format jpeg -s formatOptions 80 in.jpg --out out.jpg`
- 動画は**短くトリム＋圧縮**（数MB以内）。アンビエント背景はループ前提なので20秒程度で十分。

---

## 7. 更新 → 反映（デプロイ）手順

```bash
# 1. ローカルでプレビュー（リポジトリ直下で）
python3 -m http.server 8000
#   → http://localhost:8000/lp.html , /tariff/... をブラウザで確認
#   → スマホ幅（〜375px）でも必ず確認

# 2. 反映
git add -A
git commit -m "変更内容を簡潔に"
git push origin main
#   → GitHub Pages が数分でビルド → https://visit.plat-yonezawa.com に反映
#   → 表示が古い場合は Cmd+Shift+R（CDNキャッシュ）
```

---

## 8. やってはいけないこと（NG）

- ❌ `index.html`（Coming Soon）を削除・差し替える（**本ローンチ判断まで維持**）
- ❌ `<!--AUTO:...-->` マーカーを削除する
- ❌ 画像を未最適化で大量追加する
- ❌ robots（noindex）を勝手に変更する
- ❌ 連絡先メールを変える（**`info1@plat-yonezawa.jp` で統一**）
- ❌ Notionと矛盾する事実（価格・仕様）をHTMLに直書きする

---

## 9. 既知の積み残し（2026-06-12時点）

- 写真エッセイ**本文（SHOT解説・あらすじ）は旧内容が残る箇所あり**（Notionに本文プロセが無いため未置換）。本文刷新は別途。
- Satoyama 3商品は Notion `status=入力中`・**価格暫定**（確定後に再反映）。
- 本ローンチ（LPをトップへ昇格・検索公開）前に: GA4 / HubSpot / Cookiebot 導入、FR・繁中の本文翻訳。

---

## 10. 関連

- Notion「商品タリフDB」= 事実の正本
- 社内PMダッシュボード（Project Hub）= `pm.plat-yonezawa.com`（Cloudflare Access・社内）
- 編集の細則・背景は本ガイドを更新して共有すること。
