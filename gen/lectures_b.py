"""M9–M15 ma'ruzalar mazmuni (Elektr va magnetizm, fan dasturi EM1306)."""

L = []

L.append(dict(
 n=9, short=r"Tokning magnit maydoni. Bio–Savar–Laplas qonuni", sim="biot", refs=[1, 2, 3], intl=["purcell", "halliday", "griffiths"], tn=["TN2", "TN3", "TN7"],
 title=r"Vakuumda tokning magnit maydoni. Magnit maydon induksiyasi. Bio–Savar–Laplas qonuni",
 goal=r"Harakatdagi zaryadlar va toklarning magnit o‘zaro ta’sirini, magnit induksiya vektorini va Bio–Savar–Laplas qonunini o‘rganish, to‘g‘ri tok va doiraviy tok maydonini hisoblash.",
 outcomes=[r"magnit maydonni harakatdagi zaryadlar hosil qilishini va unga ta’sir qilishini tushuntiradi;",
           r"magnit induksiya vektorini kuch ta’siri orqali ta’riflaydi, yo‘nalishini parma qoidasi bilan aniqlaydi;",
           r"Bio–Savar–Laplas qonunini vektor ko‘rinishda yozadi;",
           r"to‘g‘ri tok, doiraviy tok markazi va o‘qidagi induksiyani hisoblaydi."],
 plan=["Magnit o‘zaro ta’sir va magnit maydon", "Magnit induksiya vektori", "Harakatdagi zaryad maydoni", "Bio–Savar–Laplas qonuni", "To‘g‘ri va doiraviy tok maydoni"],
 terms=["magnit maydon", "magnit induksiya", "tesla", "Bio–Savar–Laplas qonuni", "parma qoidasi", "magnit doimiysi"],
 theory=[
  ("Magnit o‘zaro ta’sir", r"""<p>Ersted tajribasi (1820): tokli o‘tkazgich magnit strelkasini buradi. Amper: parallel toklar tortishadi, qarama-qarshilari itariladi. Magnit maydon <b>harakatdagi zaryadlar</b> (toklar) va magnitlangan jismlar tomonidan hosil qilinadi va faqat harakatdagi zaryadlarga ta’sir qiladi. Elektr va magnit maydonlar yagona elektromagnit maydonning ikki ko‘rinishi; ularning nisbati sanoq sistemasiga bog‘liq.</p>"""),
  ("Magnit induksiya vektori", r"""<p>Magnit maydonning kuch xarakteristikasi — <b>magnit induksiya</b> \(\vec B\). Uni tokli ramkaga ta’sir etuvchi maksimal moment yoki harakatdagi zaryadga ta’sir etuvchi kuch orqali aniqlaymiz: \(B=\dfrac{M_{max}}{p_m}\), \(p_m=IS\); birligi tesla (T). Yo‘nalishi — erkin magnit strelkaning shimoliy qutbi yo‘nalishi. Magnit maydon chiziqlari yopiq (uyurmaviy maydon); to‘g‘ri tok atrofida ular konsentrik aylanalar, yo‘nalishi parma (o‘ng vint) qoidasi bilan topiladi.</p>"""),
  ("Bio–Savar–Laplas qonuni", r"""<p>Tok elementi \(Id\vec l\) hosil qiladigan maydon:</p>
$$d\vec B=\frac{\mu_0}{4\pi}\frac{I\,d\vec l\times\vec r}{r^3},\qquad dB=\frac{\mu_0}{4\pi}\frac{I\,dl\sin\alpha}{r^2},\quad\mu_0=4\pi\cdot10^{-7}\ \text{H/m}.$$
<p>Tezlik bilan harakatlanayotgan nuqtaviy zaryad maydoni (\(v\ll c\)): \(\vec B=\dfrac{\mu_0}{4\pi}\dfrac{q\vec v\times\vec r}{r^3}\). Butun o‘tkazgich maydoni superpozitsiya bo‘yicha integrallanadi.</p>"""),
  ("Asosiy natijalar", r"""<ul><li>To‘g‘ri tokning chekli qismi: \(B=\dfrac{\mu_0I}{4\pi r_0}(\cos\alpha_1-\cos\alpha_2)\); cheksiz uzun to‘g‘ri tok: \(B=\dfrac{\mu_0I}{2\pi r}\).</li><li>Doiraviy tok markazida: \(B=\dfrac{\mu_0I}{2R}\); o‘qida: \(B=\dfrac{\mu_0IR^2}{2(R^2+x^2)^{3/2}}\).</li><li>Uzoq masofada doiraviy tok — magnit dipol: \(B\approx\dfrac{\mu_0}{4\pi}\dfrac{2p_m}{x^3}\), \(p_m=I\pi R^2\).</li></ul>""")],
 example=(r"To‘g‘ri va doiraviy tok",
  r"1) Cheksiz uzun to‘g‘ri simdan 10 A tok o‘tmoqda. 5 sm masofadagi induksiya? Yer magnit maydoni (≈ 50 mkT) bilan taqqoslang. 2) Radiusi 10 sm o‘ramdan 5 A tok o‘tmoqda. Markazdagi va o‘qda 10 sm uzoqlikdagi induksiyani toping.",
  r"1) \(B=\mu_0I/2\pi r=4\pi\cdot10^{-7}\cdot10/(2\pi\cdot0{,}05)=40\) mkT — Yer maydoniga yaqin, shuning uchun kompas og‘adi. 2) Markazda \(B=\mu_0I/2R=31{,}4\) mkT; \(x=R\) da \(B=\mu_0IR^2/(2\cdot(2R^2)^{3/2})=B_0/2^{3/2}=11{,}1\) mkT."),
 simtask=[r"“To‘g‘ri tok” rejimida \(B(r)\) ning \(1/r\) qonuniyatini tekshiring.",
          r"“Doiraviy o‘ram” rejimida o‘q bo‘yicha \(B(x)\) ni kuzating va misoldagi qiymatlarni o‘qing.",
          r"“Solenoid” rejimida uzunlikni oshiring: o‘rtadagi maydon \(\mu_0nI\) ga qanday yaqinlashadi?"],
 mistakes=[(r"“Magnit maydon tinch zaryadga ham ta’sir qiladi.”", r"Faqat harakatdagi zaryadga: \(\vec F=q\vec v\times\vec B\)."),
           (r"“Magnit chiziqlari tokdan chiqib, tokka kiradi.”", r"Magnit chiziqlari yopiq — manbasiz (\(\nabla\cdot\vec B=0\))."),
           (r"“\(d\vec B\) tok elementi bo‘ylab yo‘nalgan.”", r"\(d\vec B\perp d\vec l\) va \(d\vec B\perp\vec r\) — vektor ko‘paytma.")],
 ai=r"""Sen magnetizm bo‘yicha repetitorsan. Mavzu: Bio–Savar–Laplas qonuni.
Menga kvadrat ramka (tomoni a) markazidagi induksiyani chekli to‘g‘ri tok formulasi orqali topishni savollar bilan o‘rgat. So‘ng Python’da Bio–Savar–Laplas integralini sonli hisoblab, natijani tekshirish kodini yozishimni so‘ra. Formulalarni LaTeX’da yoz.""",
 quiz=[
  (r"Cheksiz to‘g‘ri tok maydoni:", [r"\(\mu_0I/2\pi r\)", r"\(\mu_0I/2r\)", r"\(\mu_0nI\)", r"\(\mu_0I/4\pi r^2\)"], 0, "Bio–Savar–Laplas."),
  (r"Doiraviy tok markazida:", [r"\(\mu_0I/2R\)", r"\(\mu_0I/2\pi R\)", r"\(\mu_0IR\)", "0"], 0, "Integrallash."),
  (r"\(\mu_0\) =", [r"\(4\pi\cdot10^{-7}\) H/m", r"\(8{,}85\cdot10^{-12}\) F/m", r"\(9\cdot10^9\) N·m²/C²", r"\(1{,}26\cdot10^{-4}\) H/m"], 0, "Magnit doimiysi."),
  (r"Magnit induksiya birligi:", ["tesla", "veber", "genri", "amper"], 0, "T = N/(A·m)."),
  (r"Magnit maydon chiziqlari:", ["yopiq", "musbat zaryaddan boshlanadi", "tokka kiradi", "parallel to‘g‘ri chiziqlar har doim"], 0, "Uyurmaviy maydon."),
  (r"Masofa 2 marta oshsa, to‘g‘ri tok maydoni:", ["2 marta kamayadi", "4 marta kamayadi", "o‘zgarmaydi", "2 marta ortadi"], 0, r"\(1/r\)."),
  (r"Ersted tajribasi nimani ko‘rsatdi?", ["tok magnit maydon hosil qiladi", "magnit tok hosil qiladi", "zaryad kvantlangan", "yorug‘lik to‘lqin"], 0, "1820-yil."),
  (r"\(d\vec B\) yo‘nalishi:", [r"\(d\vec l\times\vec r\) bo‘ylab", r"\(\vec r\) bo‘ylab", r"\(d\vec l\) bo‘ylab", "ixtiyoriy"], 0, "Vektor ko‘paytma."),
  (r"Uzoq masofada doiraviy tok maydoni:", [r"\(1/x^3\)", r"\(1/x\)", r"\(1/x^2\)", "o‘zgarmas"], 0, "Magnit dipol."),
  (r"10 A tokdan 5 sm masofada \(B\):", ["40 mkT", "4 mT", "0,4 mkT", "400 mkT"], 0, r"\(\mu_0I/2\pi r\).")],
 blits=["Nima uchun kompas tokli sim yonida og‘adi?", "Yer magnit maydonini nima hosil qiladi?", "MRT apparatida maydon qancha?", "Ikki parallel tok nima uchun tortishadi?"]))

