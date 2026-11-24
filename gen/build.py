"""Elektron darslik sahifalarini generatsiya qilish: python3 build.py <chiqish_papkasi>"""
import os, sys, re
sys.path.insert(0, os.path.dirname(__file__))
from common import *
from lectures_a import L as LA
from lectures_b import L as LB
from amaliy import A, SEM
import other, json, random
from quiz_extra import Q as QX
from tours import T as TOURS
from alifbo import html_to_new

OUT = sys.argv[1] if len(sys.argv) > 1 else "../site"
LECT = LA + LB
SIMNAME = {"coulomb": "Kulon qonuni", "field": "Kuch chiziqlari va superpozitsiya", "gauss": "Gauss teoremasi: E(r)", "potential": "Potensial va ekvipotensial chiziqlar", "dielectric": "Dielektrikda maydon", "capacitor": "Yassi kondensator", "ohm": "To‘la zanjir uchun Om qonuni", "kirchhoff": "Kirxgof qoidalari", "biot": "Bio–Savar–Laplas qonuni", "ampere": "Parallel toklar va Amper kuchi", "lorentzf": "Lorens kuchi: zarra trayektoriyasi", "hyster": "Magnit gisterezisi", "rl": "RL zanjir: o‘zinduksiya", "wave": "Elektromagnit to‘lqin", "ac": "O‘zgaruvchan tok: vektor diagramma", "rc": "RC zanjir: zaryadlanish va energiya", "rlc": "Tebranish konturi", "trafo": "Transformator va uch fazali tok"}
TN_TEXT = {
 "TN1": "Pedagogik-metodik kompetensiya: o‘quvchilarning mustaqil bilim olish faoliyatini tashkil etish va boshqarish ko‘nikmasi",
 "TN2": "Ilmiy-nazariy kompetensiya: fizika qonunlari va hodisalarning mohiyati, matematik ifodasi va o‘zaro bog‘lanishlarini tushunish",
 "TN3": "Terminologik va masalalar yechish kompetensiyasi: pedagogik va fizik terminologiya, masala turlari va yechish metodlarini bilish",
 "TN4": "Amaliy va tahliliy kompetensiya: nazariy bilimlarni amaliyotga qo‘llash, fizik doimiylar jadvallari bilan ishlash, masalalar yechish",
 "TN5": "Axborot-metodik kompetensiya: ilmiy-metodik adabiyotlar bilan ishlash va metodik yo‘riqnomalar tuzish",
 "TN6": "O‘quvchilarning mustaqil bilim olish faoliyatini tashkil etish va boshqarish ko‘nikmasi",
 "TN7": "Fizika qonunlari va hodisalarning mohiyati, matematik ifodalari, o‘zaro bog‘lanishlari va ilg‘or pedagogik texnologiyalarni o‘rganish",
 "TN8": "Pedagogik va fizik terminologiyalar, masala turlari va ularni yechish usullarini bilish",
 "TN9": "Nazariy bilimlarni amaliyotga qo‘llash, fizik doimiylar jadvallari bilan ishlash, masalalar yechish ko‘nikmasi",
 "TN10": "Ilmiy-metodik adabiyotlar bilan ishlash, zaruriy metodik yo‘riqnomalar tuzish",
}
_MAT = {1: "+--", 2: "++-", 3: "+--", 4: "++-", 5: "-++", 6: "+++", 7: "++-", 8: "+--", 9: "+--", 10: "+++"}
TN_MATRIX = {f"TN{i}": tuple("+" if ch == "+" else "—" for ch in v) for i, v in _MAT.items()}


def fix_math(html):
    f = lambda m: m.group(0).replace("<", "\\lt ")
    html = re.sub(r"\\\(.*?\\\)", f, html, flags=re.S)
    return re.sub(r"\$\$.*?\$\$", f, html, flags=re.S)


def write(name, html):
    html = html_to_new(fix_math(html))
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(html)


def strip_tags(s):
    return re.sub(r"<[^>]+>|\\\(|\\\)|\\[a-zA-Z]+|[{}$]", "", s)


def shuffled_quiz(items, seed):
    rnd = random.Random(seed); out = []
    for k, (q, opts, a, ex) in enumerate(items):
        idx = list(range(len(opts))); rnd.shuffle(idx)
        out.append((q, [opts[i] for i in idx], idx.index(a), ex))
    return out


def sim_block(sim, uid):
    steps = TOURS.get(sim, [])
    lis = "".join(f"<li data-set='{json.dumps(p)}'>{t}</li>" for p, t in steps)
    tour = (f'<div class="tour-bar"><button class="voice-btn" type="button" data-tour="tour-{uid}">{SPEAKER}<span>Ovozli namoyish</span></button>'
            f'<span class="muted" style="font-size:.82rem">Model o‘zi parametrlarni o‘zgartirib, natijani tushuntiradi; so‘ng boshqaruv sizga o‘tadi.</span></div>'
            f'<div class="tour-cap" aria-live="polite"></div><ol class="vh tour-steps" id="tour-{uid}">{lis}</ol>') if steps else ""
    return f'<div class="sim-wrap"><div class="sim-box" data-sim="{sim}"></div>{tour}</div>'


def tn_chips(tns):
    return "".join(f'<span class="chip g" title="{TN_TEXT[t]}">{t}</span>' for t in tns)


def refs_html(refs, intl):
    items = [f"[{r}] {BASE_LIT[r]}" for r in refs] + [INTL[k] for k in intl]
    return ul(items) + '<p class="muted" style="font-size:.85rem">[1]–[5] — fan dasturidagi asosiy adabiyotlar raqamlanishi. Xalqaro darsliklar mustaqil chuqurlashtirish uchun tavsiya etiladi.</p>'


def pager(prev, nxt):
    p = card_link(prev[0], "← Oldingi", prev[1], "") if prev else "<span></span>"
    n = card_link(nxt[0], "Keyingi →", nxt[1], "").replace('class="card"', 'class="card next"') if nxt else "<span></span>"
    return f'<nav class="pager" aria-label="Sahifalar">{p}{n}</nav>'


