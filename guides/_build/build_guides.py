# -*- coding: utf-8 -*-
"""ガイドアプリ（YONEZAWA GUIDES）用に、各ガイドを2つの版で書き出す。

  guides/<slug>/index.html        … 観光客向けだけ（誰でも見られる）
  guides/staff/<slug>/index.html  … 完全版＝観光客＋ガイド・通訳向け（暗証番号の内側）
  guides/assets/<slug>/...        … 画像・動画（両方の版から絶対パスで参照）

多言語ガイド（上杉まつり・戦国花火・上杉神社）は plat-dashboard の
multilingual-cultural-event-guide スキルの build.py で作る（正は plat-dashboard 側）。
新田織物は同じフォルダの nitta_build.py で作る。

  python3 guides/_build/build_guides.py --pm-repo ~/Plat-yonezawa_Calude

生成物は手で直さない（直すのは plat-dashboard の projects/guides/<slug>.json か nitta_content.py）。
"""
import argparse
import os
import re
import shutil
import subprocess
import sys
from urllib.parse import unquote

HERE = os.path.dirname(os.path.abspath(__file__))
GUIDES = os.path.dirname(HERE)            # visit の guides/

# 多言語ガイド。config が無いもの（参考実装）は html を書く。
MULTI = [
    {"slug": "uesugi-matsuri", "html": "projects/uesugi-matsuri-guide.html"},
    {"slug": "sengoku-hanabi", "config": "projects/guides/sengoku-hanabi.json",
     "built": "projects/sengoku-hanabi-guide.html"},
    {"slug": "uesugi-jinja", "config": "projects/guides/uesugi-jinja.json",
     "built": "projects/uesugi-jinja-guide.html"},
]
ASSET_RE = re.compile(r'\b(?:src|poster)="((?:images|videos)/[^"]+)"')


def copy_assets(pm, source_html, slug):
    """ガイドが参照する画像・動画だけを guides/assets/<slug>/ へ写す。"""
    text = open(source_html, encoding="utf-8").read()
    n = 0
    for rel in sorted(set(ASSET_RE.findall(text))):
        rel = unquote(rel)
        src = os.path.join(pm, "projects", rel)
        if not os.path.exists(src):
            sys.exit("画像・動画が見つかりません: %s" % src)
        dst = os.path.join(GUIDES, "assets", slug, rel)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        if not os.path.exists(dst) or os.path.getsize(dst) != os.path.getsize(src):
            shutil.copy2(src, dst)
        n += 1
    return n


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit("失敗: %s\n%s%s" % (" ".join(cmd), r.stdout, r.stderr))
    return r.stdout


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pm-repo", default=os.path.expanduser("~/Plat-yonezawa_Calude"),
                    help="plat-dashboard のリポジトリ（スキルと config がある所）")
    args = ap.parse_args()
    pm = os.path.abspath(args.pm_repo)
    build = os.path.join(pm, ".claude/skills/multilingual-cultural-event-guide/scripts/build.py")
    if not os.path.exists(build):
        sys.exit("build.py が見つかりません: %s" % build)

    for g in MULTI:
        slug = g["slug"]
        src_html = os.path.join(pm, g.get("built") or g["html"])
        n = copy_assets(pm, src_html, slug)
        common = ["--asset-prefix", "/guides/assets/%s/" % slug, "--home-url", "/guides/", "--quiet"]
        source = (["--config", os.path.join(pm, g["config"])] if g.get("config")
                  else ["--from-html", os.path.join(pm, g["html"])])
        out_v = os.path.join(GUIDES, slug, "index.html")
        out_f = os.path.join(GUIDES, "staff", slug, "index.html")
        run([sys.executable, build] + source + ["--variant", "visitor", "--output", out_v,
                                                "--staff-url", "/guides/staff/%s/?mode=interpreter" % slug] + common)
        run([sys.executable, build] + source + ["--variant", "full", "--output", out_f] + common)
        print("%-15s 観光客向け %7s bytes ／ 完全版 %7s bytes ／ 画像・動画 %d点"
              % (slug, f"{os.path.getsize(out_v):,}", f"{os.path.getsize(out_f):,}", n))

    print(run([sys.executable, os.path.join(HERE, "nitta_build.py")]).strip())


if __name__ == "__main__":
    main()