L.append(dict(
 n=10, short=r"Magnit induksiya sirkulyatsiyasi", sim="ampere", refs=[1, 2, 3], intl=["purcell", "griffiths", "halliday"], tn=["TN2", "TN4", "TN7"],
 title=r"Bio–Savar–Laplas qonunining tatbiqi. Magnit induksiya vektorining sirkulyatsiyasi. Magnit oqimi",
 goal=r"Magnit induksiya vektorining sirkulyatsiyasi haqidagi teoremani (to‘la tok qonuni) o‘rganish, magnit maydonning uyurmaviy xarakterini tushunish va teoremani solenoid, toroid, koaksial kabel maydonini hisoblashga tatbiq etish.",
 outcomes=[r"to‘la tok qonunini \(\oint\vec B\cdot d\vec l=\mu_0\sum I\) ko‘rinishida yozadi;",
           r"magnit maydonning uyurmaviy va elektrostatik maydonning potensial xarakterini taqqoslaydi;",
           r"solenoid, toroid va koaksial kabel maydonini hisoblaydi;",
           r"magnit oqimi va magnit uchun Gauss teoremasini qo‘llaydi."],
 plan=["Sirkulyatsiya haqidagi teorema", "Magnit maydonning uyurmaviy xarakteri", "Solenoid va toroid maydoni", "Tokli silindr va koaksial kabel", "Magnit oqimi, Gauss teoremasi"],
 terms=["sirkulyatsiya", "to‘la tok qonuni", "solenoid", "toroid", "magnit oqimi", "veber"],
 theory=[
  ("To‘la tok qonuni", r"""<p>Ixtiyoriy yopiq kontur bo‘yicha \(\vec B\) sirkulyatsiyasi kontur o‘rab olgan toklarning algebraik yig‘indisiga proporsional:</p>
$$\oint_L\vec B\cdot d\vec l=\mu_0\sum I_k,\qquad\nabla\times\vec B=\mu_0\vec j.$$
<p>Tok yo‘nalishi kontur aylanishi bilan o‘ng vint qoidasi bo‘yicha bog‘langan bo‘lsa musbat. Sirkulyatsiya nolga teng emas — maydon <b>uyurmaviy</b> (elektrostatik maydondan farqli: \(\oint\vec E\cdot d\vec l=0\)), shuning uchun magnit maydonga skalyar potensial kiritib bo‘lmaydi.</p>"""),
  ("Solenoid va toroid", r"""<p><b>Uzun solenoid</b> (birlik uzunlikdagi o‘ramlar soni \(n=N/l\)): to‘g‘ri burchakli kontur tanlab,</p>
$$B=\mu_0nI\ (\text{ichkarida, bir jinsli}),\qquad B\approx0\ (\text{tashqarida}).$$
<p>Chekli solenoid uchlarida maydon ikki marta kichik: \(B=\mu_0nI/2\). <b>Toroid</b> (\(N\) o‘ram): \(B=\dfrac{\mu_0NI}{2\pi r}\) ichkarida, tashqarida nol.</p>"""),
  ("Tokli silindr va koaksial kabel", r"""<p>Radiusi \(R\) bo‘lgan sim bo‘ylab tok bir tekis taqsimlangan: ichkarida \(B=\dfrac{\mu_0Ir}{2\pi R^2}\), tashqarida \(B=\dfrac{\mu_0I}{2\pi r}\). Koaksial kabelda ichki va tashqi o‘tkazgichlar orasida \(B=\mu_0I/2\pi r\), kabeldan tashqarida maydon nol — shuning uchun kabel tashqariga tarqalmaydi va tashqi xalaqitdan himoyalangan.</p>"""),
  ("Magnit oqimi", r"""<p>Magnit oqimi \(\Phi=\int\vec B\cdot d\vec S\), birligi veber (Wb = T·m²). Magnit zaryadlari (monopollar) yo‘q, shuning uchun har qanday yopiq sirt orqali:</p>
$$\oint_S\vec B\cdot d\vec S=0,\qquad\nabla\cdot\vec B=0.$$
<p>Solenoid ichidagi oqim \(\Phi=BS\), to‘liq oqim ilashishi \(\Psi=N\Phi=\mu_0n^2lSI\).</p>""")],
 example=(r"Solenoid va toroid",
  r"1) Uzunligi 50 sm solenoidda 500 o‘ram bor, tok 2 A. Ichidagi induksiya? 2) Toroidda 500 o‘ram, tok 1 A, o‘rta radiusi 10 sm. Induksiya? 3) Ikki parallel sim 10 sm masofada, toklar 20 A dan, qarama-qarshi yo‘nalgan: o‘rtadagi induksiya?",
  r"1) \(n=1000\) m⁻¹, \(B=\mu_0nI=2{,}51\) mT. 2) \(B=\mu_0NI/2\pi r=1{,}0\) mT. 3) Har bir sim 5 sm da \(\mu_0I/2\pi r=80\) mkT beradi; qarama-qarshi toklarda o‘rtada maydonlar bir yo‘nalishda: \(B=160\) mkT."),
 simtask=[r"Ikki parallel tokni bir yo‘nalishda qo‘ying: o‘rtada \(B\) nimaga teng? Kuch tortishishmi yoki itarishmi?",
          r"Masofani o‘zgartirib, birlik uzunlikka kuch \(1/d\) qonuniyatini tekshiring.",
          r"Misoldagi 3-holatni modelda takrorlang."],
 mistakes=[(r"“Sirkulyatsiya teoremasi faqat aylana konturlar uchun.”", r"Istalgan yopiq kontur uchun; maydonni topish uchun simmetriya kerak."),
           (r"“Solenoid tashqarisida maydon kuchli.”", r"Uzun solenoid tashqarisida maydon deyarli nol."),
           (r"“Magnit oqimi yopiq sirt orqali ichidagi magnitga teng.”", r"Har doim nol: magnit monopollar yo‘q.")],
 ai=r"""Sen magnetizm bo‘yicha repetitorsan. Mavzu: to‘la tok qonuni.
Menga koaksial kabelning to‘rt sohasi uchun \(B(r)\) ni sirkulyatsiya teoremasi bilan topishni savollar orqali o‘rgat va natijani grafikda tasvirlashni so‘ra. Formulalarni LaTeX’da yoz.""",
 quiz=[
  (r"To‘la tok qonuni:", [r"\(\oint\vec B\cdot d\vec l=\mu_0I\)", r"\(\oint\vec B\cdot d\vec S=\mu_0I\)", r"\(\oint\vec E\cdot d\vec l=0\)", r"\(B=\mu_0I\)"], 0, "Sirkulyatsiya."),
  (r"Uzun solenoid ichida:", [r"\(\mu_0nI\)", r"\(\mu_0I/2R\)", r"\(\mu_0I/2\pi r\)", "0"], 0, "Bir jinsli maydon."),
  (r"Toroid ichida:", [r"\(\mu_0NI/2\pi r\)", r"\(\mu_0nI/2\)", r"\(\mu_0NI\)", "0"], 0, "Sirkulyatsiya."),
  (r"Yopiq sirt orqali magnit oqimi:", ["0", r"\(\mu_0I\)", r"\(BS\)", "cheksiz"], 0, "Monopol yo‘q."),
  (r"Magnit oqimi birligi:", ["veber", "tesla", "genri", "gauss"], 0, "Wb = T·m²."),
  (r"Tokli sim ichida (bir tekis tok) \(B\):", ["markazdan masofaga chiziqli o‘sadi", "o‘zgarmas", "nol", r"\(1/r\)"], 0, r"\(\mu_0Ir/2\pi R^2\)."),
  (r"Magnit maydon:", ["uyurmaviy", "potensial", "manbali", "statik zaryadli"], 0, r"\(\nabla\times\vec B\ne0\)."),
  (r"Chekli solenoid uchida maydon o‘rtadagiga nisbatan:", ["2 marta kichik", "teng", "2 marta katta", "nol"], 0, "Yarim cheksiz solenoid."),
  (r"Koaksial kabeldan tashqarida maydon:", ["0", r"\(\mu_0I/2\pi r\)", r"\(\mu_0I\)", "maksimal"], 0, "Toklar yig‘indisi nol."),
  (r"Differensial shakl:", [r"\(\nabla\times\vec B=\mu_0\vec j\)", r"\(\nabla\cdot\vec B=\mu_0\vec j\)", r"\(\nabla\times\vec E=0\)", r"\(\nabla\cdot\vec E=0\)"], 0, "Rotor.")],
 blits=["Nima uchun solenoid ichida maydon bir jinsli?", "Tokamak qurilmasida toroid nima uchun?", "Antenna kabeli nima uchun koaksial?", "Magnit monopol topilsa, qaysi tenglama o‘zgaradi?"]))