# ---------------- Ma'ruza sahifalari ----------------
def lecture_page(L, i):
    n = L["n"]
    toc = [("maqsad", "Maqsad va natijalar"), ("reja", "Reja va tayanch tushunchalar"), ("nazariya", "Nazariy qism"), ("misol", "Ishlangan misol"), ("model", "Interaktiv model"), ("si", "SI bilan ishlash"), ("xatolar", "Tipik xato tushunchalar"), ("test", "Nazorat testi"), ("blits", "Blits-so‘rov"), ("adabiyot", "Adabiyotlar"), ("oqituvchi", "O‘qituvchi uchun")]
    S = []
    S.append(sec("maqsad", 1, "Maqsad va kutilayotgan natijalar", f'<p>{L["goal"]}</p><h3>Mashg‘ulotdan so‘ng talaba:</h3>{ul(L["outcomes"])}<p class="muted">Fan dasturidagi ta’lim natijalari: {", ".join(f"<b>{t}</b> — {TN_TEXT[t]}" for t in L["tn"])}.</p>'))
    terms = "".join(f'<span class="chip c">{t}</span>' for t in L["terms"])
    S.append(sec("reja", 2, "Reja va tayanch tushunchalar", f'{ul(L["plan"], True)}<h3>Tayanch tushunchalar</h3><div class="chips">{terms}</div>'))
    th = "".join(f"<h3>{n}.{k+1}. {h}</h3>{b}" for k, (h, b) in enumerate(L["theory"]))
    S.append(sec("nazariya", 3, "Nazariy qism", th))
    et, eg, es = L["example"]
    S.append(sec("misol", 4, "Ishlangan misol", f'<div class="example"><div class="ex-h">{et}</div><div class="ex-b"><p><b>Shart.</b> {eg}</p><details><summary>Yechimni ko‘rsatish</summary><p>{es}</p></details></div></div><div class="callout info"><b>Mustaqil tekshiring</b>Natijani quyidagi interaktiv model yoki Python bilan qayta hisoblang va birliklarni tekshiring.</div>'))
    S.append(sec("model", 5, f"Interaktiv model: {SIMNAME[L['sim']]}", f'{sim_block(L["sim"], f"m{n}")}<h3>Model bilan topshiriqlar</h3>{ul(L["simtask"], True)}<p class="muted" style="font-size:.85rem">Model o‘quv maqsadida soddalashtirilgan (nuqtaviy zaryadlar, ideal elementlar, vakuum); natijani analitik hisob yoki amaliy mashg‘ulotdagi Python kodi bilan solishtiring.</p>'))
    S.append(sec("si", 6, "Sun’iy intellekt bilan ishlash topshirig‘i", f'<div class="callout ai"><b>Qoidalar</b>SI — tekshirilishi shart bo‘lgan yordamchi. Har bir formula va son darslik yoki mustaqil hisob bilan solishtiriladi. Baholanadigan ishda SI dan qanday foydalanilgani (prompt va tekshiruv) ilova qilinadi.</div>{prompt(f"ai-{n}", L["ai"])}<h3>Javobni tekshirish ro‘yxati</h3>{ul(["Birliklar va o‘lchamlilik to‘g‘rimi?", "Limit holatlar (\\(r\\to\\infty\\), \\(R\\to0\\), \\(\\omega\\to0\\), \\(\\varepsilon=1\\)) mantiqiymi?", "Sonlar darslikdagi ishlangan misol bilan mos keladimi?", "Manba ko‘rsatilmagan parametrlar “taxmin” deb belgilanganmi?"])}'))
    S.append(sec("xatolar", 7, "Tipik xato tushunchalar", table(["Noto‘g‘ri tasavvur", "To‘g‘ri tushuncha"], L["mistakes"])))
    S.append(sec("test", 8, "Nazorat testi (10 savol, o‘z-o‘zini tekshirish)", quiz(shuffled_quiz(L["quiz"] + QX[n], 1000 + n), f"m{n}") + '<p class="muted" style="font-size:.85rem;margin-top:.6rem">Bu test o‘z-o‘zini tekshirish uchun; rasmiy oraliq nazorat HEMIS’da o‘tkaziladi.</p>'))
    S.append(sec("blits", 9, "Blits-so‘rov va muhokama savollari", ul(L["blits"], True) + '<p class="muted">Bog‘liq mustaqil ta’lim mavzulari: <a href="mustaqil.html">mustaqil ta’lim sahifasi</a>.</p>'))
    S.append(sec("adabiyot", 10, "Adabiyotlar", refs_html(L["refs"], L["intl"])))
    S.append(f'<section class="doc-sec teacher-note" id="oqituvchi"><h2>O‘qituvchi uchun: 80 daqiqalik dars rejasi</h2>{table(["Vaqt", "Bosqich", "Faoliyat"], [["0–10", "Kirish", "Blits-so‘rov (9-bo‘lim), oldingi mavzu bilan bog‘lash"], ["10–45", "Nazariya", "3-bo‘lim; formulalarni doskada keltirib chiqarish"], ["45–60", "Model", "5-bo‘lim: simulyatorni proyektorda namoyish qilish, talabalar bashorati → tekshiruv"], ["60–72", "Misol", "4-bo‘lim: talabalar juftlikda yechadi, so‘ng yechim ochiladi"], ["72–80", "Yakun", "Nazorat testi, tipik xatolar muhokamasi, mustaqil topshiriq"]])}<p class="muted">Batafsil: <a href="oqituvchi.html">o‘qituvchi qo‘llanmasi</a>.</p></section>')
    prev = (f"lecture{n-1}.html", f"{n-1}-ma’ruza") if n > 1 else ("annotatsiya.html", "Darslik haqida")
    nxt = (f"lecture{n+1}.html", f"{n+1}-ma’ruza") if n < 15 else ("amaliy1.html", "1-amaliy mashg‘ulot")
    chips = [("c", f"M{n}"), ("", "2 akademik soat"), ("v", "Model: " + SIMNAME[L["sim"]]), ("a", "Adabiyot: " + ", ".join(f"[{r}]" for r in L["refs"]))]
    body = head(f"{n}-ma’ruza: {strip_tags(L['short'])}", strip_tags(L["goal"])[:160]) + header("index.html#maruzalar") + '<main id="main">' + hero([("index.html", "Bosh sahifa"), ("index.html#maruzalar", "Ma’ruzalar"), ("", f"{n}-ma’ruza")], f"{n}-ma’ruza · M{n}", L["title"], "", chips, read="maqsad,reja,nazariya,misol,xatolar") + f'<div class="container" style="padding-top:1rem"><div class="chips">{tn_chips(L["tn"])}</div></div>' + doc(toc, S, pager(prev, nxt)) + "</main>" + footer(sims=True)
    write(f"lecture{n}.html", body)


# ---------------- Amaliy sahifalari ----------------
DF_RUBRIC = table(["Daraja", "Ball (20 dan)", "Mezon (fan dasturi bo‘yicha)"], [
    ["Yuqori", "18–20", "Masalaning fizik mohiyatini to‘liq tushunadi, kerakli qonuniyatlarni (Kulon, Gauss, Om, Kirxgof, Bio–Savar–Laplas) aniq tanlaydi, elektr va magnit maydon chizmalari hamda zanjir sxemalarini bexato chizib, mustaqil yechish algoritmini tuzadi."],
    ["Yetarli", "14–17", "Masala shartini tushunadi va asosiy qonuniyatlarni yozadi, biroq murakkabroq sxemalarni (masalan, tarmoqlangan zanjirlar) chizishda yoki yechish ketma-ketligini tuzishda o‘qituvchi yordamiga tayanadi."],
    ["Minimal", "12–13", "Faqat eng sodda, bitta formulaga qo‘yiladigan masalalarning shartini yoza oladi; chizma va sxemalarni mustaqil tuza olmaydi, qonuniyatlarni tanlashda adashadi."],
    ["Erishilmagan", "0–11", "Masala shartini umuman tushunmaydi, fizik qonuniyatlarni amaliyotga bog‘lay olmaydi, sxema va chizmalar chiza olmaydi."]])


def amaliy_page(a):
    n = a["n"]
    toc = [("maqsad", "Maqsad"), ("nazariy", "Nazariy asos"), ("ishlangan", "Ishlangan masalalar"), ("mustaqil", "Mustaqil yechish"), ("model", "Interaktiv model"), ("kod", "Modellashtirish (Python)"), ("savollar", "Nazorat savollari"), ("baho", "Baholash")]
    S = [sec("maqsad", 1, "Mashg‘ulot maqsadi", f'<p>{a["goal"]}</p><p class="muted">Nazariy asos: <a href="lecture{a["lec"]}.html">{a["lec"]}-ma’ruza</a>. Ta’lim natijalari: {", ".join(f"<b>{t}</b>" for t in a["tn"])}.</p><div class="callout info"><b>Kerakli vositalar</b>Kalkulyator, Python (Google Colab yoki Jupyter), darslikdagi interaktiv model.</div>'),
         sec("nazariy", 2, "Qisqacha nazariy asos", a["theory"])]
    ex = "".join(f'<div class="example"><div class="ex-h">{k+1}-masala. {t}</div><div class="ex-b"><p><b>Shart.</b> {c}</p><details><summary>Yechim</summary><p>{s}</p></details></div></div>' for k, (t, c, s) in enumerate(a["solved"]))
    S.append(sec("ishlangan", 3, "Ishlangan masalalar", ex))
    tk = "".join(f'<li>{c}<details><summary>Javob</summary><p>{ans}</p></details></li>' for c, ans in a["tasks"])
    S.append(sec("mustaqil", 4, "Darsda mustaqil yechish uchun masalalar", f"<ol>{tk}</ol>"))
    S.append(sec("model", 5, f"Interaktiv model: {SIMNAME[a['sim']]}", sim_block(a["sim"], f"a{n}")))
    lang, code = a["model"]
    lab = "Python (Colab/Jupyter)"
    S.append(sec("kod", 6, "Kompyuterda modellashtirish", f'<p class="muted">{lab} — nusxalab ishga tushiring va natijani qo‘lda hisob bilan solishtiring (TN4, TN9).</p><div class="prompt-box"><button class="secondary copy" type="button" data-copy="code-{n}">Nusxalash</button><pre class="code" id="code-{n}">{esc(code)}</pre></div>'))
    S.append(sec("savollar", 7, "Nazorat savollari", ul(a["questions"], True)))
    S.append(sec("baho", 8, "Darsdagi faollikni baholash (JN tarkibida 20 ball)", DF_RUBRIC + '<p class="muted" style="font-size:.85rem">Darsdagi faollik (DF) butun semestr davomidagi amaliy mashg‘ulotlar bo‘yicha jami 20 ball bilan baholanadi. Ball oraliqlari fanning umumiy foiz chegaralari (90/70/60 %) asosida keltirilgan. Rasmiy ball HEMIS’da qo‘yiladi.</p>'))
    prev = (f"amaliy{n-1}.html", f"{n-1}-amaliy") if n > 1 else ("lecture15.html", "15-ma’ruza")
    nxt = (f"amaliy{n+1}.html", f"{n+1}-amaliy") if n < len(A) else ("mustaqil.html", "Mustaqil ta’lim")
    body = head(f"{n}-amaliy mashg‘ulot", strip_tags(a["goal"])[:160]) + header("index.html#amaliy") + '<main id="main">' + hero([("index.html", "Bosh sahifa"), ("index.html#amaliy", "Amaliy mashg‘ulotlar"), ("", f"A{n}")], f"{n}-amaliy mashg‘ulot · A{n}", a["title"], "", [("c", f"A{n}"), ("", "2 akademik soat"), ("v", "Model: " + SIMNAME[a["sim"]])], read="maqsad,nazariy,ishlangan") + doc(toc, S, pager(prev, nxt)) + "</main>" + footer(sims=True)
    write(f"amaliy{n}.html", body)


