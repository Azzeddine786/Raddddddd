(function () {
  'use strict';
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  function lsGet(k) { try { return localStorage.getItem(k); } catch (e) { return null; } }
  function lsSet(k, v) { try { localStorage.setItem(k, v); } catch (e) {} }

  var toastEl = $('#toast'), toastTimer;
  function toast(msg) {
    if (!toastEl) return;
    toastEl.textContent = msg;
    toastEl.classList.add('show');
    clearTimeout(toastTimer);
    toastTimer = setTimeout(function () { toastEl.classList.remove('show'); }, 2600);
  }

  /* ---------- common: menu, clock, cookie notice ---------- */
  var menuBtn = $('#menuBtn'), nav = $('#mainNav');
  if (menuBtn && nav) {
    menuBtn.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      menuBtn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }

  var clock = $('#clock');
  if (clock) {
    var tick = function () {
      try {
        clock.textContent = new Date().toLocaleTimeString('en-GB', { timeZone: 'Africa/Casablanca', hour: '2-digit', minute: '2-digit' });
      } catch (e) { clock.textContent = ''; }
    };
    tick(); setInterval(tick, 20000);
  }

  var cookie = $('#cookieBar');
  if (cookie && !lsGet('rm_cookie')) {
    cookie.classList.add('show');
    $('#cookieOk').addEventListener('click', function () {
      lsSet('rm_cookie', '1');
      cookie.classList.remove('show');
    });
  }

  /* ---------- article: reading progress + copy link ---------- */
  var bar2 = $('#progress'), prose = $('.prose');
  if (bar2 && prose) {
    var onScroll = function () {
      var r = prose.getBoundingClientRect(), total = r.height - window.innerHeight * 0.6;
      var pct = Math.min(100, Math.max(0, (-r.top / Math.max(total, 1)) * 100));
      bar2.style.width = pct + '%';
    };
    window.addEventListener('scroll', onScroll, { passive: true }); onScroll();
  }
  $$('[data-copy]').forEach(function (b) {
    b.addEventListener('click', function () {
      var u = b.getAttribute('data-copy');
      var done = function () { toast('تم نسخ الرابط'); };
      if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(u).then(done, done); else done();
    });
  });

  /* ---------- home: directory + player ---------- */
  var grid = $('#stationGrid');
  if (!grid) return;

  var stations = [];
  try { stations = JSON.parse($('#stations-data').textContent); } catch (e) {}
  var byId = {};
  stations.forEach(function (s) { byId[s.id] = s; });

  var favs = [];
  try { favs = JSON.parse(lsGet('rm_favs') || '[]'); } catch (e) { favs = []; }
  var filter = 'all', query = '';
  var cards = $$('.station', grid);
  var countEl = $('#countTxt'), emptyEl = $('#emptyBox'), search = $('#mainSearch');

  function norm(s) { return (s || '').toLowerCase().trim(); }

  function applyFilter() {
    var shown = 0;
    cards.forEach(function (c) {
      var id = +c.getAttribute('data-id');
      var ok = true;
      if (filter === 'fav') ok = favs.indexOf(id) > -1;
      else if (filter.indexOf('cat:') === 0) ok = c.getAttribute('data-cat') === filter.slice(4);
      else if (filter.indexOf('lang:') === 0) ok = c.getAttribute('data-lang').indexOf(filter.slice(5)) > -1;
      if (ok && query) ok = c.getAttribute('data-search').indexOf(query) > -1;
      c.hidden = !ok;
      if (ok) shown++;
    });
    if (countEl) countEl.textContent = shown;
    if (emptyEl) emptyEl.hidden = shown > 0;
  }

  $$('.chip').forEach(function (chip) {
    chip.addEventListener('click', function () {
      $$('.chip').forEach(function (x) { x.setAttribute('aria-pressed', 'false'); });
      chip.setAttribute('aria-pressed', 'true');
      filter = chip.getAttribute('data-filter');
      applyFilter();
    });
  });

  var st;
  if (search) {
    search.addEventListener('input', function () {
      clearTimeout(st);
      st = setTimeout(function () { query = norm(search.value); applyFilter(); }, 120);
    });
  }

  function setFavUi(btn, on) { btn.setAttribute('aria-pressed', on ? 'true' : 'false'); }
  cards.forEach(function (c) {
    var id = +c.getAttribute('data-id');
    setFavUi($('.fav', c), favs.indexOf(id) > -1);
    var img = $('.logo img', c);
    if (img) img.addEventListener('error', function () { img.remove(); });
  });

  grid.addEventListener('click', function (e) {
    var fav = e.target.closest('.fav');
    if (fav) {
      var id = +fav.getAttribute('data-fav');
      var i = favs.indexOf(id);
      if (i > -1) favs.splice(i, 1); else favs.push(id);
      lsSet('rm_favs', JSON.stringify(favs));
      setFavUi(fav, i === -1);
      toast(i === -1 ? 'أضيفت إلى المفضلة' : 'أزيلت من المفضلة');
      if (filter === 'fav') applyFilter();
      return;
    }
    var play = e.target.closest('[data-play]');
    if (play) playStation(+play.getAttribute('data-play'));
  });

  var heroPlay = $('#heroPlay');
  if (heroPlay) heroPlay.addEventListener('click', function () { playStation(1); });

  /* player */
  var audio = new Audio();
  audio.preload = 'none';
  var hls = null, currentId = null, hlsPromise = null;
  var bar = $('#playerBar'), pName = $('#pName'), pStatus = $('#pStatus'), pDot = $('#pDot'), pLogo = $('#pLogo'), playBtn = $('#playBtn');
  var ICON_PLAY = '<svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M8 5v14l11-7z"/></svg>';
  var ICON_PAUSE = '<svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M6 4h4v16H6zM14 4h4v16h-4z"/></svg>';

  function loadHls() {
    if (window.Hls) return Promise.resolve();
    if (hlsPromise) return hlsPromise;
    hlsPromise = new Promise(function (res, rej) {
      var s = document.createElement('script');
      s.src = 'https://cdn.jsdelivr.net/npm/hls.js@1';
      s.onload = res; s.onerror = rej;
      document.head.appendChild(s);
    });
    return hlsPromise;
  }

  function markPlaying() {
    cards.forEach(function (c) {
      var on = currentId === +c.getAttribute('data-id') && !audio.paused;
      c.classList.toggle('playing', on);
      var label = $('.play-label', c);
      if (label) label.textContent = on ? 'قيد التشغيل' : 'استمع';
    });
  }

  function fail() {
    pStatus.textContent = 'البث غير متوفر حالياً';
    pDot.style.background = '#777';
    playBtn.innerHTML = ICON_PLAY;
    toast('تعذّر تشغيل هذا البث. جرّب محطة أخرى أو أعد المحاولة لاحقاً.');
    markPlaying();
  }

  function playStation(id) {
    var s = byId[id];
    if (!s) return;
    if (currentId === id && !audio.paused) { audio.pause(); return; }
    currentId = id;
    bar.classList.add('open');
    document.body.classList.add('player-open');
    pName.textContent = s.name;
    pStatus.textContent = 'جاري التحميل…';
    pDot.style.background = '#f39c7d';
    pLogo.textContent = s.init;
    if (s.logo) {
      var im = new Image();
      im.alt = '';
      im.referrerPolicy = 'no-referrer';
      im.onload = function () { if (currentId === id) { pLogo.textContent = ''; pLogo.appendChild(im); } };
      im.src = s.logo;
    }
    playBtn.innerHTML = '<span class="spin"></span>';
    if (hls) { hls.destroy(); hls = null; }
    audio.pause(); audio.removeAttribute('src'); audio.load();

    if (/\.m3u8(\?|$)/.test(s.stream) && !audio.canPlayType('application/vnd.apple.mpegurl')) {
      loadHls().then(function () {
        if (currentId !== id) return;
        if (!window.Hls || !Hls.isSupported()) return fail();
        hls = new Hls();
        hls.loadSource(s.stream);
        hls.attachMedia(audio);
        hls.on(Hls.Events.MANIFEST_PARSED, function () { audio.play().catch(fail); });
        hls.on(Hls.Events.ERROR, function (_, d) { if (d && d.fatal) fail(); });
      }).catch(fail);
    } else {
      audio.src = s.stream;
      audio.play().catch(fail);
    }

    if ('mediaSession' in navigator) {
      try {
        navigator.mediaSession.metadata = new MediaMetadata({ title: s.name, artist: 'راديو المغرب' });
        navigator.mediaSession.setActionHandler('play', function () { audio.play(); });
        navigator.mediaSession.setActionHandler('pause', function () { audio.pause(); });
        navigator.mediaSession.setActionHandler('stop', stop);
      } catch (e) {}
    }
    markPlaying();
  }

  function stop() {
    audio.pause();
    if (hls) { hls.destroy(); hls = null; }
    audio.removeAttribute('src'); audio.load();
    currentId = null;
    bar.classList.remove('open');
    document.body.classList.remove('player-open');
    markPlaying();
  }

  audio.addEventListener('playing', function () {
    pStatus.textContent = 'مباشر';
    pDot.style.background = '#4ade80';
    playBtn.innerHTML = ICON_PAUSE;
    markPlaying();
  });
  audio.addEventListener('pause', function () {
    if (currentId) pStatus.textContent = 'متوقف مؤقتاً';
    playBtn.innerHTML = ICON_PLAY;
    markPlaying();
  });
  audio.addEventListener('error', function () { if (currentId && audio.getAttribute('src')) fail(); });

  playBtn.addEventListener('click', function () {
    if (!currentId) return playStation(1);
    if (audio.paused) audio.play().catch(fail); else audio.pause();
  });
  $('#stopBtn').addEventListener('click', stop);

  /* promo banner (home only, once per browser unless dismissed) */
  var promo = $('#promo');
  if (promo && !lsGet('rm_promo')) {
    setTimeout(function () { promo.classList.add('show'); }, 2500);
    $('#promoClose').addEventListener('click', function () {
      promo.classList.remove('show');
      lsSet('rm_promo', '1');
    });
  } else if (promo) { promo.remove(); }

  applyFilter();
})();