L.append(dict(
 n=11, short=r"Amper qonuni. Lorens kuchi. Xoll effekti", sim="lorentzf", refs=[1, 2, 4], intl=["halliday", "serway", "purcell"], tn=["TN3", "TN4", "TN9"],
 title=r"Magnit maydonning tokka ta’siri. Amper qonuni. Lorens kuchi. Zaryadli zarralar harakati. Xoll effekti",
 goal=r"Magnit maydonning tokli o‘tkazgich va harakatdagi zaryadga ta’sirini (Amper va Lorens kuchlari), magnit maydon kuchlarining ishini, zaryadli zarralarning elektr va magnit maydondagi harakatini hamda Xoll effektini o‘rganish.",
 outcomes=[r"Amper kuchini \(d\vec F=Id\vec l\times\vec B\) bo‘yicha hisoblaydi, chap qo‘l qoidasini qo‘llaydi;",
           r"tokli ramkaga ta’sir etuvchi moment va magnit kuchlari ishini topadi;",
           r"Lorens kuchi ta’sirida zarra trayektoriyasini (aylana, vint chiziq) tahlil qiladi;",
           r"Xoll kuchlanishidan zaryad tashuvchilar konsentratsiyasi va ishorasini aniqlaydi."],
 plan=["Amper qonuni", "Tokli ramka magnit maydonda; magnit kuchlar ishi", "Lorens kuchi", "Zaryadli zarralarning elektr va magnit maydondagi harakati", "Xoll effekti"],
 terms=["Amper kuchi", "Lorens kuchi", "siklotron chastotasi", "vint chiziq", "Xoll effekti", "massa-spektrometr"],
 theory=[
  ("Amper qonuni", r"""$$d\vec F=I\,d\vec l\times\vec B,\qquad F=IBl\sin\alpha.$$
<p>Yo‘nalish — chap qo‘l qoidasi. Ikki parallel tok orasidagi kuch (birlik uzunlikka): \(\dfrac{F}{l}=\dfrac{\mu_0I_1I_2}{2\pi d}\) — amper birligi shu asosda ta’riflangan. Tokli ramkaga moment \(\vec M=\vec p_m\times\vec B\), \(p_m=ISN\). Tokli kontur ko‘chirilganda magnit kuchlar ishi \(A=I\Delta\Phi\).</p>"""),
  ("Lorens kuchi", r"""$$\vec F=q\vec E+q\vec v\times\vec B.$$
<p>Magnit qism tezlikka perpendikulyar — ish bajarmaydi, zarra energiyasini o‘zgartirmaydi. Bir jinsli magnit maydonda \(\vec v\perp\vec B\) bo‘lsa, zarra aylana bo‘ylab harakatlanadi:</p>
$$r=\frac{mv}{|q|B},\qquad T=\frac{2\pi m}{|q|B},\qquad\omega_c=\frac{|q|B}{m}.$$
<p>Davr tezlikka bog‘liq emas (siklotron asosi). Ixtiyoriy burchakda — vint chiziq, qadami \(h=v_\parallel T\). Elektr maydonda zarra \(a=qE/m\) tezlanish oladi (parabola, ossillograf trubkasi). Kesishgan \(\vec E\perp\vec B\) maydonlarda \(v=E/B\) tezlikli zarralar og‘maydi (tezlik filtri).</p>"""),
  ("Xoll effekti", r"""<p>Tokli plastina (qalinligi \(d\)) ko‘ndalang magnit maydonga qo‘yilsa, Lorens kuchi tashuvchilarni bir qirraga suradi va ko‘ndalang <b>Xoll kuchlanishi</b> paydo bo‘ladi:</p>
$$U_H=R_H\frac{IB}{d},\qquad R_H=\frac{1}{nq}.$$
<p>\(U_H\) ishorasidan tashuvchilar ishorasi (elektron yoki teshik), qiymatidan konsentratsiyasi topiladi. Metallarda \(U_H\) juda kichik (mkV), yarimo‘tkazgichlarda katta — Xoll datchiklari magnit maydon o‘lchash va kontaktsiz tok sensorlarida ishlatiladi.</p>"""),
  ("Qo‘llanilishi", r"""<p><b>Massa-spektrometr</b>: \(r=mv/qB\) bo‘yicha izotoplarni ajratadi. <b>Siklotron</b>: \(f=qB/2\pi m\) chastotali o‘zgaruvchan kuchlanish zarrani har yarim aylanishda tezlashtiradi. <b>Qutb nurlari</b>: Quyosh shamoli zarralari Yer magnit maydon chiziqlari bo‘ylab vint chiziq bo‘yicha qutblarga yo‘naladi. <b>Elektr dvigatel</b>: tokli ramkaga ta’sir etuvchi moment.</p>""")],
 example=(r"Elektron magnit maydonda va Xoll kuchlanishi",
  r"1) 1 keV energiyali elektron \(B=1\) mT maydonga tik uchib kirdi. Tezligi, aylana radiusi va davri? 2) Qalinligi 0,1 mm mis plastinadan 10 A tok o‘tmoqda, \(B=1\) T (\(n=8{,}5\cdot10^{28}\) m⁻³). Xoll kuchlanishi? 3) Uzunligi 20 sm simdan 5 A tok o‘tmoqda, \(B=0{,}5\) T maydonga tik. Amper kuchi?",
  r"1) \(v=\sqrt{2E/m}=1{,}88\cdot10^7\) m/s; \(r=mv/eB=10{,}7\) sm; \(T=2\pi m/eB=35{,}7\) ns. 2) \(U_H=IB/(ned)=10\cdot1/(8{,}5\cdot10^{28}\cdot1{,}602\cdot10^{-19}\cdot10^{-4})=7{,}3\) mkV. 3) \(F=IBl=0{,}5\) N."),
 simtask=[r"Faqat magnit maydon qoldiring (\(E=0\)): trayektoriya aylana. Radius tezlikka qanday bog‘liq?",
          r"Tezlikka maydon bo‘ylab tashkil etuvchi bering (burchak < 90°): vint chiziqni kuzating.",
          r"\(E\) ni yoqing: \(v=E/B\) da zarra to‘g‘ri chiziq bo‘ylab ketishini (tezlik filtri) tekshiring; boshqa hollarda dreyf (sikloida)."],
 mistakes=[(r"“Magnit maydon zarrani tezlashtiradi (energiya beradi).”", r"Lorens kuchining magnit qismi \(\vec F\perp\vec v\) — ish bajarmaydi, faqat yo‘nalishni o‘zgartiradi."),
           (r"“Siklotron davri tezlik oshganda ortadi.”", r"Norelyativistik zarra uchun \(T=2\pi m/qB\) tezlikka bog‘liq emas."),
           (r"“Xoll kuchlanishi faqat elektronlar uchun.”", r"Teshiklarda ishora teskari — tashuvchi turini aniqlash usuli shu.")],
 ai=r"""Sen elektrodinamika bo‘yicha repetitorsan. Mavzu: Lorens kuchi.
Menga kesishgan \(\vec E\perp\vec B\) maydonlarda tinch holatdan boshlagan zarra sikloida bo‘ylab harakatlanishini savollar orqali tushuntir: dreyf tezligi \(E/B\), harakat tenglamalari, yechim. So‘ng Python’da Boris usuli bilan trayektoriyani integrallash topshirig‘ini ber. Formulalarni LaTeX’da yoz.""",
 quiz=[
  (r"Lorens kuchi:", [r"\(q\vec E+q\vec v\times\vec B\)", r"\(q\vec v\cdot\vec B\)", r"\(qE+qvB\) har doim", r"\(I\vec l\times\vec B\)"], 0, "To‘liq ifoda."),
  (r"Magnit maydonda aylana radiusi:", [r"\(mv/qB\)", r"\(qB/mv\)", r"\(mvB/q\)", r"\(qvB/m\)"], 0, r"\(qvB=mv^2/r\)."),
  (r"Siklotron davri:", [r"\(2\pi m/qB\)", r"\(2\pi qB/m\)", r"\(2\pi r/qB\)", r"\(mv/qB\)"], 0, "Tezlikka bog‘liq emas."),
  (r"Amper kuchi:", [r"\(IBl\sin\alpha\)", r"\(IBl\cos\alpha\)", r"\(qvB\)", r"\(\mu_0I/2\pi r\)"], 0, "Tokli o‘tkazgichga."),
  (r"Magnit kuchning zarra ustida bajargan ishi:", ["0", r"\(qvBr\)", r"\(mv^2/2\)", "har doim musbat"], 0, r"\(\vec F\perp\vec v\)."),
  (r"Tezlik filtri sharti:", [r"\(v=E/B\)", r"\(v=B/E\)", r"\(v=EB\)", r"\(v=qE/m\)"], 0, "Elektr va magnit kuchlar muvozanati."),
  (r"Xoll doimiysi:", [r"\(1/nq\)", r"\(nq\)", r"\(\sigma/n\)", r"\(n/q\)"], 0, r"\(R_H=1/nq\)."),
  (r"Parallel toklar (bir yo‘nalishda):", ["tortishadi", "itariladi", "ta’sirlashmaydi", "buriladi"], 0, "Amper tajribasi."),
  (r"Tezlik \(\vec B\) ga burchak ostida bo‘lsa, trayektoriya:", ["vint chiziq", "aylana", "to‘g‘ri chiziq", "parabola"], 0, r"\(v_\parallel\) saqlanadi."),
  (r"Tokli ramkaga moment:", [r"\(\vec p_m\times\vec B\)", r"\(\vec p_m\cdot\vec B\)", r"\(IB/S\)", "0"], 0, "Elektr dvigatel asosi.")],
 blits=["Qutb yog‘dusi nima uchun faqat qutblar yaqinida?", "Elektr dvigatel qanday ishlaydi?", "Smartfondagi kompas qaysi effektga asoslangan?", "Massa-spektrometr izotoplarni qanday ajratadi?"]))