# ---------------- Bosh sahifa ----------------
def index_page():
    lec_cards = "".join(card_link(f"lecture{L['n']}.html", f"{L['n']}-ma’ruza", L["short"], strip_tags(L["goal"])[:120] + "…") for L in LECT)
    am_cards = "".join(card_link(f"amaliy{a['n']}.html", f"A{a['n']}", a["title"], f"Bog‘liq ma’ruza: M{a['lec']} · model: {SIMNAME[a['sim']]}") for a in A)

    sims = {}
    for L in LECT: sims.setdefault(L["sim"], f"lecture{L['n']}.html")
    for a in A: sims.setdefault(a["sim"], f"amaliy{a['n']}.html")
    sim_cards = "".join(f'<a class="card" href="{h}#model"><span class="badge">model</span><h3>{SIMNAME[k]}</h3><p class="muted">Sahifada ochish →</p></a>' for k, h in sims.items())
    steps = [("1", "Diagnostika", "Blits-so‘rov va 10 savolli o‘z-o‘zini tekshirish testi orqali boshlang‘ich bilimni aniqlash."), ("2", "Nazariya", "Tajribadan qonungacha: har bir formula keltirib chiqariladi va fizik ma’nosi izohlanadi."), ("3", "Interaktiv model", f"{len(SIMNAME)} ta brauzer simulyatori: parametrni o‘zgartiring, bashorat qiling, tekshiring."), ("4", "Masalalar", "21 amaliy mashg‘ulot: ishlangan masalalar, javobli mustaqil masalalar va Python kodlari."), ("5", "Doimiylar va SI", "Fizik doimiylar jadvallari bilan ishlash, natijalarni SI da izohlash (TN4, TN9)."), ("6", "Keys va loyiha", "Elektrotexnik muammolarni hal qilish: keys-stadi va taqdimot himoyasi.")]
    st = "".join(f'<article class="card"><span class="badge">QADAM {a}</span><h3>{b}</h3><p class="muted">{c}</p></article>' for a, b, c in steps)
    html = head("Bosh sahifa", f"Elektr va magnetizm — bakalavriat uchun interaktiv elektron darslik: 15 ma’ruza, 21 amaliy mashg‘ulot, 54 mustaqil ta’lim mavzusi, {len(SIMNAME)} interaktiv model.") + header() + f"""<main id="main">
<section class="hero"><div class="container"><div class="eyebrow">60530700 — Astronomiya · Bakalavriat · EM1306</div><h1>Elektr va magnit hodisalarni <span>ko‘ring, hisoblang va tushuning.</span></h1><p class="lead">Kulon qonuni va Gauss teoremasidan kondensatorlar, o‘zgarmas tok va Kirxgof qoidalarigacha, tokning magnit maydoni, Lorens kuchi va magnetiklardan elektromagnit induksiya, Maksvell tenglamalari va o‘zgaruvchan tokkacha — fan dasturi asosidagi ochiq elektron darslik. Baholash va rasmiy topshirish HEMIS orqali amalga oshiriladi.</p>
<div class="grid grid-4" style="margin-top:2rem"><div class="card"><div class="eyebrow">01</div><h3>15 ta ma’ruza</h3><p class="muted">30 soat: nazariya, ishlangan misol, ovozli o‘qish va 10 savolli test.</p></div><div class="card"><div class="eyebrow">02</div><h3>21 ta amaliy</h3><p class="muted">42 soat: ishlangan masalalar, javoblar va Python kodlari.</p></div><div class="card"><div class="eyebrow">03</div><h3>54 ta mustaqil ish</h3><p class="muted">108 soat: taqdimot va keys-stadi yo‘riqnomalari.</p></div><div class="card"><div class="eyebrow">04</div><h3>{len(SIMNAME)} ta model</h3><p class="muted">Brauzerda ishlaydigan elektromagnit simulyatorlar, ovozli namoyish bilan.</p></div></div></div></section>
<section id="darslik" class="section"><div class="container"><div class="section-head"><div class="eyebrow">Darslik haqida</div><h2>Annotatsiya, baholash va ilovalar</h2><p class="muted">6 ECTS kredit (180 soat), 3-semestr. Darslik fan dasturi, ECTS va xalqaro sifat mezonlariga muvofiq tuzilgan.</p></div><div class="grid grid-3">
{card_link("annotatsiya.html", "Kirish", "Annotatsiya, mundarija va xalqaro standartlar", "Bibliografik ma’lumot, uch tildagi annotatsiya, ta’lim natijalari va sifat mezonlariga muvofiqlik.")}
{card_link("baholash.html", "Baholash", "JN · ON · YaN rubrikalari", "100 ballik tizim, saralash ballari, TN–nazorat matritsasi va baho kalkulyatori.")}
{card_link("oqituvchi.html", "O‘qituvchi", "O‘qituvchi uchun qo‘llanma", "15 haftalik taqvim (haftada 5 soat), dars rejasi shabloni, modellardan foydalanish va SI siyosati.")}
{card_link("mustaqil.html", "Mustaqil ta’lim", "54 mavzu va keys-stadi banki", f"Har bir mavzu uchun reja, manbalar va taqdimot talablari; {len(other.KEYS)} ta keys.")}
{card_link("glossariy.html", "1-ilova", "Atamalar lug‘ati", f"{len(other.GLOSS)} ta atama: o‘zbekcha–inglizcha, qisqa ta’rif va mavzu havolasi.")}
{card_link("vositalar.html", "2-ilova", "Dasturiy vositalar", "PhET, Falstad, Python, LTspice, FEMM va onlayn kurslar.")}
</div></div></section>
<section id="model" class="section"><div class="container"><div class="section-head"><div class="eyebrow">O‘quv modeli</div><h2>Har bir mavzu bo‘yicha olti qadam</h2><p class="muted">Nazariya, interaktiv model, hisob va muhokama bitta o‘quv sikliga birlashtirilgan.</p></div><div class="grid grid-3">{st}</div></div></section>
<section id="maruzalar" class="section"><div class="container"><div class="section-head"><div class="eyebrow">Ma’ruzalar · 30 soat</div><h2>15 ta ma’ruza</h2></div><div class="grid grid-3">{lec_cards}</div></div></section>
<section id="amaliy" class="section"><div class="container"><div class="section-head"><div class="eyebrow">Amaliy mashg‘ulotlar · 42 soat</div><h2>21 ta amaliy mashg‘ulot</h2><p class="muted">Har birida ishlangan masalalar, javobli mustaqil masalalar, interaktiv model va Python kodi.</p></div><div class="grid grid-3">{am_cards}</div></div></section>
<section id="simulyatorlar" class="section"><div class="container"><div class="section-head"><div class="eyebrow">Interaktiv modellar</div><h2>Virtual laboratoriya</h2><p class="muted">Quyida ikkita model; qolganlari tegishli mavzu sahifasida. Har bir model ostidagi “Ovozli namoyish” tugmasi uni o‘zi boshqarib tushuntiradi.</p></div>
{sim_block("field", "i1")}<div style="margin-top:1.4rem">{sim_block("ac", "i2")}</div>
<div class="grid grid-4" style="margin-top:1.5rem">{sim_cards}</div></div></section>
<section id="ai-lab" class="section"><div class="container"><div class="section-head"><div class="eyebrow">SI integratsiyasi</div><h2>Prompt generatori</h2><p class="muted">Mavzu va rolni tanlang — tekshiruv qoidalari kiritilgan tayyor prompt hosil bo‘ladi.</p></div><div class="grid grid-2"><div class="card"><label class="control">Mavzu<select id="p-topic">{''.join(f'<option>{strip_tags(L["short"])}</option>' for L in LECT)}</select></label><label class="control" style="margin-top:.8rem">Daraja<select id="p-level"><option>Boshlang‘ich</option><option selected>O‘rta</option><option>Ilg‘or</option></select></label><label class="control" style="margin-top:.8rem">Rol<select id="p-role"><option value="student">talaba</option><option value="teacher">o‘qituvchi</option></select></label><button class="primary" id="gen-prompt" style="margin-top:1rem" type="button">Prompt yaratish</button></div><div class="card"><div class="prompt-box"><button class="secondary copy" type="button" data-copy="p-out">Nusxalash</button><pre id="p-out">Prompt shu yerda ko‘rinadi…</pre></div></div></div></div></section>
<section id="hemis" class="section"><div class="container"><div class="card" style="border-left:4px solid #38bdf8"><div class="eyebrow">Rasmiy jarayonlar</div><h2>Baholash va topshiriqlarni topshirish — HEMIS’da</h2><p class="muted">Ushbu sayt ochiq o‘quv materiallari to‘plami bo‘lib, hisob yaratmaydi va baho qo‘ymaydi. 1-MT (5-hafta), 2-MT (10-hafta), oraliq nazorat testi (12-hafta) va yakuniy nazorat natijalari universitetning HEMIS axborot tizimida belgilangan tartibda yuritiladi.</p></div></div></section>
<section id="muallif" class="section"><div class="container"><div class="card author-card"><img class="author-photo" src="img/author.jpg" width="480" height="566" alt="{AUTHOR_FULL}" loading="lazy"><div class="author-info"><div class="eyebrow">Muallif</div><h2>{AUTHOR_FULL}</h2><p class="author-role">Professor, PhD</p><p class="muted">Qo‘qon davlat universiteti, Fizika va astronomiya kafedrasi. “Elektr va magnetizm” fani o‘quv dasturi tuzuvchisi.</p><p class="muted">Taqrizchilar: R. Rasulov (Farg‘ona davlat universiteti); M. Qo‘chqorov (Qo‘qon davlat universiteti, “Fizika va astronomiya” kafedrasi).</p></div></div></div></section>
</main>""" + footer(sims=True)
    write("index.html", html)


