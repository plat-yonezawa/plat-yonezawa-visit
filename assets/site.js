/* ============================================================
   PLAT YONEZAWA visit. — 計測・同意 集中管理（GA4 / GSC / Cookiebot）
   各ページは <script src="/assets/site.js" defer></script> を読むだけ。
   ▼ 本番化の手順（ここ1ファイルを編集するだけ）
     1) GA4_ID に GA4 測定ID（G-XXXXXXXXXX）を入れる
     2) （任意）COOKIEBOT_ID に Cookiebot のグループIDを入れる＝同意後にGA4発火
     3) GSC は index.html の google-site-verification メタ（または検証用HTML）で実施
   ※ ID が placeholder の間は外部スクリプトを一切読み込まない
     ＝ ソフト公開(noindex)を汚さない安全設計。
   ============================================================ */
(function () {
  var GA4_ID = 'G-XXXXXXXXXX';        // TODO: GA4 測定ID
  var COOKIEBOT_ID = 'CBID-XXXXXXXX'; // TODO: Cookiebot グループID（任意・同意管理）
  var isPlaceholder = function (v) { return !v || v.indexOf('XXXX') >= 0; };

  // ---- Consent Mode v2：既定は全拒否（同意後に update で許可） ----
  window.dataLayer = window.dataLayer || [];
  function gtag() { dataLayer.push(arguments); }
  window.gtag = window.gtag || gtag;
  gtag('consent', 'default', {
    ad_storage: 'denied',
    analytics_storage: 'denied',
    ad_user_data: 'denied',
    ad_personalization: 'denied',
    wait_for_update: 500
  });

  // ID 未設定なら計測タグを読み込まない（土台のみ・ソフト公開を維持）
  if (isPlaceholder(GA4_ID)) return;

  // ---- GA4（gtag.js）読み込み ----
  var s = document.createElement('script');
  s.async = true;
  s.src = 'https://www.googletagmanager.com/gtag/js?id=' + GA4_ID;
  document.head.appendChild(s);
  gtag('js', new Date());
  gtag('config', GA4_ID, { anonymize_ip: true });

  // ---- Cookiebot 同意連携（COOKIEBOT_ID 設定時のみ） ----
  if (!isPlaceholder(COOKIEBOT_ID)) {
    var c = document.createElement('script');
    c.id = 'Cookiebot';
    c.src = 'https://consent.cookiebot.com/uc.js';
    c.setAttribute('data-cbid', COOKIEBOT_ID);
    c.setAttribute('data-blockingmode', 'auto');
    c.async = true;
    document.head.appendChild(c);
    window.addEventListener('CookiebotOnConsentReady', function () {
      if (window.Cookiebot && Cookiebot.consent && Cookiebot.consent.statistics) {
        gtag('consent', 'update', { analytics_storage: 'granted' });
      }
    });
  }
})();