L.append(dict(
 n=12, short=r"Moddaning magnit xossalari", sim="hyster", refs=[1, 2, 3], intl=["purcell", "kittel", "sivukhin"], tn=["TN2", "TN5", "TN7"],
 title=r"Moddalarning magnit xossalari. Magnitlanganlik. Diamagnetizm, paramagnetizm, ferromagnetizm",
 goal=r"Atom va molekulalarning magnit momentlarini, moddaning magnitlanganligi va magnit maydon kuchlanganligini, modda uchun to‘la tok qonunini hamda dia-, para- va ferromagnetiklarning xossalari va gisterezis hodisasini o‘rganish.",
 outcomes=[r"elektronning orbital va spin magnit momentini, Bor magnetonini tushuntiradi;",
           r"\(\vec B=\mu_0(\vec H+\vec M)\), \(\vec M=\chi\vec H\), \(\mu=1+\chi\) bog‘lanishlarni qo‘llaydi;",
           r"dia-, para- va ferromagnetiklarni \(\chi\) qiymati va mexanizmi bo‘yicha tasniflaydi;",
           r"gisterezis sirtmog‘idan qoldiq induksiya, koersitiv kuch va energiya isroflarini aniqlaydi."],
 plan=["Atom va molekulalarning magnit momentlari", "Magnitlanganlik va magnit maydon kuchlanganligi", "Diamagnetizm va paramagnetizm", "Ferromagnetizm va domenlar", "Magnit gisterezisi"],
 terms=["magnitlanganlik", "magnit qabul qiluvchanlik", "magnit singdiruvchanlik", "Bor magnetoni", "Kyuri nuqtasi", "gisterezis"],
 theory=[
  ("Atomning magnit momenti", r"""<p>Orbitadagi elektron — elementar tok: \(p_m=IS=\dfrac{evr}{2}\); orbital mexanik moment bilan bog‘lanishi \(\vec p_m=-\dfrac{e}{2m}\vec L\). Kvant mexanikasida magnit moment birligi — <b>Bor magnetoni</b> \(\mu_B=\dfrac{e\hbar}{2m}=9{,}27\cdot10^{-24}\) A·m². Elektron xususiy (spin) magnit momentiga ham ega. Atomning magnit momenti elektronlarning orbital va spin momentlari yig‘indisi.</p>"""),
  ("Magnitlanganlik", r"""<p>Birlik hajmdagi magnit moment — <b>magnitlanganlik</b> \(\vec M=\sum\vec p_m/\Delta V\) (A/m). Magnit maydon kuchlanganligi \(\vec H\) kiritiladi:</p>
$$\vec B=\mu_0(\vec H+\vec M),\quad\vec M=\chi\vec H,\quad\vec B=\mu_0\mu\vec H,\ \mu=1+\chi;\qquad\oint\vec H\cdot d\vec l=\sum I_{o‘tk}.$$
<p>\(\vec H\) sirkulyatsiyasi faqat o‘tkazuvchanlik toklariga bog‘liq (molekulyar toklar hisobga olinmaydi) — elektrostatikadagi \(\vec D\) analogi.</p>"""),
  ("Dia- va paramagnetiklar", r"""<p><b>Diamagnetiklar</b> (\(\chi\sim-10^{-5}\), Bi, Cu, H₂O): tashqi maydon elektron orbitalarining pretsessiyasini (Larmor) yuzaga keltiradi va maydonga qarshi moment induksiyalanadi; barcha moddalarda bor, haroratga bog‘liq emas. O‘ta o‘tkazgich — ideal diamagnetik (\(\chi=-1\), Meysner effekti). <b>Paramagnetiklar</b> (\(\chi\sim10^{-5}\ldots10^{-3}\), Al, O₂, Pt): atomlar doimiy magnit momentiga ega, maydon ularni yo‘naltiradi; Kyuri qonuni \(\chi=C/T\).</p>"""),
  ("Ferromagnetiklar va gisterezis", r"""<p><b>Ferromagnetiklar</b> (Fe, Ni, Co, ularning qotishmalari): \(\mu\sim10^2\ldots10^5\), \(\mu\) maydonga bog‘liq, to‘yinish va gisterezis kuzatiladi. Sababi — almashinuv o‘zaro ta’siri tufayli spinlar parallel joylashgan <b>domenlar</b>. Kyuri haroratidan yuqorida (temir uchun 1043 K) ferromagnetik paramagnetikka aylanadi (Kyuri–Veyss qonuni \(\chi=C/(T-T_C)\)).</p>
<p><b>Gisterezis sirtmog‘i</b>: \(B_r\) — qoldiq induksiya, \(H_c\) — koersitiv kuch. Yumshoq ferromagnetiklar (kichik \(H_c\), tor sirtmoq) transformator o‘zaklarida, qattiqlari (katta \(H_c\)) doimiy magnitlarda ishlatiladi. Bir siklda birlik hajmdagi isrof sirtmoq yuzasiga teng: \(w=\oint H\,dB\).</p>""")],
 example=(r"Temir o‘zakli solenoid",
  r"Solenoidda \(n=500\) m⁻¹, tok 0,2 A. O‘zak magnit singdiruvchanligi \(\mu=2000\). \(H\), \(B\), \(M\) va o‘zaksiz induksiyani toping. Temir to‘yinish magnitlanganligi \(M_s=1{,}7\cdot10^6\) A/m bo‘lsa, to‘yinish induksiyasi taxminan qancha?",
  r"\(H=nI=100\) A/m. O‘zaksiz \(B_0=\mu_0H=0{,}126\) mT. O‘zak bilan \(B=\mu_0\mu H=0{,}251\) T — 2000 marta katta. \(M=(\mu-1)H\approx2\cdot10^5\) A/m. To‘yinishda \(B_s\approx\mu_0M_s=2{,}1\) T."),
 simtask=[r"“Ferromagnetik” rejimida \(H\) amplitudasini oshirib, sirtmoq to‘yinishga chiqishini kuzating.",
          r"Koersitiv kuchni o‘zgartirib, “yumshoq” va “qattiq” materiallarni taqqoslang: isrof (sirtmoq yuzasi) qanday o‘zgaradi?",
          r"Dia- va paramagnetik rejimlarida \(M(H)\) chiziqlarining qiyaligini ferromagnetik bilan solishtiring."],
 mistakes=[(r"“Magnitlar faqat temirni tortadi, boshqa moddalar magnit emas.”", r"Barcha moddalar magnit maydonga javob beradi; dia- va paramagnetiklarda effekt juda kuchsiz."),
           (r"“Ferromagnetikning \(\mu\) o‘zgarmas.”", r"\(\mu\) maydonga va tarixga (gisterezis) bog‘liq."),
           (r"“\(\vec B\) va \(\vec H\) bir xil kattalik.”", r"\(\vec B=\mu_0(\vec H+\vec M)\); \(\vec H\) faqat o‘tkazuvchanlik toklariga bog‘liq.")],
 ai=r"""Sen magnit materiallar bo‘yicha repetitorsan. Mavzu: ferromagnetizm va gisterezis.
Menga transformator o‘zagi va doimiy magnit uchun material tanlash mezonlarini (\(B_r\), \(H_c\), isrof) savollar orqali tushuntir. So‘ng gisterezis sirtmog‘i yuzasidan quvvat isrofini hisoblash masalasini ber. Formulalarni LaTeX’da yoz.""",
 quiz=[
  (r"\(\vec B\), \(\vec H\), \(\vec M\) bog‘lanishi:", [r"\(\vec B=\mu_0(\vec H+\vec M)\)", r"\(\vec B=\vec H+\vec M\)", r"\(\vec H=\mu_0(\vec B+\vec M)\)", r"\(\vec M=\mu_0\vec B\)"], 0, "Ta’rif."),
  (r"Diamagnetik uchun \(\chi\):", ["kichik manfiy", "kichik musbat", "juda katta", "1"], 0, r"\(\sim-10^{-5}\)."),
  (r"Paramagnetik \(\chi\) haroratga:", [r"\(1/T\) bo‘yicha bog‘liq", "bog‘liq emas", r"\(T\) ga proporsional", r"\(T^2\)"], 0, "Kyuri qonuni."),
  (r"Bor magnetoni:", [r"\(e\hbar/2m\)", r"\(e\hbar/m\)", r"\(\hbar/2e\)", r"\(em/2\hbar\)"], 0, r"\(9{,}27\cdot10^{-24}\) A·m²."),
  (r"Kyuri nuqtasidan yuqorida ferromagnetik:", ["paramagnetikka aylanadi", "diamagnetikka aylanadi", "o‘ta o‘tkazgich bo‘ladi", "o‘zgarmaydi"], 0, "Domenlar yo‘qoladi."),
  (r"Koersitiv kuch:", [r"magnitlanganlikni yo‘qotish uchun kerak bo‘lgan \(H\)", "qoldiq induksiya", "to‘yinish maydoni", "Kyuri harorati"], 0, r"\(H_c\)."),
  (r"Transformator o‘zagi uchun:", ["yumshoq ferromagnetik", "qattiq ferromagnetik", "diamagnetik", "paramagnetik"], 0, "Kichik isrof."),
  (r"Gisterezis isrofi:", ["sirtmoq yuzasiga proporsional", r"\(B_r\) ga teng", "nol", "chastotaga bog‘liq emas"], 0, r"\(\oint H\,dB\)."),
  (r"O‘ta o‘tkazgich uchun \(\chi\):", ["−1", "0", "+1", "∞"], 0, "Meysner effekti."),
  (r"\(\vec H\) sirkulyatsiyasi nimaga bog‘liq?", ["o‘tkazuvchanlik toklariga", "molekulyar toklarga", r"\(\mu\) ga", "magnitlanganlikka"], 0, "To‘la tok qonuni (moddada).")],
 blits=["Qurbaqani magnitda “uchirish” mumkinmi?", "Nima uchun qizdirilgan magnit xossasini yo‘qotadi?", "Qattiq diskda ma’lumot qanday yoziladi?", "Kislorod suyuqligi magnitga tortiladimi?"]))

