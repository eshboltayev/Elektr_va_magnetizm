"""M1–M8 ma'ruzalar mazmuni (Elektr va magnetizm, fan dasturi EM1306)."""

L = []

L.append(dict(
 n=1, short=r"Elektr zaryadlari. Kulon qonuni", sim="coulomb", refs=[1, 2, 4], intl=["purcell", "halliday", "feynman2"], tn=["TN2", "TN3", "TN7"],
 title=r"Elektrostatik maydon va uning xarakteristikalari. Elektr zaryadlari. Kulon qonuni",
 goal=r"Elektromagnit o‘zaro ta’sirning tabiatini, elektr zaryadining asosiy xossalarini (diskretlik, saqlanish, invariantlik), Kulon qonunini va elektrostatikadagi birliklar sistemalarini o‘rganish.",
 outcomes=[r"elektromagnit maydonni elektromagnit o‘zaro ta’sirning moddiy eltuvchisi sifatida izohlaydi;",
           r"zaryadning kvantlanishi va saqlanish qonunini misollar bilan tushuntiradi;",
           r"Kulon qonunini vektor ko‘rinishda yozadi va muhitdagi kuchni hisoblaydi;",
           r"SI va SGSE sistemalarida Kulon qonuni ko‘rinishini taqqoslaydi."],
 plan=["Elektromagnit o‘zaro ta’sir va maydon", "Elektr zaryadi va uning xossalari", "Zaryadning saqlanish qonuni", "Kulon qonuni", "Elektrostatikada birliklar sistemasi"],
 terms=["elektr zaryadi", "elementar zaryad", "zaryadning saqlanish qonuni", "nuqtaviy zaryad", "Kulon qonuni", "dielektrik singdiruvchanlik"],
 theory=[
  ("Elektromagnit maydon — o‘zaro ta’sir eltuvchisi", r"""<p>Zaryadlar bir-biriga bevosita emas, balki o‘zlari hosil qilgan <b>elektromagnit maydon</b> orqali ta’sir qiladi. Maydon — materiyaning alohida turi: u energiya, impuls va chekli tezlik \(c\approx3\cdot10^8\) m/s bilan tarqalish xossasiga ega. Qo‘zg‘almas zaryadlar maydoni <b>elektrostatik maydon</b> deyiladi. Elektromagnit o‘zaro ta’sir atom va molekulalarning tuzilishini, kimyoviy bog‘lanishni, ishqalanish va elastiklik kuchlarini belgilaydi.</p>"""),
  ("Elektr zaryadi va uning xossalari", r"""<ul><li><b>Ikki xil ishorali:</b> musbat va manfiy; bir xil ishorali zaryadlar itariladi, har xillari tortishadi.</li><li><b>Diskretlik:</b> har qanday zaryad elementar zaryadga karrali: \(q=Ne\), \(e=1{,}602\cdot10^{-19}\) C (Milliken tajribasi).</li><li><b>Saqlanish qonuni:</b> yopiq sistemada zaryadlarning algebraik yig‘indisi o‘zgarmaydi: \(\sum q_i=\text{const}\).</li><li><b>Relyativistik invariantlik:</b> zaryad sanoq sistemasiga va tezlikka bog‘liq emas.</li></ul>
<p>Jismlar ishqalanish, elektrostatik induksiya yoki kontakt orqali zaryadlanadi; zaryad elektroskop va elektrometr bilan aniqlanadi.</p>"""),
  ("Kulon qonuni", r"""<p>Vakuumdagi ikki qo‘zg‘almas nuqtaviy zaryadning o‘zaro ta’sir kuchi zaryadlar ko‘paytmasiga to‘g‘ri, masofa kvadratiga teskari proporsional va ularni tutashtiruvchi to‘g‘ri chiziq bo‘ylab yo‘nalgan (1785):</p>
$$\vec F_{12}=k\frac{q_1q_2}{r^2}\frac{\vec r_{12}}{r},\qquad k=\frac{1}{4\pi\varepsilon_0}=8{,}988\cdot10^9\ \frac{\text{N·m}^2}{\text{C}^2},\quad\varepsilon_0=8{,}854\cdot10^{-12}\ \text{F/m}.$$
<p>Bir jinsli dielektrik muhitda kuch \(\varepsilon\) marta kamayadi: \(F=\dfrac{|q_1q_2|}{4\pi\varepsilon_0\varepsilon r^2}\). Kulon kuchlari Nyutonning uchinchi qonuniga bo‘ysunadi va superpozitsiya prinsipi bo‘yicha qo‘shiladi.</p>"""),
  ("Birliklar sistemasi", r"""<p><b>SI</b> da zaryad birligi — kulon: \(1\ \text{C}=1\ \text{A·s}\); Kulon qonunida \(k=1/4\pi\varepsilon_0\). <b>SGSE</b> (Gauss) sistemasida \(k=1\) deb olinadi: \(F=q_1q_2/r^2\), zaryad birligi \(1\ \text{SGSE}_q\approx3{,}336\cdot10^{-10}\) C. Nazariy fizikada Gauss sistemasi, muhandislik va o‘quv jarayonida SI qo‘llaniladi; ikkala sistemadagi formulalarni bir-biriga o‘tkaza bilish kerak.</p>""")],
 example=(r"Kulon kuchi va gravitatsiya",
  r"1) \(q_1=2\) mkC va \(q_2=-3\) mkC zaryadlar vakuumda \(r=30\) sm masofada turibdi. O‘zaro ta’sir kuchini toping; ular suvga (\(\varepsilon=81\)) tushirilsa-chi? 2) Vodorod atomidagi elektron va proton uchun elektr va gravitatsion tortishish kuchlari nisbati?",
  r"1) \(F=8{,}988\cdot10^9\cdot2\cdot10^{-6}\cdot3\cdot10^{-6}/0{,}09=0{,}599\) N (tortishish). Suvda \(F/81=7{,}4\) mN. 2) \(F_e/F_g=ke^2/(Gm_em_p)=2{,}27\cdot10^{39}\) — masofaga bog‘liq emas; atomlarda gravitatsiyani hisobga olmaslik mumkin."),
 simtask=[r"Misoldagi qiymatlarni o‘rnatib, kuch 0,6 N ekanini tekshiring.",
          r"Masofani 2 marta oshiring — kuch necha marta kamaydi? Grafikda \(1/r^2\) bog‘liqlikni ko‘ring.",
          r"Ikkinchi zaryad ishorasini o‘zgartiring: kuch yo‘nalishi qanday o‘zgaradi? Muhit singdiruvchanligini oshirib ko‘ring."],
 mistakes=[(r"“Katta zaryad kichik zaryadga kattaroq kuch bilan ta’sir qiladi.”", r"Nyutonning uchinchi qonuni: \(\vec F_{12}=-\vec F_{21}\) — kuchlar moduli teng."),
           (r"“Zaryad har qanday qiymatda bo‘lishi mumkin.”", r"Erkin zaryad elementar zaryadga karrali: \(q=Ne\)."),
           (r"“Kulon qonuni har qanday jismlar uchun to‘g‘ri.”", r"Faqat nuqtaviy (yoki sferik simmetrik) zaryadlar uchun; cho‘ziq jismlar uchun integrallash kerak.")],
 ai=r"""Sen umumiy fizika bo‘yicha sokratik repetitorsan. Mavzu: Kulon qonuni.
Javobni darhol berma, avval 2 ta yo‘naltiruvchi savol ber. Menga uchta zaryad (uchburchak uchlarida) uchun natijaviy kuchni vektorlar yordamida topishni bosqichma-bosqich o‘rgat. Formulalarni LaTeX’da yoz, SI birliklarini ko‘rsat.""",
 quiz=[
  (r"Elementar zaryad qiymati:", [r"\(1{,}602\cdot10^{-19}\) C", r"\(9{,}109\cdot10^{-31}\) C", r"\(6{,}02\cdot10^{23}\) C", r"\(1{,}6\cdot10^{-27}\) C"], 0, "Milliken tajribasi."),
  (r"Masofa 3 marta oshsa, Kulon kuchi:", ["9 marta kamayadi", "3 marta kamayadi", "9 marta ortadi", "o‘zgarmaydi"], 0, r"\(F\propto1/r^2\)."),
  (r"\(k=1/4\pi\varepsilon_0\) qiymati:", [r"\(8{,}99\cdot10^9\) N·m²/C²", r"\(8{,}85\cdot10^{-12}\) F/m", r"\(6{,}67\cdot10^{-11}\) N·m²/kg²", r"\(4\pi\cdot10^{-7}\) H/m"], 0, "SI dagi Kulon doimiysi."),
  (r"Zaryadlar suvga (\(\varepsilon=81\)) tushirilsa, kuch:", ["81 marta kamayadi", "9 marta kamayadi", "81 marta ortadi", "o‘zgarmaydi"], 0, r"\(F=F_0/\varepsilon\)."),
  (r"Zaryadning saqlanish qonuni:", ["yopiq sistemada zaryadlar yig‘indisi o‘zgarmaydi", "zaryad tezlikka bog‘liq", "zaryad faqat musbat bo‘ladi", "zaryad massaga proporsional"], 0, "Fundamental qonun."),
  (r"1 C zaryadda nechta elementar zaryad bor?", [r"\(6{,}24\cdot10^{18}\)", r"\(1{,}6\cdot10^{19}\)", r"\(6{,}02\cdot10^{23}\)", r"\(10^{12}\)"], 0, r"\(1/1{,}602\cdot10^{-19}\)."),
  (r"Elektron va proton uchun \(F_e/F_g\) taxminan:", [r"\(10^{39}\)", r"\(10^{9}\)", r"\(10^{20}\)", r"\(10^{3}\)"], 0, r"\(2{,}27\cdot10^{39}\)."),
  (r"Gauss (SGSE) sistemasida Kulon qonuni:", [r"\(F=q_1q_2/r^2\)", r"\(F=q_1q_2/4\pi r^2\)", r"\(F=4\pi q_1q_2/r^2\)", r"\(F=q_1q_2/\varepsilon_0r^2\)"], 0, r"\(k=1\)."),
  (r"Elektrostatik maydon hosil qiladi:", ["qo‘zg‘almas zaryadlar", "o‘zgarmas tok", "harakatdagi magnit", "o‘zgaruvchan tok"], 0, "Ta’rif."),
  (r"Kulon kuchi yo‘nalishi:", ["zaryadlarni tutashtiruvchi to‘g‘ri chiziq bo‘ylab", "unga perpendikulyar", "har doim pastga", "tezlik bo‘ylab"], 0, "Markaziy kuch.")],
 blits=["Qog‘oz parchalari nima uchun taroqqa tortiladi?", "Zaryad kvantlanmaganda dunyo qanday bo‘lardi?", "Nima uchun atomlarda gravitatsiya hisobga olinmaydi?", "Momaqaldiroq bulutida zaryad qanday ajraladi?"]))

