/* ============================================================
   PLAT YONEZAWA visit. — 計測・同意 集中管理
   GA4 / GSC / Microsoft Clarity / HubSpot ＋ UTM経路計測 ＋ イベントAPI
   各ページは <script src="/assets/site.js" defer></script> を読むだけ。

   ▼ 本番化：下の CONFIG に各IDを入れるだけ（ここ1ファイル）
     GA4_ID       … GA4 測定ID（G-XXXXXXXXXX）
     CLARITY_ID   … Microsoft Clarity プロジェクトID（ヒートマップ/録画）
     HUBSPOT_ID   … HubSpot ポータルID（トラッキング／CRM）
     COOKIEBOT_ID … Cookiebot グループID（同意管理・任意）
     GSC          … index.html / lp.html の google-site-verification メタで実施
                    （＋GA4管理画面で GA4↔GSC を連携）

   ▼ 設計方針
     - ID が placeholder の間は外部スクリプトを一切読み込まない（ソフト公開を汚さない）。
     - GA4 は Consent Mode v2（既定 denied）。Cookiebot の同意で update。
     - Clarity / HubSpot は Cookie を使うため「同意後のみ」ロード（Cookiebot 連携時）。
     - UTM（qr / メール / 展示会 等の経路）を初回タッチで保持 → GA4 と フォーム(HubSpot)へ。
     - window.plat.track(name, params) で任意イベントを GA4 に送れる（資料請求・予約リクエスト等）。
   ============================================================ */
(function () {
  // ===== CONFIG（本番化時にここを編集） =====
  var GA4_ID       = 'G-35LZ144XYC';   // ✅ GA4測定ID（プロパティ PLAT YONEZAWA visit. / ストリーム visit）
  var CLARITY_ID   = 'CLARITYXXXX';    // TODO: Microsoft Clarity プロジェクトID（陽平）
  var HUBSPOT_ID   = '245638622';      // ✅ HubSpot ポータルID（na2）投入済み（同意後にロード）
  var COOKIEBOT_ID = 'CBID-XXXXXXXX';  // TODO: Cookiebot グループID（同意管理／これが入ると統計系がロード）
  var ph = function (v) { return !v || v.indexOf('XXXX') >= 0; };

  // ===== dataLayer / gtag shim（常に用意） =====
  window.dataLayer = window.dataLayer || [];
  function gtag(){ dataLayer.push(arguments); }
  window.gtag = window.gtag || gtag;

  // ===== UTM 経路の取得・保持（QR/メール/展示会などの流入元） =====
  function parseUTM(){
    var p = new URLSearchParams(location.search), o = {}, keys = ['utm_source','utm_medium','utm_campaign','utm_content','utm_term'];
    keys.forEach(function(k){ if(p.get(k)) o[k] = p.get(k); });
    return o;
  }
  var cur = parseUTM(), stored = {};
  try { stored = JSON.parse(sessionStorage.getItem('plat_utm') || '{}'); } catch(e){}
  if (Object.keys(cur).length) {            // 初回タッチのUTMを保持
    stored = cur;
    try { sessionStorage.setItem('plat_utm', JSON.stringify(cur)); } catch(e){}
  }

  // ===== 公開API：window.plat =====
  window.plat = window.plat || {};
  window.plat.utm = stored;                                   // フォームのhidden等に使う
  window.plat.track = function (name, params) {               // 任意イベント→GA4
    try { gtag('event', name, Object.assign({}, stored, params || {})); } catch(e){}
  };
  // フォームのhidden inputへUTMを自動流し込み（name="utm_source"等があれば）
  window.plat.fillUTM = function (form) {
    if(!form) return;
    Object.keys(stored).forEach(function(k){
      var el = form.querySelector('[name="'+k+'"]'); if(el) el.value = stored[k];
    });
  };

  // ===== Consent Mode v2（既定 denied／同意後に update） =====
  gtag('consent', 'default', {
    ad_storage:'denied', analytics_storage:'denied',
    ad_user_data:'denied', ad_personalization:'denied', wait_for_update:500
  });

  // ===== GA4 本体（consentは既定denied＝Cookieless計測から開始） =====
  if (!ph(GA4_ID)) {
    var s = document.createElement('script');
    s.async = true; s.src = 'https://www.googletagmanager.com/gtag/js?id=' + GA4_ID;
    document.head.appendChild(s);
    gtag('js', new Date());
    // UTMはGA4が自動でsource/medium/campaignに取り込む。content粒度も送る。
    gtag('config', GA4_ID, { anonymize_ip:true, campaign_content: stored.utm_content || undefined });
  }

  // ===== 同意後にのみロードするもの（Clarity / HubSpot / GA4のstorage許可） =====
  function onConsentGranted(){
    gtag('consent','update',{ analytics_storage:'granted' });
    if (!ph(CLARITY_ID)) {  // Microsoft Clarity（ヒートマップ・録画）
      (function(c,l,a,r,i,t,y){c[a]=c[a]||function(){(c[a].q=c[a].q||[]).push(arguments)};
        t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;
        y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);})(window,document,"clarity","script",CLARITY_ID);
    }
    if (!ph(HUBSPOT_ID)) {  // HubSpot トラッキング
      var h=document.createElement('script'); h.id='hs-script-loader'; h.async=true; h.defer=true;
      h.src='//js.hs-scripts.com/'+HUBSPOT_ID+'.js'; document.head.appendChild(h);
    }
  }

  // ===== 同意の取り扱い =====
  if (!ph(COOKIEBOT_ID)) {
    var c=document.createElement('script'); c.id='Cookiebot';
    c.src='https://consent.cookiebot.com/uc.js'; c.setAttribute('data-cbid',COOKIEBOT_ID);
    c.setAttribute('data-blockingmode','auto'); c.async=true; document.head.appendChild(c);
    window.addEventListener('CookiebotOnConsentReady', function(){
      if (window.Cookiebot && Cookiebot.consent && Cookiebot.consent.statistics) onConsentGranted();
    });
  }
  // ※ Cookiebot未設定の間、Clarity/HubSpotは読み込まれません（同意管理が入るまで安全側）。
  //   同意管理なしで有効化したい場合のみ、ここで onConsentGranted() を明示呼び出し。
})();