# ---------------- Annotatsiya ----------------
def annot_page():
    toc = [("bib", "Bibliografik ma’lumot"), ("ann", "Annotatsiya (uz/ru/en)"), ("soz", "So‘z boshi"), ("fan", "Fan ma’lumotlari"), ("tn", "Ta’lim natijalari"), ("std", "Xalqaro standartlar"), ("mund", "Mundarija"), ("foyd", "Foydalanish tavsiyalari")]
    S = []
    S.append(sec("bib", 1, "Bibliografik ma’lumot", f"""<p><b>{AUTHOR}</b> Elektr va magnetizm: interaktiv elektron darslik (bakalavriat, 60530700 — Astronomiya). — Qo‘qon: Qo‘qon davlat universiteti, 2026.</p>
<p><b>Taqrizchilar:</b> R. Rasulov (Farg‘ona davlat universiteti); M. Qo‘chqorov (Qo‘qon davlat universiteti, “Fizika va astronomiya” kafedrasi).</p>
<p class="muted">Darslik “Elektr va magnetizm” fanining 2026/2027 o‘quv yili uchun tasdiqlangan o‘quv dasturi (EM1306, o‘quv reja raqami 1.03) asosida tayyorlangan. Litsenziya: CC BY-SA 4.0.</p>"""))
    S.append(sec("ann", 2, "Annotatsiya", """<h3>O‘zbekcha</h3><p>Elektron darslikda umumiy fizikaning “Elektr va magnetizm” bo‘limi fenomenologik darajada bayon etilgan: elektr zaryadi va Kulon qonuni, elektr maydon kuchlanganligi va superpozitsiya, Gauss teoremasi, potensial, dielektriklar va o‘tkazgichlar, kondensatorlar va maydon energiyasi, o‘zgarmas tok qonunlari va Kirxgof qoidalari, tokning magnit maydoni va Bio–Savar–Laplas qonuni, Amper va Lorens kuchlari, moddaning magnit xossalari, elektromagnit induksiya, elektromagnit tebranishlar va to‘lqinlar, Maksvell tenglamalari, o‘zgaruvchan tok. Har bir mavzu nazariy qism, ishlangan misol, interaktiv model, sun’iy intellekt bilan ishlash topshirig‘i, nazorat testi va adabiyotlardan iborat. Darslik bakalavrlar va bo‘lajak fizika o‘qituvchilari uchun mo‘ljallangan.</p>
<div lang="ru"><h3>Русский</h3><p>В электронном учебнике на феноменологическом уровне изложен раздел общей физики «Электричество и магнетизм»: электрический заряд и закон Кулона, напряжённость поля и принцип суперпозиции, теорема Гаусса, потенциал, диэлектрики и проводники, конденсаторы и энергия поля, законы постоянного тока и правила Кирхгофа, магнитное поле тока и закон Био–Савара–Лапласа, силы Ампера и Лоренца, магнитные свойства вещества, электромагнитная индукция, электромагнитные колебания и волны, уравнения Максвелла, переменный ток. Каждая тема содержит теорию, решённый пример, интерактивную модель, задание с ИИ, тест и литературу. Учебник предназначен для бакалавров и будущих учителей физики.</p></div>
<div lang="en"><h3>English</h3><p>This interactive e-textbook presents the Electricity and Magnetism part of general physics at the phenomenological level: electric charge and Coulomb’s law, electric field and superposition, Gauss’s law, potential, dielectrics and conductors, capacitors and field energy, DC circuits and Kirchhoff’s rules, magnetic fields of currents and the Biot–Savart law, the Ampère and Lorentz forces, magnetic properties of matter, electromagnetic induction, electromagnetic oscillations and waves, Maxwell’s equations and alternating current. Each topic includes theory, a worked example, an interactive model, an AI-assisted task, a self-check quiz and references. It is intended for undergraduate students and future physics teachers.</p></div>"""))
    S.append(sec("soz", 3, "So‘z boshi", "<p>Elektromagnit o‘zaro ta’sir atomlarning tuzilishidan tortib elektr stansiyalari, aloqa va kompyuterlargacha bo‘lgan barcha hodisalarni belgilaydi. Bo‘lajak fizika o‘qituvchisi bu qonuniyatlarni nafaqat bilishi, balki ularni tajriba, chizma va hisob orqali o‘quvchilarga tushuntira olishi ham kerak (TN1, TN6).</p><p>Darslik har bir mavzuda bir xil yo‘lni takrorlaydi: hodisa → tajriba → qonun → formula → misol → model. Interaktiv modellar maydon chiziqlari, potensial, zanjirlar va to‘lqinlarni ko‘z bilan ko‘rish imkonini beradi; amaliy mashg‘ulotlardagi masalalar va Python kodlari esa natijani mustaqil tekshirish vositasidir. Barcha natijalar SI birliklarida, fizik doimiylar jadvallari asosida izohlanadi (TN4, TN9).</p>"))
    S.append(sec("fan", 4, "Fan ma’lumotlari", table(["Ko‘rsatkich", "Qiymat"], [["Fan kodi", "EM1306"], ["Ta’lim yo‘nalishi", "60530700 — Astronomiya (bakalavriat), o‘quv reja raqami 1.03"], ["O‘quv yili / semestr", "2026/2027 / 3-semestr"], ["ECTS kreditlar", "6 (1 kredit = 30 soat)"], ["Jami yuklama", "180 soat: ma’ruza 30, amaliy 42, mustaqil ta’lim 108"], ["Haftalik auditoriya soati", "5"], ["Fan turi / tili", "Majburiy / o‘zbek"], ["Baholash", "JN 30 + ON 20 + YaN 50 = 100 ball; saralash 18/12/30"]]) + "<h3>Boshlang‘ich bilimlar (prerekvizitlar)</h3>" + ul(["Mexanika va molekulyar fizika (MM11212)", "Chiziqli algebra va analitik geometriya (CG1106)", "Fizpraktikum (FP11234620)"])))
    S.append(sec("tn", 5, "Ta’lim natijalari (TN1–TN10)", "<p>Fan maqsadi — talabalarda bo‘lajak fizika o‘qituvchisiga zarur darajada umumiy fizikaning “Elektr va magnetizm” bo‘limiga tegishli mavzular bo‘yicha fenomenologik bilim, ko‘nikma va malakalarni shakllantirish. TN1–TN5 — kasbiy kompetensiyalar, TN6–TN10 — ko‘nikmalar.</p>" + table(["Kod", "Natija", "Darslikdagi mavzular"], [[t, TN_TEXT[t], ", ".join([f'<a href="lecture{L["n"]}.html">M{L["n"]}</a>' for L in LECT if t in L["tn"]] + [f'<a href="amaliy{a["n"]}.html">A{a["n"]}</a>' for a in A if t in a["tn"]]) or "Mustaqil ta’lim, keys-stadi"] for t in TN_TEXT])))
    S.append(sec("std", 6, "Xalqaro ta’lim talablariga muvofiqlik", "<p>Darslik quyidagi xalqaro mezonlar asosida loyihalangan. Jadvalda har bir mezon darslikda qanday amalga oshirilgani ko‘rsatilgan.</p>" + table(["Mezon", "Talab", "Darslikda amalga oshirilishi"], [
        ["ECTS Users’ Guide (2015), Bolonya jarayoni", "Ta’lim natijalari va kredit yuklamasi aniq; 1 kredit ≈ 25–30 soat", "6 ECTS = 180 soat; har bir mavzu TN kodlariga bog‘langan; mustaqil ta’lim soatlari mavzular bo‘yicha ko‘rsatilgan"],
        ["Dublin deskriptorlari (1-bosqich — bakalavriat)", "Bilim va tushunish, qo‘llash, mustaqil xulosa, kommunikatsiya, o‘rganish ko‘nikmasi", "Nazariya + misol (bilim), model va hisob (qo‘llash), keys-stadi (xulosa), taqdimot himoyasi (kommunikatsiya)"],
        ["Konstruktiv moslashuv (Biggs) va Blum taksonomiyasi", "Natija → faoliyat → baholash bir-biriga mos", "TN–nazorat matritsasi (baholash sahifasi); “eslash”dan “baholash/yaratish”gacha bo‘lgan topshiriqlar"],
        ["Quality Matters (QM) — oliy ta’lim kurs dizayni rubrikasi", "Aniq maqsadlar, o‘lchanadigan natijalar, ochiq baholash mezonlari, faol o‘rganish, texnologiya, qulaylik", "Har bir sahifada maqsad va natijalar; rubrikalar ochiq; interaktiv modellar va testlar; navigatsiya va mundarija"],
        ["IOP (Institute of Physics) akkreditatsiya talablari — fizika bakalavriati yadrosi", "Elektromagnetizm: elektrostatika, magnitostatika, induksiya, Maksvell tenglamalari, zanjirlar", "M1–M6 elektrostatika; M7–M8 zanjirlar; M9–M12 magnitostatika; M13–M15 induksiya, to‘lqinlar, o‘zgaruvchan tok"],
        ["WCAG 2.2 AA (veb-qulaylik)", "Kontrast, klaviatura bilan boshqarish, matnli muqobil, harakatni kamaytirish", "“Asosiy mazmunga o‘tish” havolasi, fokus belgisi, aria-yorliqlar, prefers-reduced-motion, chop etish uslubi, ovozli o‘qish"],
        ["UNESCO OER tavsiyasi (2019), CC BY-SA 4.0", "Ochiq, qayta foydalaniladigan o‘quv resurslari", "Ochiq litsenziya, ro‘yxatdan o‘tishsiz kirish, manba kodi GitHub’da"],
        ["SI birliklar tizimi (BIPM)", "Kattaliklar va birliklarning bir xil yozilishi", "Barcha misollarda SI birliklari; SGSE (Gauss) sistemasi bilan bog‘lanish M1 da ko‘rsatilgan"],
        ["Akademik halollik va SI dan mas’uliyatli foydalanish", "SI yordamini oshkor qilish, natijani tekshirish", "Har bir ma’ruzada SI topshirig‘i tekshiruv ro‘yxati bilan; baholanadigan ishda prompt ilova qilinadi"],
        ["Xalqaro dasturlar bilan qiyoslash", "Mazmunni yetakchi universitetlar dasturlari bilan solishtirish", "Fan dasturida ko‘rsatilgan University of Manchester BSc Physics dasturlari hamda Purcell, Griffiths, Halliday–Resnick darsliklari asosida mavzular qamrovi"]])
        + '<p class="muted" style="font-size:.85rem">Eslatma: jadval darslik dizayni qaysi mezonlarga yo‘naltirilganini ko‘rsatadi; rasmiy akkreditatsiya yoki sertifikatlashni anglatmaydi.</p>'))
    mund = "<h3>I. Ma’ruzalar</h3>" + ul([f'<a href="lecture{L["n"]}.html">{L["n"]}. {L["title"]}</a>' for L in LECT]) + "<h3>II. Amaliy mashg‘ulotlar</h3>" + ul([f'<a href="amaliy{a["n"]}.html">A{a["n"]}. {a["title"]}</a>' for a in A]) + "<h3>III. Mustaqil ta’lim va baholash</h3>" + ul(['<a href="mustaqil.html">54 ta mustaqil ta’lim mavzusi va keys-stadi banki</a>', '<a href="baholash.html">Baholash rubrikalari va kalkulyator</a>', '<a href="oqituvchi.html">O‘qituvchi uchun qo‘llanma</a>']) + "<h3>Ilovalar</h3>" + ul(['<a href="glossariy.html">1-ilova. Atamalar lug‘ati</a>', '<a href="vositalar.html">2-ilova. Dasturiy vositalar</a>'])
    S.append(sec("mund", 7, "Mundarija", mund))
    S.append(sec("foyd", 8, "Foydalanish tavsiyalari", ul(["<b>Talabaga:</b> ma’ruza sahifasini tartib bilan o‘qing; ishlangan misolni yechimni ochmasdan avval o‘zingiz yeching; modelda bashorat qiling, keyin tekshiring; testni oxirida bajaring.", "<b>O‘qituvchiga:</b> har bir ma’ruza oxirida 80 daqiqalik dars rejasi berilgan; modellarni proyektorda “Ovozli namoyish” rejimida ko‘rsatish mumkin.", "<b>Tinglash:</b> sarlavha yonidagi tugma matnni o‘zbekcha neyron ovozda o‘qiydi; formulalar so‘z bilan aytiladi.", "<b>Chop etish:</b> brauzerda Ctrl+P — interaktiv elementlarsiz toza matn chiqadi (PDF sifatida saqlash mumkin).", "<b>Formulalar</b> KaTeX bilan ko‘rsatiladi va internetsiz ham ishlaydi.", "<b>Rasmiy topshirish</b> faqat HEMIS’da."])))
    html = head("Darslik haqida", "Annotatsiya, fan ma’lumotlari, ta’lim natijalari va xalqaro standartlarga muvofiqlik") + header("annotatsiya.html") + '<main id="main">' + hero([("index.html", "Bosh sahifa"), ("", "Darslik haqida")], "Kirish", "Annotatsiya, so‘z boshi va mundarija", "Bibliografik ma’lumot, uch tildagi annotatsiya, fan ma’lumotlari, ta’lim natijalari va xalqaro ta’lim talablariga muvofiqlik.", [("c", "6 ECTS"), ("", "180 soat"), ("g", "TN1–TN10")]) + doc(toc, S) + "</main>" + footer()
    write("annotatsiya.html", html)