L.append(dict(
 n=2, short=r"Elektr maydon kuchlanganligi. Superpozitsiya", sim="field", refs=[1, 2, 5], intl=["purcell", "halliday", "griffiths"], tn=["TN2", "TN3", "TN8"],
 title=r"Elektr maydon kuchlanganligi. Nuqtaviy zaryad maydoni. Maydonlar superpozitsiyasi prinsipi",
 goal=r"Elektr maydon kuchlanganligi tushunchasini kiritish, nuqtaviy zaryad va zaryadlar sistemasi maydonini superpozitsiya prinsipi asosida hisoblash, uzluksiz taqsimlangan zaryadlar maydonini integrallash usulini o‘zlashtirish.",
 outcomes=[r"kuchlanganlikni \(\vec E=\vec F/q_0\) orqali ta’riflaydi;",
           r"nuqtaviy zaryad maydonini hisoblaydi va kuch chiziqlarini chizadi;",
           r"superpozitsiya prinsipi bilan bir necha zaryad maydonini vektor yig‘indi sifatida topadi;",
           r"zaryadlangan halqa va ip maydonini integrallash orqali hisoblaydi."],
 plan=["Maydon kuchlanganligi", "Nuqtaviy zaryad maydoni", "Superpozitsiya prinsipi", "Elektr dipol maydoni", "Uzluksiz taqsimlangan zaryadlar"],
 terms=["kuchlanganlik", "sinov zaryadi", "superpozitsiya prinsipi", "elektr dipol", "chiziqli zichlik", "sirt zichligi"],
 theory=[
  ("Kuchlanganlik", r"""<p>Elektr maydonning kuch xarakteristikasi — <b>kuchlanganlik</b>: maydonning berilgan nuqtasiga qo‘yilgan musbat sinov zaryadiga ta’sir etuvchi kuchning shu zaryadga nisbati:</p>
$$\vec E=\frac{\vec F}{q_0},\qquad[E]=\text{N/C}=\text{V/m}.$$
<p>Nuqtaviy zaryad maydoni: \(\vec E=\dfrac{1}{4\pi\varepsilon_0}\dfrac{q}{r^2}\dfrac{\vec r}{r}\). Musbat zaryad maydoni zaryaddan tashqariga, manfiyniki — zaryad tomon yo‘nalgan. Maydonni kuch chiziqlari bilan tasvirlaymiz: urinma \(\vec E\) yo‘nalishini, chiziqlar zichligi esa \(E\) modulini ko‘rsatadi.</p>"""),
  ("Superpozitsiya prinsipi", r"""<p>Zaryadlar sistemasining maydoni har bir zaryad alohida hosil qilgan maydonlarning vektor yig‘indisiga teng:</p>
$$\vec E=\sum_{i=1}^{N}\vec E_i=\frac{1}{4\pi\varepsilon_0}\sum_i\frac{q_i(\vec r-\vec r_i)}{|\vec r-\vec r_i|^3}.$$
<p>Uzluksiz taqsimlangan zaryad uchun yig‘indi integralga aylanadi: \(dq=\lambda\,dl\) (chiziqli), \(dq=\sigma\,dS\) (sirt), \(dq=\rho\,dV\) (hajmiy): \(\vec E=\frac{1}{4\pi\varepsilon_0}\int\frac{dq\,\vec r}{r^3}\).</p>"""),
  ("Elektr dipol", r"""<p>Ikki teng va qarama-qarshi ishorali zaryad \(\pm q\), oralig‘i \(l\) — <b>dipol</b>; dipol momenti \(\vec p=q\vec l\) (manfiydan musbatga). Katta masofada (\(r\gg l\)):</p>
$$E_\parallel=\frac{1}{4\pi\varepsilon_0}\frac{2p}{r^3}\ (\text{o‘q bo‘ylab}),\qquad E_\perp=\frac{1}{4\pi\varepsilon_0}\frac{p}{r^3}\ (\text{perpendikulyar}).$$
<p>Dipol maydoni nuqtaviy zaryadnikiga qaraganda tezroq (\(1/r^3\)) kamayadi.</p>"""),
  ("Integrallash misollari", r"""<p><b>Zaryadlangan halqa</b> (radius \(R\), zaryad \(q\)) o‘qida: \(E=\dfrac{1}{4\pi\varepsilon_0}\dfrac{qx}{(R^2+x^2)^{3/2}}\); markazda \(E=0\), maksimum \(x=R/\sqrt2\) da. <b>Cheksiz uzun ip</b> (\(\lambda\)): \(E=\dfrac{\lambda}{2\pi\varepsilon_0r}\). <b>Cheksiz tekislik</b> (\(\sigma\)): \(E=\dfrac{\sigma}{2\varepsilon_0}\) — masofaga bog‘liq emas.</p>""")],
 example=(r"Ikki zaryad maydoni",
  r"\(q_1=+4\) nC va \(q_2=-4\) nC zaryadlar orasidagi masofa 30 sm. 1) Ularning o‘rtasidagi nuqtada; 2) o‘rta perpendikulyarda, chiziqdan 20 sm uzoqlikdagi nuqtada kuchlanganlikni toping.",
  r"1) Har bir zaryad maydoni \(kq/r^2=8{,}988\cdot10^9\cdot4\cdot10^{-9}/0{,}15^2=1598\) V/m, ikkalasi ham manfiy zaryad tomon yo‘nalgan: \(E=3196\) V/m. 2) Masofa \(r=\sqrt{0{,}15^2+0{,}2^2}=0{,}25\) m; vertikal tashkil etuvchilar yo‘qoladi, gorizontallar qo‘shiladi: \(E=2\cdot\frac{kq}{r^2}\cdot\frac{0{,}15}{0{,}25}=690\) V/m (musbatdan manfiy tomonga, zaryadlarni tutashtiruvchi chiziqqa parallel)."),
 simtask=[r"“Dipol” konfiguratsiyasini tanlang: kuch chiziqlari musbatdan chiqib manfiyga kirishini kuzating.",
          r"Ikkala zaryadni bir xil ishorali qiling: o‘rtada \(E=0\) bo‘lgan nuqta paydo bo‘ladimi?",
          r"Sinov nuqtasini misoldagi joyga qo‘yib, 690 V/m ni tekshiring."],
 mistakes=[(r"“Kuch chiziqlari zaryadning harakat trayektoriyasi.”", r"Kuch chiziqlari kuch yo‘nalishini ko‘rsatadi; tezlik bor zaryad ulardan og‘ishi mumkin."),
           (r"“Ikki zaryad maydonlari modullari qo‘shiladi.”", r"Vektor yig‘indi olinadi — yo‘nalishlarni hisobga olish shart."),
           (r"“Kuch chiziqlari kesishishi mumkin.”", r"Har bir nuqtada \(\vec E\) yagona, shuning uchun chiziqlar kesishmaydi.")],
 ai=r"""Sen elektrostatika bo‘yicha repetitorsan. Mavzu: superpozitsiya prinsipi.
Menga zaryadlangan halqa o‘qidagi maydonni integrallash orqali topishni savollar bilan o‘rgat: \(dq\), \(d\vec E\), simmetriya, integral. So‘ng Python’da kvadrat uchlaridagi to‘rt zaryad maydonini hisoblash kodini tuzishimni so‘ra. Formulalarni LaTeX’da yoz.""",
 quiz=[
  (r"Kuchlanganlik birligi:", ["V/m", "V·m", "C/m", "J/C"], 0, "N/C = V/m."),
  (r"Nuqtaviy zaryad maydoni masofaga qanday bog‘liq?", [r"\(1/r^2\)", r"\(1/r\)", r"\(1/r^3\)", r"\(r\)"], 0, "Kulon qonunidan."),
  (r"Dipol maydoni katta masofada:", [r"\(1/r^3\)", r"\(1/r^2\)", r"\(1/r\)", r"\(1/r^4\)"], 0, "Zaryadlar maydonlari deyarli kompensatsiyalanadi."),
  (r"Superpozitsiya prinsipi:", ["maydonlar vektor sifatida qo‘shiladi", "faqat modullar qo‘shiladi", "eng katta maydon olinadi", "maydonlar ko‘paytiriladi"], 0, "Chiziqlilik."),
  (r"Cheksiz tekislik maydoni:", [r"\(\sigma/2\varepsilon_0\)", r"\(\sigma/\varepsilon_0\)", r"\(\sigma/4\pi\varepsilon_0r^2\)", r"\(\sigma r/\varepsilon_0\)"], 0, "Masofaga bog‘liq emas."),
  (r"Cheksiz ip maydoni:", [r"\(\lambda/2\pi\varepsilon_0r\)", r"\(\lambda/4\pi\varepsilon_0r^2\)", r"\(\lambda/\varepsilon_0\)", r"\(\lambda r/2\varepsilon_0\)"], 0, "Integrallash yoki Gauss teoremasi."),
  (r"Zaryadlangan halqa markazida \(E\) =", ["0", r"\(kq/R^2\)", r"\(kq/R\)", "cheksiz"], 0, "Simmetriya."),
  (r"Dipol momenti yo‘nalishi:", ["manfiydan musbat zaryadga", "musbatdan manfiyga", "maydon bo‘ylab har doim", "perpendikulyar"], 0, "Ta’rif."),
  (r"Kuch chiziqlari zichligi nimani ko‘rsatadi?", ["kuchlanganlik modulini", "potensialni", "zaryad massasini", "tezlikni"], 0, "Ta’rif."),
  (r"Misoldagi o‘rta nuqtadagi kuchlanganlik:", ["≈ 3,2 kV/m", "0", "≈ 1,6 kV/m", "≈ 690 V/m"], 0, "Ikki maydon bir yo‘nalishda.")],
 blits=["Nima uchun kuch chiziqlari kesishmaydi?", "Qaysi nuqtada ikki musbat zaryad maydoni nolga teng?", "Dipol maydoni nima uchun tez kamayadi?", "Uzluksiz zaryad qachon nuqtaviy deb qaraladi?"]))