L.append(dict(
 n=13, short=r"Elektromagnit induksiya", sim="rl", refs=[1, 2, 3], intl=["halliday", "purcell", "feynman2"], tn=["TN2", "TN4", "TN9"],
 title=r"Elektromagnit induksiya hodisasi. Induksiya EYuK. O‘zaro induksiya va o‘zinduksiya. Magnit maydon energiyasi",
 goal=r"Faradeyning elektromagnit induksiya qonunini va Lens qoidasini, induksiya EYuK ni hisoblashni, o‘zaro induksiya va o‘zinduksiyani, zanjirda tokning qaror topishi va yo‘qolishini hamda magnit maydon energiyasini o‘rganish.",
 outcomes=[r"Faradey qonunini \(\mathcal E=-d\Phi/dt\) va Lens qoidasini qo‘llaydi;",
           r"harakatdagi o‘tkazgich va aylanayotgan ramkada EYuK ni hisoblaydi;",
           r"induktivlikni hisoblaydi va RL zanjirida tokning o‘tish jarayonlarini tahlil qiladi;",
           r"magnit maydon energiyasini \(W=LI^2/2\), \(w=B^2/2\mu_0\mu\) bilan topadi."],
 plan=["Elektromagnit induksiya hodisasi", "Faradey qonuni va Lens qoidasi", "Induksiya EYuK ni hisoblash", "O‘zinduksiya va o‘zaro induksiya", "Tokning qaror topishi va yo‘qolishi; magnit maydon energiyasi"],
 terms=["elektromagnit induksiya", "Lens qoidasi", "induktivlik", "genri", "o‘zaro induksiya", "Fuko toklari"],
 theory=[
  ("Faradey qonuni", r"""<p>Yopiq kontur bilan ilashgan magnit oqimi o‘zgarganda unda induksiya toki paydo bo‘ladi (Faradey, 1831):</p>
$$\mathcal E_i=-\frac{d\Phi}{dt},\qquad\mathcal E_i=-N\frac{d\Phi}{dt}=-\frac{d\Psi}{dt}.$$
<p><b>Lens qoidasi</b> (minus ishora): induksiya toki o‘zini vujudga keltirgan sababga qarshilik qiladigan yo‘nalishda bo‘ladi — energiyaning saqlanish qonunining natijasi. Differensial shakl (Maksvellning ikkinchi tenglamasi): \(\nabla\times\vec E=-\partial\vec B/\partial t\) — o‘zgaruvchan magnit maydon uyurmaviy elektr maydon hosil qiladi.</p>"""),
  ("EYuK ni hisoblash", r"""<ul><li>Maydonda \(v\) tezlik bilan harakatlanayotgan sterjen: \(\mathcal E=Bvl\) (Lorens kuchi natijasi).</li><li>\(\omega\) bilan aylanayotgan ramka (\(N\) o‘ram, yuza \(S\)): \(\mathcal E=NBS\omega\sin\omega t\) — o‘zgaruvchan tok generatori.</li><li>Massiv o‘tkazgichlarda <b>Fuko (uyurma) toklari</b> — induksion pechlar, elektromagnit tormoz; isroflarni kamaytirish uchun o‘zaklar plastinkalardan yig‘iladi.</li></ul>"""),
  ("O‘zinduksiya va o‘zaro induksiya", r"""<p>Kontur o‘z toki magnit oqimi bilan ilashgan: \(\Psi=LI\), \(L\) — induktivlik (genri). O‘zinduksiya EYuK \(\mathcal E_s=-L\,dI/dt\). Solenoid: \(L=\mu_0\mu n^2V=\mu_0\mu\dfrac{N^2S}{l}\). Ikki kontur: \(\Psi_{21}=L_{21}I_1\), \(L_{12}=L_{21}=M\) — o‘zaro induktivlik (transformator asosi).</p>"""),
  ("RL zanjir va energiya", r"""<p>EYuK \(\mathcal E\) manba ulanganda: \(I(t)=\dfrac{\mathcal E}{R}\left(1-e^{-t/\tau}\right)\); uzilganda: \(I=I_0e^{-t/\tau}\), \(\tau=L/R\). Magnit maydon energiyasi:</p>
$$W=\frac{LI^2}{2},\qquad w=\frac{B^2}{2\mu_0\mu}=\frac{BH}{2}.$$""")],
 example=(r"Induksiya EYuK, induktivlik va RL zanjir",
  r"1) Uzunligi 0,5 m sterjen \(B=0{,}2\) T maydonda 4 m/s tezlik bilan harakatlanmoqda. EYuK? 2) 200 o‘ramli, yuzasi 100 sm² g‘altakdagi induksiya 0,1 s da 0,5 T ga tekis o‘zgardi. EYuK? 3) 1000 o‘ramli, uzunligi 50 sm, kesimi 10 sm² solenoid induktivligi? 4) \(L=0{,}5\) H, \(R=10\) Ω: vaqt doimiysi va \(\mathcal E=10\) V da barqaror tokdagi energiya?",
  r"1) \(\mathcal E=Bvl=0{,}4\) V. 2) \(\mathcal E=NS\Delta B/\Delta t=200\cdot0{,}01\cdot5=10\) V. 3) \(L=\mu_0N^2S/l=4\pi\cdot10^{-7}\cdot10^6\cdot10^{-3}/0{,}5=2{,}51\) mH. 4) \(\tau=L/R=50\) ms; \(I=1\) A, \(W=LI^2/2=0{,}25\) J; \(t=\tau\) da tok 63 % ga yetadi."),
 simtask=[r"Kalitni ulab, tok \(\tau=L/R\) vaqtda 63 % ga yetishini grafikdan tekshiring.",
          r"Induktivlikni oshiring: o‘tish jarayoni qanday cho‘ziladi? Qarshilikni oshiring-chi?",
          r"Uzish rejimida o‘zinduksiya EYuK grafigini kuzating: nima uchun kalit uzilganda uchqun chiqadi?"],
 mistakes=[(r"“Induksiya toki magnit maydon kuchli bo‘lgani uchun paydo bo‘ladi.”", r"Faqat oqim o‘zgarganda; o‘zgarmas kuchli maydon EYuK bermaydi."),
           (r"“Lens qoidasi — maydon yo‘nalishi bilan tok yo‘nalishi bir xil.”", r"Induksiya toki oqim o‘zgarishiga qarshilik qiladi: oqim ortsa — qarshi, kamaysa — bir yo‘nalishda."),
           (r"“Induktivlik tokka bog‘liq.”", r"\(L\) geometriya va \(\mu\) ga bog‘liq (ferromagnitsiz holda).")],
 ai=r"""Sen elektromagnit induksiya bo‘yicha repetitorsan. Mavzu: Faradey qonuni va Lens qoidasi.
Menga magnit halqa ichidan tushayotgan magnit (Lens trubkasi) tajribasini savollar orqali tushuntir: oqim o‘zgarishi, induksiya toki yo‘nalishi, tormozlovchi kuch, energiya. So‘ng RL zanjir tenglamasini Python’da sonli yechish topshirig‘ini ber. Formulalarni LaTeX’da yoz.""",
 quiz=[
  (r"Faradey qonuni:", [r"\(\mathcal E=-d\Phi/dt\)", r"\(\mathcal E=d\Phi/dI\)", r"\(\mathcal E=\Phi t\)", r"\(\mathcal E=-LI\)"], 0, "Induksiya EYuK."),
  (r"Lens qoidasi qaysi qonunning natijasi?", ["energiyaning saqlanishi", "zaryadning saqlanishi", "Kulon qonuni", "Om qonuni"], 0, "Aks holda perpetuum mobile bo‘lardi."),
  (r"Harakatdagi sterjen EYuK:", [r"\(Bvl\)", r"\(Bv/l\)", r"\(Bl/v\)", r"\(B^2vl\)"], 0, "Lorens kuchidan."),
  (r"Solenoid induktivligi:", [r"\(\mu_0\mu N^2S/l\)", r"\(\mu_0NS/l\)", r"\(\mu_0N^2l/S\)", r"\(\mu_0NI\)"], 0, "Oqim ilashishidan."),
  (r"RL zanjir vaqt doimiysi:", [r"\(L/R\)", r"\(RL\)", r"\(R/L\)", r"\(\sqrt{LR}\)"], 0, "Ta’rif."),
  (r"Magnit maydon energiyasi:", [r"\(LI^2/2\)", r"\(LI\)", r"\(L^2I/2\)", r"\(CU^2/2\)"], 0, "Induktivlikda."),
  (r"Induktivlik birligi:", ["genri", "veber", "tesla", "farad"], 0, "H = Wb/A."),
  (r"Energiya zichligi:", [r"\(B^2/2\mu_0\mu\)", r"\(\mu_0B^2/2\)", r"\(B/2\mu_0\)", r"\(\varepsilon_0E^2\)"], 0, "J/m³."),
  (r"\(t=\tau\) da (ulash) tok barqaror qiymatning:", ["63 %", "50 %", "37 %", "100 %"], 0, r"\(1-e^{-1}\)."),
  (r"Transformator ishlashi asosida:", ["o‘zaro induksiya", "Xoll effekti", "termoelektrik effekt", "pyezoeffekt"], 0, "Umumiy magnit oqimi.")],
 blits=["Induksion plita qanday qilib idishni qizdiradi?", "Velosiped dinamosi qanday ishlaydi?", "Nima uchun transformator o‘zagi plastinkalardan yig‘iladi?", "Simsiz zaryadlash qaysi hodisaga asoslangan?"]))

