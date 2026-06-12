# CLAUDE.md — visit.plat-yonezawa.com

このリポジトリで作業する際は、**まず `EDITING_GUIDE.md` を読んで遵守すること**。
以下は絶対に守る要点（詳細はガイド参照）。

## 必須ルール
1. **コンテンツの正本は Notion「商品タリフDB」**（collection `3149db54-5efa-8004-9d7e-000b5116597c`）。価格・仕様などの事実はDBに一致させる。HTMLに直書きで矛盾させない。
2. **AUTOマーカー** `<!--AUTO:title|subtitle|price|quickfacts|spec|included-->…<!--/AUTO:x-->` は削除しない。内側はNotion由来＝Notion値に合わせる。外側（写真エッセイ本文）は手作り可。
3. **ファイル名・表示PID（tariff_O-STY-01.html / O-STY-01 等）は変えない**（リンク維持）。商品差し替えは「スロットの中身入替」。サイトはスロット番号で運用（Notion PIDとズレる場合あり）。
4. **多言語**: 文言は `<span class="en/ja/fr/zh">`。en/jaは必須、fr/zh無しはENに自動フォールバック。`applyLang`・言語CSSは触らない。
5. **robots**: タリフは `noindex,nofollow` を維持。`index.html`（Coming Soon）は削除・差替しない（本ローンチ判断まで）。
6. **画像**は長辺2000px・JPEG品質80程度に最適化してから追加（repo肥大化防止）。動画は短尺・圧縮。
7. **連絡先メールは `info1@plat-yonezawa.jp`** で統一。
8. 反映は `git push origin main`（GitHub Pages・数分で反映）。push前にローカル(`python3 -m http.server`)とスマホ幅で確認。

## 構成
- `/index.html` Coming Soon ／ `/lp.html` LP(4言語) ／ `/tariff/Yonezawa_Tariff_v1_GrossOnly.html` 商談タリフ目次 ／ `/tariff/tariff_<PID>.html` 個別5 ／ `/tariff/pdf/` Gross PDF。
- 商品: C-NTA-01 / S-TKO-01 / O-STY-01(Magari) / O-STY-02(Katemono) / O-STY-03(Forest Bathing)。

詳細・NG事項・既知の積み残しは **EDITING_GUIDE.md** を参照。