L.append(dict(
 n=3, short=r"Gauss teoremasi", sim="gauss", refs=[1, 2, 3], intl=["purcell", "griffiths", "feynman2"], tn=["TN2", "TN4", "TN7"],
 title=r"Elektr maydon kuch chiziqlari. Kuchlanganlik va induksiya vektorlari oqimi. Gauss teoremasi",
 goal=r"Kuchlanganlik va elektr induksiya vektorlari oqimi tushunchalarini kiritish, Ostrogradskiy–Gauss teoremasini isbotlash va undan simmetrik zaryad taqsimotlari maydonini hisoblashda foydalanish.",
 outcomes=[r"vektor oqimini \(\Phi=\oint\vec E\cdot d\vec S\) ko‘rinishida hisoblaydi;",
           r"Gauss teoremasini integral va differensial ko‘rinishda yozadi;",
           r"sfera, shar, silindr va tekislik maydonlarini Gauss teoremasi bilan topadi;",
           r"\(\vec E\) va \(\vec D=\varepsilon_0\varepsilon\vec E\) vektorlarini farqlaydi."],
 plan=["Kuch chiziqlari va oqim", "Elektr induksiya vektori", "Gauss teoremasi", "Differensial shakl", "Simmetrik maydonlarni hisoblash"],
 terms=["vektor oqimi", "elektr induksiya", "Gauss teoremasi", "yopiq sirt", "divergensiya", "zaryad zichligi"],
 theory=[
  ("Vektor oqimi", r"""<p>\(dS\) yuzacha orqali kuchlanganlik oqimi \(d\Phi_E=\vec E\cdot d\vec S=E\,dS\cos\alpha\), bunda \(d\vec S\) — tashqi normal bo‘ylab yo‘nalgan yuza vektori. Oqim yuzani kesib o‘tuvchi kuch chiziqlari soniga proporsional. Muhitda elektr induksiya (siljish) vektori \(\vec D=\varepsilon_0\varepsilon\vec E\) kiritiladi; uning oqimi faqat erkin zaryadlarga bog‘liq.</p>"""),
  ("Ostrogradskiy–Gauss teoremasi", r"""<p>Ixtiyoriy yopiq sirt orqali kuchlanganlik oqimi sirt ichidagi zaryadlar yig‘indisining \(\varepsilon_0\) ga nisbatiga teng:</p>
$$\oint_S\vec E\cdot d\vec S=\frac{1}{\varepsilon_0}\sum q_{ich},\qquad\oint_S\vec D\cdot d\vec S=\sum q_{erkin}.$$
<p>Isbot: nuqtaviy zaryad uchun sfera orqali oqim \(E\cdot4\pi r^2=q/\varepsilon_0\), istalgan shakldagi sirt uchun ham xuddi shu (fazoviy burchak). Tashqaridagi zaryadlar oqimga hissa qo‘shmaydi. Teorema Kulon qonunining \(1/r^2\) ko‘rinishidan kelib chiqadi.</p>"""),
  ("Differensial shakl", r"""<p>Ostrogradskiy teoremasi \(\oint\vec E\cdot d\vec S=\int\nabla\cdot\vec E\,dV\) yordamida:</p>
$$\nabla\cdot\vec E=\frac{\rho}{\varepsilon_0},\qquad\nabla\cdot\vec D=\rho.$$
<p>Bu Maksvellning tenglamalaridan biri: maydon manbalari — zaryadlar; kuch chiziqlari musbat zaryadlarda boshlanib, manfiylarda tugaydi.</p>"""),
  ("Tatbiqlar", r"""<table class="t"><thead><tr><th>Zaryad taqsimoti</th><th>Ichkarida</th><th>Tashqarida</th></tr></thead><tbody>
<tr><td>Sferik qobiq (\(Q,R\))</td><td>\(E=0\)</td><td>\(E=\dfrac{Q}{4\pi\varepsilon_0r^2}\)</td></tr>
<tr><td>Bir jinsli zaryadlangan shar</td><td>\(E=\dfrac{Qr}{4\pi\varepsilon_0R^3}\)</td><td>\(E=\dfrac{Q}{4\pi\varepsilon_0r^2}\)</td></tr>
<tr><td>Cheksiz silindr / ip (\(\lambda\))</td><td>silindr hajmiy: \(E=\dfrac{\lambda r}{2\pi\varepsilon_0R^2}\)</td><td>\(E=\dfrac{\lambda}{2\pi\varepsilon_0r}\)</td></tr>
<tr><td>Cheksiz tekislik (\(\sigma\))</td><td colspan="2">\(E=\sigma/2\varepsilon_0\); ikki qarama-qarshi zaryadlangan tekislik orasida \(E=\sigma/\varepsilon_0\)</td></tr></tbody></table>
<p>Gauss sirti simmetriyaga mos tanlanadi: sfera, koaksial silindr yoki “quti”.</p>""")],
 example=(r"Zaryadlangan shar maydoni",
  r"Radiusi \(R=10\) sm bo‘lgan shar hajmi bo‘yicha \(Q=10\) nC zaryad bilan bir jinsli zaryadlangan. Markazdan 5, 10 va 20 sm masofalardagi kuchlanganlikni toping.",
  r"Ichkarida \(E=kQr/R^3\): \(r=5\) sm da \(8{,}988\cdot10^9\cdot10^{-8}\cdot0{,}05/10^{-3}=4494\) V/m. Sirtda \(kQ/R^2=8988\) V/m (maksimum). \(r=20\) sm da \(kQ/r^2=2247\) V/m. Grafik: markazdan sirtgacha chiziqli o‘sish, so‘ng \(1/r^2\) bo‘yicha kamayish."),
 simtask=[r"“Bir jinsli shar” rejimida misoldagi qiymatlarni grafikdan o‘qing.",
          r"“Sferik qobiq” rejimiga o‘ting: ichkarida maydon nimaga teng va nima uchun?",
          r"“Cheksiz silindr” va “tekislik” rejimlarida \(E(r)\) qonuniyatlarini taqqoslang."],
 mistakes=[(r"“Oqim nolga teng bo‘lsa, sirtda maydon yo‘q.”", r"Oqim nol — ichkarida zaryad yo‘q degani; sirt nuqtalarida maydon bo‘lishi mumkin (tashqi zaryadlar)."),
           (r"“Gauss teoremasi faqat sferik sirtlar uchun.”", r"Istalgan yopiq sirt uchun to‘g‘ri; lekin maydonni topish uchun simmetriya kerak."),
           (r"“Tashqi zaryadlar oqimga ta’sir qiladi.”", r"Tashqi zaryad maydoni sirtga kirib-chiqadi, umumiy oqimi nol.")],
 ai=r"""Sen elektrodinamika bo‘yicha repetitorsan. Mavzu: Gauss teoremasi.
Menga koaksial kabel (ichki sim va tashqi qobiq) maydonini Gauss teoremasi bilan topishni savollar orqali o‘rgat: simmetriya, Gauss sirtini tanlash, oqim, ichki zaryad. Har bir sohadagi natijani tekshir. Formulalarni LaTeX’da yoz.""",
 quiz=[
  (r"Gauss teoremasi:", [r"\(\oint\vec E\cdot d\vec S=q/\varepsilon_0\)", r"\(\oint\vec E\cdot d\vec l=0\)", r"\(\oint\vec B\cdot d\vec S=0\)", r"\(E=q/\varepsilon_0\)"], 0, "Integral shakl."),
  (r"Differensial shakl:", [r"\(\nabla\cdot\vec E=\rho/\varepsilon_0\)", r"\(\nabla\times\vec E=0\)", r"\(\nabla\cdot\vec B=0\)", r"\(\nabla\phi=\rho\)"], 0, "Divergensiya."),
  (r"Zaryadlangan sferik qobiq ichida \(E\) =", ["0", r"\(kQ/R^2\)", r"\(kQr/R^3\)", "cheksiz"], 0, "Ichkarida zaryad yo‘q."),
  (r"Bir jinsli shar ichida \(E\) masofaga:", ["chiziqli bog‘liq", r"\(1/r^2\)", "bog‘liq emas", r"\(r^2\)"], 0, r"\(E\propto r\)."),
  (r"Ikki qarama-qarshi zaryadlangan tekislik orasida:", [r"\(\sigma/\varepsilon_0\)", r"\(\sigma/2\varepsilon_0\)", "0", r"\(2\sigma/\varepsilon_0\)"], 0, "Maydonlar qo‘shiladi."),
  (r"\(\vec D\) oqimi nimaga bog‘liq?", ["faqat erkin zaryadlarga", "bog‘langan zaryadlarga", r"muhit \(\varepsilon\) ga", "sirt shakliga"], 0, r"\(\oint\vec D\cdot d\vec S=q_{erkin}\)."),
  (r"Yopiq sirtdan tashqaridagi zaryadning oqimi:", ["0", r"\(q/\varepsilon_0\)", r"\(-q/\varepsilon_0\)", "masofaga bog‘liq"], 0, "Kiruvchi = chiquvchi."),
  (r"Oqim birligi (\(\Phi_E\)):", ["V·m", "V/m", "C", "C/m²"], 0, "(V/m)·m²."),
  (r"Cheksiz ip maydoni uchun Gauss sirti:", ["koaksial silindr", "sfera", "kub", "tekislik"], 0, "Simmetriya."),
  (r"Misoldagi shar sirtidagi kuchlanganlik:", ["≈ 9 kV/m", "≈ 4,5 kV/m", "≈ 2,2 kV/m", "0"], 0, r"\(kQ/R^2\).")],
 blits=["Nima uchun Gauss teoremasi Kulon qonunining natijasi?", "Metall qobiq ichida maydon nima uchun yo‘q?", "Gauss teoremasi gravitatsiya uchun ham to‘g‘rimi?", "Faraday qafasi qanday ishlaydi?"]))