# ---------------- Mustaqil ta'lim ----------------
def mustaqil_page():
    items = []
    for i, (t, plan, src, hrs) in enumerate(other.MT, 1):
        srcs = "; ".join(f"[{s}]" for s in dict.fromkeys(src))
        items.append(f'<details class="mt-item"><summary><span class="badge">MT-{i:02d}</span> {t} <span class="muted" style="margin-left:auto;font-weight:500">{hrs} soat</span></summary><div class="body"><b>Taqdimot rejasi:</b>{ul(plan)}<p class="muted">Asosiy manbalar: {srcs} (fan dasturi ro‘yxati) va <a href="glossariy.html">lug‘at</a>. Hajmi: 10–12 slayd, kamida bitta chizma yoki grafik (o‘zingiz qurgan), kamida 3 manba.</p></div></details>')
    keys = "".join(f'<div class="example"><div class="ex-h">{t}</div><div class="ex-b"><p>{d}</p><p class="tn">{", ".join(tn)}</p></div></div>' for t, d, tn in other.KEYS)
    toc = [("umumiy", "Umumiy talablar"), ("mavzular", "54 ta mavzu"), ("taqdimot", "1-MT: taqdimot talablari"), ("keys", "2-MT: keys-stadi banki"), ("halollik", "Akademik halollik")]
    S = [sec("umumiy", 1, "Umumiy talablar", table(["Ko‘rsatkich", "Qiymat"], [["Jami hajm", "108 soat (54 mavzu × 2 soat)"], ["1-MT", "Taqdimot va himoya — 5 ball, 5-hafta. Elektr va magnetizm mavzularini mustaqil o‘rganish va yoritish (54 mavzudan biri)"], ["2-MT", "Keys-stadi tahlili va yechimi — 5 ball, 10-hafta (HEMIS’ga yuklash)"], ["Mavzuni tanlash", "O‘qituvchi tomonidan guruh ro‘yxati bo‘yicha taqsimlanadi (bir mavzu — bir talaba)"]])),
         sec("mavzular", 2, "Mustaqil ta’lim mavzulari", f'<input class="search" type="text" placeholder="Mavzu bo‘yicha qidirish…" data-filter=".mt-item" data-count="mt-count" aria-label="Mavzu qidirish"><p class="muted" id="mt-count">{len(other.MT)} ta natija</p><div class="acc">{"".join(items)}</div>'),
         sec("taqdimot", 3, "1-MT: taqdimot va himoya talablari (5 ball)", table(["Daraja", "Tavsif (fan dasturi bo‘yicha)"], [["Yuqori", "Qo‘shimcha ilmiy-metodik adabiyotlardan foydalanib mukammal taqdimot tayyorlagan; fizik jarayonlar, formulalar va chizmalarni mantiqiy izchil bayon qilib, himoyada mustaqil, erkin fikr bildiradi."], ["Yetarli", "Mavzu asosan yoritilgan, taqdimot tushunarli, ammo asosiy darsliklar bilan cheklangan; himoyada tayyor matnga qaram, ayrim fizik atamalar yoki formulalarni tushuntirishda kichik noaniqliklar bor."], ["Minimal", "Taqdimot yuzaki, ko‘chirmachilikka yo‘l qo‘yilgan, slaydlarda kerakli vizual (chizma, diagramma) yo‘q, mavzuni tushuntira olmaydi."], ["Erishilmagan", "Taqdimot tayyorlanmagan yoki 5-hafta muddatida HEMIS’ga yuklanmagan."]]) + "<h3>Slaydlar tuzilishi (tavsiya)</h3>" + ul(["Sarlavha, muallif, guruh", "Mavzuning nazariy fizikadagi o‘rni", "Hodisa va tajriba", "Qonun, formula va uning fizik ma’nosi", "Grafik yoki sonli modellashtirish natijasi (o‘zingiz qurgan)", "Xulosa va 3–5 manba"], True)),
         sec("keys", 4, "2-MT: keys-stadi banki (5 ball)", f'<p>Har bir talaba bitta keysni tanlaydi (yoki o‘qituvchi tayinlaydi). Yechim 3–5 betlik hisobot: muammo tahlili → fizik model va qonuniyatlar → hisob (SI da) → kamida ikki yechim variantini taqqoslash → xulosa.</p>{keys}<h3>Baholash mezoni (fan dasturi bo‘yicha)</h3>' + table(["Daraja", "Tavsif"], [["Yuqori", "Muammoli fizik vaziyat chuqur tahlil qilingan, elektromagnit qonuniyatlari asosida to‘liq va ijodiy yechim taklif etilgan, xulosalar ilmiy asoslangan."], ["Yetarli", "Asosiy fizik qonunlar qisman to‘g‘ri qo‘llangan, yechimlarni asoslashda yoki formulalarni amaliyotga bog‘lashda kamchiliklar bor, mustaqil yondashuv yetishmaydi."], ["Minimal", "Muammoli vaziyatning fizik mohiyati to‘liq anglanmagan, aniq yechim yo‘q, umumiy so‘zlar bilan cheklangan."], ["Erishilmagan", "Keys bajarilmagan yoki 10-hafta muddatida topshirilmagan."]])),
         sec("halollik", 5, "Akademik halollik va SI", ul(["Taqdimot va keys yechimi talabaning o‘z ishi bo‘lishi kerak; boshqa manbalardan olingan rasm va matnlar havola bilan beriladi.", "SI vositalaridan foydalanilgan bo‘lsa, ishga qisqa ilova qo‘shiladi: qaysi vosita, qaysi prompt, natija qanday tekshirildi.", "SI yozgan matnni o‘zgartirmasdan topshirish va manbalarni uydirish qoidabuzarlik hisoblanadi."]))]
    html = head("Mustaqil ta’lim", "54 ta mustaqil ta’lim mavzusi, taqdimot talablari va keys-stadi banki") + header("mustaqil.html") + '<main id="main">' + hero([("index.html", "Bosh sahifa"), ("", "Mustaqil ta’lim")], "Mustaqil ta’lim · 108 soat", "Mustaqil ta’lim topshiriqlari", "Fan dasturidagi 54 ta mavzu bo‘yicha taqdimot yo‘riqnomalari va elektrotexnik muammolarga oid keys-stadilar.", [("c", "54 mavzu"), ("a", "1-MT: 5-hafta"), ("a", "2-MT: 10-hafta")]) + doc(toc, S) + "</main>" + footer()
    write("mustaqil.html", html)


