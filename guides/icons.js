/* YONEZAWA GUIDES の線アイコン（24×24・線だけ）。
   ガイドアプリ（/guides/）と管理画面（pm の /dashboard/guide-app/）の両方がこのファイルを読む。
   足すときは名前と path を1行足すだけ。管理画面の選択肢にも自動で出る。 */
window.YG_ICONS = {
  flag:     { label: '旗・まつり',   d: '<path d="M5 21V4"/><path d="M5 4h12l-2.5 4L17 12H5"/>' },
  fireworks:{ label: '花火',         d: '<path d="M12 3v4M12 17v4M3 12h4M17 12h4M5.6 5.6l2.8 2.8M15.6 15.6l2.8 2.8M5.6 18.4l2.8-2.8M15.6 8.4l2.8-2.8"/>' },
  torii:    { label: '神社',         d: '<path d="M3 5.5c4 1.2 14 1.2 18 0"/><path d="M4.5 9.5h15"/><path d="M7 6.3V21M17 6.3V21"/><path d="M12 9.5v-3"/>' },
  thread:   { label: '織物・手仕事', d: '<rect x="8" y="5" width="8" height="14" rx="1"/><path d="M6 5h12M6 19h12M8 9l8 2.5M8 13l8 2.5"/>' },
  sake:     { label: '酒蔵',         d: '<path d="M10 3h4v4l2 3v10a1 1 0 0 1-1 1H9a1 1 0 0 1-1-1V10l2-3z"/><path d="M8 13h8"/>' },
  mountain: { label: '山・自然',     d: '<path d="M3 19l6-10 4 6 3-4 5 8z"/>' },
  leaf:     { label: '里山・食',     d: '<path d="M5 19C5 11 11 5 19 5c0 8-6 14-14 14z"/><path d="M5 19l8-8"/>' },
  castle:   { label: '城下町・建物', d: '<path d="M4 21V10l4-3 4 3 4-3 4 3v11z"/><path d="M10 21v-5h4v5"/>' },
  pin:      { label: '場所・地図',   d: '<path d="M12 21s-6-5.5-6-11a6 6 0 0 1 12 0c0 5.5-6 11-6 11z"/><circle cx="12" cy="10" r="2"/>' },
  book:     { label: '読みもの',     d: '<path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20V3H6.5A2.5 2.5 0 0 0 4 5.5z"/><path d="M4 19.5A2.5 2.5 0 0 0 6.5 22H20v-5"/>' },
  mail:     { label: 'お問い合わせ', d: '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3.5 6.5l8.5 6.5 8.5-6.5"/>' },
  stay:     { label: '食・宿',       d: '<path d="M3 18V7M3 14h18v4M21 14v-2a3 3 0 0 0-3-3h-7v5"/><circle cx="7" cy="11" r="1.6"/>' },
  ticket:   { label: 'ツアー・予約', d: '<path d="M4 7h16v3a2 2 0 0 0 0 4v3H4v-3a2 2 0 0 0 0-4z"/><path d="M14 7v10" stroke-dasharray="1.5 2"/>' },
  help:     { label: '使い方',       d: '<circle cx="12" cy="12" r="9"/><path d="M9.6 9.4a2.5 2.5 0 1 1 3.4 2.4c-.6.3-1 .8-1 1.5v.7M12 17h.01"/>' },
  info:     { label: 'このサイトについて', d: '<circle cx="12" cy="12" r="9"/><path d="M12 11v5M12 8h.01"/>' },
};
window.YG_ICON_SVG = function (name, size) {
  var i = window.YG_ICONS[name] || window.YG_ICONS.book;
  var s = size || 30;
  return '<svg viewBox="0 0 24 24" width="' + s + '" height="' + s + '" fill="none" stroke="currentColor"' +
    ' stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' + i.d + '</svg>';
};
