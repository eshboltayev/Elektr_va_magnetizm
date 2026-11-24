# Elektr va magnetizm — interaktiv elektron darslik

**60530700 — Astronomiya (bakalavriat) · EM1306 · 6 ECTS (180 soat) · 3-semestr**
Muallif: Eshboltayev Iqbol Mamirjonovich, professor, PhD (Qo‘qon davlat universiteti)

Sayt: https://eshboltayev.github.io/Elektr_va_magnetizm/

## Tarkibi (fan dasturi asosida)

| Bo‘lim | Hajm | Sahifalar |
|---|---|---|
| Ma’ruzalar M1–M15 | 30 soat | `lecture1.html` … `lecture15.html` — nazariya, ishlangan misol, interaktiv model, SI topshirig‘i, 10 savolli test |
| Amaliy mashg‘ulotlar A1–A21 | 42 soat | `amaliy1.html` … `amaliy21.html` — ishlangan va javobli masalalar, Python kodi |
| Mustaqil ta’lim (54 mavzu × 2 soat) | 108 soat | `mustaqil.html` — taqdimot rejalari, 8 ta keys-stadi |
| Baholash | JN 30 + ON 20 + YaN 50 | `baholash.html` — rubrikalar, TN1–TN10 matritsasi, kalkulyator |
| O‘qituvchi uchun | 15 hafta | `oqituvchi.html` |
| Ilovalar | — | `glossariy.html`, `vositalar.html`, `annotatsiya.html` |

18 ta interaktiv model (`js/sims.js`): Kulon qonuni, kuch chiziqlari, Gauss teoremasi, potensial, dielektrik, kondensator, to‘la zanjir, Kirxgof qoidalari, Bio–Savar–Laplas, parallel toklar, Lorens kuchi, gisterezis, RL va RC zanjirlar, tebranish konturi, elektromagnit to‘lqin, o‘zgaruvchan tok, transformator va uch fazali tok. Har birida ovozli namoyish (`gen/tours.py`).

## Ovoz

O‘zbekcha matnlar neyron ovozda (Microsoft Edge TTS, `uz-UZ-SardorNeural`) oldindan MP3 qilib tayyorlanadi. `*.html` yoki `js/app.js` o‘zgarib GitHub’ga yuklanganda **Actions → “Ovoz (o‘zbekcha MP3)”** avtomatik ishga tushadi (`audio/uz/`).

## Yangilash

Mazmun `gen/` papkasida: `lectures_a.py`, `lectures_b.py`, `amaliy.py`, `other.py`, `tours.py`, `common.py`.

```bash
python3 gen/build.py .
```

## GitHub Pages

Settings → Pages → Source: *Deploy from a branch* → `main` / `(root)`.

Litsenziya: CC BY-SA 4.0.