L.append(dict(
 n=4, short=r"Elektrostatik maydon potensiali", sim="potential", refs=[1, 2, 5], intl=["purcell", "halliday", "griffiths"], tn=["TN2", "TN4", "TN9"],
 title=r"Elektrostatik kuchlarning ishi. Elektrostatik maydon potensiali. Kuchlanganlik va potensial orasidagi bog‘lanish",
 goal=r"Elektrostatik maydonning potensialligini isbotlash, potensial va potensiallar farqini ta’riflash, kuchlanganlik bilan potensial orasidagi bog‘lanishdan foydalanib turli maydonlarning potensialini hisoblash.",
 outcomes=[r"elektrostatik kuchlar ishi yo‘lga bog‘liq emasligini ko‘rsatadi (\(\oint\vec E\cdot d\vec l=0\));",
           r"nuqtaviy zaryad va zaryadlar sistemasining potensialini hisoblaydi;",
           r"\(\vec E=-\nabla\varphi\) bog‘lanishni qo‘llaydi va ekvipotensial sirtlarni chizadi;",
           r"zaryadning maydondagi potensial energiyasi va tezlanishini hisoblaydi."],
 plan=["Elektrostatik kuchlar ishi", "Maydonning potensialligi", "Potensial va potensiallar farqi", "Kuchlanganlik va potensial bog‘lanishi", "Ekvipotensial sirtlar va hisoblash misollari"],
 terms=["potensial", "potensiallar farqi", "kuchlanish", "ekvipotensial sirt", "gradiyent", "elektronvolt"],
 theory=[
  ("Ish va potensial energiya", r"""<p>Nuqtaviy zaryad maydonida \(q_0\) ni 1-nuqtadan 2-nuqtaga ko‘chirishdagi ish faqat boshlang‘ich va oxirgi holatlarga bog‘liq:</p>
$$A_{12}=\frac{qq_0}{4\pi\varepsilon_0}\left(\frac{1}{r_1}-\frac{1}{r_2}\right)=W_1-W_2,\qquad\oint\vec E\cdot d\vec l=0.$$
<p>Demak elektrostatik maydon <b>potensial</b> (konservativ). Zaryadning potensial energiyasi \(W=\dfrac{qq_0}{4\pi\varepsilon_0r}\) (cheksizlikda nol).</p>"""),
  ("Potensial", r"""<p><b>Potensial</b> — birlik musbat zaryadning potensial energiyasi: \(\varphi=W/q_0\), birligi volt (V). Nuqtaviy zaryad: \(\varphi=\dfrac{q}{4\pi\varepsilon_0r}\). Zaryadlar sistemasi potensiali skalyar yig‘indi: \(\varphi=\sum\varphi_i\) — vektorlarni qo‘shishdan oson. Ish: \(A_{12}=q_0(\varphi_1-\varphi_2)=q_0U\). Atom fizikasida energiya birligi \(1\ \text{eV}=1{,}602\cdot10^{-19}\) J.</p>"""),
  ("Kuchlanganlik va potensial", r"""$$\vec E=-\nabla\varphi=-\left(\frac{\partial\varphi}{\partial x}\vec i+\frac{\partial\varphi}{\partial y}\vec j+\frac{\partial\varphi}{\partial z}\vec k\right),\qquad\varphi_1-\varphi_2=\int_1^2\vec E\cdot d\vec l.$$
<p>Kuchlanganlik potensial eng tez kamayadigan yo‘nalishda. Bir jinsli maydonda \(E=U/d\). <b>Ekvipotensial sirtlar</b> (\(\varphi=\text{const}\)) kuch chiziqlariga perpendikulyar; ular bo‘ylab zaryadni ko‘chirishda ish nol.</p>"""),
  ("Hisoblash misollari", r"""<ul><li>Zaryadlangan sfera (\(Q,R\)): tashqarida \(\varphi=kQ/r\), ichkarida \(\varphi=kQ/R=\text{const}\).</li><li>Ikki parallel tekislik: \(U=Ed=\sigma d/\varepsilon_0\).</li><li>Dipol: \(\varphi=\dfrac{p\cos\theta}{4\pi\varepsilon_0r^2}\).</li><li>Cheksiz ip: \(\varphi_1-\varphi_2=\dfrac{\lambda}{2\pi\varepsilon_0}\ln\dfrac{r_2}{r_1}\).</li></ul>""")],
 example=(r"Potensial va ish",
  r"\(Q=10\) nC zaryaddan 10 sm uzoqlikdagi nuqtaning potensialini toping. \(q=1\) nC zaryadni cheksizlikdan shu nuqtaga keltirish uchun qancha ish kerak? Elektron 100 V potensiallar farqida tinch holatdan tezlashsa, tezligi qancha bo‘ladi?",
  r"\(\varphi=kQ/r=8{,}988\cdot10^9\cdot10^{-8}/0{,}1=899\) V. Tashqi kuch ishi \(A=q\varphi=0{,}899\) mkJ (maydon kuchlari ishi shuncha manfiy). Elektron: \(eU=mv^2/2\) ⇒ \(v=\sqrt{2eU/m}=5{,}93\cdot10^6\) m/s; energiyasi 100 eV."),
 simtask=[r"Ikki qarama-qarshi zaryad uchun ekvipotensial chiziqlarni kuzating: ular kuch chiziqlariga perpendikulyarmi?",
          r"O‘q bo‘yicha \(\varphi(x)\) grafigida qiyalik eng katta joy kuchlanganlik eng katta joy ekanini tekshiring.",
          r"Ikkala zaryadni musbat qiling: potensial nolga teng nuqtalar qolarmi?"],
 mistakes=[(r"“Potensial nol bo‘lgan joyda maydon ham nol.”", r"Dipol o‘rtasida \(\varphi=0\), lekin \(E\ne0\). Maydon potensial gradiyentiga bog‘liq."),
           (r"“Potensial vektor kattalik.”", r"Potensial — skalyar; superpozitsiyada oddiy yig‘iladi."),
           (r"“Elektron kuch chiziqlari bo‘ylab harakatlanadi.”", r"Manfiy zaryadga kuch \(\vec E\) ga qarshi ta’sir qiladi; elektron potensial ortadigan tomonga tezlashadi.")],
 ai=r"""Sen elektrostatika bo‘yicha repetitorsan. Mavzu: potensial va kuchlanganlik bog‘lanishi.
Menga dipol potensialidan \(\vec E=-\nabla\varphi\) orqali maydon komponentlarini qutb koordinatalarida topishni savollar bilan o‘rgat. So‘ng potensial xaritasini Python’da (matplotlib contour) qurish topshirig‘ini ber. Formulalarni LaTeX’da yoz.""",
 quiz=[
  (r"Nuqtaviy zaryad potensiali:", [r"\(q/4\pi\varepsilon_0r\)", r"\(q/4\pi\varepsilon_0r^2\)", r"\(qr/4\pi\varepsilon_0\)", r"\(q/\varepsilon_0\)"], 0, "Ta’rif."),
  (r"\(\vec E\) va \(\varphi\) bog‘lanishi:", [r"\(\vec E=-\nabla\varphi\)", r"\(\vec E=\nabla\varphi\)", r"\(\varphi=-\nabla\cdot\vec E\)", r"\(E=\varphi r\)"], 0, "Gradiyent."),
  (r"Elektrostatik maydonda yopiq kontur bo‘ylab ish:", ["0", r"\(qU\)", "konturga bog‘liq", "har doim musbat"], 0, "Konservativ maydon."),
  (r"1 eV =", [r"\(1{,}602\cdot10^{-19}\) J", r"\(1{,}6\cdot10^{-13}\) J", "1 J", r"\(9{,}1\cdot10^{-31}\) J"], 0, "Elektron zaryadi × 1 V."),
  (r"Ekvipotensial sirt va kuch chiziqlari orasidagi burchak:", ["90°", "0°", "45°", "ixtiyoriy"], 0, "Ish nol."),
  (r"Bir jinsli maydonda \(U=200\) V, \(d=4\) mm. \(E\) =", ["50 kV/m", "800 V/m", "5 kV/m", "0,8 V/m"], 0, r"\(U/d\)."),
  (r"Zaryadlangan sfera ichida potensial:", ["o‘zgarmas, sirtdagiga teng", "nol", "markazga qarab kamayadi", "cheksiz"], 0, r"\(E=0\) ⇒ \(\varphi=\text{const}\)."),
  (r"Dipol o‘rta perpendikulyarida potensial:", ["0", "maksimal", r"\(kp/r^2\)", "cheksiz"], 0, r"\(\cos\theta=0\)."),
  (r"Elektron 100 V da tezlashgandagi tezligi taxminan:", [r"\(6\cdot10^6\) m/s", r"\(6\cdot10^4\) m/s", r"\(3\cdot10^8\) m/s", r"\(6\cdot10^8\) m/s"], 0, r"\(\sqrt{2eU/m}\)."),
  (r"Zaryadlar sistemasi potensiali:", ["har bir zaryad potensiallarining algebraik yig‘indisi", "vektor yig‘indi", "eng katta potensial", "o‘rtacha qiymat"], 0, "Skalyar superpozitsiya.")],
 blits=["Qush yuqori kuchlanishli simda nima uchun zarar ko‘rmaydi?", "Potensial nolini qayerda tanlash mumkin?", "Ekvipotensial sirtlarning zichligi nimani ko‘rsatadi?", "Elektronvolt nima uchun qulay birlik?"]))