# ---------------- Baholash ----------------
def baholash_page():
    toc = [("tartib", "Umumiy tartib"), ("matritsa", "TN–nazorat matritsasi"), ("jn", "Joriy nazorat (30)"), ("on", "Oraliq nazorat (20)"), ("yn", "Yakuniy nazorat (50)"), ("baho", "Yakuniy baho"), ("kalk", "Baho kalkulyatori")]
    mat = table(["TN", "Natija", "JN", "ON", "YaN"], [[t, TN_TEXT[t]] + [f'<span class="{"plus" if v == "+" else "minus"}">{v}</span>' for v in TN_MATRIX[t]] for t in TN_TEXT])
    S = [sec("tartib", 1, "Baholashning umumiy tartibi", table(["Nazorat turi", "Maksimal ball", "Saralash bali", "Vosita"], [["Joriy nazorat (JN)", "30", "18", "1-MT: taqdimot va himoya (5); DF: fizik masalalarni tahlil qilish va yechish modelini tuzish — darsdagi faollik (20); 2-MT: keys-stadi (5)"], ["Oraliq nazorat (ON)", "20", "12", "12-hafta, HEMIS’da 20 savolli test"], ["Yakuniy nazorat (YaN)", "50", "30", "Yozma ish: 3 nazariy savol + 1 amaliy keys (Kulon, Bio–Savar–Laplas, Maksvell qonuniyatlari tatbiqi)"], ["Jami", "100", "—", ""]]) + '<div class="callout warn"><b>Muhim</b>Har bir nazorat turidan ajratilgan ballning kamida 60 % i to‘planishi shart. Bir nazorat turidagi yetishmagan ball boshqasidagi yuqori ball hisobiga qoplanmaydi.</div>'),
         sec("matritsa", 2, "Ta’lim natijasi — baholash vositasi muvofiqligi", mat),
         sec("jn", 3, "Joriy nazorat rubrikasi — 30 ball", table(["Mezon", "Ball", "Yuqori", "Yetarli", "Minimal", "Erishilmagan"], [
             ["1-MT: taqdimot va himoya", "5", "Qo‘shimcha adabiyot bilan mukammal taqdimot; fizik jarayonlar, formulalar va chizmalarni izchil bayon qiladi", "Tushunarli, lekin darsliklar bilan cheklangan; himoyada matnga qaram", "Yuzaki; chizma va formulalar yo‘q", "Tayyorlanmagan yoki 5-haftada yuklanmagan"],
             ["DF: darsdagi faollik (elektrostatika, tok va magnetizm masalalari, sxemalar)", "20", "Kulon, Gauss, Om, Kirxgof, Bio–Savar–Laplas qonunlarini aniq tanlaydi, chizma va sxemalarni bexato chizadi, yechish algoritmini mustaqil tuzadi", "Asosiy qonuniyatlarni yozadi, tarmoqlangan zanjirlar va murakkab sxemalarda yordamga tayanadi", "Faqat sodda, bitta formulali masalalar; sxemani mustaqil tuza olmaydi", "Shartni tushunmaydi, sxema chiza olmaydi"],
             ["2-MT: keys-stadi", "5", "Chuqur tahlil, to‘g‘ri model va asoslangan yechim", "Qisman to‘g‘ri, formulalarni amaliyotga bog‘lashda kamchilik", "Mohiyat anglanmagan, umumiy so‘zlar", "Bajarilmagan yoki 10-haftada topshirilmagan"]])),
         sec("on", 4, "Oraliq nazorat rubrikasi — 20 ball", table(["Daraja", "To‘g‘ri javoblar (20 tadan)", "Tavsif"], [["Yuqori", "18–20 (90–100 %)", "Elektr va magnetizm qonuniyatlari mohiyatini to‘liq tushunadi, mustaqil mushohada yuritadi"], ["Yetarli", "14–17 (70–89,9 %)", "Mohiyatni tushunadi, murakkab hisoblarda xato qiladi"], ["Minimal", "12–13 (60–69,9 %)", "Umumiy tasavvurga ega, sodda savollarni yechadi"], ["Erishilmagan", "0–11 (0–59,9 %)", "Dastur o‘zlashtirilmagan"]]) + '<p class="muted">Tayyorgarlik uchun har bir ma’ruzadagi nazorat testlaridan foydalaning (jami 150 savol).</p>'),
         sec("yn", 5, "Yakuniy nazorat rubrikasi — 50 ball", table(["Topshiriq", "Ball", "Yuqori", "Yetarli", "Minimal", "Erishilmagan"], [["Nazariy savollar (1–3), har biri 10 ball: mohiyat (4) + atamalar (3) + mantiqiy bayon (3)", "30", "27–30", "21–26", "18–20", "0–17"], ["Keys topshirig‘i (4-savol): fizik qonuniyatlarni (Kulon, Bio–Savar–Laplas, Maksvell tenglamalari) muammoli vaziyatga tatbiq etish va masalani yechish", "20", "18–20", "14–17", "12–13", "0–11"]]) + "<h3>Namunaviy keys (4-savol)</h3><p>Uzunligi 50 sm, 1000 o‘ramli, kesimi 10 sm² havo o‘zakli solenoid EYuK 12 V, ichki qarshiligi 1 Ω manbaga 5 Ω rezistor orqali ulanadi. 1) Barqaror tok va solenoid ichidagi induksiyani toping. 2) Induktivlik va vaqt doimiysini hisoblang. 3) Ulangandan 1 ms keyingi tok va magnit maydon energiyasini aniqlang. 4) Zanjir uzilganda nima uchun uchqun chiqishini Lens qoidasi bilan tushuntiring. (Yechim yo‘nalishi: <a href=\"amaliy18.html\">A18</a>, <a href=\"lecture13.html\">M13</a>.)</p>"),
         sec("baho", 6, "Fan bo‘yicha bahoni aniqlash", table(["Jami ball", "Baho", "Tavsif"], [["90–100", "A’lo", "Ta’lim natijalarini yuqori darajada egallagan; bilimni mustaqil tahlil qiladi va yangi vaziyatlarda qo‘llaydi."], ["70–89,9", "Yaxshi", "Asosiy natijalarni barqaror egallagan; amaliy vaziyatlarda qo‘llaydi."], ["60–69,9", "Qoniqarli", "Minimal natijalarga erishgan, tahlil va asoslashda cheklovlar bor."], ["0–59,9", "Qoniqarsiz", "Minimal natijalarga yetarli darajada erishmagan."]])),
         sec("kalk", 7, "Baho kalkulyatori", """<div id="grade-calc" class="two"><div>
<label class="control">1-MT taqdimot (0–5) <output data-for="jn-mt1"></output><input id="jn-mt1" type="range" min="0" max="5" step="0.5" value="4"></label>
<label class="control">DF darsdagi faollik (0–20) <output data-for="jn-df"></output><input id="jn-df" type="range" min="0" max="20" step="0.5" value="15"></label>
<label class="control">2-MT keys-stadi (0–5) <output data-for="jn-mt2"></output><input id="jn-mt2" type="range" min="0" max="5" step="0.5" value="4"></label>
<label class="control">Oraliq nazorat (0–20) <output data-for="on"></output><input id="on" type="range" min="0" max="20" step="1" value="15"></label>
<label class="control">Yakuniy nazorat (0–50) <output data-for="yn"></output><input id="yn" type="range" min="0" max="50" step="1" value="38"></label></div>
<div class="card kpi"><div class="l">Jami</div><div class="calc-out" id="calc-total"></div><div class="l" style="margin-top:.6rem">Baho</div><div class="v" id="calc-grade" style="font-size:1.3rem"></div><p class="muted" id="calc-detail" style="font-size:.8rem"></p></div></div><p class="muted" style="font-size:.85rem">Kalkulyator ma’lumot uchun; rasmiy ball HEMIS’da hisoblanadi.</p>""")]
    html = head("Baholash", "JN, ON, YaN rubrikalari, TN–nazorat matritsasi va baho kalkulyatori") + header("baholash.html") + '<main id="main">' + hero([("index.html", "Bosh sahifa"), ("", "Baholash")], "Baholash · 100 ball", "Talaba bilimini baholash mezonlari", "Fan dasturidagi baholash tartibi, rubrikalar va ta’lim natijalari bilan muvofiqlik.", [("c", "JN 30 / 18"), ("c", "ON 20 / 12"), ("c", "YaN 50 / 30")]) + doc(toc, S) + "</main>" + footer()
    write("baholash.html", html)


