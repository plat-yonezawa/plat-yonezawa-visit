# 新田織物 コンテンツガイド — 引き継ぎ / 運用メモ

`guides/nitta-guide.html`（visit.plat-yonezawa.com/guides/nitta-guide.html）についての引き継ぎドキュメント。
**メンバーはまずこれを読めば運用・更新・Claudeへの頼み方が分かる**ようにしてあります。

---

## 1. これは何か

海外ゲスト向け＆ガイド育成用の「新田織物（米沢織・紅花染）」コンテンツガイド。
上杉まつりガイドの2軸トグル形を準拠し、トンマナは visit. に合わせています。

- **言語（3軸）**：English / Français / 繁體中文
- **モード（2軸）**：
  - 🧭 **Visitors**（案内モード）＝**公開**（海外ゲスト向けの物語・多言語）
  - 🔑 **Staff Only — Guide Team**（学習モード）＝**認証**（ガイド用トークスクリプト全14シーン・FAQ・用語集・現場フレーズ）
- `noindex` かつ**どこからもリンクしていない**（＝直URLを知っている人だけ）。

## 2. ファイルの場所（すべて git 上で確認可）

| ファイル | 役割 |
|---|---|
| `guides/nitta-guide.html` | **成果物（これが本体）** |
| `guides/nitta-guide.README.md` | 本ドキュメント |
| `guides/_build/nitta_content.py` | コンテンツ本文（14シーン日英・FAQ等）のデータ |
| `guides/_build/nitta_build.py` | 生成スクリプト（データ＋ビジター文＋トグル＋ゲートを組んでHTML出力） |

**コンテンツ原本（正）**：Notion「🧵 新田」トークスクリプト
`https://app.notion.com/p/35d9db545efa80379709e7d36b866808`
（素材ハブ：`https://app.notion.com/p/3649db545efa8096b69fe0b9e3395b24`）

## 3. 認証の設計（⚠️ 重要）

- **現状＝叩き台の暫定ゲート**：Staff Only モード選択時にメール登録で解錠（クライアント側・localStorage）。
  **これはセキュアではありません**（HTMLに本文が含まれる）。社外に直URLを出さないこと。
- **本番＝Cloudflare Access（メール認証）**に置き換える：
  - メール入力 → ワンタイムコード/リンク → 閲覧、**セッション3時間**、**認証メールはログ→CRM（HubSpot）へ蓄積**。
  - 設定：Zero Trust → Access → Applications → Add self-hosted →
    domain `visit.plat-yonezawa.com` / path `guides` → Policy=One-time PIN / Session=3h。
- **本番設計の分離**：公開の物語（Visitors）は将来 `/guide/`（公開・SEO）へ、
  ガイド資料（Staff Only）は `/guides/` に置いて Access 保護、と分けるのが理想
  （Access はURL単位保護のため、1ページ内で公開/認証を混在できない）。

## 4. 更新のしかた（3通り）

### A. Claudeに頼む（推奨・いちばん楽） → 第6章のプロンプト参照
### B. HTMLを直接編集
`guides/nitta-guide.html` をエディタで開いて文言修正 → commit → push。小さな直しはこれで十分。
### C. スクリプトで再生成（要 Python3・大きめの更新時）
```
cd guides/_build
python3 nitta_build.py      # → ../nitta-guide.html を再生成
```
本文を変えるときは `nitta_content.py`（データ）を編集してから上記を実行。

## 5. 公開（push）と確認

```
cd ~/plat-yonezawa-visit
git add guides/
git commit -m "guides: 新田ガイド更新"
git pull --no-edit origin main   # 他メンバーの更新を取り込み
git push origin main
```
- 反映：GitHub Pages ビルド後 数分。
- ⚠️ **Cloudflare Access を掛けるまでは、Staff Only の直URLを社外に出さない**（noindex・未リンクで運用）。

## 6. 🗣 Claude での呼び出し方（コピペ用プロンプト）

> Claude Code を `~/plat-yonezawa-visit` で起動して、以下のように頼めばOK。ファイルはパスで指定するとクリックで開けます。

**内容を更新する**
```
guides/nitta-guide.html を更新して。原本は Notion「🧵 新田」トークスクリプト
(app.notion.com/p/35d9db545efa80379709e7d36b866808)。
シーン8（紅花染め）に「◯◯」を追記して、再生成→ローカル確認まで。
```

**別の工房のガイドを新規作成する**
```
guides/nitta-guide.html の形（言語3軸×モード2軸・Visitors公開/Staff Only認証）を準拠して、
東光(S-TKO-01)のガイドページを作って。原本Notionは △△。トンマナはvisitに合わせて。
```

**認証を本番化する（Cloudflare Access）**
```
/guides/ を Cloudflare Access（メール認証・セッション3時間・認証メールをCRMへ蓄積）で
保護する設定手順を、ダッシュボード操作ベースで出して。
```

**ビジター向けの物語を /guide/ 公開ページに分離する**
```
新田ガイドの Visitors 部分を /guide/nitta/ の公開ページに分離して（SEO用・indexさせる）、
Staff Only は /guides/ に残して Access 保護前提に。構成案を出して。
```

**公開する**
```
guides/nitta-guide.html を visit. repo にコミットして push して。
```

**ローカルで見たい**
```
visit のローカルサーバを立てて、guides/nitta-guide.html を確認できるURLを出して。
（内部的には .claude/launch.json の "visit"(:8802) を使用）
```

## 7. 残タスク / TODO

- [ ] **Cloudflare Access** 設定（メール認証・3時間・メール→CRM）＝本番の認証
- [ ] Visitors（公開）と Staff Only（認証）の**パス分離**（/guide/ 公開・/guides/ 認証）
- [ ] 繁體中文の精度チェック（ビジター文は初版・要ネイティブ確認）
- [ ] Staff Only の「現場フレーズ集（仏・繁中）」を各シーンへ拡充
- [ ] ビジター向けの**写真**差し込み（現在はテキストのみ）
- [ ] サイト構造のコーポレート化（Experiences / Guide / For the Trade）
      モック：dashboard repo `projects/ranope/visit_corporate_mock.html`

---
_作成：Plat 米沢 / Claude。内容の正は Notion「🧵 新田」。本ファイルは git（plat-yonezawa-visit）で管理。_