L.append(dict(
 n=5, short=r"Dielektriklarda elektr maydon", sim="dielectric", refs=[1, 2, 3], intl=["purcell", "griffiths", "sivukhin"], tn=["TN2", "TN7", "TN8"],
 title=r"Dielektriklarda elektr maydon. Dielektriklarning qutblanishi",
 goal=r"O‘tkazgich, dielektrik va yarimo‘tkazgichlarni farqlash, dielektriklarning qutblanish mexanizmlarini, qutblanganlik va elektr induksiya vektorlarini hamda dielektrik mavjud bo‘lgandagi maydonni hisoblashni o‘rganish.",
 outcomes=[r"qutbli va qutbsiz molekulalar, elektron, ion va oriyentatsion qutblanishni tushuntiradi;",
           r"qutblanganlik \(\vec P=\varepsilon_0\chi\vec E\) va \(\vec D=\varepsilon_0\vec E+\vec P\) ni bog‘laydi;",
           r"dielektrikli kondensatordagi \(E\), \(D\), \(P\) va bog‘langan zaryadlarni hisoblaydi;",
           r"ikki muhit chegarasida maydonning sinish shartlarini qo‘llaydi."],
 plan=["O‘tkazgichlar, dielektriklar, yarimo‘tkazgichlar", "Dielektrik molekulalarining dipol momentlari", "Qutblanish turlari va qutblanganlik", "Elektr induksiya vektori", "Chegaraviy shartlar"],
 terms=["dielektrik", "qutblanish", "qutblanganlik", "dielektrik qabul qiluvchanlik", "bog‘langan zaryad", "segnetoelektrik"],
 theory=[
  ("Moddalar tasnifi va dipollar", r"""<p><b>O‘tkazgichlarda</b> erkin zaryadlar bor (metallar: \(n\sim10^{28}\) m⁻³), <b>dielektriklarda</b> (izolyatorlarda) zaryadlar bog‘langan, <b>yarimo‘tkazgichlarda</b> erkin zaryadlar soni harorat va kirishmalarga kuchli bog‘liq. Dielektrik molekulalari <b>qutbsiz</b> (H₂, N₂, CO₂ — maydon yo‘qligida \(\vec p=0\)) yoki <b>qutbli</b> (H₂O: \(p=6{,}2\cdot10^{-30}\) C·m) bo‘ladi. Tashqi maydonda dipolga \(\vec M=\vec p\times\vec E\) moment ta’sir qiladi, energiyasi \(W=-\vec p\cdot\vec E\).</p>"""),
  ("Qutblanish", r"""<p>Qutblanish turlari: <b>elektron</b> (elektron bulutning siljishi), <b>ion</b> (ion panjaralarining siljishi), <b>oriyentatsion</b> (qutbli molekulalarning maydon bo‘ylab burilishi; haroratga bog‘liq). Birlik hajmdagi dipol momenti — <b>qutblanganlik</b>:</p>
$$\vec P=\frac{\sum\vec p_i}{\Delta V}=\varepsilon_0\chi\vec E,\qquad\varepsilon=1+\chi.$$
<p>Qutblanish natijasida dielektrik sirtida <b>bog‘langan zaryadlar</b> paydo bo‘ladi: \(\sigma'=P_n\). Ular tashqi maydonni susaytiradi: \(E=E_0/\varepsilon\).</p>"""),
  ("Elektr induksiya vektori", r"""$$\vec D=\varepsilon_0\vec E+\vec P=\varepsilon_0\varepsilon\vec E,\qquad\oint\vec D\cdot d\vec S=q_{erkin}.$$
<p>\(\vec D\) maydon erkin zaryadlar bilan aniqlanadi, \(\vec E\) esa barcha (erkin va bog‘langan) zaryadlar bilan. Yassi kondensatorda dielektrik: \(D=\sigma\), \(E=\sigma/\varepsilon_0\varepsilon\), \(P=\sigma(1-1/\varepsilon)\).</p>"""),
  ("Chegaraviy shartlar va maxsus dielektriklar", r"""<p>Ikki dielektrik chegarasida (sirt erkin zaryadi bo‘lmasa): \(E_{1\tau}=E_{2\tau}\), \(D_{1n}=D_{2n}\). Bundan kuch chiziqlarining sinish qonuni:</p>
$$\frac{\operatorname{tg}\alpha_1}{\operatorname{tg}\alpha_2}=\frac{\varepsilon_1}{\varepsilon_2}.$$
<p><b>Segnetoelektriklar</b> (BaTiO₃) — juda katta \(\varepsilon\sim10^3\), gisterezis va Kyuri nuqtasiga ega. <b>Pyezoelektriklar</b> (kvars) mexanik deformatsiyada qutblanadi va aksincha — ultratovush manbalari, soat rezonatorlarida qo‘llaniladi.</p>""")],
 example=(r"Dielektrikli kondensator",
  r"Yassi kondensator qoplamalarida erkin zaryad sirt zichligi \(\sigma=1\) mkC/m², oraliq \(\varepsilon=4\) dielektrik bilan to‘ldirilgan. \(D\), \(E\), \(P\), \(\chi\) va bog‘langan zaryad zichligini toping. Kuch chiziqlari havodan (\(\varepsilon_1=1\)) shishaga (\(\varepsilon_2=7\)) 45° burchak ostida tushsa, sinish burchagi qancha?",
  r"\(D=\sigma=10^{-6}\) C/m²; \(E=\sigma/\varepsilon_0\varepsilon=28{,}2\) kV/m (vakuumdagidan 4 marta kichik); \(P=\sigma(1-1/\varepsilon)=0{,}75\) mkC/m² \(=\sigma'\); \(\chi=3\). Sinish: \(\operatorname{tg}\alpha_2=\operatorname{tg}45^\circ\cdot7=7\) ⇒ \(\alpha_2=81{,}9^\circ\) (normalga nisbatan) — chiziqlar chegaraga yaqinlashadi."),
 simtask=[r"\(\varepsilon\) ni 1 dan 10 gacha oshiring: \(E\) qanday kamayadi, \(D\) o‘zgaradimi?",
          r"Misoldagi qiymatlarni o‘rnatib, bog‘langan zaryad zichligi 0,75 mkC/m² ekanini tekshiring.",
          r"Chegarada kuch chiziqlari sinishini kuzating: qaysi muhitda chiziqlar normalga yaqinroq?"],
 mistakes=[(r"“Dielektrikda maydon nolga teng.”", r"Bu o‘tkazgich uchun; dielektrikda maydon \(\varepsilon\) marta susayadi, lekin nol emas."),
           (r"“\(\vec D\) va \(\vec E\) bir xil narsa.”", r"\(\vec D\) faqat erkin zaryadlarga bog‘liq, \(\vec E\) — barcha zaryadlarga; ular \(\varepsilon_0\varepsilon\) ko‘paytuvchi bilan farq qiladi."),
           (r"“Qutblanish dielektrikda erkin zaryad hosil qiladi.”", r"Paydo bo‘ladigan zaryadlar bog‘langan; ularni ajratib olib bo‘lmaydi.")],
 ai=r"""Sen materiallar fizikasi bo‘yicha repetitorsan. Mavzu: dielektriklarda qutblanish.
Menga oriyentatsion qutblanish uchun Lanjeven formulasini (\(\langle\cos\theta\rangle\)) kichik maydon yaqinlashuvida keltirib chiqarishni savollar bilan o‘rgat va \(\chi\propto1/T\) ekanini tushuntir. Formulalarni LaTeX’da yoz.""",
 quiz=[
  (r"\(\vec D\) =", [r"\(\varepsilon_0\vec E+\vec P\)", r"\(\varepsilon_0\vec E-\vec P\)", r"\(\vec P/\varepsilon_0\)", r"\(\varepsilon\vec P\)"], 0, "Ta’rif."),
  (r"\(\varepsilon\) va \(\chi\) bog‘lanishi:", [r"\(\varepsilon=1+\chi\)", r"\(\varepsilon=\chi\)", r"\(\varepsilon=1-\chi\)", r"\(\varepsilon=1/\chi\)"], 0, "Ta’rif."),
  (r"Dielektrikda maydon vakuumdagiga nisbatan:", [r"\(\varepsilon\) marta kichik", r"\(\varepsilon\) marta katta", "nol", "o‘zgarmaydi"], 0, "Bog‘langan zaryadlar susaytiradi."),
  (r"Qutbli molekula:", ["H₂O", "N₂", "H₂", "CO₂"], 0, "Doimiy dipol momenti bor."),
  (r"Haroratga kuchli bog‘liq qutblanish:", ["oriyentatsion", "elektron", "ion", "hech biri"], 0, "Issiqlik harakati tartibni buzadi."),
  (r"Chegarada uzluksiz qoladi:", [r"\(E_\tau\) va \(D_n\)", r"\(E_n\) va \(D_\tau\)", r"faqat \(E\)", r"faqat \(P\)"], 0, "Chegaraviy shartlar."),
  (r"Dipolning maydondagi energiyasi:", [r"\(-\vec p\cdot\vec E\)", r"\(\vec p\times\vec E\)", r"\(pE^2\)", r"\(p/E\)"], 0, "Minimum — maydon bo‘ylab."),
  (r"Bog‘langan zaryad sirt zichligi:", [r"\(\sigma'=P_n\)", r"\(\sigma'=D\)", r"\(\sigma'=\varepsilon_0E\)", r"\(\sigma'=0\)"], 0, "Qutblanganlik normal tashkil etuvchisi."),
  (r"Segnetoelektrik xossasi:", [r"gisterezis va katta \(\varepsilon\)", "ferromagnetizm", "o‘ta o‘tkazuvchanlik", r"\(\varepsilon<1\)"], 0, "BaTiO₃."),
  (r"Pyezoelektrik effekt:", ["deformatsiyada qutblanish", "qizdirishda tok", "yorug‘likda tok", "magnitlanish"], 0, "Kvars.")],
 blits=["Nima uchun suvning \\(\\varepsilon\\) katta (81)?", "Mikroto‘lqinli pech ovqatni qanday isitadi?", "Zajigalkadagi pyezoelement qanday ishlaydi?", "Dielektrik kondensator sig‘imini nima uchun oshiradi?"]))