L.append(dict(
 n=14, short=r"Elektromagnit tebranishlar va to‘lqinlar. Maksvell tenglamalari", sim="wave", refs=[1, 2, 3], intl=["feynman2", "griffiths", "purcell"], tn=["TN2", "TN5", "TN7", "TN10"],
 title=r"Elektromagnit tebranishlar. Maksvell tenglamalari. Elektromagnit to‘lqinlar va ularning xossalari",
 goal=r"Tebranish konturidagi xususiy so‘nmas, so‘nuvchi va majburiy elektromagnit tebranishlarni, siljish toki va Maksvell tenglamalari sistemasini, elektromagnit to‘lqinlarning paydo bo‘lishi va xossalarini o‘rganish.",
 outcomes=[r"LC konturda Tomson formulasini keltirib chiqaradi va energiya almashinuvini tushuntiradi;",
           r"RLC konturda so‘nish koeffitsiyenti, logarifmik dekrement va asllikni hisoblaydi;",
           r"Maksvell tenglamalarini integral va differensial ko‘rinishda yozadi, fizik ma’nosini izohlaydi;",
           r"elektromagnit to‘lqin tezligi, \(E/B\) nisbati, intensivligi va Umov–Poynting vektorini hisoblaydi."],
 plan=["Xususiy so‘nmas tebranishlar (LC kontur)", "So‘nuvchi va majburiy tebranishlar", "Siljish toki", "Maksvell tenglamalari sistemasi", "Elektromagnit to‘lqinlar va ularning xossalari"],
 terms=["tebranish konturi", "Tomson formulasi", "asllik", "siljish toki", "Maksvell tenglamalari", "Umov–Poynting vektori"],
 theory=[
  ("Tebranish konturi", r"""<p>LC konturda kondensator elektr energiyasi induktivlik magnit energiyasiga davriy aylanadi. Kirxgof qoidasidan:</p>
$$\ddot q+\omega_0^2q=0,\quad\omega_0=\frac{1}{\sqrt{LC}},\quad T=2\pi\sqrt{LC}\ (\text{Tomson formulasi}).$$
<p>To‘liq energiya \(W=\dfrac{q^2}{2C}+\dfrac{LI^2}{2}=\text{const}\). Qarshilik bo‘lsa: \(\ddot q+2\beta\dot q+\omega_0^2q=0\), \(\beta=R/2L\), \(q=q_0e^{-\beta t}\cos\omega t\), \(\omega=\sqrt{\omega_0^2-\beta^2}\); asllik \(Q=\dfrac{1}{R}\sqrt{\dfrac LC}\); kritik qarshilik \(R_{kr}=2\sqrt{L/C}\). Tashqi o‘zgaruvchan EYuK ta’sirida majburiy tebranishlar va rezonans yuzaga keladi (M15).</p>"""),
  ("Siljish toki va Maksvell tenglamalari", r"""<p>Kondensator orqali o‘tkazuvchanlik toki o‘tmaydi, lekin zanjirda tok bor — Maksvell <b>siljish toki</b>ni kiritdi: \(\vec j_{sil}=\partial\vec D/\partial t\). U ham magnit maydon hosil qiladi.</p>
$$\oint\vec E\cdot d\vec l=-\frac{d}{dt}\int\vec B\cdot d\vec S,\qquad\oint\vec H\cdot d\vec l=\int\left(\vec j+\frac{\partial\vec D}{\partial t}\right)\cdot d\vec S,$$
$$\oint\vec D\cdot d\vec S=q,\qquad\oint\vec B\cdot d\vec S=0;\qquad\vec D=\varepsilon_0\varepsilon\vec E,\ \vec B=\mu_0\mu\vec H,\ \vec j=\sigma\vec E.$$
<p>Birinchi juftlik: o‘zgaruvchan magnit maydon uyurmaviy elektr maydon hosil qiladi va aksincha. Bu ikki maydonning bir-birini “tug‘dirishi” fazoda tarqaluvchi to‘lqinni beradi.</p>"""),
  ("Elektromagnit to‘lqinlar", r"""<p>Maksvell tenglamalaridan to‘lqin tenglamasi kelib chiqadi: \(\nabla^2\vec E=\dfrac{1}{v^2}\dfrac{\partial^2\vec E}{\partial t^2}\), \(v=\dfrac{c}{\sqrt{\varepsilon\mu}}\), \(c=\dfrac{1}{\sqrt{\varepsilon_0\mu_0}}=3\cdot10^8\) m/s. Yassi to‘lqin: \(\vec E\perp\vec B\perp\vec v\) (ko‘ndalang), \(E\) va \(B\) bir fazada, \(E=vB\). Gers tajribasi (1888) ularni tajribada isbotladi.</p>"""),
  ("Energiya va impuls", r"""<p>Energiya oqimi zichligi — <b>Umov–Poynting vektori</b> \(\vec S=\vec E\times\vec H\); o‘rtacha intensivlik \(I=\dfrac12c\varepsilon_0E_0^2\). To‘lqin impuls tashiydi va bosim beradi: \(p=I/c\) (yutilganda), \(2I/c\) (qaytganda). Elektromagnit to‘lqinlar shkalasi: radioto‘lqinlar, mikroto‘lqinlar, infraqizil, ko‘rinadigan yorug‘lik (380–760 nm), ultrabinafsha, rentgen, gamma nurlari.</p>""")],
 example=(r"Tebranish konturi va elektromagnit to‘lqin",
  r"1) \(L=10\) mH, \(C=1\) mkF kontur: \(\omega_0\), \(f\), \(T\). \(R=20\) Ω bo‘lsa, \(\beta\) va asllik? 2) Yassi elektromagnit to‘lqinda \(E_0=100\) V/m. \(B_0\) va o‘rtacha intensivlik?",
  r"1) \(\omega_0=1/\sqrt{LC}=10^4\) rad/s, \(f=1{,}59\) kGs, \(T=0{,}628\) ms. \(\beta=R/2L=1000\) s⁻¹, \(Q=\sqrt{L/C}/R=100/20=5\). 2) \(B_0=E_0/c=3{,}3\cdot10^{-7}\) T; \(I=c\varepsilon_0E_0^2/2=13{,}3\) W/m² (Quyosh nurlari ~1000 W/m²)."),
 simtask=[r"To‘lqin animatsiyasida \(\vec E\) va \(\vec B\) bir-biriga va tarqalish yo‘nalishiga perpendikulyar ekanini kuzating.",
          r"Muhit sindirish ko‘rsatkichini (\(n=\sqrt{\varepsilon\mu}\)) oshiring: to‘lqin uzunligi va tezligi qanday o‘zgaradi?",
          r"Amplitudani 2 marta oshiring: intensivlik necha marta ortadi?"],
 mistakes=[(r"“Elektromagnit to‘lqin tarqalishi uchun muhit kerak.”", r"Vakuumda ham tarqaladi — maydonlar bir-birini hosil qiladi."),
           (r"“To‘lqinda \(E\) maksimum bo‘lganda \(B\) nol.”", r"Yassi yuguruvchi to‘lqinda \(E\) va \(B\) bir fazada; LC konturda esa energiya almashinadi."),
           (r"“Siljish toki — zaryadlar harakati.”", r"Siljish toki — o‘zgaruvchan elektr maydon; u ham magnit maydon hosil qiladi.")],
 ai=r"""Sen elektrodinamika bo‘yicha repetitorsan. Mavzu: Maksvell tenglamalari va elektromagnit to‘lqinlar.
Menga vakuumdagi Maksvell tenglamalaridan to‘lqin tenglamasini keltirib chiqarishni savollar bilan o‘rgat (\(\nabla\times\nabla\times\vec E\) ayniyati). So‘ng \(c=1/\sqrt{\varepsilon_0\mu_0}\) ni son bilan hisoblashimni so‘ra. Formulalarni LaTeX’da yoz.""",
 quiz=[
  (r"Tomson formulasi:", [r"\(T=2\pi\sqrt{LC}\)", r"\(T=2\pi LC\)", r"\(T=2\pi\sqrt{L/C}\)", r"\(T=1/\sqrt{LC}\)"], 0, "LC kontur."),
  (r"Yorug‘lik tezligi:", [r"\(1/\sqrt{\varepsilon_0\mu_0}\)", r"\(\sqrt{\varepsilon_0\mu_0}\)", r"\(\varepsilon_0\mu_0\)", r"\(1/\varepsilon_0\mu_0\)"], 0, "Maksvell bashorati."),
  (r"Siljish toki zichligi:", [r"\(\partial\vec D/\partial t\)", r"\(\sigma\vec E\)", r"\(\partial\vec B/\partial t\)", r"\(\nabla\times\vec H\)"], 0, "Maksvell."),
  (r"Elektromagnit to‘lqin:", ["ko‘ndalang", "bo‘ylama", "aralash", "turg‘un har doim"], 0, r"\(\vec E\perp\vec B\perp\vec v\)."),
  (r"Yassi to‘lqinda \(E/B\) =", [r"\(c\)", r"\(1/c\)", r"\(c^2\)", "1"], 0, "Vakuumda."),
  (r"RLC konturda \(\beta\) =", [r"\(R/2L\)", r"\(R/L\)", r"\(2L/R\)", r"\(1/RC\)"], 0, "So‘nish koeffitsiyenti."),
  (r"Umov–Poynting vektori:", [r"\(\vec E\times\vec H\)", r"\(\vec E\cdot\vec H\)", r"\(\vec D\times\vec B\)", r"\(\varepsilon_0E^2\)"], 0, "Energiya oqimi."),
  (r"\(\oint\vec B\cdot d\vec S=0\) nimani ifodalaydi?", ["magnit monopollar yo‘qligini", "Faradey qonunini", "zaryad saqlanishini", "Gauss teoremasini elektr uchun"], 0, "Maksvell tenglamasi."),
  (r"Ko‘rinadigan yorug‘lik diapazoni:", ["380–760 nm", "1–10 mm", "0,01–1 nm", "1–100 m"], 0, "Ko‘z sezgirligi."),
  (r"Misoldagi kontur chastotasi:", ["≈ 1,6 kGs", "≈ 10 kGs", "≈ 160 Gs", "≈ 16 kGs"], 0, r"\(10^4/2\pi\).")],
 blits=["Radio qanday qilib kerakli stansiyani tanlaydi?", "Nima uchun Maksvell tenglamalari nisbiylik nazariyasiga mos?", "Quyosh yelkani qanday ishlaydi?", "Mikroto‘lqinli pech chastotasi qancha?"]))