# ---------------- O'qituvchi qo'llanmasi ----------------
def teacher_page():
    rows = [[str(w), f'<a href="lecture{m}.html">M{m}</a>: {strip_tags(LECT[m-1]["short"])}', "<br>".join(f'<a href="amaliy{a}.html">A{a}</a>: {A[a-1]["title"][:55]}{"…" if len(A[a-1]["title"]) > 55 else ""}' for a in am), f"{2 + 2 * len(am)}", note or "—"] for w, m, am, note in other.CAL]
    toc = [("taqvim", "15 haftalik taqvim"), ("shablon", "Dars rejasi shabloni"), ("model", "Modellardan foydalanish"), ("si", "SI siyosati"), ("baholash", "Baholashni tashkil etish"), ("moslash", "Darslikni moslashtirish")]
    S = [sec("taqvim", 1, "15 haftalik o‘quv taqvimi (o‘rtacha haftada 5 soat)", table(["Hafta", "Ma’ruza (2 soat)", "Amaliy mashg‘ulotlar (har biri 2 soat)", "Soat", "Nazorat / izoh"], rows) + '<p class="muted" style="font-size:.85rem">Jami: ma’ruza 30 soat + amaliy 42 soat = 72 soat auditoriya. Tartib fan dasturidagi M1–M15 va A1–A21 ketma-ketligiga mos; 6 ta haftada ikkitadan amaliy mashg‘ulot o‘tkaziladi.</p>'),
         sec("shablon", 2, "Ma’ruza va amaliy dars rejasi shabloni", "<h3>Ma’ruza (80 daqiqa)</h3>" + table(["Vaqt", "Bosqich", "O‘qituvchi", "Talaba"], [["0–10", "Kirish", "Blits-so‘rov, muammoli savol", "Javob beradi, bashorat qiladi"], ["10–45", "Nazariya", "Formulalarni keltirib chiqaradi", "Konspekt, savollar"], ["45–60", "Model", "Simulyatorni namoyish qiladi", "Bashorat → kuzatish → izoh"], ["60–72", "Misol", "Masalani beradi, yo‘naltiradi", "Juftlikda yechadi"], ["72–80", "Yakun", "Test, xato tushunchalar", "O‘z-o‘zini tekshiradi"]]) + "<h3>Amaliy mashg‘ulot (80 daqiqa)</h3>" + table(["Vaqt", "Bosqich"], [["0–10", "Nazariy asosni takrorlash, formulalar ro‘yxati"], ["10–30", "Ishlangan masalalarni birga tahlil qilish"], ["30–60", "Mustaqil masalalar (javoblar yashirin) — DF bahosi uchun kuzatish"], ["60–75", "Python kodi yoki interaktiv model bilan tekshirish"], ["75–80", "Nazorat savollari, uyga vazifa"]])),
         sec("model", 3, "Interaktiv modellardan foydalanish", ul(["<b>Bashorat → kuzatish → tushuntirish (POE):</b> parametrni o‘zgartirishdan oldin talabalardan natijani bashorat qilishni so‘rang.", "<b>Ishlangan misol bilan tekshirish:</b> misoldagi qiymatlarni modelga kiriting — natija mos kelishi kerak.", "<b>Cheklovlarni muhokama qiling:</b> modellar soddalashtirilgan (nuqtaviy zaryadlar, ideal elementlar, chet effektlarsiz kondensator); qaysi effektlar hisobga olinmaganini so‘rang.", "<b>Proyektor uchun:</b> brauzerni to‘liq ekranga o‘tkazing (F11); modellar internetsiz ham ishlaydi.", "<b>Chop etish:</b> sahifa chop etilganda modellar yashiriladi.", "<b>Ovozli namoyish:</b> model ostidagi “Ovozli namoyish” tugmasi parametrlarni o‘zi bosqichma-bosqich o‘zgartirib, natijani ovoz va yozuv bilan tushuntiradi; tugagach boshqaruv talabalarga o‘tadi.", "<b>Tinglash:</b> mavzu sarlavhasi yonidagi tugma nazariya va misolni o‘qiydi, formulalarni so‘z bilan aytadi. O‘qish paytida pastda boshqaruv paneli chiqadi: pauza / davom etish, oldingi va keyingi xatboshi, to‘xtatish (Esc). Istalgan xatboshini bosing — “Shu yerdan o‘qish” tugmasi chiqadi. O‘zbekcha matnlar oldindan tayyorlangan neyron ovozda (MP3) o‘qiladi, shuning uchun barcha kompyuter va telefonlarda bir xil tabiiy eshitiladi; ruscha va inglizcha tarjimada brauzer ovozi ishlatiladi.", "<b>Til:</b> yuqoridagi UZ / RU / EN tugmalari butun saytni (testlar bilan birga) Google Translate orqali tarjima qiladi; tanlov boshqa sahifalarda ham saqlanadi."])),
         sec("si", 4, "Sun’iy intellekt bo‘yicha kurs siyosati (tavsiya)", ul(["SI tushuntirish, kod qoralamasi va hisobni tekshirish uchun ruxsat etiladi.", "Baholanadigan ishda SI ishlatilgan bo‘lsa, prompt va tekshiruv natijasi ilova qilinadi.", "SI bergan son va formulalar darslik yoki mustaqil hisob (masalan, Python) bilan tasdiqlanishi shart.", "Yozma nazoratlarda (ON, YaN) SI dan foydalanish taqiqlanadi.", "Matnni “insonlashtiruvchi” xizmatlardan o‘tkazish va manbalarni uydirish qoidabuzarlik hisoblanadi."])),
         sec("baholash", 5, "Baholashni tashkil etish bo‘yicha tavsiyalar", ul(["<b>DF (20 ball):</b> har amaliy mashg‘ulotda 2–3 talabani doskada yoki mustaqil masala bo‘yicha kuzating: sxema chizish, vektor diagramma qurish, natijani SI da izohlash; 4 darajali rubrikadan foydalaning (amaliy sahifalarining 8-bo‘limi).", "<b>1-MT:</b> mavzularni 1-haftada taqsimlang; himoya 5–7 daqiqa + 3 daqiqa savol.", f"<b>2-MT:</b> keys-stadi bankidan ({len(other.KEYS)} ta) tanlov; hisobot 3–5 bet.", "<b>ON:</b> ma’ruzalardagi nazorat testlari savol banki uchun namuna bo‘la oladi (HEMIS uchun yangi variantlar tuzish tavsiya etiladi).", "<b>YaN:</b> namunaviy keys baholash sahifasida."])),
         sec("moslash", 6, "Darslikni moslashtirish va yangilash", "<p>Sayt statik HTML/CSS/JS fayllaridan iborat va GitHub Pages’da ishlaydi. Mazmun <code>gen/</code> papkasidagi Python fayllarida saqlanadi: <code>lectures_a.py</code>, <code>lectures_b.py</code> (ma’ruzalar), <code>amaliy.py</code> (21 amaliy mashg‘ulot), <code>other.py</code> (mustaqil ta’lim, lug‘at, vositalar, taqvim), <code>tours.py</code> (ovozli namoyishlar). Matnni o‘zgartirgach, <code>python3 gen/build.py .</code> buyrug‘i barcha sahifalarni qayta yaratadi; GitHub’ga yuklangach, ovozli MP3 fayllar avtomatik yangilanadi. Simulyatorlar <code>js/sims.js</code> faylida.</p>")]
    html = head("O‘qituvchi uchun", "15 haftalik taqvim, dars rejasi shabloni, modellar va SI siyosati") + header("oqituvchi.html") + '<main id="main">' + hero([("index.html", "Bosh sahifa"), ("", "O‘qituvchi uchun")], "Metodik qo‘llanma", "O‘qituvchi uchun qo‘llanma", "Fan dasturi asosidagi haftalik taqvim, dars shablonlari, baholashni tashkil etish va darslikni yangilash bo‘yicha ko‘rsatmalar.", [("a", "15 hafta"), ("", "72 soat auditoriya")]) + doc(toc, S) + "</main>" + footer()
    write("oqituvchi.html", html)