L.append(dict(
 n=6, short=r"O‘tkazgichlar. Kondensatorlar. Maydon energiyasi", sim="capacitor", refs=[1, 2, 4], intl=["halliday", "purcell", "serway"], tn=["TN3", "TN4", "TN9"],
 title=r"Elektrostatik maydonda o‘tkazgichlar. Elektr sig‘imi. Kondensatorlar. Elektr maydon energiyasi",
 goal=r"O‘tkazgichda zaryadlar taqsimoti va elektrostatik induksiyani, yakkalangan o‘tkazgich va kondensator sig‘imini, kondensatorlarni ulash qoidalarini hamda zaryadlar sistemasi va elektr maydon energiyasini o‘rganish.",
 outcomes=[r"o‘tkazgich ichida \(E=0\) va zaryad sirtda joylashishini tushuntiradi;",
           r"yassi, sferik va silindrik kondensator sig‘imini hisoblaydi;",
           r"ketma-ket va parallel ulangan kondensatorlar sig‘imini topadi;",
           r"kondensator va maydon energiyasini \(W=CU^2/2\), \(w=\varepsilon_0\varepsilon E^2/2\) bilan hisoblaydi."],
 plan=["O‘tkazgichda zaryadlar taqsimoti", "Elektrostatik induksiya", "Elektr sig‘imi va kondensatorlar", "Kondensatorlarni ulash", "Zaryadlar sistemasi va maydon energiyasi"],
 terms=["elektrostatik induksiya", "elektr sig‘imi", "kondensator", "farad", "energiya zichligi", "elektrostatik himoya"],
 theory=[
  ("O‘tkazgichlar elektrostatik maydonda", r"""<p>Muvozanatda o‘tkazgich ichida \(\vec E=0\), barcha nuqtalari bir xil potensialda, ortiqcha zaryad faqat sirtda joylashadi; sirt yaqinida maydon unga perpendikulyar: \(E=\sigma/\varepsilon_0\). Zaryad o‘tkir uchlarda zichroq to‘planadi (yashin qaytargich, toj razryadi). Tashqi maydonga kiritilgan o‘tkazgichda zaryadlar ajraladi — <b>elektrostatik induksiya</b>. Yopiq o‘tkazgich qobiq ichini tashqi maydondan himoyalaydi (Faradey qafasi).</p>"""),
  ("Elektr sig‘imi", r"""<p>Yakkalangan o‘tkazgich uchun \(q\propto\varphi\): \(C=q/\varphi\), birligi farad (F). Shar: \(C=4\pi\varepsilon_0\varepsilon R\) (Yer uchun ≈ 0,7 mF). <b>Kondensator</b> — dielektrik bilan ajratilgan ikki o‘tkazgich: \(C=q/U\).</p>
<table class="t"><thead><tr><th>Kondensator</th><th>Sig‘im</th></tr></thead><tbody><tr><td>Yassi</td><td>\(C=\dfrac{\varepsilon_0\varepsilon S}{d}\)</td></tr><tr><td>Sferik</td><td>\(C=4\pi\varepsilon_0\varepsilon\dfrac{R_1R_2}{R_2-R_1}\)</td></tr><tr><td>Silindrik</td><td>\(C=\dfrac{2\pi\varepsilon_0\varepsilon l}{\ln(R_2/R_1)}\)</td></tr></tbody></table>"""),
  ("Ulash", r"""<p><b>Parallel</b>: kuchlanish bir xil, zaryadlar qo‘shiladi: \(C=C_1+C_2+\ldots\). <b>Ketma-ket</b>: zaryad bir xil, kuchlanishlar qo‘shiladi: \(\dfrac1C=\dfrac1{C_1}+\dfrac1{C_2}+\ldots\). Ketma-ket ulash teshilish kuchlanishini oshirish, parallel — sig‘imni oshirish uchun qo‘llaniladi.</p>"""),
  ("Energiya", r"""<p>Nuqtaviy zaryadlar sistemasi: \(W=\dfrac12\sum q_i\varphi_i\). Zaryadlangan o‘tkazgich va kondensator:</p>
$$W=\frac{qU}{2}=\frac{CU^2}{2}=\frac{q^2}{2C}.$$
<p>Energiya maydonda joylashgan; uning hajmiy zichligi:</p>
$$w=\frac{\varepsilon_0\varepsilon E^2}{2}=\frac{ED}{2}.$$
<p>Qoplamalarning tortishish kuchi \(F=\dfrac{q^2}{2\varepsilon_0\varepsilon S}\).</p>""")],
 example=(r"Yassi kondensator",
  r"Qoplamalar yuzasi \(S=100\) sm², oraliq \(d=1\) mm, havo. Sig‘im, \(U=100\) V dagi zaryad, energiya va maydon energiyasi zichligini toping. Shu kondensator bilan 2 mkF va 3 mkF kondensatorlarni ketma-ket va parallel ulashning umumiy sig‘imini ham hisoblang (faqat 2 va 3 mkF).",
  r"\(C=\varepsilon_0S/d=8{,}854\cdot10^{-12}\cdot0{,}01/10^{-3}=88{,}5\) pF. \(q=CU=8{,}85\) nC. \(W=CU^2/2=0{,}443\) mkJ. \(E=U/d=10^5\) V/m, \(w=\varepsilon_0E^2/2=0{,}0443\) J/m³; \(w\cdot Sd=0{,}443\) mkJ ✓. Ketma-ket: \(C=2\cdot3/5=1{,}2\) mkF; parallel: 5 mkF."),
 simtask=[r"Misoldagi qiymatlarni o‘rnatib, sig‘im 88,5 pF ekanini tekshiring.",
          r"Oraliqni 2 marta oshiring (manbadan uzilgan holda): kuchlanish va energiya qanday o‘zgaradi? Bajarilgan ish qayerga ketdi?",
          r"Dielektrik kiriting: sig‘im, zaryad (manba ulangan) va energiya qanday o‘zgaradi?"],
 mistakes=[(r"“Sig‘im zaryadga bog‘liq.”", r"Sig‘im faqat geometriya va dielektrikka bog‘liq; \(q\) oshsa \(U\) ham proporsional oshadi."),
           (r"“Ketma-ket ulashda sig‘imlar qo‘shiladi.”", r"Ketma-ketda teskari qiymatlar qo‘shiladi; umumiy sig‘im eng kichigidan ham kichik."),
           (r"“Energiya qoplamalardagi zaryadlarda joylashgan.”", r"Energiya maydonda taqsimlangan: \(w=\varepsilon_0\varepsilon E^2/2\).")],
 ai=r"""Sen elektrostatika bo‘yicha repetitorsan. Mavzu: kondensatorlar.
Menga ikki xil holatni solishtirishni o‘rgat: kondensator manbaga ulangan va uzilgan holda dielektrik kiritilganda \(C\), \(q\), \(U\), \(E\), \(W\) qanday o‘zgaradi. Avval men jadval to‘ldiray, sen tekshir. Formulalarni LaTeX’da yoz.""",
 quiz=[
  (r"Yassi kondensator sig‘imi:", [r"\(\varepsilon_0\varepsilon S/d\)", r"\(\varepsilon_0Sd\)", r"\(\varepsilon_0d/S\)", r"\(4\pi\varepsilon_0S\)"], 0, "Ta’rif."),
  (r"O‘tkazgich ichida elektrostatik maydon:", ["0", "sirtdagiga teng", "cheksiz", r"\(\sigma/\varepsilon_0\)"], 0, "Erkin zaryadlar qayta taqsimlanadi."),
  (r"2 mkF va 3 mkF ketma-ket:", ["1,2 mkF", "5 mkF", "6 mkF", "0,83 mkF"], 0, r"\(C_1C_2/(C_1+C_2)\)."),
  (r"Kondensator energiyasi:", [r"\(CU^2/2\)", r"\(CU\)", r"\(C^2U/2\)", r"\(qU\)"], 0, "Ta’rif."),
  (r"Maydon energiyasi zichligi:", [r"\(\varepsilon_0\varepsilon E^2/2\)", r"\(\varepsilon_0E\)", r"\(E^2/2\varepsilon_0\)", r"\(\varepsilon_0E^3\)"], 0, "J/m³."),
  (r"Shar sig‘imi:", [r"\(4\pi\varepsilon_0\varepsilon R\)", r"\(\varepsilon_0R^2\)", r"\(4\pi\varepsilon_0/R\)", r"\(\varepsilon_0R\)"], 0, "Yakkalangan o‘tkazgich."),
  (r"Manbadan uzilgan kondensatorga dielektrik kiritilsa:", [r"\(U\) kamayadi, \(q\) o‘zgarmaydi", r"\(q\) ortadi", r"\(U\) ortadi", "hech narsa o‘zgarmaydi"], 0, r"\(U=q/C\)."),
  (r"Faradey qafasi:", ["ichini tashqi elektr maydondan himoyalaydi", "maydonni kuchaytiradi", "magnit maydonni yo‘qotadi", "tok hosil qiladi"], 0, "Elektrostatik himoya."),
  (r"Zaryad o‘tkazgichning qayerida zichroq?", ["o‘tkir uchlarda", "botiq joylarda", "bir tekis", "ichkarida"], 0, "Egrilik katta joyda."),
  (r"Misoldagi kondensator sig‘imi:", ["88,5 pF", "8,85 nF", "0,885 pF", "885 pF"], 0, r"\(\varepsilon_0S/d\).")],
 blits=["Nima uchun mashina ichida chaqmoqdan himoyalangansiz?", "Defibrillyator kondensatori qancha energiya saqlaydi?", "Sensorli ekran qanday ishlaydi?", "Superkondensatorlarning afzalligi nimada?"]))