L.append(dict(
 n=15, short=r"O‘zgaruvchan tok", sim="ac", refs=[1, 2, 4], intl=["halliday", "serway", "tipler"], tn=["TN3", "TN4", "TN9", "TN6"],
 title=r"O‘zgaruvchan tok qonunlari. Aktiv, induktiv va sig‘im qarshiliklar. Rezonans. Transformatorlar. Uch fazali tok",
 goal=r"O‘zgaruvchan tokning amplituda va effektiv qiymatlarini, aktiv, induktiv va sig‘im qarshiliklarni, vektor diagrammalar usulini, kuchlanishlar va toklar rezonansini, quvvat koeffitsiyentini hamda transformator va uch fazali tok asoslarini o‘rganish.",
 outcomes=[r"effektiv qiymatlarni \(I=I_0/\sqrt2\) bo‘yicha hisoblaydi;",
           r"\(X_L=\omega L\), \(X_C=1/\omega C\) va to‘liq qarshilik \(Z\) ni topadi, vektor diagramma quradi;",
           r"ketma-ket va parallel zanjirlarda rezonans shartlarini tahlil qiladi;",
           r"quvvat, \(\cos\varphi\), transformator nisbati va uch fazali tizim kuchlanishlarini hisoblaydi."],
 plan=["O‘zgaruvchan tok, amplituda va effektiv qiymat", "R, L, C elementlar va vektor diagrammalar", "To‘liq qarshilik va quvvat", "Rezonansning ikki turi; parallel zanjir", "Transformatorlar va uch fazali tok"],
 terms=["effektiv qiymat", "reaktiv qarshilik", "impedans", "quvvat koeffitsiyenti", "kuchlanishlar rezonansi", "transformator"],
 theory=[
  ("Effektiv qiymat va elementlar", r"""<p>\(i=I_0\sin\omega t\). <b>Effektiv (ta’sir etuvchi)</b> qiymat — shunday o‘zgarmas tokki, aktiv qarshilikda xuddi shuncha issiqlik ajratadi: \(I=I_0/\sqrt2\), \(U=U_0/\sqrt2\) (tarmoq: 220 V effektiv, amplituda 311 V).</p>
<table class="t"><thead><tr><th>Element</th><th>Qarshilik</th><th>Faza (kuchlanish tokka nisbatan)</th></tr></thead><tbody><tr><td>Rezistor R</td><td>\(R\)</td><td>0</td></tr><tr><td>G‘altak L</td><td>\(X_L=\omega L\)</td><td>\(+\pi/2\) (oldinda)</td></tr><tr><td>Kondensator C</td><td>\(X_C=1/\omega C\)</td><td>\(-\pi/2\) (orqada)</td></tr></tbody></table>"""),
  ("Ketma-ket RLC zanjir", r"""<p>Vektor diagrammadan:</p>
$$Z=\sqrt{R^2+\left(\omega L-\frac{1}{\omega C}\right)^2},\qquad I=\frac UZ,\qquad\operatorname{tg}\varphi=\frac{\omega L-1/\omega C}{R}.$$
<p>O‘rtacha quvvat \(P=UI\cos\varphi=I^2R\); \(\cos\varphi=R/Z\) — quvvat koeffitsiyenti. Reaktiv quvvat \(Q=UI\sin\varphi\), to‘liq quvvat \(S=UI\) (V·A).</p>"""),
  ("Rezonansning ikki turi", r"""<p><b>Kuchlanishlar rezonansi</b> (ketma-ket): \(\omega_0=1/\sqrt{LC}\) da \(X_L=X_C\), \(Z=R\) minimal, tok maksimal, \(U_L=U_C=QU\) — tarmoq kuchlanishidan ko‘p marta katta bo‘lishi mumkin. <b>Toklar rezonansi</b> (parallel L va C): zanjirdagi umumiy tok minimal, shoxobchalardagi toklar katta va qarama-qarshi fazada; ideal holda zanjir qarshiligi cheksiz. Radiopriyomnik konturlari, filtrlar shu hodisadan foydalanadi.</p>"""),
  ("Transformator va uch fazali tok", r"""<p><b>Transformator</b>: \(\dfrac{U_1}{U_2}=\dfrac{N_1}{N_2}=k\), \(I_1U_1\approx I_2U_2\) (FIK 95–99 %). Elektr energiyasini uzatishda kuchlanish oshiriladi — liniyadagi isrof \(I^2R\) kamayadi. <b>Uch fazali tok</b>: uchta EYuK bir xil amplitudali, fazalari \(120^\circ\) ga siljigan. Yulduz ulashda \(U_l=\sqrt3U_f\) (380 = √3·220), uchburchakda \(I_l=\sqrt3I_f\). Simmetrik yuklamada neytral simdagi tok nol. Uch fazali tok aylanuvchi magnit maydon hosil qiladi — asinxron dvigatel asosi.</p>""")],
 example=(r"RLC zanjir 50 Gs tarmoqda",
  r"\(R=100\) Ω, \(L=0{,}5\) H, \(C=10\) mkF ketma-ket 220 V, 50 Gs tarmoqqa ulangan. \(X_L\), \(X_C\), \(Z\), tok, \(\cos\varphi\), faza va aktiv quvvatni toping. Rezonans chastotasi qancha?",
  r"\(\omega=314\) rad/s. \(X_L=157{,}1\) Ω, \(X_C=318{,}3\) Ω. \(Z=\sqrt{100^2+161{,}2^2}=189{,}7\) Ω. \(I=1{,}16\) A. \(\cos\varphi=0{,}527\), \(\varphi=-58{,}2^\circ\) (sig‘im xarakterli, tok oldinda). \(P=I^2R=134\) W. \(f_0=1/(2\pi\sqrt{LC})=71{,}2\) Gs."),
 simtask=[r"Misoldagi qiymatlarni o‘rnatib, \(Z\), \(I\) va \(\cos\varphi\) ni tekshiring; vektor diagrammada \(U_L\) va \(U_C\) ni solishtiring.",
          r"Chastotani 71 Gs ga yaqinlashtiring: tok va \(U_C\) qanday o‘zgaradi? Vektor diagramma qanday ko‘rinadi?",
          r"Qarshilikni kamaytirib, rezonans egri chizig‘ining keskinlashishini (asllik ortishini) kuzating."],
 mistakes=[(r"“Voltmetr amplituda qiymatni ko‘rsatadi.”", r"Asboblar effektiv qiymatni ko‘rsatadi; amplituda \(\sqrt2\) marta katta."),
           (r"“Ketma-ket zanjirda kuchlanishlar arifmetik qo‘shiladi.”", r"Fazalari farq qiladi — vektor (kompleks) qo‘shiladi: \(U\ne U_R+U_L+U_C\)."),
           (r"“Kondensator va g‘altak energiya isrof qiladi.”", r"Ideal L va C da o‘rtacha quvvat nol — energiya manbaga qaytadi; isrof faqat \(R\) da.")],
 ai=r"""Sen elektrotexnika bo‘yicha repetitorsan. Mavzu: o‘zgaruvchan tok va vektor diagrammalar.
Menga kompleks amplitudalar usulini (\(Z=R+j(\omega L-1/\omega C)\)) savollar orqali o‘rgat va parallel RLC zanjirning umumiy tokini topishni so‘ra. So‘ng Python’da rezonans egri chizig‘ini chizish topshirig‘ini ber. Formulalarni LaTeX’da yoz.""",
 quiz=[
  (r"Effektiv qiymat:", [r"\(I_0/\sqrt2\)", r"\(I_0/2\)", r"\(\sqrt2I_0\)", r"\(I_0\)"], 0, "Sinusoidal tok."),
  (r"Induktiv qarshilik:", [r"\(\omega L\)", r"\(1/\omega L\)", r"\(L/\omega\)", r"\(\omega/L\)"], 0, "Chastota bilan ortadi."),
  (r"Sig‘im qarshilik:", [r"\(1/\omega C\)", r"\(\omega C\)", r"\(C/\omega\)", r"\(\omega/C\)"], 0, "Chastota bilan kamayadi."),
  (r"Kuchlanishlar rezonansida:", [r"\(Z=R\), tok maksimal", "tok minimal", r"\(Z\) cheksiz", r"\(\cos\varphi=0\)"], 0, r"\(X_L=X_C\)."),
  (r"Rezonans chastotasi:", [r"\(1/\sqrt{LC}\)", r"\(\sqrt{LC}\)", r"\(1/LC\)", r"\(\sqrt{L/C}\)"], 0, "Burchak chastota."),
  (r"Aktiv quvvat:", [r"\(UI\cos\varphi\)", r"\(UI\sin\varphi\)", r"\(UI\)", r"\(U^2/Z\) har doim"], 0, "O‘rtacha quvvat."),
  (r"G‘altakda kuchlanish tokdan:", [r"\(\pi/2\) oldinda", r"\(\pi/2\) orqada", "bir fazada", r"\(\pi\) ga siljigan"], 0, "Faza."),
  (r"Yulduz ulashda liniya va faza kuchlanishlari:", [r"\(U_l=\sqrt3U_f\)", r"\(U_l=U_f\)", r"\(U_l=3U_f\)", r"\(U_f=\sqrt3U_l\)"], 0, "380 = √3·220."),
  (r"Transformatorda \(U_1/U_2\) =", [r"\(N_1/N_2\)", r"\(N_2/N_1\)", r"\(I_1/I_2\)", "1"], 0, "Ideal transformator."),
  (r"Tarmoq 220 V ning amplitudasi:", ["≈ 311 V", "220 V", "≈ 156 V", "380 V"], 0, r"\(220\sqrt2\).")],
 blits=["Nima uchun elektr tarmog‘i o‘zgaruvchan tokda ishlaydi?", "Telefon zaryadlagich ichida nima bor?", "Uydagi 220 V va sanoatdagi 380 V qanday bog‘langan?", "Quvvat koeffitsiyentini oshirish nima uchun foydali?"]))
