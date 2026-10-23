/* Label checker for /label-checker/ — www.isedrepresentative.com
   Resizes photos in the browser, decodes QR codes where the browser can,
   posts to /api/label-check, shows the free summary, and unlocks the full
   report through the Netlify form "label-check" + /api/label-report. */
(function () {
  'use strict';
  var MAX_PHOTOS = 3, MAX_EDGE = 2000, QUALITY = 0.85;
  var $ = function (id) { return document.getElementById(id); };
  var form = $('lc-form'), thumbs = $('lc-thumbs'), go = $('lc-go'), busy = $('lc-busy'),
      err = $('lc-error'), sumEl = $('lc-summary'), gate = $('lc-gate'), repEl = $('lc-report');
  if (!form) return;

  var photos = []; // {data, type, url, kind, qr:[]}
  var last = null; // {summary, sealed, answers}
  var KINDS = [['device_label', 'Label on the device'], ['packaging', 'Packaging'], ['electronic_label_screen', 'E-label screen'], ['user_manual_page', 'Manual page']];
  var STATUS = { fail: 'Fix', warn: 'Review', check: 'Confirm', pass: 'OK' };
  var MARKET = { CA: 'Canada (ISED)', US: 'United States (FCC)' };

  function esc(s) { return String(s == null ? '' : s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  function track(name, params) { try { if (window.gtag) window.gtag('event', name, params || {}); } catch (e) {} }
  function showError(msg) { err.innerHTML = esc(msg); err.hidden = false; err.scrollIntoView({ behavior: 'smooth', block: 'center' }); }
  function clearError() { err.hidden = true; err.textContent = ''; }

  // ---------- photos ----------
  function loadImage(file) {
    return new Promise(function (resolve, reject) {
      var url = URL.createObjectURL(file);
      var img = new Image();
      img.onload = function () { resolve({ img: img, url: url }); };
      img.onerror = function () { URL.revokeObjectURL(url); reject(new Error('unreadable')); };
      img.src = url;
    });
  }

  function decodeQr(source) {
    if (!('BarcodeDetector' in window)) return Promise.resolve([]);
    try {
      var det = new window.BarcodeDetector({ formats: ['qr_code'] });
      return det.detect(source).then(function (codes) { return codes.map(function (c) { return c.rawValue; }).filter(Boolean); }).catch(function () { return []; });
    } catch (e) { return Promise.resolve([]); }
  }

  function addFiles(list) {
    clearError();
    var files = Array.prototype.slice.call(list || []);
    var room = MAX_PHOTOS - photos.length;
    if (files.length > room) showError('You can add up to ' + MAX_PHOTOS + ' photos. The extra ones were left out.');
    files.slice(0, room).forEach(function (file) {
      loadImage(file).then(function (r) {
        var scale = Math.min(1, MAX_EDGE / Math.max(r.img.naturalWidth, r.img.naturalHeight));
        var c = document.createElement('canvas');
        c.width = Math.round(r.img.naturalWidth * scale); c.height = Math.round(r.img.naturalHeight * scale);
        c.getContext('2d').drawImage(r.img, 0, 0, c.width, c.height);
        var dataUrl = c.toDataURL('image/jpeg', QUALITY);
        return decodeQr(c).then(function (qr) {
          photos.push({ data: dataUrl.split(',')[1], type: 'image/jpeg', url: dataUrl, kind: photos.length ? 'packaging' : 'device_label', qr: qr });
          URL.revokeObjectURL(r.url);
          renderThumbs();
        });
      }).catch(function () {
        showError('That file could not be opened as an image. On a computer, HEIC photos from an iPhone may need converting to JPEG first; on the phone itself, “Take a photo” works directly.');
      });
    });
  }

  function renderThumbs() {
    thumbs.innerHTML = '';
    photos.forEach(function (p, i) {
      var li = document.createElement('li');
      var opts = KINDS.map(function (k) { return '<option value="' + k[0] + '"' + (p.kind === k[0] ? ' selected' : '') + '>' + k[1] + '</option>'; }).join('');
      li.innerHTML = '<img src="' + p.url + '" alt="Photo ' + (i + 1) + '">' +
        '<label class="lc-sr" for="lc-kind-' + i + '">What this photo shows</label><select id="lc-kind-' + i + '">' + opts + '</select>' +
        (p.qr.length ? '<span class="lc-qr">QR code read</span>' : '') +
        '<button type="button" class="lc-remove" aria-label="Remove photo ' + (i + 1) + '">Remove</button>';
      li.querySelector('select').addEventListener('change', function (e) { p.kind = e.target.value; });
      li.querySelector('button').addEventListener('click', function () { photos.splice(i, 1); renderThumbs(); });
      thumbs.appendChild(li);
    });
    go.disabled = photos.length === 0;
  }

  $('lc-camera').addEventListener('change', function (e) { addFiles(e.target.files); e.target.value = ''; });
  $('lc-files').addEventListener('change', function (e) { addFiles(e.target.files); e.target.value = ''; });

  function syncRadio() { var none = form.querySelector('input[name=radio]:checked').value === 'none'; $('lc-radio-more').hidden = none; }
  Array.prototype.forEach.call(form.querySelectorAll('input[name=radio]'), function (r) { r.addEventListener('change', syncRadio); });

  function answers() {
    var v = function (n) { var el = form.querySelector('input[name=' + n + ']:checked'); return el ? el.value : ''; };
    var t = function (n) { return (form.elements[n].value || '').trim(); };
    var qr = []; photos.forEach(function (p) { qr = qr.concat(p.qr); });
    return {
      markets: { ca: form.elements.mk_ca.checked, us: form.elements.mk_us.checked },
      radio: v('radio'), module: v('module'), digital: v('digital'), small: v('small'), display: v('display'),
      expected: { ic: t('exp_ic'), fcc: t('exp_fcc'), hvin: t('exp_hvin'), pmn: t('exp_pmn') },
      qr_decoded: qr
    };
  }

  // ---------- run the check ----------
  form.addEventListener('submit', function (e) {
    e.preventDefault();
    clearError();
    if (!photos.length) return showError('Please add a photo of the label.');
    var a = answers();
    if (!a.markets.ca && !a.markets.us) return showError('Choose at least one market.');
    go.disabled = true; busy.hidden = false; sumEl.hidden = true; gate.hidden = true; repEl.hidden = true;
    busy.scrollIntoView({ behavior: 'smooth', block: 'center' });
    track('label_check_run', { photos: photos.length });
    fetch('/api/label-check', {
      method: 'POST', headers: { 'content-type': 'application/json' },
      body: JSON.stringify({ images: photos.map(function (p) { return { data: p.data, type: p.type }; }), kinds: photos.map(function (p) { return p.kind; }), answers: a, website: form.elements.website.value })
    }).then(function (res) {
      return res.json().catch(function () { return { error: 'The checker did not respond. Please try again.' }; }).then(function (j) { j._ok = res.ok; return j; });
    }).then(function (j) {
      busy.hidden = true; go.disabled = false;
      if (!j._ok || !j.summary) return showError(j.error || 'Something went wrong. Please try again.');
      last = { summary: j.summary, sealed: j.sealed, answers: a };
      renderSummary(j.summary);
    }).catch(function () {
      busy.hidden = true; go.disabled = false;
      showError('The connection failed. Please check your network and try again.');
    });
  });

  function seenHtml(s) {
    var rows = [['IC number', s.ic], ['FCC ID', s.fcc], ['HVIN / model', s.hvin], ['Product name', s.names], ['ICES marking', s.ices]];
    return '<table class="lc-seen"><caption>What we read from your photo — check it is right</caption><tbody>' + rows.map(function (r) {
      return '<tr><th scope="row">' + r[0] + '</th><td>' + (r[1] && r[1].length ? r[1].map(function (x) { return '<code>' + esc(x) + '</code>'; }).join('<br>') : '<span class="lc-none">not found</span>') + '</td></tr>';
    }).join('') + '</tbody></table>';
  }

  function renderSummary(s) {
    var head = s.overall === 'fail' ? ['lc-bad', 'Changes needed'] : s.overall === 'warn' ? ['lc-mid', 'Items to review'] : ['lc-good', 'No problems found in what we could see'];
    var h = '<div class="lc-banner ' + head[0] + '"><b>' + head[1] + '</b></div><div class="lc-markets">';
    Object.keys(s.markets).forEach(function (m) {
      var c = s.markets[m];
      h += '<div><h3>' + MARKET[m] + '</h3><p><span class="lc-n lc-fail">' + c.fail + ' to fix</span><span class="lc-n lc-warn">' + c.warn + ' to review</span><span class="lc-n lc-check">' + c.check + ' to confirm</span><span class="lc-n lc-pass">' + c.pass + ' OK</span></p></div>';
    });
    h += '</div>';
    if (s.headlines.length) {
      h += '<h3>Found on your label</h3><ul class="lc-heads">' + s.headlines.map(function (x) {
        return '<li><span class="lc-tag lc-' + x.status + '">' + STATUS[x.status] + '</span> ' + (x.market === 'CA' ? 'Canada' : 'US') + ': ' + esc(x.title) + '</li>';
      }).join('') + '</ul>';
    }
    h += seenHtml(s.seen);
    sumEl.innerHTML = h; sumEl.hidden = false;
    gate.hidden = false;
    gate.elements.summary.value = textSummary(s);
    gate.elements.read_from_label.value = JSON.stringify(s.seen).slice(0, 4000);
    gate.elements.answers.value = JSON.stringify(last.answers).slice(0, 2000);
    sumEl.scrollIntoView({ behavior: 'smooth', block: 'start' });
    track('label_check_summary', { overall: s.overall });
  }

  function textSummary(s) {
    var out = ['Overall: ' + s.overall];
    Object.keys(s.markets).forEach(function (m) { var c = s.markets[m]; out.push(m + ': ' + c.fail + ' fix, ' + c.warn + ' review, ' + c.check + ' confirm, ' + c.pass + ' ok'); });
    s.headlines.forEach(function (x) { out.push('[' + x.market + ' ' + x.status + '] ' + x.title); });
    return out.join('\n').slice(0, 4000);
  }

  // ---------- unlock the full report ----------
  gate.addEventListener('submit', function (e) {
    e.preventDefault();
    clearError();
    if (!last) return;
    var btn = gate.querySelector('button[type=submit]');
    var email = (gate.elements.email.value || '').trim();
    if (!gate.checkValidity()) { gate.reportValidity(); return; }
    btn.disabled = true; btn.textContent = 'Preparing your report…';
    var fd = new FormData(gate);
    var lead = fetch('/', { method: 'POST', headers: { 'Content-Type': 'application/x-www-form-urlencoded' }, body: new URLSearchParams(fd).toString() }).catch(function () {});
    var rep = fetch('/api/label-report', {
      method: 'POST', headers: { 'content-type': 'application/json' },
      body: JSON.stringify({ sealed: last.sealed, email: email, product: gate.elements.product.value, website: gate.elements.website.value })
    }).then(function (res) { return res.json().then(function (j) { j._ok = res.ok; return j; }); });
    Promise.all([lead, rep]).then(function (r) {
      var j = r[1];
      btn.disabled = false; btn.textContent = 'Show my full report';
      if (!j._ok || !j.report) return showError(j.error || 'Something went wrong. Please try again.');
      gate.hidden = true;
      renderReport(j.report, j.emailed, email);
      track('generate_lead', { form_name: 'label-check' });
    }).catch(function () {
      btn.disabled = false; btn.textContent = 'Show my full report';
      showError('The connection failed. Please try again.');
    });
  });

  function renderReport(r, emailed, email) {
    var h = '<h2>Full report</h2><p class="hint">' + (emailed ? 'A copy has been sent to ' + esc(email) + '. ' : '') + 'Rules reviewed ' + esc(r.summary.version) + '.</p>';
    ['CA', 'US'].forEach(function (m) {
      var list = r.items.filter(function (i) { return i.market === m; });
      if (!list.length) return;
      var order = { fail: 0, warn: 1, check: 2, pass: 3 };
      list.sort(function (a, b) { return order[a.status] - order[b.status]; });
      h += '<h3>' + MARKET[m] + '</h3><ol class="lc-items">';
      list.forEach(function (i) {
        h += '<li class="lc-item lc-b-' + i.status + '"><p class="lc-it"><span class="lc-tag lc-' + i.status + '">' + STATUS[i.status] + '</span> <b>' + esc(i.title) + '</b></p><p>' + esc(i.detail) + '</p>' +
          (i.fix ? '<p class="lc-fix"><b>What to do:</b> ' + esc(i.fix) + '</p>' : '') +
          (i.cite.length ? '<p class="lc-cite">' + i.cite.map(function (c) { return '<a href="' + esc(c.url) + '" rel="noopener" target="_blank">' + esc(c.label) + '</a>'; }).join(' · ') + '</p>' : '') + '</li>';
      });
      h += '</ol>';
    });
    if (r.notes && r.notes.length) h += '<h3>Reader notes</h3><p class="hint">Automated observations about the photo, not legal conclusions.</p><ul>' + r.notes.map(function (n) { return '<li>' + esc(n) + '</li>'; }).join('') + '</ul>';
    h += '<p class="lc-disclaim">This is an automated reading of your photos, checked against the labelling rules cited above. It is general information, not legal advice and not a review by a lawyer. It does not test the product or decide which standards apply to it, and your certification body or test lab has the final word on the label for a specific device.</p>';
    h += '<p><button type="button" class="btn" id="lc-print">Print or save as PDF</button> <a class="btn btn-primary" href="/label-and-manual-review/">Have a lawyer review the label (US$249)</a> <button type="button" class="btn" id="lc-again">Check another label</button></p>';
    repEl.innerHTML = h; repEl.hidden = false;
    $('lc-print').addEventListener('click', function () { window.print(); });
    $('lc-again').addEventListener('click', function () { photos = []; renderThumbs(); repEl.hidden = true; sumEl.hidden = true; last = null; form.scrollIntoView({ behavior: 'smooth' }); });
    repEl.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }
})();