L.append(dict(
 n=7, short=r"Elektr toki. O‘zgarmas tok qonunlari", sim="ohm", refs=[1, 2, 5], intl=["halliday", "serway", "purcell"], tn=["TN3", "TN4", "TN9"],
 title=r"Elektr toki va uning xarakteristikalari. Om qonuni. Joul–Lens qonuni. Tok manbaining EYuK",
 goal=r"Elektr tokining mikroskopik tabiatini, tok kuchi va zichligini, zanjir qismi va to‘la zanjir uchun Om qonunini, Joul–Lens qonunini hamda tok manbaining EYuK va quvvat balansini o‘rganish.",
 outcomes=[r"tok kuchi, tok zichligi va dreyf tezligini \(j=nev\) orqali bog‘laydi;",
           r"Om qonunini integral (\(I=U/R\)) va differensial (\(\vec j=\sigma\vec E\)) ko‘rinishda qo‘llaydi;",
           r"Joul–Lens qonuni bilan issiqlik va quvvatni hisoblaydi;",
           r"bir jinsli bo‘lmagan zanjir qismi va to‘la zanjir uchun Om qonunini qo‘llab, foydali quvvat va FIK ni topadi."],
 plan=["Elektr toki va uning xarakteristikalari", "Zanjir qismi uchun Om qonuni, qarshilik", "Joul–Lens qonuni", "Tok manbaining EYuK", "Bir jinsli bo‘lmagan zanjir qismi va to‘la zanjir"],
 terms=["tok kuchi", "tok zichligi", "solishtirma qarshilik", "elektr yurituvchi kuch", "ichki qarshilik", "Joul–Lens qonuni"],
 theory=[
  ("Tok va uning xarakteristikalari", r"""<p><b>Elektr toki</b> — zaryadlarning tartibli harakati. Tok kuchi \(I=dq/dt\) (amper), tok zichligi \(\vec j=ne\vec v_d\), \(I=\int\vec j\cdot d\vec S\). Metallarda dreyf tezligi juda kichik (\(\sim10^{-4}\) m/s), lekin elektr maydon simda yorug‘lik tezligiga yaqin tarqaladi. Uzluksizlik tenglamasi: \(\nabla\cdot\vec j=-\partial\rho/\partial t\); o‘zgarmas tokda \(\oint\vec j\cdot d\vec S=0\).</p>"""),
  ("Om qonuni", r"""$$I=\frac{U}{R},\qquad R=\rho\frac{l}{S},\qquad\vec j=\sigma\vec E,\ \sigma=1/\rho.$$
<p>Qarshilik haroratga bog‘liq: \(\rho=\rho_0(1+\alpha t)\) (metallar uchun \(\alpha\approx1/273\) K⁻¹). Ketma-ket: \(R=R_1+R_2\), parallel: \(1/R=1/R_1+1/R_2\).</p>"""),
  ("Joul–Lens qonuni", r"""<p>Tok o‘tganda ajralgan issiqlik:</p>
$$Q=I^2Rt=UIt=\frac{U^2}{R}t,\qquad P=IU,\qquad w=jE=\sigma E^2\ (\text{differensial shakl}).$$
<p>Ketma-ket ulangan qarshiliklarda ko‘proq issiqlik kattaroq qarshilikda, parallelda esa kichikroq qarshilikda ajraladi.</p>"""),
  ("EYuK va to‘la zanjir", r"""<p>Tok manbaida begona (nonelektrostatik) kuchlar zaryadlarni ko‘chiradi; ularning birlik zaryadga ishi — <b>EYuK</b> \(\mathcal E\). Bir jinsli bo‘lmagan zanjir qismi uchun: \(IR_{12}=\varphi_1-\varphi_2+\mathcal E_{12}\). To‘la zanjir uchun:</p>
$$I=\frac{\mathcal E}{R+r},\qquad U=\mathcal E-Ir,\qquad I_{qt}=\frac{\mathcal E}{r}.$$
<p>Foydali quvvat \(P=I^2R\) maksimal \(R=r\) da: \(P_{max}=\mathcal E^2/4r\), bunda FIK \(\eta=R/(R+r)=50\%\).</p>""")],
 example=(r"Mis sim va akkumulyator",
  r"1) Ko‘ndalang kesimi 1 mm² mis simdan 2 A tok o‘tmoqda (\(n=8{,}5\cdot10^{28}\) m⁻³). Dreyf tezligi? 2) EYuK 12 V, ichki qarshiligi 0,5 Ω manbaga 5,5 Ω yuklama ulangan. Tok, klemmalardagi kuchlanish, foydali quvvat va FIK? Maksimal foydali quvvat qancha?",
  r"1) \(v=I/(neS)=2/(8{,}5\cdot10^{28}\cdot1{,}602\cdot10^{-19}\cdot10^{-6})=0{,}147\) mm/s. 2) \(I=12/6=2\) A; \(U=12-1=11\) V; \(P=I^2R=22\) W; \(\eta=5{,}5/6=91{,}7\)%. \(R=r=0{,}5\) Ω da \(P_{max}=144/2=72\) W (FIK 50 %)."),
 simtask=[r"Misoldagi qiymatlarni o‘rnatib, \(I=2\) A va \(P=22\) W ekanini tekshiring.",
          r"Yuklama qarshiligini o‘zgartirib, foydali quvvat maksimumini toping — u \(R=r\) dami?",
          r"Qisqa tutashuvda (\(R\to0\)) tok va FIK nimaga teng?"],
 mistakes=[(r"“Elektronlar simda yorug‘lik tezligida harakatlanadi.”", r"Dreyf tezligi mm/s tartibida; tezda tarqaladigan narsa — elektromagnit maydon."),
           (r"“EYuK — bu kuchlanish.”", r"EYuK begona kuchlar ishi; klemmalardagi kuchlanish \(U=\mathcal E-Ir\) dan kichik (tok bo‘lsa)."),
           (r"“Maksimal quvvatda FIK ham maksimal.”", r"\(R=r\) da FIK atigi 50 %; FIK \(R\gg r\) da yuqori.")],
 ai=r"""Sen elektr zanjirlari bo‘yicha repetitorsan. Mavzu: to‘la zanjir uchun Om qonuni.
Menga \(P(R)\) funksiyasini tuzib, maksimum shartini hosila orqali topishni savollar bilan o‘rgat. So‘ng Python’da \(P(R)\) va \(\eta(R)\) grafiklarini chizish topshirig‘ini ber. Formulalarni LaTeX’da yoz.""",
 quiz=[
  (r"Tok zichligi:", [r"\(j=nev\)", r"\(j=I\cdot S\)", r"\(j=U/R\)", r"\(j=ne/v\)"], 0, "Mikroskopik ta’rif."),
  (r"Om qonuni differensial shaklda:", [r"\(\vec j=\sigma\vec E\)", r"\(\vec E=\sigma\vec j\)", r"\(j=E/\sigma^2\)", r"\(I=UR\)"], 0, "Lokal ko‘rinish."),
  (r"Simning uzunligi 2 marta, kesimi 2 marta oshsa, qarshilik:", ["o‘zgarmaydi", "4 marta ortadi", "2 marta ortadi", "4 marta kamayadi"], 0, r"\(R=\rho l/S\)."),
  (r"To‘la zanjir uchun Om qonuni:", [r"\(I=\mathcal E/(R+r)\)", r"\(I=\mathcal E/R\)", r"\(I=\mathcal E r/R\)", r"\(I=(\mathcal E-U)/R\)"], 0, "Ta’rif."),
  (r"Maksimal foydali quvvat sharti:", [r"\(R=r\)", r"\(R=0\)", r"\(R\to\infty\)", r"\(R=2r\)"], 0, "Moslashtirish."),
  (r"Joul–Lens qonuni:", [r"\(Q=I^2Rt\)", r"\(Q=IRt\)", r"\(Q=I^2t/R\)", r"\(Q=UR t\)"], 0, "Issiqlik."),
  (r"Qisqa tutashuv toki:", [r"\(\mathcal E/r\)", "0", r"\(\mathcal E/R\)", "cheksiz har doim"], 0, r"\(R=0\)."),
  (r"Metallarda dreyf tezligi tartibi:", [r"\(10^{-4}\) m/s", r"\(10^{6}\) m/s", r"\(3\cdot10^8\) m/s", "1 m/s"], 0, "Juda kichik."),
  (r"\(R=r\) da FIK:", ["50 %", "100 %", "0", "75 %"], 0, r"\(R/(R+r)\)."),
  (r"Metall qarshiligi harorat oshganda:", ["ortadi", "kamayadi", "o‘zgarmaydi", "nolga tushadi"], 0, "Fononlar bilan sochilish.")],
 blits=["Nima uchun chiroq o‘chirgich bosilishi bilan yonadi?", "Elektr choynakning qarshiligi qancha?", "Nima uchun elektr uzatish liniyalarida yuqori kuchlanish ishlatiladi?", "Akkumulyatorning ichki qarshiligi nima uchun muhim?"]))

