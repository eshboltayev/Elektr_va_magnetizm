/* Elektr va magnetizm — interaktiv simulyatorlar.
   Har bir simulyator HTML’da <div class="sim-box" data-sim="KALIT"></div> ko‘rinishida chaqiriladi.
   Modellar o‘quv maqsadida soddalashtirilgan; birliklar SI (alohida ko‘rsatilmagan bo‘lsa). */
(() => {
  'use strict';
  const g0 = 9.81, k0 = 8.988e9, e0 = 8.854e-12, mu0 = 4e-7 * Math.PI, qe = 1.602e-19, me = 9.109e-31, mp = 1.673e-27, cL = 2.998e8;
  const A = s => (window.YAF_ALIF ? window.YAF_ALIF.A(s) : String(s));
  const C = { cyan:'#22d3ee', green:'#34d399', amber:'#fbbf24', rose:'#fb7185', violet:'#a78bfa', blue:'#60a5fa', grid:'#1e2c44', axis:'#64748b', text:'#cbd5e1' };
  const SUP = { '-':'⁻', '0':'⁰','1':'¹','2':'²','3':'³','4':'⁴','5':'⁵','6':'⁶','7':'⁷','8':'⁸','9':'⁹' };
  const sci = (v, d = 2) => {
    if (!isFinite(v)) return '—';
    if (v === 0) return '0';
    const e = Math.floor(Math.log10(Math.abs(v)));
    if (e >= -2 && e <= 3) return v.toFixed(Math.max(0, d - (e > 0 ? e : 0)));
    const m = v / 10 ** e;
    return `${m.toFixed(d)}·10${String(e).split('').map(ch => SUP[ch]).join('')}`;
  };
  const fx = (v, d = 3) => (isFinite(v) ? Number(v).toFixed(d) : '—');

  function ctx2d(canvas) {
    const r = canvas.getBoundingClientRect();
    const zoom = parseFloat(getComputedStyle(document.documentElement).zoom) || 1;
    const dpr = Math.min((window.devicePixelRatio || 1) * zoom, 4);
    const w = Math.max(1, Math.floor(canvas.clientWidth || r.width)), h = Math.max(1, Math.floor(canvas.clientHeight || r.height));
    if (canvas.width !== w * dpr || canvas.height !== h * dpr) { canvas.width = w * dpr; canvas.height = h * dpr; }
    const c = canvas.getContext('2d'); c.setTransform(dpr, 0, 0, dpr, 0, 0); c.clearRect(0, 0, w, h);
    return { c, w, h };
  }

  function niceTicks(a, b, n = 5) {
    const span = b - a; if (span <= 0) return [a];
    const raw = span / n, mag = 10 ** Math.floor(Math.log10(raw));
    const step = [1, 2, 2.5, 5, 10].map(s => s * mag).find(s => span / s <= n + .5) || mag * 10;
    const out = []; for (let t = Math.ceil(a / step) * step; t <= b + step * 1e-6; t += step) out.push(+t.toPrecision(10));
    return out;
  }

  /* Umumiy grafik chizuvchi */
  function plot(c, box, o) {
    const [X0, Y0, W, H] = box, L = 54, R = 12, T = 22, B = 36;
    const px = X0 + L, py = Y0 + T, pw = W - L - R, ph = H - T - B;
    const tx = v => (o.logx ? Math.log10(v) : v), ty = v => (o.logy ? Math.log10(Math.max(v, 1e-300)) : v);
    const [xa, xb] = o.xr.map(tx), [ya, yb] = o.yr.map(ty);
    const X = v => px + (tx(v) - xa) / (xb - xa) * pw;
    const Y = v => py + ph - (ty(v) - ya) / (yb - ya) * ph;
    c.save(); c.font = '11px JetBrains Mono, monospace'; c.lineWidth = 1;
    const xt = o.logx ? range(Math.ceil(xa), Math.floor(xb)).map(e => 10 ** e) : niceTicks(o.xr[0], o.xr[1], o.nx || 6);
    const yt = o.logy ? range(Math.ceil(ya), Math.floor(yb)).filter((e, i, arr) => arr.length < 9 || i % 2 === 0).map(e => 10 ** e) : niceTicks(o.yr[0], o.yr[1], o.ny || 5);
    c.strokeStyle = C.grid; c.fillStyle = C.axis; c.textAlign = 'center';
    xt.forEach(t => { const x = X(t); c.beginPath(); c.moveTo(x, py); c.lineTo(x, py + ph); c.stroke(); c.fillText(fmtTick(t), x, py + ph + 15); });
    c.textAlign = 'right';
    yt.forEach(t => { const y = Y(t); c.beginPath(); c.moveTo(px, y); c.lineTo(px + pw, y); c.stroke(); c.fillText(fmtTick(t), px - 6, y + 4); });
    c.strokeStyle = C.axis; c.strokeRect(px, py, pw, ph);
    if (!o.logy && o.yr[0] < 0 && o.yr[1] > 0) { c.strokeStyle = '#475569'; c.beginPath(); c.moveTo(px, Y(0)); c.lineTo(px + pw, Y(0)); c.stroke(); }
    if (!o.logx && o.xr[0] < 0 && o.xr[1] > 0) { c.strokeStyle = '#475569'; c.beginPath(); c.moveTo(X(0), py); c.lineTo(X(0), py + ph); c.stroke(); }
    c.fillStyle = C.text; c.textAlign = 'center'; c.fillText(A(o.xl || ''), px + pw / 2, py + ph + 30);
    c.textAlign = 'left'; c.fillText(A(o.yl || ''), px, py - 8);
    c.beginPath(); c.rect(px, py, pw, ph); c.clip();
    (o.fill || []).forEach(f => { c.fillStyle = f.c; c.beginPath(); f.pts.forEach(([x, y], i) => (i ? c.lineTo(X(x), Y(y)) : c.moveTo(X(x), Y(y)))); c.closePath(); c.fill(); });
    (o.series || []).forEach(s => {
      c.strokeStyle = s.c || C.cyan; c.lineWidth = s.w || 2; c.setLineDash(s.dash || []); c.beginPath(); let started = false;
      s.pts.forEach(([x, y]) => { if (!isFinite(y) || !isFinite(x) || (o.logy && y <= 0) || (o.logx && x <= 0)) { started = false; return; } const xx = X(x), yy = Y(y); if (!started) { c.moveTo(xx, yy); started = true; } else c.lineTo(xx, yy); });
      c.stroke(); c.setLineDash([]);
    });
    (o.vl || []).forEach(v => { c.strokeStyle = v.c || C.amber; c.setLineDash([5, 4]); c.beginPath(); c.moveTo(X(v.x), py); c.lineTo(X(v.x), py + ph); c.stroke(); c.setLineDash([]); if (v.l) { c.fillStyle = v.c || C.amber; c.fillText(A(v.l), X(v.x) + 4, py + 12); } });
    (o.hl || []).forEach(v => { c.strokeStyle = v.c || C.amber; c.setLineDash([5, 4]); c.beginPath(); c.moveTo(px, Y(v.y)); c.lineTo(px + pw, Y(v.y)); c.stroke(); c.setLineDash([]); if (v.l) { c.fillStyle = v.c || C.amber; c.fillText(A(v.l), px + 6, Y(v.y) - 5); } });
    (o.marks || []).forEach(m => { c.fillStyle = m.c || '#fff'; c.beginPath(); c.arc(X(m.x), Y(m.y), m.r || 5, 0, 7); c.fill(); if (m.l) { c.fillText(A(m.l), X(m.x) + 8, Y(m.y) - 8); } });
    c.restore();
    if ((o.legend || []).length) { c.fillStyle = 'rgba(3,7,18,.82)'; c.fillRect(px + pw - 156, py + 2, 152, o.legend.length * 16 + 8); }
    (o.legend || []).forEach((g, i) => { c.font = '11px Inter, sans-serif'; c.fillStyle = g.c; c.fillRect(px + pw - 150, py + 8 + i * 16, 12, 3); c.fillStyle = C.text; c.textAlign = 'left'; c.fillText(A(g.l), px + pw - 133, py + 13 + i * 16); });
    return { X, Y };
  }
  const fmtTick = t => (Math.abs(t) >= 1000 || (Math.abs(t) < .01 && t !== 0) ? sci(t, 1) : String(+t.toFixed(3)));
  const range = (a, b) => { const r = []; for (let i = a; i <= b; i++) r.push(i); return r; };
  const lin = (a, b, n) => Array.from({ length: n }, (_, i) => a + (b - a) * i / (n - 1));
  const label = (c, t, x, y, col = C.text, al = 'left') => { c.fillStyle = col; c.font = '12px Inter, sans-serif'; c.textAlign = al; c.fillText(A(t), x, y); };

  /* ---------- Chizish yordamchilari ---------- */
  const ln = (c, x1, y1, x2, y2, col = C.text, w = 1.5, dash) => { c.strokeStyle = col; c.lineWidth = w; c.setLineDash(dash || []); c.beginPath(); c.moveTo(x1, y1); c.lineTo(x2, y2); c.stroke(); c.setLineDash([]); };
  const arrow = (c, x1, y1, x2, y2, col = C.amber, w = 2) => { if (Math.hypot(x2 - x1, y2 - y1) < 1) return; ln(c, x1, y1, x2, y2, col, w); const a = Math.atan2(y2 - y1, x2 - x1), s = 8; c.fillStyle = col; c.beginPath(); c.moveTo(x2, y2); c.lineTo(x2 - s * Math.cos(a - .4), y2 - s * Math.sin(a - .4)); c.lineTo(x2 - s * Math.cos(a + .4), y2 - s * Math.sin(a + .4)); c.closePath(); c.fill(); };
  const circ = (c, x, y, r, col = C.text, fill, w = 1.5) => { c.beginPath(); c.arc(x, y, Math.max(r, .5), 0, 7); if (fill) { c.fillStyle = fill; c.fill(); } if (col) { c.strokeStyle = col; c.lineWidth = w; c.stroke(); } };
  const txt = (c, t, x, y, col = C.text, al = 'center', size = 12) => { c.fillStyle = col; c.font = `${size}px Inter, sans-serif`; c.textAlign = al; c.fillText(A(t), x, y); };
  const poly = (c, pts, col, w = 2, dash) => { c.strokeStyle = col; c.lineWidth = w; c.setLineDash(dash || []); c.beginPath(); pts.forEach(([x, y], i) => (i ? c.lineTo(x, y) : c.moveTo(x, y))); c.stroke(); c.setLineDash([]); };
  const rk4 = (f, s, dt) => { const k1 = f(s), k2 = f(s.map((v, i) => v + dt / 2 * k1[i])), k3 = f(s.map((v, i) => v + dt / 2 * k2[i])), k4 = f(s.map((v, i) => v + dt * k3[i])); return s.map((v, i) => v + dt / 6 * (k1[i] + 2 * k2[i] + 2 * k3[i] + k4[i])); };
  const agm = (a, b) => { for (let i = 0; i < 30; i++) { const t = (a + b) / 2; b = Math.sqrt(a * b); a = t; } return a; };
  const deg = Math.PI / 180;
  /* Parametrlar o‘zgarganda keshni yangilash (animatsiyali modellar uchun) */
  const cache = (cv, P, make) => { const key = JSON.stringify(P); if (cv._key !== key) { cv._key = key; cv._d = make(); cv._t = 0; } return cv._d; };
  const tick = (cv, dt) => { cv._t = (cv._t || 0) + Math.max(0, dt || 0); return cv._t; };

  const S = {};
  const sgnCol = q => (q > 0 ? C.rose : q < 0 ? C.blue : C.axis);
  const charge = (c, x, y, q, r = 11) => { circ(c, x, y, r, '#fff', sgnCol(q), 1.5); txt(c, q > 0 ? '+' : q < 0 ? '−' : '0', x, y + 4.5, '#fff', 'center', 14); };
  const resistor = (c, x1, y1, x2, y2, lab) => { const mx = (x1 + x2) / 2, my = (y1 + y2) / 2, hor = Math.abs(x2 - x1) > Math.abs(y2 - y1); if (hor) { ln(c, x1, y1, mx - 22, my, C.text, 2); ln(c, mx + 22, my, x2, y2, C.text, 2); c.strokeStyle = C.amber; c.lineWidth = 2; c.strokeRect(mx - 22, my - 8, 44, 16); if (lab) txt(c, lab, mx, my - 13, C.amber, 'center', 11); } else { ln(c, x1, y1, mx, my - 22, C.text, 2); ln(c, mx, my + 22, x2, y2, C.text, 2); c.strokeStyle = C.amber; c.lineWidth = 2; c.strokeRect(mx - 8, my - 22, 16, 44); if (lab) txt(c, lab, mx + 14, my + 4, C.amber, 'left', 11); } };
  const battery = (c, x, y1, y2, lab, up = true) => { const my = (y1 + y2) / 2; ln(c, x, y1, x, my - 6, C.text, 2); ln(c, x, my + 6, x, y2, C.text, 2); const [a, b] = up ? [my - 6, my + 6] : [my + 6, my - 6]; ln(c, x - 14, a, x + 14, a, C.text, 2.5); ln(c, x - 7, b, x + 7, b, C.text, 4); txt(c, '+', x + 18, a + 4, C.rose, 'left', 12); if (lab) txt(c, lab, x - 18, my + 4, C.green, 'right', 11); };

  /* M1, A1 — Kulon qonuni */
  S.coulomb = {
    title: 'Kulon qonuni: ikki nuqtaviy zaryad',
    params: [
      { k: 'q1', l: 'q₁, mkC', min: -5, max: 5, step: .1, v: 2 },
      { k: 'q2', l: 'q₂, mkC', min: -5, max: 5, step: .1, v: -3 },
      { k: 'r', l: 'Masofa r, m', min: .05, max: 1, step: .01, v: .3 },
      { k: 'eps', l: 'Muhit ε', min: 1, max: 81, step: 1, v: 1 }
    ],
    draw(cv, P) {
      const { c, w, h } = ctx2d(cv), q1 = P.q1 * 1e-6, q2 = P.q2 * 1e-6, F = k0 * q1 * q2 / (P.eps * P.r * P.r), W2 = w * .5;
      const sep = 70 + P.r * (W2 - 160), x1 = W2 * .5 - sep / 2, x2 = W2 * .5 + sep / 2, y = h * .45;
      ln(c, x1, y + 34, x2, y + 34, C.axis, 1, [4, 4]); txt(c, `r = ${fx(P.r, 2)} m`, (x1 + x2) / 2, y + 50, C.axis);
      const L = Math.min(90, 18 * Math.max(0, Math.log10(Math.abs(F) * 1e4) + 1)), dir = F > 0 ? -1 : 1;
      if (F !== 0) { arrow(c, x1 - (dir < 0 ? 14 : -14), y, x1 + dir * (L + 14) * (dir < 0 ? 1 : 1), y, C.amber, 2.5); arrow(c, x2 + (dir < 0 ? 14 : -14), y, x2 - dir * (L + 14), y, C.amber, 2.5); }
      charge(c, x1, y, q1, 12 + 2 * Math.abs(P.q1)); charge(c, x2, y, q2, 12 + 2 * Math.abs(P.q2));
      txt(c, `q₁ = ${fx(P.q1, 1)} mkC`, x1, y - 34, C.text); txt(c, `q₂ = ${fx(P.q2, 1)} mkC`, x2, y + 70, C.text);
      txt(c, F > 0 ? 'itarish' : F < 0 ? 'tortishish' : 'ta’sir yo‘q', W2 / 2, 22, C.amber, 'center', 13);
      if (P.eps > 1) { c.fillStyle = '#60a5fa14'; c.fillRect(8, 30, W2 - 16, h - 40); txt(c, `muhit: ε = ${P.eps}`, 14, h - 16, C.blue, 'left', 11); }
      const rs = lin(.05, 1, 200), K = Math.abs(k0 * q1 * q2 / P.eps) || 1e-12;
      plot(c, [W2, 0, w - W2, h], { xr: [.05, 1], yr: [Math.max(K, 1e-9), K / .0025 * 1.2], logy: true, xl: 'r, m', yl: '|F|, N', series: [{ pts: rs.map(r => [r, K / r / r]), c: C.cyan, w: 2.5 }], marks: [{ x: P.r, y: K / P.r / P.r, c: C.amber }] });
      return { '|F|, N': sci(Math.abs(F), 3), 'Turi': F > 0 ? 'itarish' : F < 0 ? 'tortishish' : '—', 'Vakuumdagi kuch, N': sci(Math.abs(F * P.eps), 3), 'q₁ dagi maydon E₂, V/m': sci(Math.abs(k0 * q2 / (P.eps * P.r * P.r)), 3) };
    }
  };

  /* M2, A2, A3 — Maydon kuch chiziqlari, superpozitsiya */
  S.field = {
    title: 'Elektr maydon: kuch chiziqlari va superpozitsiya',
    params: [
      { k: 'cfg', l: 'Konfiguratsiya', type: 'sel', opts: ['Ikki zaryad', 'Uch zaryad (uchburchak)', 'Kvadrat (+, +, −, −)'], v: 'Ikki zaryad' },
      { k: 'k', l: 'q₂/q₁ (ikki zaryad), q₁ = 4 nC', min: -3, max: 3, step: .1, v: -1 },
      { k: 'px', l: 'Sinov nuqtasi x, sm', min: -40, max: 40, step: 1, v: 0 },
      { k: 'py', l: 'Sinov nuqtasi y, sm', min: -30, max: 30, step: 1, v: 20 }
    ],
    draw(cv, P) {
      const { c, w, h } = ctx2d(cv), q0 = 4e-9; let Q;
      if (P.cfg[0] === 'I') Q = [[q0, -.15, 0], [P.k * q0, .15, 0]];
      else if (P.cfg[0] === 'U') Q = [[q0, -.15, -.087], [q0, .15, -.087], [-q0, 0, .173]];
      else Q = [[q0, -.1, -.1], [q0, .1, -.1], [-q0, .1, .1], [-q0, -.1, .1]];
      const E = (x, y) => { let ex = 0, ey = 0; for (const [q, a, b] of Q) { const dx = x - a, dy = y - b, r2 = dx * dx + dy * dy, r3 = r2 * Math.sqrt(r2) + 1e-12; ex += k0 * q * dx / r3; ey += k0 * q * dy / r3; } return [ex, ey]; };
      const sc = Math.min(w / .9, h / .7), cx = w / 2, cy = h / 2, T = (x, y) => [cx + sc * x, cy - sc * y];
      const pos = Q.filter(q => q[0] > 0), seeds = pos.length ? pos : Q, sg = pos.length ? 1 : -1;
      for (const [q, a, b] of seeds) { const n = Math.round(14 * Math.abs(q) / q0); for (let i = 0; i < n; i++) { const t = 2 * Math.PI * (i + .5) / n; let x = a + .012 * Math.cos(t), y = b + .012 * Math.sin(t); const pts = [T(x, y)]; for (let s = 0; s < 700; s++) { const [ex, ey] = E(x, y), m = Math.hypot(ex, ey) || 1; x += sg * .004 * ex / m; y += sg * .004 * ey / m; pts.push(T(x, y)); if (Math.abs(x) > .6 || Math.abs(y) > .45 || Q.some(([qq, aa, bb]) => qq * sg < 0 && Math.hypot(x - aa, y - bb) < .01)) break; } poly(c, pts, '#94a3b8aa', 1.2); } }
      Q.forEach(([q, a, b]) => charge(c, ...T(a, b), q, 11));
      const px = P.px / 100, py = P.py / 100, [ex, ey] = E(px, py), Em = Math.hypot(ex, ey), Pp = T(px, py);
      const L = Math.min(70, 18 + 12 * Math.log10(Em + 1)); if (Em > 0) arrow(c, Pp[0], Pp[1], Pp[0] + L * ex / Em, Pp[1] - L * ey / Em, C.amber, 2.5);
      circ(c, Pp[0], Pp[1], 4, null, '#fff'); txt(c, `E = ${fx(Em, 0)} V/m`, Pp[0] + 8, Pp[1] + 18, C.amber, 'left', 12);
      txt(c, '10 sm', 20 + sc * .05, h - 12, C.axis); ln(c, 20, h - 22, 20 + sc * .1, h - 22, C.axis, 2);
      let phi = 0; for (const [q, a, b] of Q) phi += k0 * q / Math.hypot(px - a, py - b);
      return { 'E, V/m': fx(Em, 1), 'Eₓ, E_y, V/m': `${fx(ex, 0)}; ${fx(ey, 0)}`, 'Yo‘nalish, °': fx(Math.atan2(ey, ex) / deg, 1), 'Potensial φ, V': fx(phi, 1) };
    }
  };

  /* M3, A4 — Gauss teoremasi */
  S.gauss = {
    title: 'Gauss teoremasi: simmetrik maydonlar E(r)',
    params: [
      { k: 'mode', l: 'Zaryad taqsimoti', type: 'sel', opts: ['Bir jinsli shar', 'Sferik qobiq', 'Cheksiz silindr (hajmiy)', 'Cheksiz qatlam (tekislik)'], v: 'Bir jinsli shar' },
      { k: 'Q', l: 'Zaryad Q, nC (silindr: nC/m, qatlam: nC/m²)', min: 1, max: 50, step: 1, v: 10 },
      { k: 'R', l: 'Radius / yarim qalinlik R, sm', min: 2, max: 30, step: 1, v: 10 },
      { k: 'r', l: 'Gauss sirti r, sm', min: 1, max: 50, step: .5, v: 5 }
    ],
    draw(cv, P) {
      const { c, w, h } = ctx2d(cv), Q = P.Q * 1e-9, R = P.R / 100, m = P.mode[0] + P.mode[1];
      const E = r => { if (m === 'Bi') return r < R ? k0 * Q * r / R ** 3 : k0 * Q / r / r; if (m === 'Sf') return r < R ? 0 : k0 * Q / r / r; if (m === 'Ch' && P.mode[9] === 's') return r < R ? Q * r / (2 * Math.PI * e0 * R * R) : Q / (2 * Math.PI * e0 * r); return r < R ? Q * r / (2 * e0 * R) : Q / (2 * e0); };
      const qin = r => { if (m === 'Bi') return Q * Math.min(1, (r / R) ** 3); if (m === 'Sf') return r < R ? 0 : Q; if (P.mode.includes('silindr')) return Q * Math.min(1, (r / R) ** 2); return Q * Math.min(1, r / R); };
      const W2 = w * .45, cx = W2 / 2, cy = h / 2, s = Math.min(W2, h) * .42 / .5, r = P.r / 100, plane = P.mode.includes('qatlam');
      if (plane) { c.fillStyle = '#fb718533'; c.fillRect(cx - s * R, 20, 2 * s * R, h - 40); c.strokeStyle = '#22d3ee'; c.setLineDash([6, 4]); c.strokeRect(cx - s * r, cy - 40, 2 * s * r, 80); c.setLineDash([]); for (const sgn of [-1, 1]) arrow(c, cx + sgn * s * r, cy, cx + sgn * (s * r + 30), cy, C.amber, 2); }
      else { const hol = m === 'Sf'; circ(c, cx, cy, s * R, C.rose, hol ? null : '#fb718533', hol ? 3 : 1.5); circ(c, cx, cy, s * r, null, null); c.strokeStyle = C.cyan; c.setLineDash([6, 4]); c.beginPath(); c.arc(cx, cy, Math.max(s * r, 1), 0, 7); c.stroke(); c.setLineDash([]); if (E(r) > 0) for (let i = 0; i < 8; i++) { const a = i * Math.PI / 4; arrow(c, cx + s * r * Math.cos(a), cy + s * r * Math.sin(a), cx + (s * r + 26) * Math.cos(a), cy + (s * r + 26) * Math.sin(a), C.amber, 1.8); } }
      txt(c, 'Gauss sirti', cx, h - 10, C.cyan, 'center', 11);
      const rs = lin(.001, .5, 300), Em = Math.max(...rs.map(E)) * 1.15;
      plot(c, [W2, 0, w - W2, h], { xr: [0, 50], yr: [0, Em], xl: 'r, sm', yl: 'E(r), V/m', series: [{ pts: rs.map(x => [x * 100, E(x)]), c: C.cyan, w: 2.5 }], vl: [{ x: P.R, l: 'R', c: C.rose }], marks: [{ x: P.r, y: E(r), c: C.amber }] });
      const Sg = plane ? 'yon yoqlar (birlik yuza)' : P.mode.includes('silindr') ? `2πrl (l = 1 m)` : '4πr²';
      return { 'E(r), V/m': fx(E(r), 1), 'Ichki zaryad q_ich': sci(qin(r) * 1e9, 3) + (plane ? ' nC/m²' : P.mode.includes('silindr') ? ' nC/m' : ' nC'), 'Oqim q_ich/ε₀, V·m': sci(qin(r) / e0, 3), 'Gauss sirti': Sg };
    }
  };

  /* M4, A5, A6 — Potensial va ekvipotensial chiziqlar */
  S.potential = {
    title: 'Potensial: ekvipotensial chiziqlar va φ(x)',
    params: [
      { k: 'cfg', l: 'Zaryadlar', type: 'sel', opts: ['Dipol (+q, −q)', 'Ikki musbat zaryad', '+2q va −q'], v: 'Dipol (+q, −q)' },
      { k: 'q', l: 'q, nC', min: 1, max: 10, step: .5, v: 4 },
      { k: 'd', l: 'Zaryadlar orasidagi masofa d, sm', min: 10, max: 40, step: 1, v: 30 }
    ],
    draw(cv, P) {
      const { c, w, h } = ctx2d(cv), q = P.q * 1e-9, d = P.d / 100;
      const Q = P.cfg[0] === 'D' ? [[q, -d / 2], [-q, d / 2]] : P.cfg[0] === 'I' ? [[q, -d / 2], [q, d / 2]] : [[2 * q, -d / 2], [-q, d / 2]];
      const phi = (x, y) => Q.reduce((s, [qq, a]) => s + k0 * qq / Math.max(Math.hypot(x - a, y), .004), 0);
      const W2 = w * .55, sc = Math.min(W2 / .7, h / .55), cx = W2 / 2, cy = h / 2, cs = 4, pm = k0 * q / .03;
      for (let X = 0; X < W2; X += cs) for (let Y = 0; Y < h; Y += cs) { const v = phi((X + cs / 2 - cx) / sc, (cy - Y - cs / 2) / sc), t = Math.max(-1, Math.min(1, v / pm)); c.fillStyle = t > 0 ? `rgba(251,113,133,${(.08 + .7 * Math.sqrt(t)).toFixed(3)})` : `rgba(96,165,250,${(.08 + .7 * Math.sqrt(-t)).toFixed(3)})`; c.fillRect(X, Y, cs, cs); }
      const levels = [-.6, -.3, -.15, -.07, 0, .07, .15, .3, .6].map(x => x * pm), g = 3;
      c.fillStyle = '#e2e8f0';
      for (let X = 0; X < W2 - g; X += 2) for (let Y = 0; Y < h - g; Y += 2) { const a = phi((X - cx) / sc, (cy - Y) / sc), b = phi((X + g - cx) / sc, (cy - Y) / sc), e = phi((X - cx) / sc, (cy - Y - g) / sc); for (const L of levels) if ((a - L) * (b - L) < 0 || (a - L) * (e - L) < 0) { c.fillRect(X, Y, 1.4, 1.4); break; } }
      Q.forEach(([qq, a]) => charge(c, cx + sc * a, cy, qq, 10));
      txt(c, 'oq chiziqlar — ekvipotensial', 10, h - 10, '#e2e8f0', 'left', 11);
      const xs = lin(-.35, .35, 500), ph = xs.map(x => [x * 100, phi(x, 0)]), Ex = xs.map(x => [x * 100, -(phi(x + 1e-4, 0) - phi(x - 1e-4, 0)) / 2e-4 / 1000]);
      const lim = pm * 1.1;
      plot(c, [W2, 0, w - W2, h / 2], { xr: [-35, 35], yr: [-lim, lim], xl: '', yl: 'φ(x, 0), V', series: [{ pts: ph, c: C.violet, w: 2 }] });
      const el = k0 * q / .01 / 1000;
      plot(c, [W2, h / 2, w - W2, h / 2], { xr: [-35, 35], yr: [-el, el], xl: 'x, sm', yl: 'Eₓ, kV/m', series: [{ pts: Ex, c: C.amber, w: 2 }] });
      const p0 = phi(0, 0), E0 = -(phi(1e-5, 0) - phi(-1e-5, 0)) / 2e-5;
      return { 'φ (o‘rtada), V': fx(p0, 1), 'Eₓ (o‘rtada), V/m': fx(E0, 0), 'q ning 1 sm dagi potensiali, V': fx(k0 * q / .01, 0), 'Elektron 100 V da tezligi, m/s': sci(Math.sqrt(2 * qe * 100 / me), 3) };
    }
  };

  /* M5 — Dielektrik */
  S.dielectric = {
    title: 'Dielektrik: qutblanish va chegarada sinish',
    params: [
      { k: 'eps', l: 'Dielektrik singdiruvchanlik ε', min: 1, max: 10, step: .1, v: 4 },
      { k: 's', l: 'Erkin zaryad σ, mkC/m²', min: .1, max: 5, step: .1, v: 1 },
      { k: 'a', l: 'Tushish burchagi α₁ (normalga), °', min: 0, max: 85, step: 1, v: 45 }
    ],
    draw(cv, P) {
      const { c, w, h } = ctx2d(cv), s = P.s * 1e-6, E0 = s / e0, E = E0 / P.eps, Pp = s * (1 - 1 / P.eps);
      const W2 = w * .52, x1 = 40, x2 = W2 - 40, top = 30, bot = h - 30, dl = x1 + (x2 - x1) * .3, dr = x1 + (x2 - x1) * .7;
      c.fillStyle = '#a78bfa22'; c.fillRect(dl, top, dr - dl, bot - top); txt(c, `ε = ${fx(P.eps, 1)}`, (dl + dr) / 2, top + 16, C.violet);
      ln(c, x1, top, x1, bot, C.rose, 5); ln(c, x2, top, x2, bot, C.blue, 5);
      for (let i = 0; i < 7; i++) { const y = top + (i + .5) * (bot - top) / 7; txt(c, '+', x1 - 12, y + 4, C.rose, 'center', 13); txt(c, '−', x2 + 12, y + 4, C.blue, 'center', 13); }
      const nB = Math.round(7 * (1 - 1 / P.eps));
      for (let i = 0; i < nB; i++) { const y = top + (i + .5) * (bot - top) / Math.max(nB, 1); txt(c, '−', dl + 7, y + 4, '#93c5fd', 'center', 11); txt(c, '+', dr - 7, y + 4, '#fda4af', 'center', 11); }
      const nE0 = 8, nE = Math.max(1, Math.round(8 / P.eps));
      for (let i = 0; i < nE0; i++) { const y = top + 20 + (i + .5) * (bot - top - 40) / nE0; arrow(c, x1 + 8, y, dl - 6, y, C.amber, 1.6); arrow(c, dr + 6, y, x2 - 8, y, C.amber, 1.6); }
      for (let i = 0; i < nE; i++) { const y = top + 20 + (i + .5) * (bot - top - 40) / nE; arrow(c, dl + 14, y, dr - 14, y, C.amber, 1.6); }
      txt(c, 'bog‘langan zaryadlar σ′ (och rangda)', W2 / 2, bot + 18, C.text, 'center', 11);
      const X0 = W2 + 10, Wb = w - X0 - 10, by = h / 2, bx = X0 + Wb / 2;
      c.fillStyle = '#a78bfa22'; c.fillRect(X0, by, Wb, h / 2 - 10); ln(c, X0, by, X0 + Wb, by, C.violet, 2); ln(c, bx, 20, bx, h - 20, '#475569', 1, [4, 4]);
      txt(c, 'ε₁ = 1 (havo)', X0 + 6, by - 8, C.text, 'left', 11); txt(c, `ε₂ = ${fx(P.eps, 1)}`, X0 + 6, by + 18, C.violet, 'left', 11);
      const a1 = P.a * deg, a2 = Math.atan(Math.tan(a1) * P.eps), L = Math.min(h / 2 - 30, Wb / 2 - 10);
      arrow(c, bx - L * Math.sin(a1), by - L * Math.cos(a1), bx, by, C.amber, 2.2); arrow(c, bx, by, bx + L * Math.sin(a2), by + L * Math.cos(a2), C.amber, 2.2);
      txt(c, `α₁ = ${fx(P.a, 0)}°`, bx - 8, by - L * .55, C.amber, 'right', 11); txt(c, `α₂ = ${fx(a2 / deg, 1)}°`, bx + 8, by + L * .55, C.amber, 'left', 11);
      return { 'D = σ, mkC/m²': fx(P.s, 2), 'E₀ (havoda), kV/m': fx(E0 / 1e3, 2), 'E (dielektrikda), kV/m': fx(E / 1e3, 2), 'P = σ′, mkC/m²': fx(Pp * 1e6, 3), 'χ = ε − 1': fx(P.eps - 1, 2), 'α₂ (tgα₂ = ε·tgα₁), °': fx(a2 / deg, 2) };
    }
  };

  /* M6, A7 — Yassi kondensator */
  S.capacitor = {
    title: 'Yassi kondensator: sig‘im, zaryad, energiya',
    params: [
      { k: 'S', l: 'Qoplama yuzasi S, sm²', min: 10, max: 500, step: 10, v: 100 },
      { k: 'd', l: 'Oraliq d, mm', min: .1, max: 10, step: .1, v: 1 },
      { k: 'eps', l: 'Dielektrik ε', min: 1, max: 10, step: .1, v: 1 },
      { k: 'U', l: 'Kuchlanish U, V', min: 10, max: 1000, step: 10, v: 100 }
    ],
    draw(cv, P) {
      const { c, w, h } = ctx2d(cv), S0 = P.S * 1e-4, d = P.d * 1e-3, C0 = e0 * P.eps * S0 / d, q = C0 * P.U, E = P.U / d, W = C0 * P.U * P.U / 2, wd = e0 * P.eps * E * E / 2;
      const W2 = w * .5, cx = W2 / 2, cy = h / 2, ph = Math.min(h - 60, 40 + Math.sqrt(P.S) * 9), gap = 14 + P.d * 18;
      if (P.eps > 1) { c.fillStyle = '#a78bfa33'; c.fillRect(cx - gap / 2, cy - ph / 2, gap, ph); }
      ln(c, cx - gap / 2, cy - ph / 2, cx - gap / 2, cy + ph / 2, C.rose, 5); ln(c, cx + gap / 2, cy - ph / 2, cx + gap / 2, cy + ph / 2, C.blue, 5);
      const nl = Math.max(2, Math.min(14, Math.round(Math.log10(Math.abs(q) * 1e12 + 1) * 3)));
      for (let i = 0; i < nl; i++) { const y = cy - ph / 2 + (i + .5) * ph / nl; if (gap > 18) arrow(c, cx - gap / 2 + 4, y, cx + gap / 2 - 4, y, C.amber, 1.2); txt(c, '+', cx - gap / 2 - 10, y + 4, C.rose, 'center', 11); txt(c, '−', cx + gap / 2 + 10, y + 4, C.blue, 'center', 11); }
      ln(c, cx - gap / 2, cy - ph / 2, cx - gap / 2, 14, C.text, 1.5); ln(c, cx + gap / 2, cy - ph / 2, cx + gap / 2, 14, C.text, 1.5); ln(c, cx - gap / 2, 14, cx - 8, 14, C.text, 1.5); ln(c, cx + gap / 2, 14, cx + 8, 14, C.text, 1.5);
      txt(c, `U = ${P.U} V`, cx, h - 12, C.green, 'center', 12);
      const items = [['C, pF', C0 * 1e12], ['q, nC', q * 1e9], ['W, mkJ', W * 1e6], ['w, mJ/m³', wd * 1e3]], x0 = W2 + 20, bw = w - x0 - 20;
      txt(c, 'Kattaliklar (log masshtab)', x0, 18, C.text, 'left', 12);
      items.forEach(([n, v], i) => { const y = 34 + i * (h - 50) / 4, L = Math.max(4, (Math.log10(Math.max(v, 1e-3)) + 3) / 9 * (bw - 120)); c.fillStyle = [C.cyan, C.rose, C.amber, C.violet][i] + '88'; c.fillRect(x0 + 80, y, L, 20); txt(c, n, x0 + 74, y + 15, C.text, 'right', 12); txt(c, sci(v, 3), x0 + 86 + L, y + 15, C.text, 'left', 11); });
      return { 'C = ε₀εS/d, pF': fx(C0 * 1e12, 2), 'q = CU, nC': fx(q * 1e9, 3), 'E = U/d, kV/m': fx(E / 1e3, 1), 'W = CU²/2, mkJ': fx(W * 1e6, 3), 'w = ε₀εE²/2, J/m³': sci(wd, 3), 'Qoplamalar tortishishi F, N': sci(q * q / (2 * e0 * P.eps * S0), 3) };
    }
  };

  /* M7, A9–A11 — To‘la zanjir uchun Om qonuni */
  S.ohm = {
    title: 'To‘la zanjir: tok, kuchlanish, quvvat va FIK',
    params: [
      { k: 'E', l: 'EYuK ℰ, V', min: 1, max: 24, step: .5, v: 12 },
      { k: 'r', l: 'Ichki qarshilik r, Ω', min: .1, max: 5, step: .1, v: .5 },
      { k: 'R', l: 'Yuklama R, Ω', min: .1, max: 20, step: .1, v: 5.5 }
    ],
    draw(cv, P) {
      const { c, w, h } = ctx2d(cv), I = P.E / (P.R + P.r), U = P.E - I * P.r, Pu = I * I * P.R, eta = P.R / (P.R + P.r);
      const W2 = w * .44, x1 = 40, x2 = W2 - 30, y1 = 50, y2 = h - 50;
      battery(c, x1, y1, y2, `ℰ = ${P.E} V`); ln(c, x1, y1, x2, y1, C.text, 2); resistor(c, x2, y1, x2, y2, `R = ${P.R} Ω`); ln(c, x1, y2, (x1 + x2) / 2 - 40, y2, C.text, 2); resistor(c, (x1 + x2) / 2 - 40, y2, x2, y2, `r = ${P.r} Ω`);
      arrow(c, (x1 + x2) / 2 - 20, y1, (x1 + x2) / 2 + 20, y1, C.cyan, 2.5); txt(c, `I = ${fx(I, 2)} A`, (x1 + x2) / 2, y1 - 10, C.cyan, 'center', 12);
      txt(c, `U = ${fx(U, 2)} V`, x2 - 14, (y1 + y2) / 2 + 40, C.green, 'right', 12);
      const Rs = lin(.05, 20, 400), Pm = P.E * P.E / (4 * P.r);
      plot(c, [W2, 0, w - W2, h], { xr: [0, 20], yr: [0, Pm * 1.2], xl: 'R, Ω', yl: 'P_foyd, W (havorang) · FIK (sariq, o‘ng masshtab ×P_max)', series: [{ pts: Rs.map(R => [R, P.E * P.E * R / (R + P.r) ** 2]), c: C.cyan, w: 2.5 }, { pts: Rs.map(R => [R, R / (R + P.r) * Pm]), c: C.amber, w: 1.6, dash: [5, 4] }], vl: [{ x: P.r, l: 'R = r', c: C.green }], marks: [{ x: P.R, y: Pu, c: '#fff' }] });
      return { 'Tok I, A': fx(I, 3), 'Klemma kuchlanishi U, V': fx(U, 3), 'Foydali quvvat, W': fx(Pu, 2), 'To‘liq quvvat ℰI, W': fx(P.E * I, 2), 'FIK': fx(eta * 100, 1) + ' %', 'P_max (R = r), W': fx(Pm, 2), 'Qisqa tutashuv toki, A': fx(P.E / P.r, 1) };
    }
  };

  /* M8, A12 — Kirxgof qoidalari */
  S.kirchhoff = {
    title: 'Kirxgof qoidalari: ikki manbali zanjir',
    params: [
      { k: 'E1', l: 'ℰ₁, V', min: 0, max: 24, step: .5, v: 12 },
      { k: 'E2', l: 'ℰ₂, V', min: 0, max: 24, step: .5, v: 6 },
      { k: 'R1', l: 'R₁, Ω', min: .5, max: 20, step: .5, v: 2 },
      { k: 'R2', l: 'R₂, Ω', min: .5, max: 20, step: .5, v: 4 },
      { k: 'R3', l: 'R₃, Ω', min: .5, max: 20, step: .5, v: 6 }
    ],
    draw(cv, P) {
      const { c, w, h } = ctx2d(cv), D = P.R1 * P.R2 + P.R1 * P.R3 + P.R2 * P.R3;
      const I1 = (P.E1 * (P.R2 + P.R3) - P.E2 * P.R3) / D, I2 = (P.E2 * (P.R1 + P.R3) - P.E1 * P.R3) / D, I3 = I1 + I2;
      const W2 = w * .6, xa = 80, xb = W2 / 2 + 10, xc = W2 - 120, y1 = 40, y2 = h - 40;
      ln(c, xa, y1, xc, y1, C.text, 2); ln(c, xa, y2, xc, y2, C.text, 2);
      battery(c, xa, y1 + (y2 - y1) * .55, y2, `ℰ₁=${P.E1}`); resistor(c, xa, y1, xa, y1 + (y2 - y1) * .55, ''); txt(c, `R₁=${P.R1}`, xa + 14, y1 + (y2 - y1) * .28, C.amber, 'left', 11);
      battery(c, xc, y1 + (y2 - y1) * .55, y2, ''); txt(c, `ℰ₂=${P.E2}`, xc + 18, y1 + (y2 - y1) * .78, C.green, 'left', 11); resistor(c, xc, y1, xc, y1 + (y2 - y1) * .55, ''); txt(c, `R₂=${P.R2}`, xc - 14, y1 + (y2 - y1) * .28, C.amber, 'right', 11);
      resistor(c, xb, y1, xb, y2, `R₃=${P.R3}`); circ(c, xb, y1, 4, null, '#fff'); circ(c, xb, y2, 4, null, '#fff');
      const cur = (x, y, up, I, n, left) => { const col = I >= 0 ? C.cyan : C.rose, d = (I >= 0) === up ? -1 : 1; arrow(c, x - 18, y + 14 * d, x - 18, y - 14 * d, col, 2.2); txt(c, `${n} = ${fx(I, 3)} A`, left ? x - 10 : x - 24, y + 4, col, left ? 'left' : 'right', 12); };
      cur(xa + 60, (y1 + y2) / 2, true, I1, 'I₁'); cur(xb + 70, (y1 + y2) / 2 + 40, false, I3, 'I₃'); cur(xc + 30, (y1 + y2) / 2 - 10, true, I2, 'I₂', true);
      const Pin = P.E1 * I1 + P.E2 * I2, Pout = I1 * I1 * P.R1 + I2 * I2 * P.R2 + I3 * I3 * P.R3;
      const items = [['ℰ₁I₁', P.E1 * I1], ['ℰ₂I₂', P.E2 * I2], ['I₁²R₁', I1 * I1 * P.R1], ['I₂²R₂', I2 * I2 * P.R2], ['I₃²R₃', I3 * I3 * P.R3]], mx = Math.max(...items.map(x => Math.abs(x[1])), 1), x0 = W2 + 60, bw = w - x0 - 60;
      txt(c, 'Quvvat balansi, W', x0 - 50, 20, C.text, 'left', 12);
      items.forEach(([n, v], i) => { const y = 36 + i * (h - 60) / 5, L = Math.abs(v) / mx * bw, neg = v < 0; c.fillStyle = (i < 2 ? (neg ? C.rose : C.green) : C.amber) + '99'; c.fillRect(x0, y, L, 18); txt(c, n, x0 - 6, y + 14, C.text, 'right', 12); txt(c, fx(v, 2), x0 + L + 6, y + 14, C.text, 'left', 11); });
      return { 'I₁, A': fx(I1, 4), 'I₂, A': fx(I2, 4), 'I₃ = I₁ + I₂, A': fx(I3, 4), 'Manbalar quvvati, W': fx(Pin, 3), 'Rezistorlardagi issiqlik, W': fx(Pout, 3), 'Izoh': I2 < 0 ? 'ℰ₂ zaryadlanmoqda' : I1 < 0 ? 'ℰ₁ zaryadlanmoqda' : 'ikkala manba energiya beradi' };
    }
  };

  /* M9, A13, A14 — Bio–Savar–Laplas */
  S.biot = {
    title: 'Bio–Savar–Laplas: tok magnit maydoni',
    params: [
      { k: 'mode', l: 'O‘tkazgich', type: 'sel', opts: ['To‘g‘ri tok', 'Doiraviy o‘ram (o‘q bo‘yicha)', 'Solenoid (o‘q bo‘yicha)'], v: 'To‘g‘ri tok' },
      { k: 'I', l: 'Tok I, A', min: .5, max: 20, step: .5, v: 10 },
      { k: 'R', l: 'O‘ram radiusi R, sm', min: 1, max: 20, step: .5, v: 10 },
      { k: 'N', l: 'Solenoid: o‘ramlar N / uzunlik l = 50 sm', min: 10, max: 2000, step: 10, v: 500 },
      { k: 'x', l: 'Nuqta: masofa r yoki x, sm', min: .5, max: 40, step: .5, v: 5 }
    ],
    draw(cv, P) {
      const { c, w, h } = ctx2d(cv), I = P.I, R = P.R / 100, x = P.x / 100, l = .5, m = P.mode[0];
      const B = m === 'T' ? (r => mu0 * I / (2 * Math.PI * r)) : m === 'D' ? (z => mu0 * I * R * R / (2 * (R * R + z * z) ** 1.5)) : (z => mu0 * P.N / l * I / 2 * ((z + l / 2) / Math.hypot(z + l / 2, R) - (z - l / 2) / Math.hypot(z - l / 2, R)));
      const W2 = w * .45, cx = W2 / 2, cy = h / 2;
      if (m === 'T') { [1, 2, 3, 4].forEach(k => { circ(c, cx, cy, k * 22, '#a78bfa88', null, 1.2); arrow(c, cx + k * 22, cy + 2, cx + k * 22, cy - 6, C.violet, 1.5); }); circ(c, cx, cy, 9, '#fff', C.amber); txt(c, '⊙', cx, cy + 5, '#000', 'center', 14); txt(c, 'tok bizga qarab', cx, h - 12, C.amber, 'center', 11); const px = cx + Math.min(x * 900, W2 / 2 - 10); circ(c, px, cy, 4, null, '#fff'); arrow(c, px, cy, px, cy - 30, C.cyan, 2.2); }
      else { const s = Math.min(W2, h) * .35 / Math.max(R, .05), rr = s * R; ln(c, 14, cy, W2 - 14, cy, '#475569', 1, [5, 4]);
        if (m === 'D') { c.strokeStyle = C.amber; c.lineWidth = 3; c.beginPath(); c.ellipse(cx - 40, cy, 10, rr, 0, 0, 7); c.stroke(); }
        else { const n = 14; for (let i = 0; i < n; i++) { c.strokeStyle = C.amber; c.lineWidth = 2; c.beginPath(); c.ellipse(cx - 70 + i * 140 / (n - 1), cy, 6, rr, 0, 0, 7); c.stroke(); } }
        const px = Math.min(W2 - 20, (m === 'D' ? cx - 40 : cx) + x * 600); circ(c, px, cy, 4, null, '#fff'); arrow(c, px, cy, px + 30, cy, C.cyan, 2.2); txt(c, 'o‘q', W2 - 20, cy - 8, '#475569', 'right', 11); }
      const xs = m === 'T' ? lin(.005, .4, 300) : lin(-.4, .4, 400), ys = xs.map(B), mx = Math.max(...ys) * 1.15;
      plot(c, [W2, 0, w - W2, h], { xr: [m === 'T' ? 0 : -40, 40], yr: [0, mx * 1e6], xl: m === 'T' ? 'r, sm' : 'x, sm', yl: 'B, mkT', series: [{ pts: xs.map((z, i) => [z * 100, ys[i] * 1e6]), c: C.cyan, w: 2.5 }], marks: [{ x: P.x, y: B(x) * 1e6, c: C.amber }], hl: m === 'S' ? [{ y: mu0 * P.N / l * I * 1e6, l: 'μ₀nI', c: '#64748b' }] : [] });
      const r = { 'B (nuqtada), mkT': fx(B(x) * 1e6, 2), 'Yer maydoniga nisbat (50 mkT)': fx(B(x) / 5e-5, 2) };
      if (m === 'D') r['B markazda = μ₀I/2R, mkT'] = fx(mu0 * I / (2 * R) * 1e6, 2);
      if (m === 'S') { r['μ₀nI, mkT'] = fx(mu0 * P.N / l * I * 1e6, 1); r['B markazda, mkT'] = fx(B(0) * 1e6, 1); r['B uchida, mkT'] = fx(B(l / 2) * 1e6, 1); }
      return r;
    }
  };

  /* M10, A15 — Ikki parallel tok, sirkulyatsiya, Amper kuchi */
  S.ampere = {
    title: 'Parallel toklar: maydon, sirkulyatsiya va Amper kuchi',
    params: [
      { k: 'I1', l: 'I₁, A (+ bizga qarab)', min: -20, max: 20, step: 1, v: 20 },
      { k: 'I2', l: 'I₂, A', min: -20, max: 20, step: 1, v: 20 },
      { k: 'd', l: 'Simlar orasi d, sm', min: 2, max: 30, step: 1, v: 10 }
    ],
    draw(cv, P) {
      const { c, w, h } = ctx2d(cv), d = P.d / 100, W2 = w * .52, sc = Math.min(W2 / .5, h / .36), cx = W2 / 2, cy = h / 2;
      const W = [[P.I1, -d / 2], [P.I2, d / 2]];
      const B = (x, y) => { let bx = 0, by = 0; for (const [I, a] of W) { const dx = x - a, r2 = dx * dx + y * y + 1e-8; bx += -mu0 * I * y / (2 * Math.PI * r2); by += mu0 * I * dx / (2 * Math.PI * r2); } return [bx, by]; };
      for (let X = 18; X < W2; X += 26) for (let Y = 16; Y < h; Y += 26) { const x = (X - cx) / sc, y = (cy - Y) / sc; if (W.some(([I, a]) => Math.hypot(x - a, y) < .012)) continue; const [bx, by] = B(x, y), m = Math.hypot(bx, by); if (m < 1e-9) continue; const L = Math.min(11, 3 + 2.2 * Math.log10(m * 1e6 + 1)); arrow(c, X - L * bx / m, Y + L * by / m, X + L * bx / m, Y - L * by / m, '#a78bfacc', 1.2); }
      c.strokeStyle = C.cyan; c.setLineDash([5, 4]); c.beginPath(); c.arc(cx - sc * d / 2, cy, sc * d * .35, 0, 7); c.stroke(); c.setLineDash([]);
      const F = mu0 * P.I1 * P.I2 / (2 * Math.PI * d);
      W.forEach(([I, a], i) => { const X = cx + sc * a; circ(c, X, cy, 11, '#fff', I === 0 ? C.axis : C.amber); txt(c, I > 0 ? '•' : I < 0 ? '×' : '', X, cy + 5, '#000', 'center', 16); txt(c, `I${i ? '₂' : '₁'}=${I} A`, X, cy - 18, C.amber, 'center', 11); if (F !== 0 && I !== 0) { const dir = (F > 0 ? 1 : -1) * (i ? -1 : 1); arrow(c, X + dir * 14, cy + 26, X + dir * 50, cy + 26, C.green, 2.5); } });
      txt(c, 'yashil — Amper kuchi; uzuq aylana — sirkulyatsiya konturi', 8, h - 8, C.text, 'left', 10);
      const xs = lin(-.25, .25, 500);
      plot(c, [W2, 0, w - W2, h], { xr: [-25, 25], yr: [-400, 400], xl: 'x, sm (simlar chizig‘ida)', yl: 'B_y, mkT', series: [{ pts: xs.map(x => [x * 100, Math.max(-1e3, Math.min(1e3, B(x, 0)[1] * 1e6))]), c: C.cyan, w: 2.2 }], vl: [{ x: -P.d / 2, c: C.amber }, { x: P.d / 2, c: C.amber }] });
      return { 'B (o‘rtada), mkT': fx(Math.hypot(...B(0, 0)) * 1e6, 2), 'F/l = μ₀I₁I₂/2πd, mN/m': fx(Math.abs(F) * 1e3, 3), 'O‘zaro ta’sir': F > 0 ? 'tortishish' : F < 0 ? 'itarish' : '—', '∮B·dl (I₁ atrofida), μT·m': fx(mu0 * P.I1 * 1e6, 3) + ' = μ₀I₁' };
    }
  };

  /* M11, A16, A17 — Lorens kuchi */
  S.lorentzf = {
    title: 'Lorens kuchi: zarra E va B maydonlarda (B ∥ z)',
    params: [
      { k: 'p', l: 'Zarra', type: 'sel', opts: ['Proton', 'Elektron', 'Alfa-zarra'], v: 'Proton' },
      { k: 'v', l: 'Tezlik v, 10⁵ m/s (elektron: 10⁷)', min: .5, max: 50, step: .5, v: 10 },
      { k: 'B', l: 'Induksiya B, mT', min: 1, max: 500, step: 1, v: 100 },
      { k: 'E', l: 'Elektr maydon E (y bo‘ylab), kV/m', min: -50, max: 50, step: 1, v: 0 },
      { k: 'a', l: 'Tezlik va B orasidagi burchak, °', min: 10, max: 90, step: 1, v: 90 }
    ],
    draw(cv, P) {
      const { c, w, h } = ctx2d(cv), par = { P: [qe, mp], E: [-qe, me], A: [2 * qe, 4 * mp] }[P.p[0]], q = par[0], m = par[1];
      const v = P.v * (P.p[0] === 'E' ? 1e7 : 1e5), B = P.B * 1e-3, E = P.E * 1e3, al = P.a * deg, T = 2 * Math.PI * m / (Math.abs(q) * B), rL = m * v * Math.sin(al) / (Math.abs(q) * B);
      let pos = [0, 0, 0], vel = [v * Math.sin(al), 0, v * Math.cos(al)]; const dt = T / 300, pts = [];
      for (let i = 0; i < 900; i++) { const t = q * B / m * dt / 2, a = q * E / m * dt / 2; const vm = [vel[0], vel[1] + a, vel[2]]; const vp = [vm[0] + vm[1] * t, vm[1] - vm[0] * t, vm[2]], s = 2 * t / (1 + t * t); const vn = [vm[0] + vp[1] * s, vm[1] - vp[0] * s, vm[2]]; vel = [vn[0], vn[1] + a, vn[2]]; pos = [pos[0] + vel[0] * dt, pos[1] + vel[1] * dt, pos[2] + vel[2] * dt]; pts.push(pos.slice()); }
      const ext = Math.max(1e-9, ...pts.map(p => Math.max(Math.abs(p[0]), Math.abs(p[1])))) * 1.15;
      const W2 = w * .5;
      plot(c, [0, 0, W2, h], { xr: [-ext * 100, ext * 100], yr: [-ext * 100, ext * 100], xl: 'x, sm', yl: 'y, sm (B ekrandan bizga)', series: [{ pts: pts.map(p => [p[0] * 100, p[1] * 100]), c: C.cyan, w: 2 }], marks: [{ x: 0, y: 0, c: C.amber, r: 4 }] });
      const zmax = Math.max(1e-9, ...pts.map(p => Math.abs(p[2])));
      if (zmax < ext * .05) { txt(c, 'v ⊥ B: B bo‘ylab siljish yo‘q (tekis aylana)', W2 + (w - W2) / 2, h / 2, C.text, 'center', 12); } else plot(c, [W2, 0, w - W2, h], { xr: [0, zmax * 100], yr: [-ext * 100, ext * 100], xl: 'z, sm (B bo‘ylab)', yl: 'x, sm — yondan ko‘rinish (vint chiziq)', series: [{ pts: pts.map(p => [p[2] * 100, p[0] * 100]), c: C.violet, w: 2 }] });
      const vd = E / B;
      return { 'Larmor radiusi r, sm': fx(rL * 100, 3), 'Davr T': sci(T, 3) + ' s', 'Chastota f, MGs': fx(1 / T / 1e6, 3), 'Vint qadami h, sm': fx(v * Math.cos(al) * T * 100, 3), 'Dreyf tezligi E/B, m/s': sci(Math.abs(vd), 3), 'Tezlik filtri': Math.abs(Math.abs(vd) - v) / v < .03 && P.a === 90 ? 'v ≈ E/B — og‘ish yo‘q' : '—' };
    }
  };

  /* M12 — Magnit gisterezisi */
  S.hyster = {
    title: 'Magnetiklar: gisterezis sirtmog‘i va domenlar',
    anim: true,
    params: [
      { k: 'mode', l: 'Modda', type: 'sel', opts: ['Ferromagnetik', 'Paramagnetik', 'Diamagnetik'], v: 'Ferromagnetik' },
      { k: 'Hm', l: 'H amplitudasi, A/m', min: 50, max: 3000, step: 50, v: 1000 },
      { k: 'Hc', l: 'Koersitiv kuch H_c, A/m', min: 10, max: 800, step: 10, v: 150 },
      { k: 'Ms', l: 'To‘yinish M_s, MA/m', min: .3, max: 2, step: .1, v: 1.2 }
    ],
    draw(cv, P, dt) {
      const { c, w, h } = ctx2d(cv), t = tick(cv, dt), Ht = P.Hm * Math.sin(t * 1.6), up = Math.cos(t * 1.6) > 0, Ms = P.Ms * 1e6, a = P.Hc / 1.2 + 1;
      const fer = P.mode[0] === 'F', chi = P.mode[0] === 'P' ? 2e-3 : -1e-5;
      const Mf = (H, branch) => Ms * Math.tanh((H - branch * P.Hc) / a);
      const M = H => (fer ? Mf(H, up ? 1 : -1) : chi * H);
      const W2 = w * .4, n = 6, cs = Math.min(W2 - 20, h - 40) / n, ox = (W2 - cs * n) / 2, oy = (h - cs * n) / 2;
      const frac = fer ? M(Ht) / Ms : Math.max(-1, Math.min(1, chi * Ht / (Math.abs(chi) * P.Hm)));
      let seed = 7; const rnd = () => (seed = (seed * 9301 + 49297) % 233280) / 233280;
      for (let i = 0; i < n; i++) for (let j = 0; j < n; j++) { const x = ox + i * cs + cs / 2, y = oy + j * cs + cs / 2, r = rnd(), th = r < (1 + frac) / 2 ? 0 : Math.PI, rot = fer ? th : (rnd() - .5) * 2 * Math.PI * (1 - Math.abs(frac)) + th; c.strokeStyle = '#334155'; c.strokeRect(x - cs / 2, y - cs / 2, cs, cs); arrow(c, x - cs * .32 * Math.cos(rot), y + cs * .32 * Math.sin(rot), x + cs * .32 * Math.cos(rot), y - cs * .32 * Math.sin(rot), Math.cos(rot) > 0 ? C.rose : C.blue, 2); }
      txt(c, fer ? 'domenlar' : 'atom magnit momentlari', W2 / 2, h - 8, C.text, 'center', 11); arrow(c, W2 / 2 - 30, 14, W2 / 2 - 30 + 60 * Ht / P.Hm, 14, C.amber, 2); txt(c, 'H', W2 / 2 + 40, 18, C.amber, 'left', 12);
      const Hs = lin(-P.Hm, P.Hm, 300);
      if (fer) { const Bm = mu0 * (P.Hm + Ms) * 1.1; plot(c, [W2, 0, w - W2, h], { xr: [-P.Hm, P.Hm], yr: [-Bm, Bm], xl: 'H, A/m', yl: 'B, T', series: [{ pts: Hs.map(H => [H, mu0 * (H + Mf(H, 1))]), c: C.cyan, w: 2.3 }, { pts: Hs.map(H => [H, mu0 * (H + Mf(H, -1))]), c: C.cyan, w: 2.3 }], marks: [{ x: Ht, y: mu0 * (Ht + M(Ht)), c: C.amber }] }); }
      else { const Mm = Math.abs(chi) * P.Hm * 1.2; plot(c, [W2, 0, w - W2, h], { xr: [-P.Hm, P.Hm], yr: [-Mm, Mm], xl: 'H, A/m', yl: 'M, A/m', series: [{ pts: Hs.map(H => [H, chi * H]), c: C.cyan, w: 2.3 }], marks: [{ x: Ht, y: chi * Ht, c: C.amber }] }); }
      let area = 0; if (fer) { for (let i = 0; i < Hs.length - 1; i++) { const dH = Hs[i + 1] - Hs[i]; area += (Mf(Hs[i], -1) - Mf(Hs[i], 1)) * mu0 * dH; } }
      return fer ? { 'Qoldiq induksiya B_r, T': fx(mu0 * Mf(0, -1), 3), 'Koersitiv kuch H_c, A/m': fx(P.Hc, 0), 'To‘yinish B_s ≈ μ₀M_s, T': fx(mu0 * Ms, 3), 'Isrof (sirtmoq yuzasi), J/m³ sikl': fx(Math.abs(area), 1), 'H(t), A/m': fx(Ht, 0) } : { 'χ': chi.toExponential(1), 'μ = 1 + χ': fx(1 + chi, 5), 'Turi': P.mode, 'M(H), A/m': fx(chi * Ht, 3) };
    }
  };

  /* M13, A18 — RL zanjir */
  S.rl = {
    title: 'O‘zinduksiya: RL zanjirda tokning qaror topishi va yo‘qolishi',
    params: [
      { k: 'mode', l: 'Jarayon', type: 'sel', opts: ['Ulash', 'Uzish (R orqali)'], v: 'Ulash' },
      { k: 'E', l: 'EYuK ℰ, V', min: 1, max: 24, step: .5, v: 10 },
      { k: 'R', l: 'Qarshilik R, Ω', min: 1, max: 50, step: .5, v: 10 },
      { k: 'L', l: 'Induktivlik L, H', min: .05, max: 2, step: .05, v: .5 }
    ],
    draw(cv, P) {
      const { c, w, h } = ctx2d(cv), tau = P.L / P.R, I0 = P.E / P.R, on = P.mode[0] === 'U' && P.mode[1] === 'l', tm = 5 * tau;
      const ts = lin(0, tm, 300), I = t => (on ? I0 * (1 - Math.exp(-t / tau)) : I0 * Math.exp(-t / tau)), Es = t => (on ? -P.E * Math.exp(-t / tau) : P.E * Math.exp(-t / tau));
      plot(c, [0, 0, w * .5, h], { xr: [0, tm * 1e3], yr: [0, I0 * 1.15], xl: 't, ms', yl: 'I(t), A', series: [{ pts: ts.map(t => [t * 1e3, I(t)]), c: C.cyan, w: 2.5 }], vl: [{ x: tau * 1e3, l: 'τ', c: C.amber }], hl: [{ y: I0 * (on ? .632 : .368), l: on ? '63 %' : '37 %', c: '#64748b' }] });
      plot(c, [w * .5, 0, w * .5, h], { xr: [0, tm * 1e3], yr: [-P.E * 1.15, P.E * 1.15], xl: 't, ms', yl: 'ℰ_s = −L dI/dt, V', series: [{ pts: ts.map(t => [t * 1e3, Es(t)]), c: C.rose, w: 2.5 }] });
      return { 'τ = L/R, ms': fx(tau * 1e3, 2), 'I∞ = ℰ/R, A': fx(I0, 3), 'I(τ), A': fx(I(tau), 3), 'Magnit energiya LI²/2, J': fx(P.L * I0 * I0 / 2, 4), 'Izoh': on ? 'o‘zinduksiya tok o‘sishiga qarshilik qiladi' : 'o‘zinduksiya tokni ushlab turadi (uzishda uchqun)' };
    }
  };

  /* M14 — Elektromagnit to‘lqin */
  S.wave = {
    title: 'Elektromagnit to‘lqin: E ⊥ B ⊥ v',
    anim: true,
    params: [
      { k: 'E0', l: 'Amplituda E₀, V/m', min: 10, max: 500, step: 10, v: 100 },
      { k: 'f', l: 'Chastota f, MGs', min: 10, max: 300, step: 5, v: 100 },
      { k: 'n', l: 'Sindirish ko‘rsatkichi n = √(εμ)', min: 1, max: 3, step: .05, v: 1 }
    ],
    draw(cv, P, dt) {
      const { c, w, h } = ctx2d(cv), t = tick(cv, dt), v = cL / P.n, lam = v / (P.f * 1e6), B0 = P.E0 / v, I = .5 * v * e0 * P.n * P.n * P.E0 * P.E0;
      const ox = 50, oy = h * .55, Lx = w - 90, kx = 2 * Math.PI / (Lx / (3 * P.n)), ph = t * 3;
      const pr = (x, y, z) => [ox + x + z * .55, oy - y - z * .32];
      arrow(c, ...pr(-10, 0, 0), ...pr(Lx + 20, 0, 0), C.axis, 1.5); txt(c, 'x (v)', ...pr(Lx + 30, -12, 0), C.axis, 'left', 12);
      arrow(c, ...pr(0, 0, 0), ...pr(0, h * .35, 0), C.amber, 1.2); txt(c, 'E', ...pr(6, h * .35, 0), C.amber, 'left', 12);
      arrow(c, ...pr(0, 0, 0), ...pr(0, 0, h * .45), C.cyan, 1.2); txt(c, 'B', ...pr(0, 6, h * .45), C.cyan, 'left', 12);
      const A = h * .28, Ae = A * Math.min(1, .3 + P.E0 / 500 * .7), xs = lin(0, Lx, 220);
      poly(c, xs.map(x => pr(x, Ae * Math.sin(kx * x - ph), 0)), C.amber, 2.2); poly(c, xs.map(x => pr(x, 0, Ae * Math.sin(kx * x - ph))), C.cyan, 2.2);
      for (let x = 0; x < Lx; x += 14) { const s = Math.sin(kx * x - ph); ln(c, ...pr(x, 0, 0), ...pr(x, Ae * s, 0), '#fbbf2455', 1); ln(c, ...pr(x, 0, 0), ...pr(x, 0, Ae * s), '#22d3ee55', 1); }
      txt(c, 'sariq — E (vertikal), havorang — B (gorizontal), ikkalasi bir fazada', 12, 18, C.text, 'left', 11);
      return { 'Tezlik v = c/n, m/s': sci(v, 4), 'To‘lqin uzunligi λ, m': fx(lam, 3), 'B₀ = E₀/v, T': sci(B0, 3), 'Intensivlik I, W/m²': fx(I, 2), 'Diapazon': lam > 1 ? 'radioto‘lqin (UQT)' : 'mikroto‘lqin' };
    }
  };

  /* M15, A20 — O‘zgaruvchan tok: vektor diagramma va rezonans */
  S.ac = {
    title: 'O‘zgaruvchan tok: RLC zanjir, vektor diagramma',
    params: [
      { k: 'R', l: 'R, Ω', min: 5, max: 300, step: 5, v: 100 },
      { k: 'L', l: 'L, H', min: .01, max: 1, step: .01, v: .5 },
      { k: 'C', l: 'C, mkF', min: 1, max: 100, step: 1, v: 10 },
      { k: 'f', l: 'Chastota f, Gs', min: 10, max: 200, step: 1, v: 50 },
      { k: 'U', l: 'Effektiv kuchlanish U, V', min: 10, max: 240, step: 10, v: 220 }
    ],
    draw(cv, P) {
      const { c, w, h } = ctx2d(cv), Cc = P.C * 1e-6, om = 2 * Math.PI * P.f, XL = om * P.L, XC = 1 / (om * Cc), Z = Math.hypot(P.R, XL - XC), I = P.U / Z, phi = Math.atan2(XL - XC, P.R);
      const UR = I * P.R, UL = I * XL, UC = I * XC, W2 = w * .46, ox = 30, oy = h / 2, sc = (W2 - 60) / Math.max(UR, P.U, 1) * .9, sv = Math.min(sc, (h / 2 - 20) / Math.max(UL, UC, 1));
      const s = Math.min(sc, sv);
      arrow(c, ox, oy, ox + W2 - 50, oy, '#475569', 1); txt(c, 'I', ox + W2 - 46, oy + 4, '#94a3b8', 'left', 12);
      arrow(c, ox, oy, ox + s * UR, oy, C.green, 2.5); txt(c, 'U_R', ox + s * UR / 2, oy + 16, C.green, 'center', 11);
      arrow(c, ox + s * UR, oy, ox + s * UR, oy - s * UL, C.amber, 2.2); txt(c, 'U_L', ox + s * UR + 6, oy - s * UL + 10, C.amber, 'left', 11);
      arrow(c, ox + s * UR + 10, oy, ox + s * UR + 10, oy + s * UC, C.blue, 2.2); txt(c, 'U_C', ox + s * UR + 16, oy + s * UC - 4, C.blue, 'left', 11);
      arrow(c, ox, oy, ox + s * UR, oy - s * (UL - UC), C.rose, 2.8); txt(c, 'U', ox + s * UR / 2 - 6, oy - s * (UL - UC) / 2 - 8, C.rose, 'right', 13);
      txt(c, `φ = ${fx(phi / deg, 1)}°`, ox + 40, oy - 8 * Math.sign(phi || 1) - 4, C.rose, 'left', 11);
      const fs = lin(5, 200, 400), If = f => P.U / Math.hypot(P.R, 2 * Math.PI * f * P.L - 1 / (2 * Math.PI * f * Cc)), f0 = 1 / (2 * Math.PI * Math.sqrt(P.L * Cc));
      plot(c, [W2, 0, w - W2, h], { xr: [5, 200], yr: [0, P.U / P.R * 1.15], xl: 'f, Gs', yl: 'I, A (rezonans egri chizig‘i)', series: [{ pts: fs.map(f => [f, If(f)]), c: C.cyan, w: 2.5 }], vl: [{ x: f0, l: 'f₀', c: C.green }], marks: [{ x: P.f, y: I, c: C.amber }] });
      return { 'X_L, Ω': fx(XL, 1), 'X_C, Ω': fx(XC, 1), 'Z, Ω': fx(Z, 1), 'I, A': fx(I, 3), 'φ, ° (xarakter)': `${fx(phi / deg, 1)} (${phi > 0 ? 'induktiv' : phi < 0 ? 'sig‘im' : 'aktiv'})`, 'cos φ': fx(Math.cos(phi), 3), 'P = I²R, W': fx(I * I * P.R, 1), 'f₀, Gs': fx(f0, 2), 'U_L, U_C, V': `${fx(UL, 0)}; ${fx(UC, 0)}` };
    }
  };

  /* A8 — RC zanjir: zaryadlash va energiya */
  S.rc = {
    title: 'RC zanjir: kondensatorning zaryadlanishi va energiya balansi',
    params: [
      { k: 'mode', l: 'Jarayon', type: 'sel', opts: ['Zaryadlash', 'Razryad'], v: 'Zaryadlash' },
      { k: 'U', l: 'Manba U₀, V', min: 1, max: 24, step: .5, v: 10 },
      { k: 'R', l: 'R, kΩ', min: .1, max: 10, step: .1, v: 1 },
      { k: 'C', l: 'C, mkF', min: 10, max: 1000, step: 10, v: 100 }
    ],
    draw(cv, P) {
      const { c, w, h } = ctx2d(cv), R = P.R * 1e3, Cc = P.C * 1e-6, tau = R * Cc, ch = P.mode[0] === 'Z', tm = 5 * tau, ts = lin(0, tm, 300);
      const uC = t => (ch ? P.U * (1 - Math.exp(-t / tau)) : P.U * Math.exp(-t / tau)), i = t => P.U / R * Math.exp(-t / tau) * (ch ? 1 : -1);
      plot(c, [0, 0, w * .5, h], { xr: [0, tm], yr: [-.05 * P.U, P.U * 1.1], xl: 't, s', yl: 'u_C, V (havorang) · i·R, V (pushti)', series: [{ pts: ts.map(t => [t, uC(t)]), c: C.cyan, w: 2.5 }, { pts: ts.map(t => [t, Math.abs(i(t)) * R]), c: C.rose, w: 1.8, dash: [5, 4] }], vl: [{ x: tau, l: 'τ = RC', c: C.amber }] });
      const W0 = Cc * P.U * P.U / 2, WC = t => Cc * uC(t) ** 2 / 2, WR = t => (ch ? W0 * (1 - Math.exp(-2 * t / tau)) : W0 * (1 - Math.exp(-2 * t / tau)));
      const Ws = ch ? [{ pts: ts.map(t => [t, Cc * P.U * P.U * (1 - Math.exp(-t / tau)) * 1e3]), c: C.green, w: 2 }] : [];
      plot(c, [w * .5, 0, w * .5, h], { xr: [0, tm], yr: [0, (ch ? 2.15 : 1.1) * W0 * 1e3], xl: 't, s', yl: 'energiya, mJ', series: Ws.concat([{ pts: ts.map(t => [t, WC(t) * 1e3]), c: C.cyan, w: 2.3 }, { pts: ts.map(t => [t, WR(t) * 1e3]), c: C.amber, w: 2.3 }]), legend: (ch ? [{ c: C.green, l: 'manba bergan' }] : []).concat([{ c: C.cyan, l: 'kondensatorda' }, { c: C.amber, l: 'R da issiqlik' }]) });
      return { 'τ = RC, s': fx(tau, 3), 'Boshlang‘ich tok, mA': fx(P.U / R * 1e3, 3), 'W_C (oxirida), mJ': fx((ch ? W0 : 0) * 1e3, 3), 'R dagi issiqlik, mJ': fx(W0 * 1e3, 3), 'Manba energiyasi, mJ': ch ? fx(2 * W0 * 1e3, 3) : '—' };
    }
  };

  /* A19 — RLC tebranish konturi */
  S.rlc = {
    title: 'Tebranish konturi: erkin va majburiy tebranishlar',
    params: [
      { k: 'mode', l: 'Rejim', type: 'sel', opts: ['Erkin (so‘nuvchi) tebranishlar', 'Majburiy: rezonans egri chizig‘i'], v: 'Erkin (so‘nuvchi) tebranishlar' },
      { k: 'L', l: 'L, mH', min: 1, max: 100, step: 1, v: 10 },
      { k: 'C', l: 'C, mkF', min: .1, max: 10, step: .1, v: 1 },
      { k: 'R', l: 'R, Ω', min: 0, max: 250, step: 1, v: 20 }
    ],
    draw(cv, P) {
      const { c, w, h } = ctx2d(cv), L = P.L * 1e-3, Cc = P.C * 1e-6, w0 = 1 / Math.sqrt(L * Cc), b = P.R / (2 * L), Q = P.R > 0 ? Math.sqrt(L / Cc) / P.R : Infinity, U0 = 10;
      if (P.mode[0] === 'E') {
        const T0 = 2 * Math.PI / w0, tm = 6 * T0; let q = Cc * U0, i = 0; const dt = tm / 6000, pu = [], pe = [];
        for (let k = 0; k <= 6000; k++) { if (k % 10 === 0) { pu.push([k * dt * 1e3, q / Cc]); pe.push([k * dt * 1e3, q * q / (2 * Cc) * 1e6, L * i * i / 2 * 1e6]); } const a = (-q / Cc - P.R * i) / L; i += a * dt; q += i * dt; }
        plot(c, [0, 0, w * .5, h], { xr: [0, tm * 1e3], yr: [-U0 * 1.1, U0 * 1.1], xl: 't, ms', yl: 'u_C(t), V', series: [{ pts: pu, c: C.cyan, w: 2 }, { pts: pu.map(p => [p[0], U0 * Math.exp(-b * p[0] / 1e3)]), c: '#64748b', dash: [4, 4], w: 1.3 }] });
        const Wm = Cc * U0 * U0 / 2 * 1e6;
        plot(c, [w * .5, 0, w * .5, h], { xr: [0, tm * 1e3], yr: [0, Wm * 1.1], xl: 't, ms', yl: 'energiya, mkJ', series: [{ pts: pe.map(p => [p[0], p[1]]), c: C.rose, w: 2 }, { pts: pe.map(p => [p[0], p[2]]), c: C.amber, w: 2 }], legend: [{ c: C.rose, l: 'W_C (elektr)' }, { c: C.amber, l: 'W_L (magnit)' }] });
      } else {
        const f0 = w0 / (2 * Math.PI), fs = lin(f0 * .2, f0 * 2, 400), Ia = f => U0 / Math.hypot(Math.max(P.R, .5), 2 * Math.PI * f * L - 1 / (2 * Math.PI * f * Cc));
        plot(c, [0, 0, w, h], { xr: [f0 * .2, f0 * 2], yr: [0, U0 / Math.max(P.R, .5) * 1.1], xl: 'f, Gs', yl: 'tok amplitudasi, A (U₀ = 10 V)', series: [{ pts: fs.map(f => [f, Ia(f)]), c: C.cyan, w: 2.5 }], vl: [{ x: f0, l: 'f₀', c: C.green }] });
      }
      const om = Math.sqrt(Math.max(w0 * w0 - b * b, 0));
      return { 'ω₀ = 1/√(LC), rad/s': fx(w0, 0), 'f₀, Gs': fx(w0 / (2 * Math.PI), 1), 'T₀, ms': fx(2 * Math.PI / w0 * 1e3, 3), 'β = R/2L, 1/s': fx(b, 1), 'Asllik Q': isFinite(Q) ? fx(Q, 2) : '∞', 'Log. dekrement δ': om > 0 ? fx(2 * Math.PI * b / om, 3) : 'aperiodik', 'R_kr = 2√(L/C), Ω': fx(2 * Math.sqrt(L / Cc), 1) };
    }
  };

  /* A21 — Transformator va uch fazali tok */
  S.trafo = {
    title: 'Transformator va uch fazali tok',
    params: [
      { k: 'N1', l: 'Birlamchi o‘ramlar N₁ (U₁ = 220 V)', min: 100, max: 2000, step: 10, v: 1100 },
      { k: 'N2', l: 'Ikkilamchi o‘ramlar N₂', min: 10, max: 2000, step: 10, v: 60 },
      { k: 'Rl', l: 'Yuklama R, Ω', min: 1, max: 200, step: 1, v: 6 },
      { k: 'eta', l: 'FIK, %', min: 80, max: 100, step: 1, v: 96 },
      { k: 'Uf', l: 'Uch fazali: faza kuchlanishi U_f, V', min: 100, max: 400, step: 10, v: 220 }
    ],
    draw(cv, P) {
      const { c, w, h } = ctx2d(cv), U1 = 220, k = P.N1 / P.N2, U2 = U1 / k, I2 = U2 / P.Rl, P2 = U2 * I2, P1 = P2 / (P.eta / 100), I1 = P1 / U1;
      const W2 = w * .45, cx = W2 / 2, cy = h / 2, cw = Math.min(W2 * .5, 150), chh = Math.min(h * .6, 160);
      c.strokeStyle = '#64748b'; c.lineWidth = 14; c.strokeRect(cx - cw / 2, cy - chh / 2, cw, chh);
      const coil = (x, n, col) => { const k2 = Math.max(3, Math.min(16, Math.round(n / 80))); for (let i = 0; i < k2; i++) { const y = cy - chh * .35 + i * chh * .7 / (k2 - 1); c.strokeStyle = col; c.lineWidth = 2.5; c.beginPath(); c.ellipse(x, y, 14, 4, 0, 0, 7); c.stroke(); } };
      coil(cx - cw / 2, P.N1, C.amber); coil(cx + cw / 2, P.N2, C.cyan);
      txt(c, `N₁ = ${P.N1}`, cx - cw / 2 - 20, cy - chh / 2 - 12, C.amber, 'center', 11); txt(c, `N₂ = ${P.N2}`, cx + cw / 2 + 20, cy - chh / 2 - 12, C.cyan, 'center', 11);
      txt(c, `U₁ = 220 V`, cx - cw / 2 - 22, cy + chh / 2 + 20, C.amber, 'center', 11); txt(c, `I₁ = ${fx(I1, 3)} A`, cx - cw / 2 - 22, cy + chh / 2 + 34, C.amber, 'center', 11);
      txt(c, `U₂ = ${fx(U2, 1)} V`, cx + cw / 2 + 22, cy + chh / 2 + 20, C.cyan, 'center', 11); txt(c, `I₂ = ${fx(I2, 2)} A`, cx + cw / 2 + 22, cy + chh / 2 + 34, C.cyan, 'center', 11);
      const ts = lin(0, .04, 300), cols = [C.amber, C.green, C.rose], Um = P.Uf * Math.SQRT2;
      plot(c, [W2, 0, w - W2, h * .55], { xr: [0, 40], yr: [-Um * 1.1, Um * 1.1], xl: 't, ms', yl: 'faza kuchlanishlari, V', series: [0, 1, 2].map(j => ({ pts: ts.map(t => [t * 1e3, Um * Math.sin(2 * Math.PI * 50 * t - j * 2 * Math.PI / 3)]), c: cols[j], w: 1.8 })) });
      const px = W2 + (w - W2) / 2, py = h * .78, r = Math.min(h * .19, (w - W2) / 4);
      const V = j => [px + r * Math.cos(Math.PI / 2 - j * 2 * Math.PI / 3), py - r * Math.sin(Math.PI / 2 - j * 2 * Math.PI / 3)];
      [0, 1, 2].forEach(j => arrow(c, px, py, ...V(j), cols[j], 2.2)); ln(c, ...V(0), ...V(1), '#94a3b8', 1.2, [4, 3]); txt(c, 'U_l', (V(0)[0] + V(1)[0]) / 2 + 6, (V(0)[1] + V(1)[1]) / 2, '#94a3b8', 'left', 11);
      txt(c, 'vektor diagramma (yulduz)', px, h - 4, C.text, 'center', 10);
      return { 'Transformatsiya koeff. k': fx(k, 2), 'U₂, V': fx(U2, 2), 'I₂, A': fx(I2, 3), 'I₁, A': fx(I1, 4), 'P₂ / P₁, W': `${fx(P2, 1)} / ${fx(P1, 1)}`, 'Liniya kuchlanishi U_l = √3·U_f, V': fx(Math.sqrt(3) * P.Uf, 1) };
    }
  };

  /* ---------- Simulyator konteynerini qurish ---------- */
  function build(box) {
    const key = box.dataset.sim, sim = S[key]; if (!sim) return;
    const id = `${key}-${Math.random().toString(36).slice(2, 7)}`;
    const ctrls = sim.params.map(p => {
      if (p.type === 'sel') return `<label class="control">${A(p.l)}<select data-k="${p.k}">${p.opts.map(o => `<option value="${o}"${o === p.v ? ' selected' : ''}>${A(o)}</option>`).join('')}</select></label>`;
      return `<label class="control">${A(p.l)} <output data-o="${p.k}"></output><input type="range" data-k="${p.k}" min="${p.min}" max="${p.max}" step="${p.step}" value="${p.v}"></label>`;
    }).join('');
    box.innerHTML = `<div class="sim-layout"><div class="card controls"><h3>${A(sim.title)}</h3>${ctrls}<div class="actions"><button class="secondary" type="button" data-reset>${A('Boshlang‘ich qiymatlar')}</button></div><div class="readout" aria-live="polite"></div></div><div class="card canvas-card"><div class="toolbar"><span>${A(sim.title)}</span><span class="stat notranslate">model · SI birliklar</span></div><canvas id="${id}" role="img" aria-label="${A(sim.title)}"></canvas></div></div>`;
    const cv = box.querySelector('canvas'), ro = box.querySelector('.readout');
    const read = () => { const P = {}; box.querySelectorAll('[data-k]').forEach(el => { const p = sim.params.find(x => x.k === el.dataset.k); P[p.k] = p.type === 'sel' ? el.value : (p.log ? 10 ** +el.value : +el.value); const o = box.querySelector(`[data-o="${p.k}"]`); if (o) o.textContent = p.log ? sci(10 ** +el.value, 1) : (+el.value).toString(); }); return P; };
    const render = (dt) => { const r = sim.draw(cv, read(), dt || 0); ro.innerHTML = Object.entries(r || {}).map(([k, v]) => `<span>${A(k)}</span><b>${A(v)}</b>`).join(''); };
    box.addEventListener('input', () => render()); box.addEventListener('change', () => render());
    box.querySelector('[data-reset]').addEventListener('click', () => { box.querySelectorAll('[data-k]').forEach(el => { const p = sim.params.find(x => x.k === el.dataset.k); el.value = p.v; }); render(); });
    window.addEventListener('resize', () => render());
    render();
    if (sim.anim) { let last = performance.now(), vis = true; new IntersectionObserver(e => { vis = e[0].isIntersecting; }).observe(box); const loop = now => { if (vis) render(Math.min((now - last) / 1000, .1)); last = now; requestAnimationFrame(loop); }; requestAnimationFrame(loop); }
  }
  window.YAF_SIMS = S;
  const init = () => document.querySelectorAll('.sim-box[data-sim]').forEach(build);
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init); else init();
})();
