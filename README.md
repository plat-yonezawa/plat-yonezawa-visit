# plat-yonezawa-visit

PLAT YONEZAWA ランオペ事業 B2Bトレード向け公開サイト（`visit.plat-yonezawa.com` / GitHub Pages）。

## 🚦 編集する前に必ず読む
- **[EDITING_GUIDE.md](./EDITING_GUIDE.md)** — 編集ルール・公開ポリシー・更新手順（必読）
- **[CLAUDE.md](./CLAUDE.md)** — Claude Code で作業する場合の遵守要点

## 最重要ルール（要約）
1. 事実情報（価格・仕様等）の**正本は Notion「商品タリフDB」**。HTMLはDBに一致させる。
2. `<!--AUTO:...-->` マーカーは**消さない**。内側はNotion由来。
3. ファイル名・PID（O-STY-01等）・robots(noindex)・`index.html`(Coming Soon) は**勝手に変えない**。
4. 画像は**最適化してから**追加。連絡先は `info1@plat-yonezawa.jp` 統一。
5. 反映: ローカル確認 → `git push origin main`（数分で公開反映）。

## 構成
```
/index.html   Coming Soon（公開トップ・維持）
/lp.html      LP（玄関・EN/JA/FR/繁中）
/tariff/      商談タリフ（目次 v1 / 個別5 / pdf / images / videos）— noindex
```
詳細は EDITING_GUIDE.md を参照。