L.append(dict(
 n=8, short=r"Tarmoqlangan zanjirlar. Kirxgof qoidalari", sim="kirchhoff", refs=[1, 2, 4], intl=["halliday", "serway", "irodov"], tn=["TN3", "TN4", "TN8"],
 title=r"Tarmoqlangan zanjirlar. Kirxgof qoidalari",
 goal=r"Tarmoqlangan zanjirlarni hisoblash uchun Kirxgofning birinchi (tugunlar) va ikkinchi (konturlar) qoidalarini o‘rganish, tenglamalar sistemasini tuzish va yechish algoritmini o‘zlashtirish.",
 outcomes=[r"tugun va kontur tushunchalarini ajratadi, mustaqil tenglamalar sonini aniqlaydi;",
           r"Kirxgof qoidalarini ishoralar qoidasiga rioya qilib yozadi;",
           r"chiziqli tenglamalar sistemasini yechib, toklar va kuchlanishlarni topadi;",
           r"Uitston ko‘prigi va manbalarni parallel ulash masalalarini tahlil qiladi."],
 plan=["Tarmoqlangan zanjir: tugun, shoxobcha, kontur", "Kirxgofning birinchi qoidasi", "Kirxgofning ikkinchi qoidasi", "Hisoblash algoritmi", "Uitston ko‘prigi va boshqa misollar"],
 terms=["tugun", "shoxobcha", "kontur", "Kirxgof qoidalari", "Uitston ko‘prigi", "potensiometr"],
 theory=[
  ("Kirxgofning birinchi qoidasi", r"""<p><b>Tugun</b> — uchta va undan ortiq o‘tkazgich tutashgan nuqta. Zaryadning saqlanishidan (o‘zgarmas tokda zaryad to‘planmaydi):</p>
$$\sum_k I_k=0.$$
<p>Tugunga kiruvchi toklarni musbat, chiquvchilarni manfiy olamiz. \(n\) ta tugunli zanjir uchun \(n-1\) ta mustaqil tenglama yoziladi.</p>"""),
  ("Kirxgofning ikkinchi qoidasi", r"""<p>Har qanday yopiq kontur uchun (bir jinsli bo‘lmagan qismlar uchun Om qonunini qo‘shib):</p>
$$\sum_kI_kR_k=\sum_k\mathcal E_k.$$
<p>Konturni aylanib chiqish yo‘nalishi tanlanadi; tok yo‘nalishi aylanish bilan mos bo‘lsa \(IR\) musbat, EYuK aylanish yo‘nalishida tok hosil qilsa (manfiydan musbat qutbga) musbat olinadi. Mustaqil konturlar soni \(m=p-n+1\) (\(p\) — shoxobchalar soni).</p>"""),
  ("Algoritm", r"""<ol><li>Har bir shoxobchadagi tok yo‘nalishini ixtiyoriy tanlang va belgilang.</li><li>\(n-1\) tugun uchun birinchi qoidani yozing.</li><li>\(p-n+1\) mustaqil kontur uchun ikkinchi qoidani yozing.</li><li>Tenglamalar sistemasini yeching (Kramer, Gauss usuli yoki Python).</li><li>Manfiy chiqqan tok haqiqatda teskari yo‘nalgan. Natijani quvvat balansi bilan tekshiring: \(\sum\mathcal E I=\sum I^2R\).</li></ol>"""),
  ("Uitston ko‘prigi", r"""<p>To‘rt qarshilik romb shaklida, bir diagonalda galvanometr, ikkinchisida manba. Galvanometrdan tok o‘tmasligi (ko‘prik muvozanati) sharti:</p>
$$\frac{R_1}{R_2}=\frac{R_3}{R_4}\ \Rightarrow\ R_x=R_2\frac{R_3}{R_4}.$$
<p>Bu usul qarshiliklarni manba EYuK siga bog‘liq bo‘lmagan holda aniq o‘lchash imkonini beradi.</p>""")],
 example=(r"Ikki manbali zanjir",
  r"\(\mathcal E_1=12\) V (\(R_1=2\) Ω shoxobchada) va \(\mathcal E_2=6\) V (\(R_2=4\) Ω shoxobchada) manbalar musbat qutblari bilan umumiy tugunga ulangan; uchinchi shoxobchada \(R_3=6\) Ω. Manbalarning ichki qarshiligi hisobga olinmasin. Barcha toklarni toping.",
  r"Tugun: \(I_1+I_2=I_3\). Konturlar: \(2I_1+6I_3=12\), \(4I_2+6I_3=6\). Yechim: \(I_1=21/11=1{,}91\) A, \(I_2=-6/11=-0{,}55\) A, \(I_3=15/11=1{,}36\) A. \(I_2\) manfiy — ikkinchi manba orqali tok teskari yo‘nalgan, u zaryadlanmoqda. Quvvat balansi: \(12\cdot1{,}909-6\cdot0{,}545=19{,}64\) W \(=2\cdot1{,}909^2+4\cdot0{,}545^2+6\cdot1{,}364^2=19{,}64\) W ✓."),
 simtask=[r"Misoldagi qiymatlarni o‘rnatib, toklarni tekshiring. Qaysi manba zaryadlanmoqda?",
          r"\(\mathcal E_2\) ni oshirib, \(I_2\) ishorasi o‘zgaradigan qiymatni toping.",
          r"Quvvat balansi har doim bajarilishini turli parametrlar uchun tekshiring."],
 mistakes=[(r"“Tok yo‘nalishini oldindan to‘g‘ri tanlash kerak.”", r"Ixtiyoriy tanlanadi; manfiy natija tok teskari ekanini bildiradi."),
           (r"“Barcha konturlar uchun tenglama yozish kerak.”", r"Faqat mustaqil konturlar uchun (\(p-n+1\) ta); ortiqchasi chiziqli bog‘liq."),
           (r"“Manba har doim energiya beradi.”", r"Teskari tok o‘tsa, manba energiya oladi (akkumulyator zaryadlanadi).")],
 ai=r"""Sen elektr zanjirlari bo‘yicha repetitorsan. Mavzu: Kirxgof qoidalari.
Menga 3 konturli zanjir uchun tenglamalarni tuzishni savollar orqali o‘rgat, so‘ng uni numpy.linalg.solve bilan yechish kodini yozishimni so‘ra. Javobni quvvat balansi bilan tekshirishni eslat. Formulalarni LaTeX’da yoz.""",
 quiz=[
  (r"Kirxgofning birinchi qoidasi qaysi qonunga asoslangan?", ["zaryadning saqlanishi", "energiyaning saqlanishi", "impulsning saqlanishi", "Kulon qonuni"], 0, "Tugunda zaryad to‘planmaydi."),
  (r"Ikkinchi qoida:", [r"\(\sum IR=\sum\mathcal E\)", r"\(\sum I=0\)", r"\(\sum U=I\)", r"\(\sum R=0\)"], 0, "Kontur uchun."),
  (r"\(n\) tugun uchun mustaqil tugun tenglamalari soni:", [r"\(n-1\)", r"\(n\)", r"\(n+1\)", r"\(2n\)"], 0, "Bittasi qolganlaridan kelib chiqadi."),
  (r"Mustaqil konturlar soni (\(p\) shoxobcha, \(n\) tugun):", [r"\(p-n+1\)", r"\(p+n\)", r"\(p-n\)", r"\(n-1\)"], 0, "Graflar nazariyasi."),
  (r"Hisobda tok manfiy chiqsa:", ["haqiqiy yo‘nalish teskari", "xato qilingan", "tok yo‘q", "qarshilik manfiy"], 0, "Ishora yo‘nalishni bildiradi."),
  (r"Uitston ko‘prigi muvozanati:", [r"\(R_1R_4=R_2R_3\)", r"\(R_1+R_2=R_3+R_4\)", r"\(R_1=R_4\)", r"\(R_1R_2=R_3R_4\)"], 0, r"\(R_1/R_2=R_3/R_4\)."),
  (r"Quvvat balansi:", [r"\(\sum\mathcal EI=\sum I^2R\)", r"\(\sum\mathcal E=\sum R\)", r"\(\sum I=\sum U\)", r"\(\sum P=0\) har doim"], 0, "Energiya saqlanishi."),
  (r"Ikkinchi qoida qaysi qonunga asoslangan?", ["elektrostatik maydonning potensialligi (energiya)", "zaryad saqlanishi", "Amper qonuni", "Faradey qonuni"], 0, r"\(\oint\vec E\cdot d\vec l=0\)."),
  (r"Misolda qaysi manba zaryadlanadi?", ["6 V li", "12 V li", "ikkalasi", "hech biri"], 0, r"\(I_2<0\)."),
  (r"Misolda \(R_3\) dagi tok:", ["≈ 1,36 A", "≈ 1,91 A", "≈ 0,55 A", "2 A"], 0, "15/11 A.")],
 blits=["Avtomobilda akkumulyator va generator qanday parallel ishlaydi?", "Nima uchun turli EYuK li batareyalarni parallel ulash xavfli?", "Uitston ko‘prigi qayerda qo‘llaniladi?", "Uydagi rozetkalar ketma-ketmi yoki parallel?"]))
