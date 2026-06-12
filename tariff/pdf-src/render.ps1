# Render all print_<PID>_<lang>.html to ../pdf/<PID>_<lang>.pdf via headless Chrome.
# Usage (PowerShell):  ./render.ps1
# Prereq:  perl build.pl   (regenerates the print_*.html from the 商品タリフDB data)
$ErrorActionPreference = "Stop"
$chrome = "C:\Program Files\Google\Chrome\Application\chrome.exe"
if (-not (Test-Path $chrome)) { $chrome = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" }
$src = $PSScriptRoot
$dst = Join-Path (Split-Path $src -Parent) "pdf"
$ud  = Join-Path $env:TEMP "chrome-pdf-profile"
# O-STY-02 は内容未確定のため配布対象から除外中（Coming Soon）。確定したらリストに戻す。
$codes = @("C-NTA-01","S-TKO-01","O-STY-01","O-STY-03")
$ok = 0
foreach ($code in $codes) { foreach ($lang in @("en","fr","zh")) {
  $inPath = Join-Path $src ("print_{0}_{1}.html" -f $code,$lang)
  $in  = "file:///" + ($inPath.Replace('\','/'))
  $out = Join-Path $dst ("{0}_{1}.pdf" -f $code,$lang)
  $a = @("--headless=new","--disable-gpu","--no-sandbox","--user-data-dir=$ud",
         "--no-pdf-header-footer","--run-all-compositor-stages-before-draw",
         "--virtual-time-budget=20000","--print-to-pdf=$out",$in)
  Start-Process -FilePath $chrome -ArgumentList $a -NoNewWindow -Wait | Out-Null
  if (Test-Path $out) { $ok++; Write-Host ("OK  {0}_{1}.pdf" -f $code,$lang) }
  else { Write-Host ("FAIL {0}_{1}" -f $code,$lang) }
}}
Write-Host "rendered $ok / 15"