# ---------------- Lug'at ----------------
def gloss_page():
    rows = "".join(f'<tr class="g-row"><td><b>{u}</b></td><td><i lang="en">{e}</i></td><td>{d}</td><td><a href="lecture{m}.html">M{m}</a></td></tr>' for u, e, d, m in sorted(other.GLOSS, key=lambda x: x[0].lower()))
    body = f'<input class="search" type="text" placeholder="Atama qidirish (o‘zbekcha yoki inglizcha)…" data-filter=".g-row" data-count="g-count" aria-label="Atama qidirish"><p class="muted" id="g-count">{len(other.GLOSS)} ta natija</p><div class="tw"><table class="t"><thead><tr><th>Atama</th><th>English</th><th>Ta’rif</th><th>Mavzu</th></tr></thead><tbody>{rows}</tbody></table></div>'
    html = head("Atamalar lug‘ati", "Elektr va magnetizm atamalari: o‘zbekcha–inglizcha lug‘at") + header("glossariy.html") + '<main id="main">' + hero([("index.html", "Bosh sahifa"), ("", "Lug‘at")], "1-ilova", "Atamalar lug‘ati", "O‘zbekcha atama, inglizcha muqobili, qisqa ta’rif va u o‘rganiladigan ma’ruza.", [("c", f"{len(other.GLOSS)} atama")]) + f'<div class="container" style="padding:2rem 0 3rem"><section class="doc-sec">{body}</section></div></main>' + footer()
    write("glossariy.html", html)


def tools_page():
    secs, toc = [], []
    for i, (cat, items) in enumerate(other.TOOLS, 1):
        rows = [[f'<a href="{u}" rel="noopener" target="_blank">{n}</a>' if u else f"<b>{n}</b>", d, a] for n, u, d, a in items]
        secs.append(sec(f"t{i}", i, cat, table(["Vosita", "Darslikda qo‘llanilishi", "Kirish"], rows)))
        toc.append((f"t{i}", cat))
    secs.append('<div class="callout info"><b>Eslatma</b>Tariflar va litsenziya shartlari o‘zgarib turadi — foydalanishdan oldin rasmiy saytni tekshiring. Darslikdagi barcha topshiriqlarni bepul vositalar (PhET, Falstad, Python, Colab, LTspice, FEMM) bilan bajarish mumkin.</div>')
    html = head("Dasturiy vositalar", "PhET, Falstad, Python, LTspice, FEMM va onlayn kurslar") + header("vositalar.html") + '<main id="main">' + hero([("index.html", "Bosh sahifa"), ("", "Vositalar")], "2-ilova", "Dasturiy vositalar va ularning bepul muqobillari", "Interaktiv tajribalar, hisoblash va modellashtirish vositalari hamda darslik topshiriqlari uchun tavsiyalar.", []) + doc(toc, secs) + "</main>" + footer()
    write("vositalar.html", html)


def notfound():
    html = head("Sahifa topilmadi", "404") + header() + '<main id="main">' + hero([("index.html", "Bosh sahifa")], "404", "Sahifa topilmadi", "So‘ralgan sahifa mavjud emas. Bosh sahifaga qayting.", []) + "</main>" + footer()
    write("404.html", html)


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for i, L in enumerate(LECT): lecture_page(L, i)
    for a in A: amaliy_page(a)
    index_page(); annot_page(); mustaqil_page(); baholash_page(); teacher_page(); gloss_page(); tools_page(); notfound()
    print("OK:", len(os.listdir(OUT)), "fayl/papka ->", os.path.abspath(OUT))
