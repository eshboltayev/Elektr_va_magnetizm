"""A1–A21 amaliy mashg'ulotlar mazmuni (Elektr va magnetizm, EM1306). Fan dasturida seminar yo'q."""

A = []
SEM = []

def _a(n, lec, sim, tn, title, goal, theory, solved, tasks, code, questions):
    A.append(dict(n=n, lec=lec, sim=sim, tn=tn, title=title, goal=goal, theory=theory, solved=solved, tasks=tasks, model=("python", code), questions=questions))

_a(1, 1, "coulomb", ["TN3", "TN4", "TN8"], r"Elektr zaryadlari. Kulon qonuni. Elektr maydon kuchlanganligi",
 r"Kulon qonuni va nuqtaviy zaryad maydon kuchlanganligi formulalarini qo‘llab, vakuum va dielektrikdagi o‘zaro ta’sir kuchlari hamda kuchlanganlikni hisoblashni o‘rganish.",
 r"""<p>\(F=\dfrac{|q_1q_2|}{4\pi\varepsilon_0\varepsilon r^2}\), \(k=\dfrac1{4\pi\varepsilon_0}=8{,}988\cdot10^9\) N·m²/C². Nuqtaviy zaryad maydoni \(E=\dfrac{|q|}{4\pi\varepsilon_0\varepsilon r^2}\), zaryadga kuch \(\vec F=q\vec E\). Zaryad kvantlangan: \(q=Ne\), \(e=1{,}602\cdot10^{-19}\) C. Ko‘paytuvchilar: 1 mkC = \(10^{-6}\) C, 1 nC = \(10^{-9}\) C.</p>""",
 [("Kerosindagi zaryadlar", r"5 nC va 8 nC zaryadlar kerosinda (\(\varepsilon=2\)) 4 sm masofada turibdi. O‘zaro ta’sir kuchi?", r"\(F=8{,}988\cdot10^9\cdot5\cdot10^{-9}\cdot8\cdot10^{-9}/(2\cdot0{,}04^2)=1{,}12\cdot10^{-4}\) N (itarish)."),
  ("Nuqtaviy zaryad maydoni", r"2 nC zaryaddan 3 sm uzoqlikdagi kuchlanganlik va shu nuqtadagi elektronga ta’sir etuvchi kuch?", r"\(E=kq/r^2=2{,}0\cdot10^4\) V/m; \(F=eE=3{,}2\cdot10^{-15}\) N (zaryad tomon)."),
  ("Muvozanat nuqtasi", r"\(+9q\) va \(+q\) zaryadlar orasidagi masofa \(d\). Uchinchi zaryadga ta’sir etuvchi kuch qayerda nolga teng?", r"\(9/x^2=1/(d-x)^2\) ⇒ \(3(d-x)=x\) ⇒ \(x=3d/4\) (katta zaryaddan). Muvozanat bo‘ylama siljishga nisbatan uchinchi zaryad ishorasiga bog‘liq.")],
 [(r"+1 nC zaryad hosil qilish uchun jismdan nechta elektron olish kerak?", r"\(6{,}24\cdot10^9\)"),
  (r"Protonga ta’sir etuvchi elektr kuchi uning og‘irligiga teng bo‘lishi uchun maydon qancha bo‘lishi kerak?", r"\(E=mg/e=1{,}02\cdot10^{-7}\) V/m"),
  (r"Ikki zaryad orasidagi masofa 3 marta kamaysa va har bir zaryad 3 marta oshsa, kuch qanday o‘zgaradi?", "81 marta ortadi"),
  (r"Vodorod atomida elektron va proton orasidagi tortishish kuchi (\(r=0{,}529\cdot10^{-10}\) m)?", r"\(8{,}2\cdot10^{-8}\) N")],
 r"""import numpy as np
k = 8.988e9
def coulomb(q1, q2, r1, r2, eps=1.0):
    r = np.array(r2, float) - np.array(r1, float); d = np.linalg.norm(r)
    return k*q1*q2/(eps*d**3)*r          # 1-zaryadning 2-zaryadga kuchi (vektor)
print("F =", coulomb(5e-9, 8e-9, [0, 0], [0.04, 0], eps=2), "N")
E = k*2e-9/0.03**2
print(f"E = {E:.0f} V/m, elektronga kuch = {1.602e-19*E:.2e} N")""",
 ["Zaryadning qaysi xossalarini bilasiz?", "Kulon qonunining qo‘llanish chegaralari?", "Kuch va kuchlanganlik qanday bog‘langan?", "Dielektrik muhit kuchni nima uchun kamaytiradi?"])

_a(2, 2, "field", ["TN3", "TN4", "TN8"], r"Maydonlar superpozitsiyasi prinsipi. Elektr maydonlarni hisoblash",
 r"Bir necha nuqtaviy zaryad va uzluksiz taqsimlangan zaryadlar maydonini superpozitsiya prinsipi asosida vektor qo‘shish va integrallash orqali hisoblash.",
 r"""<p>\(\vec E=\sum\vec E_i\). Hisoblash tartibi: 1) har bir zaryad maydonining modulini toping; 2) chizmada yo‘nalishlarini ko‘rsating; 3) o‘qlarga proyeksiyalab qo‘shing: \(E_x=\sum E_{ix}\), \(E_y=\sum E_{iy}\), \(E=\sqrt{E_x^2+E_y^2}\). Simmetriyadan foydalaning — ko‘p tashkil etuvchilar o‘zaro yo‘qoladi. Uzluksiz zaryad: \(d\vec E=k\,dq\,\vec r/r^3\).</p>""",
 [("Teng tomonli uchburchak", r"Tomoni 10 sm teng tomonli uchburchak uchlarida 10 nC dan zaryadlar. Markazdagi kuchlanganlik va bitta zaryadga ta’sir etuvchi kuch?", r"Markazda simmetriya bo‘yicha \(E=0\). Bitta zaryadga ikki kuch \(F_1=kq^2/a^2=9\cdot10^{-5}\) N, ular orasidagi burchak 60°: \(F=\sqrt3F_1=1{,}56\cdot10^{-4}\) N, burchak bissektrisasi bo‘ylab tashqariga."),
  ("Kvadrat uchlaridagi zaryadlar", r"Tomoni 10 sm kvadratning bir tomonidagi ikki uchida \(+1\) nC, qarama-qarshi tomonidagi ikki uchida \(-1\) nC zaryad. Markazdagi \(E\)?", r"Har bir zaryad maydoni \(kq/(a^2/2)=1798\) V/m. Musbatlardan uzoqlashuvchi, manfiylarga yo‘nalgan maydonlarning tomonlarga parallel tashkil etuvchilari yo‘qoladi, perpendikulyarlari qo‘shiladi: \(E=4\cdot1798\cdot\cos45^\circ=5085\) V/m, musbat tomondan manfiy tomonga."),
  ("Zaryadlangan halqa", r"Radiusi 5 sm halqada 10 nC zaryad. O‘qda markazdan 5 sm uzoqlikda \(E\)?", r"\(E=kqx/(R^2+x^2)^{3/2}=8{,}988\cdot10^9\cdot10^{-8}\cdot0{,}05/(0{,}005)^{3/2}=1{,}27\cdot10^4\) V/m.")],
 [(r"Ikki teng musbat zaryad orasidagi masofa \(2a\). O‘rta perpendikulyarda \(E\) maksimal bo‘ladigan masofa?", r"\(x=a/\sqrt2\)"),
  (r"Dipol (\(p=10^{-12}\) C·m) o‘qida 10 sm masofada \(E\)?", r"\(2kp/r^3=18\) V/m"),
  (r"Cheksiz ip (\(\lambda=2\) nC/m) dan 4 sm masofada \(E\)?", r"\(\lambda/2\pi\varepsilon_0r=899\) V/m"),
  (r"Tekislik (\(\sigma=1\) mkC/m²) va undan 1 m uzoqlikdagi 1 nC zaryad: kuch?", r"\(q\sigma/2\varepsilon_0=56{,}5\) mkN")],
 r"""import numpy as np
k = 8.988e9
def E_field(charges, P):
    P = np.array(P, float); E = np.zeros(2)
    for q, (x, y) in charges:
        r = P - np.array([x, y]); E += k*q*r/np.linalg.norm(r)**3
    return E
a = 0.1
sq = [(1e-9, (0, 0)), (1e-9, (a, 0)), (-1e-9, (a, a)), (-1e-9, (0, a))]
E = E_field(sq, [a/2, a/2]); print("Kvadrat markazi: E =", E.round(1), "|E| =", round(np.linalg.norm(E), 1), "V/m")
# Halqa: sonli integrallash (N bo'lak)
R, q, x, N = 0.05, 1e-8, 0.05, 2000
phi = np.linspace(0, 2*np.pi, N, endpoint=False)
r = np.stack([x - 0*phi, -R*np.cos(phi), -R*np.sin(phi)], 1)
Ex = np.sum(k*(q/N)*r[:, 0]/np.linalg.norm(r, axis=1)**3)
print(f"Halqa o'qida: sonli {Ex:.0f} V/m, formula {k*q*x/(R**2+x**2)**1.5:.0f} V/m")""",
 ["Superpozitsiya prinsipi qaysi tajribaviy faktga asoslangan?", "Simmetriyadan qanday foydalanamiz?", "Uzluksiz zaryadni qanday bo‘laklarga ajratamiz?", "Dipol maydonining nuqtaviy zaryad maydonidan farqi?"])

_a(3, 3, "field", ["TN2", "TN4", "TN7"], r"Kuchlanganlik va induksiya vektorlari chiziqlari. Induksiya vektori oqimi. Gauss teoremasi",
 r"Kuchlanganlik va elektr induksiya vektorlari oqimini hisoblash, Gauss teoremasini turli yopiq sirtlar uchun qo‘llash.",
 r"""<p>Bir jinsli maydonda tekis yuzadan oqim \(\Phi_E=ES\cos\alpha\) (\(\alpha\) — \(\vec E\) va normal orasidagi burchak). Gauss teoremasi: \(\oint\vec E\cdot d\vec S=q_{ich}/\varepsilon_0\), \(\oint\vec D\cdot d\vec S=q_{erkin}\). Simmetriya: zaryad kub markazida bo‘lsa, har bir yoqdan oqimning 1/6 qismi o‘tadi.</p>""",
 [("Tekis yuzadan oqim", r"\(E=200\) V/m bir jinsli maydonda 0,5 m² yuza normali maydon bilan 60° burchak tashkil etadi. Oqim?", r"\(\Phi=ES\cos60^\circ=50\) V·m."),
  ("Kub markazidagi zaryad", r"1 mkC zaryad kub markazida. Bitta yoq orqali oqim?", r"\(\Phi=q/6\varepsilon_0=1{,}88\cdot10^4\) V·m."),
  ("Bir nechta zaryad", r"Sfera ichida 2 nC va −5 nC zaryadlar, tashqarisida 10 nC. Sfera orqali oqim?", r"Faqat ichki zaryadlar: \(\Phi=(2-5)\cdot10^{-9}/\varepsilon_0=-339\) V·m (manfiy — oqim ichkariga).")],
 [(r"Nuqtaviy zaryad \(q\) yarim sfera markazida. Yarim sfera orqali oqim?", r"\(q/2\varepsilon_0\)"),
  (r"\(\vec E\) yuzaga parallel bo‘lsa, oqim?", "0"),
  (r"\(\varepsilon=5\) dielektrik ichidagi 1 nC zaryadni o‘rab olgan sirt orqali \(\vec D\) va \(\vec E\) oqimlari?", r"\(\Phi_D=1\) nC; \(\Phi_E=q/(\varepsilon_0\varepsilon)=22{,}6\) V·m"),
  (r"Yer sirtida \(E\approx130\) V/m (pastga). Yer zaryadi taxminan?", r"\(q=-4\pi\varepsilon_0R^2E\approx-5{,}9\cdot10^5\) C")],
 r"""import numpy as np
k, e0 = 8.988e9, 8.854e-12
q = 1e-6
# Kub yog'i orqali oqimni sonli integrallash (kub tomoni 2, zaryad markazda)
n = 600; s = np.linspace(-1, 1, n); X, Y = np.meshgrid(s, s); dA = (s[1]-s[0])**2
Ez = k*q*1/(X**2 + Y**2 + 1)**1.5       # z = 1 yuqori yoq
print(f"Bir yoq oqimi: sonli {Ez.sum()*dA:.0f}, nazariya q/6e0 = {q/(6*e0):.0f} V*m")""",
 ["Oqim qanday fizik ma’noga ega?", "\\(\\vec D\\) oqimi nima uchun dielektrikka bog‘liq emas?", "Gauss teoremasi qachon maydonni topishga imkon beradi?", "Manfiy oqim nimani bildiradi?"])

_a(4, 3, "gauss", ["TN2", "TN4", "TN9"], r"Gauss teoremasining turli elektrostatik maydonlarni hisoblashga tatbiqi",
 r"Gauss teoremasi yordamida zaryadlangan tekislik, tekisliklar, silindr, sfera va shar maydonlarini hisoblash va \(E(r)\) grafiklarini qurish.",
 r"""<p>Algoritm: 1) simmetriyani aniqlang (sferik, silindrik, tekis); 2) maydon moduli o‘zgarmas va sirtga perpendikulyar (yoki parallel) bo‘ladigan Gauss sirtini tanlang; 3) \(E\cdot S_{Gauss}=q_{ich}/\varepsilon_0\); 4) ichki zaryadni zichlik orqali ifodalang. Natijalar: shar ichida \(E=\rho r/3\varepsilon_0\), ip/silindr tashqarisida \(\lambda/2\pi\varepsilon_0r\), tekislik \(\sigma/2\varepsilon_0\).</p>""",
 [("Zaryadlangan silindr", r"Cheksiz uzun ip (\(\lambda=1\) nC/m). 5 sm masofadagi \(E\)?", r"Koaksial silindr: \(E\cdot2\pi rl=\lambda l/\varepsilon_0\) ⇒ \(E=360\) V/m."),
  ("Ikki parallel tekislik", r"Tekisliklar \(\pm\sigma\), \(\sigma=0{,}2\) mkC/m². Orasidagi va tashqaridagi maydon?", r"Orasida \(E=\sigma/\varepsilon_0=22{,}6\) kV/m, tashqarida 0 (maydonlar yo‘qoladi)."),
  ("Hajmiy zaryadlangan shar", r"Shar \(R=10\) sm, \(Q=10\) nC. \(r=5\) sm va \(r=20\) sm da \(E\)?", r"Ichkarida \(kQr/R^3=4494\) V/m, tashqarida \(kQ/r^2=2247\) V/m.")],
 [(r"Sferik qobiq (\(Q=5\) nC, \(R=10\) sm) markazdan 5 sm va 15 sm da \(E\)?", r"0 va 2 kV/m"),
  (r"Bir xil \(+\sigma\) zaryadlangan ikki parallel tekislik orasidagi maydon?", "0"),
  (r"Radiusi \(R\) silindr hajmi bo‘yicha zaryadlangan (\(\rho\)). Ichkarida \(E(r)\)?", r"\(E=\rho r/2\varepsilon_0\)"),
  (r"Qalinligi \(2d\) bo‘lgan cheksiz plastina hajmiy zaryad \(\rho\) bilan. Ichida \(E(x)\)?", r"\(E=\rho x/\varepsilon_0\) (\(|x|<d\))")],
 r"""import numpy as np
k = 8.988e9
Q, R = 1e-8, 0.1
for r in (0.02, 0.05, 0.1, 0.15, 0.2, 0.3):
    E = k*Q*r/R**3 if r < R else k*Q/r**2
    print(f"r = {r*100:4.0f} sm   E = {E:7.0f} V/m")""",
 ["Gauss sirtini tanlash qoidalari?", "Nima uchun shar ichida maydon chiziqli o‘sadi?", "Cheksiz tekislik maydoni nima uchun masofaga bog‘liq emas?", "Real kondensatorda chet effektlari qanday?"])

_a(5, 4, "potential", ["TN3", "TN4", "TN9"], r"Elektrostatik kuchlarning ishi. Ish va potensial energiya bog‘lanishi",
 r"Elektrostatik kuchlar ishini va zaryadlar sistemasining potensial energiyasini hisoblash, ishning yo‘lga bog‘liq emasligidan foydalanish.",
 r"""<p>\(A_{12}=\dfrac{qQ}{4\pi\varepsilon_0}\left(\dfrac1{r_1}-\dfrac1{r_2}\right)=W_1-W_2=q(\varphi_1-\varphi_2)\). Zaryadlar sistemasi potensial energiyasi \(W=\sum_{i<j}\dfrac{kq_iq_j}{r_{ij}}\). Tashqi kuch ishi maydon kuchlari ishiga teng va qarama-qarshi ishorali.</p>""",
 [("Zaryadni yaqinlashtirish", r"20 nC zaryad maydonida 2 nC zaryad 10 sm dan 5 sm gacha yaqinlashtirildi. Maydon kuchlari ishi?", r"\(A=kqQ(1/r_1-1/r_2)=8{,}988\cdot10^9\cdot4\cdot10^{-17}\cdot(10-20)=-3{,}6\) mkJ — tashqi kuch +3,6 mkJ ish bajaradi."),
  ("Uch zaryad energiyasi", r"Tomoni 10 sm teng tomonli uchburchak uchlarida 10 nC dan zaryadlar. Sistema energiyasi?", r"\(W=3kq^2/a=27\) mkJ — zaryadlarni cheksizlikdan yig‘ish uchun shuncha ish kerak."),
  ("Elektronning tezlashishi", r"Elektron tinch holatdan 500 V potensiallar farqini o‘tdi. Tezligi?", r"\(v=\sqrt{2eU/m}=1{,}33\cdot10^7\) m/s.")],
 [(r"Zaryad ekvipotensial sirt bo‘ylab ko‘chirilganda ish?", "0"),
  (r"Proton 1 kV potensiallar farqidan o‘tdi. Kinetik energiyasi (eV va J)?", r"1 keV = \(1{,}6\cdot10^{-16}\) J"),
  (r"Ikki elektron 1 nm masofada. O‘zaro potensial energiya (eV)?", "1,44 eV"),
  (r"Kvadrat uchlarida bir xil \(q\) zaryadlar (tomon \(a\)). Energiya?", r"\(W=\frac{kq^2}{a}(4+\sqrt2)\)")],
 r"""import numpy as np, itertools
k = 8.988e9
def energy(charges):
    return sum(k*q1*q2/np.linalg.norm(np.subtract(p1, p2))
               for (q1, p1), (q2, p2) in itertools.combinations(charges, 2))
a = 0.1
tri = [(1e-8, (0, 0)), (1e-8, (a, 0)), (1e-8, (a/2, a*np.sqrt(3)/2))]
print(f"Uchburchak: W = {energy(tri)*1e6:.2f} mkJ")
sq = [(1e-8, p) for p in [(0, 0), (a, 0), (a, a), (0, a)]]
print(f"Kvadrat: W = {energy(sq)*1e6:.2f} mkJ  (formula {k*1e-16/a*(4+np.sqrt(2))*1e6:.2f})")""",
 ["Nima uchun elektrostatik kuchlar ishi yo‘lga bog‘liq emas?", "Potensial energiya nolini qayerda tanlaymiz?", "Musbat va manfiy ish nimani bildiradi?", "Elektronvolt va joul bog‘lanishi?"])

_a(6, 4, "potential", ["TN2", "TN4", "TN9"], r"Elektrostatik maydon potensiali. Kuchlanganlik va potensiallar ayirmasi bog‘lanishi",
 r"Zaryadlar sistemasining potensialini, potensiallar farqini hisoblash, \(\vec E=-\nabla\varphi\) va \(U=\int\vec E\cdot d\vec l\) bog‘lanishlarni qo‘llash.",
 r"""<p>\(\varphi=\sum\dfrac{kq_i}{r_i}\); \(\vec E=-\nabla\varphi\); bir jinsli maydonda \(U=Ed\). Zaryadlangan sfera: tashqarida \(kQ/r\), ichida \(kQ/R\). Cheksiz ip: \(\Delta\varphi=\dfrac{\lambda}{2\pi\varepsilon_0}\ln\dfrac{r_2}{r_1}\). Tekisliklar: \(U=\sigma d/\varepsilon_0\).</p>""",
 [("Gradiyentdan maydon", r"Potensial \(\varphi=3x^2y-z\) (V, m). \((1;2;3)\) nuqtada \(\vec E\)?", r"\(\vec E=-\nabla\varphi=(-6xy;\,-3x^2;\,1)=(-12;\,-3;\,1)\) V/m, \(|E|=12{,}4\) V/m."),
  ("Kvadrat markazi", r"Tomoni 10 sm kvadrat uchlarida +1, +1, −1, −1 nC (bir tomonda musbatlar). Markazdagi potensial va kuchlanganlik?", r"\(\varphi=\sum kq/r=0\) (musbat va manfiy hissalar teng), lekin \(E=5085\) V/m (A2). Potensial nol — maydon nol degani emas."),
  ("Silindrik kondensator", r"Ip (\(\lambda=1\) nC/m) va unga koaksial silindr: \(r_1=1\) mm, \(r_2=1\) sm. Potensiallar farqi?", r"\(U=\frac{\lambda}{2\pi\varepsilon_0}\ln10=41{,}4\) V.")],
 [(r"Bir jinsli maydonda 2 sm masofadagi potensiallar farqi 100 V. \(E\)?", "5 kV/m"),
  (r"Radiusi 5 sm sfera potensiali 900 V. Zaryadi?", "5 nC"),
  (r"\(\varphi=a/r\) uchun \(E(r)\)?", r"\(E=a/r^2\)"),
  (r"Ikki teng musbat zaryad orasidagi o‘rta nuqtada \(E\) va \(\varphi\)?", r"\(E=0\), \(\varphi=2kq/(d/2)\ne0\)")],
 r"""import numpy as np
k = 8.988e9
a = 0.1
ch = [(1e-9, (0, 0)), (1e-9, (a, 0)), (-1e-9, (a, a)), (-1e-9, (0, a))]
def phi(x, y): return sum(k*q/np.hypot(x - px, y - py) for q, (px, py) in ch)
h = 1e-6; x0, y0 = a/2, a/2
Ex = -(phi(x0 + h, y0) - phi(x0 - h, y0))/(2*h); Ey = -(phi(x0, y0 + h) - phi(x0, y0 - h))/(2*h)
print(f"phi = {phi(x0, y0):.3f} V,  E = ({Ex:.0f}, {Ey:.0f}) V/m  (E = -grad phi)")""",
 ["Potensial va potensial energiya farqi?", "Ekvipotensial sirtlar va kuch chiziqlari qanday joylashadi?", "Potensial nol bo‘lgan nuqtada maydon bo‘lishi mumkinmi?", "\\(U=Ed\\) qachon to‘g‘ri?"])

_a(7, 6, "capacitor", ["TN3", "TN4", "TN9"], r"Elektr sig‘imi. Kondensatorlar. Kondensatorlarni ketma-ket va parallel ulash",
 r"Yakkalangan o‘tkazgich va kondensatorlar sig‘imini hisoblash, aralash ulangan kondensatorlar batareyasining sig‘imi, zaryadlari va kuchlanishlarini topish.",
 r"""<p>\(C=q/U\). Yassi: \(\varepsilon_0\varepsilon S/d\); sferik: \(4\pi\varepsilon_0\varepsilon\frac{R_1R_2}{R_2-R_1}\); silindrik: \(\frac{2\pi\varepsilon_0\varepsilon l}{\ln(R_2/R_1)}\). Parallel: \(C=\sum C_i\), \(U\) bir xil. Ketma-ket: \(1/C=\sum1/C_i\), \(q\) bir xil. Qatlamli dielektrik — ketma-ket kondensatorlar.</p>""",
 [("Sferik kondensator", r"\(R_1=2\) sm, \(R_2=3\) sm, havo. Sig‘im?", r"\(C=4\pi\varepsilon_0\cdot0{,}02\cdot0{,}03/0{,}01=6{,}68\) pF."),
  ("Aralash ulash", r"\(C_1=2\) mkF va \(C_2=3\) mkF parallel, ularga \(C_3=5\) mkF ketma-ket; batareya 100 V. Umumiy sig‘im, zaryadlar va kuchlanishlar?", r"\(C_{12}=5\) mkF; \(C=5\cdot5/10=2{,}5\) mkF; \(q=250\) mkC; \(U_3=50\) V, \(U_{12}=50\) V; \(q_1=100\) mkC, \(q_2=150\) mkC."),
  ("Yer sig‘imi", r"Yerni shar (\(R=6371\) km) deb sig‘imini toping.", r"\(C=4\pi\varepsilon_0R=709\) mkF — kichik! Farad juda katta birlik.")],
 [(r"Yassi kondensator oralig‘i yarmiga \(\varepsilon=3\) plastina kiritildi. Sig‘im qanday o‘zgaradi?", r"\(C'=\frac{2\varepsilon}{\varepsilon+1}C_0=1{,}5C_0\)"),
  (r"Uchta 6 mkF kondensator: barcha ulash usullari bilan qanday sig‘imlar olinadi?", "18; 2; 4; 9 mkF"),
  (r"Koaksial kabel: \(R_1=0{,}5\) mm, \(R_2=2\) mm, \(\varepsilon=2{,}3\). 1 m uzunlik sig‘imi?", "≈ 92 pF"),
  (r"Ikki kondensator ketma-ket: 1 va 4 mkF, 100 V. Kuchlanishlar?", "80 V va 20 V")],
 r"""def series(*c): return 1/sum(1/x for x in c)
def parallel(*c): return sum(c)
C12 = parallel(2e-6, 3e-6); C = series(C12, 5e-6); U = 100
q = C*U; U3 = q/5e-6; U12 = U - U3
print(f"C = {C*1e6:.2f} mkF, q = {q*1e6:.0f} mkC, U3 = {U3:.0f} V, q1 = {2e-6*U12*1e6:.0f} mkC, q2 = {3e-6*U12*1e6:.0f} mkC")""",
 ["Sig‘im nimalarga bog‘liq?", "Ketma-ket ulashda nima uchun zaryadlar teng?", "Kondensator teshilishi nima?", "Qanday qilib katta sig‘im va katta kuchlanishga chidamlilikni birga olish mumkin?"])

_a(8, 6, "rc", ["TN3", "TN4", "TN9"], r"Kondensator energiyasi. Zaryadlar sistemasi energiyasi. Elektr maydon energiyasi",
 r"Zaryadlangan o‘tkazgich, kondensator va zaryadlar sistemasi energiyasini, maydon energiyasi zichligini hisoblash; kondensator zaryadlanishida energiya balansini tahlil qilish.",
 r"""<p>\(W=\frac{CU^2}{2}=\frac{q^2}{2C}=\frac{qU}{2}\); \(w=\frac{\varepsilon_0\varepsilon E^2}{2}\). Zaryadlangan sfera maydoni energiyasi \(W=\frac{Q^2}{8\pi\varepsilon_0R}\). RC zanjirda zaryadlanish: \(q=CU_0(1-e^{-t/RC})\); manba bergan energiya \(CU_0^2\) — yarmi kondensatorda, yarmi rezistorda issiqlikka aylanadi (R ga bog‘liq emas).</p>""",
 [("Kondensator energiyasi", r"10 mkF kondensator 200 V gacha zaryadlangan. Energiya?", r"\(W=CU^2/2=0{,}2\) J."),
  ("Kondensatorlarni ulash", r"Zaryadlangan \(C\) kondensator (\(U_0\)) xuddi shunday zaryadsiz kondensatorga parallel ulandi. Energiya qanday o‘zgaradi?", r"Zaryad teng bo‘linadi: \(U=U_0/2\); \(W'=2\cdot C(U_0/2)^2/2=W_0/2\). Yarmi o‘tkazgichlarda issiqlik va nurlanishga ketadi."),
  ("Sfera maydoni energiyasi", r"\(R=10\) sm sferada 10 nC zaryad. Maydon energiyasi?", r"\(W=Q^2/(8\pi\varepsilon_0R)=kQ^2/2R=4{,}49\) mkJ.")],
 [(r"Yassi kondensator (\(E=10^6\) V/m, havo) maydon energiyasi zichligi?", r"4,43 J/m³"),
  (r"RC zanjirda \(R=10\) kΩ, \(C=100\) mkF: vaqt doimiysi?", "1 s"),
  (r"Manbadan uzilgan kondensator qoplamalari orasini 2 marta kattalashtirildi. Energiya?", "2 marta ortadi (tashqi ish hisobiga)"),
  (r"\(t=RC\) da zaryadlanayotgan kondensatordagi zaryad ulushi?", "63 %")],
 r"""import numpy as np
R, C, U0 = 1e3, 100e-6, 10.0
t = np.linspace(0, 10*R*C, 100001); dt = t[1] - t[0]
I = U0/R*np.exp(-t/(R*C)); q = C*U0*(1 - np.exp(-t/(R*C)))
W_src = np.sum(U0*I)*dt; W_R = np.sum(I**2*R)*dt; W_C = q[-1]**2/(2*C)
print(f"Manba: {W_src*1e3:.3f} mJ, rezistor: {W_R*1e3:.3f} mJ, kondensator: {W_C*1e3:.3f} mJ")""",
 ["Energiya qayerda joylashgan — zaryadlarda yoki maydonda?", "Nima uchun zaryadlanishda energiyaning yarmi yo‘qoladi?", "Fotoaparat chaqnoq lampasi qanday ishlaydi?", "Energiya zichligi formulasini yassi kondensatordan keltirib chiqaring."])

_a(9, 7, "ohm", ["TN3", "TN4", "TN9"], r"O‘tkazgich qarshiligi. Ketma-ket va parallel ulash. Zanjir qismi uchun Om qonuni",
 r"O‘tkazgich qarshiligini geometriya va material bo‘yicha hisoblash, aralash ulangan qarshiliklar zanjirini soddalashtirish va Om qonunini qo‘llash.",
 r"""<p>\(R=\rho l/S\), \(\rho=\rho_0(1+\alpha t)\). Ketma-ket: \(R=\sum R_i\), \(I\) bir xil, \(U_i\propto R_i\). Parallel: \(1/R=\sum1/R_i\), \(U\) bir xil, \(I_i\propto1/R_i\). Ikki parallel: \(R=R_1R_2/(R_1+R_2)\). Simmetrik zanjirlarda bir xil potensialli nuqtalarni birlashtirish mumkin.</p>""",
 [("Mis sim", r"Uzunligi 100 m, kesimi 0,5 mm² mis sim (\(\rho=1{,}7\cdot10^{-8}\) Ω·m). Qarshilik?", r"\(R=1{,}7\cdot10^{-8}\cdot100/0{,}5\cdot10^{-6}=3{,}4\) Ω."),
  ("Volfram tola", r"Lampa tolasi 20 °C da 30 Ω, ish haroratida 2500 °C (\(\alpha=4{,}5\cdot10^{-3}\) K⁻¹). Ishchi qarshilik (0 °C ga nisbatan taqribiy)?", r"\(R/R_0\approx(1+\alpha\cdot2500)/(1+\alpha\cdot20)=12{,}25/1{,}09=11{,}2\) ⇒ \(R\approx337\) Ω — shuning uchun lampa yoqilganda tok “sakraydi”."),
  ("Aralash ulash", r"\(R_2=6\) Ω va \(R_3=12\) Ω parallel ulangan, ularga \(R_1=4\) Ω ketma-ket ulangan. Zanjir 24 V. Toklar?", r"\(R_{23}=4\) Ω, \(R=8\) Ω, \(I=3\) A; \(U_1=12\) V, \(U_{23}=12\) V; \(I_2=2\) A, \(I_3=1\) A.")],
 [(r"Simni 2 marta cho‘zib (hajm o‘zgarmas) uzaytirildi. Qarshilik?", "4 marta ortadi"),
  (r"Kub qirralari 1 Ω dan. Qarama-qarshi uchlar orasidagi qarshilik?", r"\(5/6\) Ω"),
  (r"\(n\) ta bir xil \(R\) parallel ulangan. Umumiy qarshilik?", r"\(R/n\)"),
  (r"Ampermetr shunti: \(R_A=0{,}9\) Ω, o‘lchash chegarasini 10 marta oshirish uchun shunt?", "0,1 Ω")],
 r"""def ser(*r): return sum(r)
def par(*r): return 1/sum(1/x for x in r)
Rz = ser(4, par(6, 12)); I = 24/Rz
print(f"R = {Rz:.1f} Ohm, I = {I:.1f} A, I2 = {I*12/18:.1f} A, I3 = {I*6/18:.1f} A")
print(f"Kub diagonali: {5/6:.4f} Ohm")""",
 ["Solishtirma qarshilik nimaga bog‘liq?", "Nima uchun uydagi asboblar parallel ulanadi?", "Shunt va qo‘shimcha qarshilik nima?", "Simmetriya bilan zanjirni qanday soddalashtiramiz?"])

_a(10, 7, "ohm", ["TN3", "TN4", "TN9"], r"Elektr tokining ishi va quvvati. Joul–Lens qonuni",
 r"Elektr tokining ishi, quvvati va ajralgan issiqlikni hisoblash, iste’molchilarni ketma-ket va parallel ulashda quvvat taqsimotini tahlil qilish.",
 r"""<p>\(A=UIt\), \(P=UI=I^2R=U^2/R\), \(Q=I^2Rt\). Ketma-ket ulashda (\(I\) bir xil) katta qarshilikda ko‘p quvvat, parallelda (\(U\) bir xil) kichik qarshilikda ko‘p quvvat ajraladi. Energiya birligi: 1 kW·soat = \(3{,}6\cdot10^6\) J. FIK \(\eta=Q_{foyd}/A\).</p>""",
 [("Elektr choynak", r"2 kW, 220 V choynak: qarshilik va tok? 1,5 l suvni 20 °C dan qaynatish vaqti (FIK 85 %)?", r"\(R=U^2/P=24{,}2\) Ω, \(I=9{,}1\) A. \(Q=cm\Delta T=4200\cdot1{,}5\cdot80=504\) kJ; \(t=Q/(\eta P)=296\) s ≈ 5 min."),
  ("Lampalar ketma-ket", r"60 W va 100 W (220 V uchun) lampalar ketma-ket 220 V ga ulandi. Qaysi biri yorqinroq?", r"\(R_1=807\) Ω, \(R_2=484\) Ω; \(I=0{,}170\) A; \(P_1=23{,}4\) W, \(P_2=14{,}1\) W — 60 W li yorqinroq!"),
  ("Elektr energiyasi narxi", r"1,5 kW konditsioner kuniga 8 soat, 30 kun ishlaydi. Sarf?", r"\(1{,}5\cdot8\cdot30=360\) kW·soat.")],
 [(r"Spiral uzunligi 10 % qisqartirildi. Plitka quvvati qanday o‘zgaradi (U o‘zgarmas)?", "≈ 11 % ortadi"),
  (r"Ikki qizdirgich alohida ulanganda suv 10 va 15 minutda qaynaydi. Parallel ulanganda?", "6 min"),
  (r"Ketma-ket ulanganda?", "25 min"),
  (r"Uzatish liniyasida quvvat 100 kW, qarshilik 5 Ω. 10 kV va 100 kV da isroflar?", "500 W va 5 W")],
 r"""U = 220
for P in (60, 100): print(f"{P} W lampa: R = {U**2/P:.0f} Ohm")
R1, R2 = U**2/60, U**2/100; I = U/(R1 + R2)
print(f"Ketma-ket: I = {I:.3f} A, P1 = {I**2*R1:.1f} W, P2 = {I**2*R2:.1f} W")
c, m, dT, eta, P = 4200, 1.5, 80, 0.85, 2000
print(f"Choynak qaynash vaqti: {c*m*dT/(eta*P):.0f} s")""",
 ["Nima uchun liniyalarda yuqori kuchlanish ishlatiladi?", "Saqlagich (predoxranitel) qanday ishlaydi?", "Quvvat formulalarining qaysi biri qachon qulay?", "LED lampa nima uchun tejamli?"])

_a(11, 7, "ohm", ["TN3", "TN4", "TN9"], r"Tok manbaining EYuK. Bir jinsli bo‘lmagan zanjir qismi uchun Om qonuni",
 r"Tok manbaining EYuK va ichki qarshiligini aniqlash, to‘la zanjir uchun Om qonunini, manbalar batareyasini va foydali quvvat, FIK ni hisoblash.",
 r"""<p>\(I=\dfrac{\mathcal E}{R+r}\), \(U=\mathcal E-Ir\). Bir jinsli bo‘lmagan qism: \(IR_{12}=\varphi_1-\varphi_2+\mathcal E_{12}\). \(n\) ta bir xil manba ketma-ket: \(\mathcal E_n=n\mathcal E\), \(r_n=nr\); parallel: \(\mathcal E\), \(r/n\). Foydali quvvat \(P=\mathcal E^2R/(R+r)^2\), maksimum \(R=r\) da.</p>""",
 [("Ikki o‘lchashdan EYuK", r"Manbaga 4 Ω ulanganda 1 A, 9 Ω ulanganda 0,5 A tok o‘tdi. \(\mathcal E\) va \(r\)?", r"\(\mathcal E=1\cdot(4+r)=0{,}5(9+r)\) ⇒ \(r=1\) Ω, \(\mathcal E=5\) V."),
  ("Batareya", r"4 ta element (\(\mathcal E=1{,}5\) V, \(r=0{,}5\) Ω) va yuklama 2 Ω. Ketma-ket va parallel ulashda tok?", r"Ketma-ket: \(I=6/(2+2)=1{,}5\) A. Parallel: \(I=1{,}5/(2+0{,}125)=0{,}71\) A. Ketma-ket ulash bu holda foydaliroq."),
  ("Qisqa tutashuv", r"Avtomobil akkumulyatori \(\mathcal E=12{,}6\) V, \(r=0{,}01\) Ω. Qisqa tutashuv toki?", r"\(I=\mathcal E/r=1260\) A — xavfli, sim erib ketishi mumkin.")],
 [(r"Manba klemmalaridagi kuchlanish yuklama 5 Ω da 10 V, 2 Ω da 8 V. \(\mathcal E\), \(r\)?", r"12 V, 1 Ω"),
  (r"\(\mathcal E=12\) V, \(r=2\) Ω: maksimal foydali quvvat?", "18 W"),
  (r"Manba zaryadlanayotganda (tok teskari) klemma kuchlanishi?", r"\(U=\mathcal E+Ir\)"),
  (r"Potensiometr usulida EYuK ni tok olmasdan o‘lchashning afzalligi?", r"ichki qarshilikdagi pasayish yo‘q, \(U=\mathcal E\)")],
 r"""import numpy as np
E, r = 12.0, 0.5
R = np.linspace(0.05, 5, 2000)
I = E/(R + r); P = I**2*R; eta = R/(R + r)
i = P.argmax()
print(f"P_max = {P[i]:.2f} W, R = {R[i]:.3f} Ohm, FIK = {eta[i]*100:.1f} %  (nazariya E^2/4r = {E**2/(4*r):.1f} W)")""",
 ["EYuK va kuchlanishning farqi?", "Ichki qarshilikni qanday o‘lchash mumkin?", "Batareyani qachon ketma-ket, qachon parallel ulash kerak?", "Nima uchun maksimal quvvat rejimi energetikada ishlatilmaydi?"])

_a(12, 8, "kirchhoff", ["TN3", "TN4", "TN8"], r"Tarmoqlangan zanjirlar. Kirxgof qoidalari. Misollar",
 r"Kirxgof qoidalari asosida tarmoqlangan zanjirlarni hisoblash, tenglamalar sistemasini tuzish va yechish, natijani quvvat balansi bilan tekshirish.",
 r"""<p>1-qoida: \(\sum I=0\) (\(n-1\) tugun). 2-qoida: \(\sum IR=\sum\mathcal E\) (\(p-n+1\) kontur). Tok yo‘nalishlari ixtiyoriy tanlanadi; manfiy natija — teskari yo‘nalish. Tekshiruv: \(\sum\mathcal E_kI_k=\sum I_k^2R_k\). Uitston ko‘prigi muvozanati: \(R_1R_4=R_2R_3\).</p>""",
 [("Ikki manbali zanjir", r"\(\mathcal E_1=10\) V (\(R_1=1\) Ω), \(\mathcal E_2=4\) V (\(R_2=2\) Ω), umumiy shoxobcha \(R_3=4\) Ω (musbat qutblar umumiy tugunda). Toklar?", r"\(I_1+I_2=I_3\); \(I_1+4I_3=10\); \(2I_2+4I_3=4\). Yechim: \(I_1=22/7=3{,}14\) A, \(I_2=-10/7=-1{,}43\) A (2-manba zaryadlanadi), \(I_3=12/7=1{,}71\) A."),
  ("Uitston ko‘prigi", r"\(R_1=100\) Ω, \(R_2=200\) Ω, \(R_3=150\) Ω. Ko‘prik muvozanatda bo‘lishi uchun \(R_4\)?", r"\(R_4=R_2R_3/R_1=300\) Ω; galvanometr toki nol."),
  ("Quvvat balansi", r"1-masala uchun quvvat balansini tekshiring.", r"\(10\cdot3{,}143-4\cdot1{,}429=25{,}71\) W; \(3{,}143^2\cdot1+1{,}429^2\cdot2+1{,}714^2\cdot4=25{,}71\) W ✓.")],
 [(r"3 tugun va 5 shoxobchali zanjirda nechta mustaqil kontur?", "3"),
  (r"Ikki bir xil manba (\(\mathcal E\), \(r\)) parallel, yuklama \(R\). Tok?", r"\(\mathcal E/(R+r/2)\)"),
  (r"Muvozanatdagi Uitston ko‘prigida galvanometr o‘rniga sim qo‘yilsa, toklar o‘zgaradimi?", "yo‘q"),
  (r"1-masalada \(\mathcal E_2\) qancha bo‘lsa, \(I_2=0\)?", r"\(\mathcal E_2=\mathcal E_1R_3/(R_1+R_3)=8\) V")],
 r"""import numpy as np
E1, E2, R1, R2, R3 = 10, 4, 1, 2, 4
A = np.array([[1, 1, -1], [R1, 0, R3], [0, R2, R3]], float)
b = np.array([0, E1, E2], float)
I1, I2, I3 = np.linalg.solve(A, b)
print(f"I1 = {I1:.3f} A, I2 = {I2:.3f} A, I3 = {I3:.3f} A")
print(f"Quvvat balansi: {E1*I1 + E2*I2:.3f} W = {I1**2*R1 + I2**2*R2 + I3**2*R3:.3f} W")""",
 ["Kirxgof qoidalari qaysi saqlanish qonunlariga asoslangan?", "Nechta tenglama kerakligini qanday aniqlaymiz?", "Kontur toklari usuli nima?", "Uitston ko‘prigining afzalligi?"])

_a(13, 9, "biot", ["TN2", "TN3", "TN7"], r"Tokning magnit maydoni. Harakatdagi zaryadlar o‘zaro ta’siri. Magnit induksiya",
 r"Harakatdagi zaryad va tok elementlari hosil qiladigan magnit maydonni, parallel toklarning o‘zaro ta’sirini hisoblash va magnit induksiya yo‘nalishini aniqlash.",
 r"""<p>Harakatdagi zaryad: \(\vec B=\dfrac{\mu_0}{4\pi}\dfrac{q\vec v\times\vec r}{r^3}\). Cheksiz to‘g‘ri tok: \(B=\mu_0I/2\pi r\). Parallel toklar birlik uzunligiga kuch: \(F/l=\mu_0I_1I_2/2\pi d\). Yo‘nalish: parma (o‘ng vint) qoidasi — parma tok yo‘nalishida ilgarilasa, dastasi aylanishi \(\vec B\) yo‘nalishini ko‘rsatadi.</p>""",
 [("Vodorod atomi yadrosida maydon", r"Bor modelida elektron \(r=0{,}529\cdot10^{-10}\) m radiusli orbitada \(v=2{,}19\cdot10^6\) m/s tezlik bilan aylanadi. Yadro joylashgan nuqtadagi induksiya?", r"\(B=\frac{\mu_0}{4\pi}\frac{ev}{r^2}=10^{-7}\cdot1{,}602\cdot10^{-19}\cdot2{,}19\cdot10^6/(0{,}529\cdot10^{-10})^2=12{,}5\) T — juda kuchli!"),
  ("Amper birligi", r"Bir-biridan 1 m masofadagi ikki cheksiz parallel simdan 1 A dan tok o‘tmoqda. Birlik uzunlikka kuch?", r"\(F/l=\mu_0I^2/2\pi d=2\cdot10^{-7}\) N/m — amperning klassik ta’rifi."),
  ("Ikki simning maydoni", r"Bir-biridan 10 sm masofadagi parallel simlarda 20 A dan bir yo‘nalishda tok. O‘rtadagi va bir simdan 5 sm tashqaridagi induksiya?", r"O‘rtada maydonlar qarama-qarshi: \(B=0\). Tashqarida: \(\mu_0I/2\pi(0{,}05)+\mu_0I/2\pi(0{,}15)=80+26{,}7=106{,}7\) mkT.")],
 [(r"Proton \(10^6\) m/s tezlik bilan harakatlanmoqda. Undan 1 mm masofada (tezlikka perpendikulyar) induksiya?", r"\(1{,}6\cdot10^{-14}\) T"),
  (r"Elektr uzatish liniyasi (1000 A) dan 20 m pastda induksiya?", "10 mkT"),
  (r"Parallel simlar (5 A va 10 A, 2 sm) orasidagi 1 m ga kuch?", "0,5 mN"),
  (r"Qarama-qarshi yo‘nalgan toklar tortishadimi yoki itariladimi?", "itariladi")],
 r"""import numpy as np
mu0 = 4e-7*np.pi
def B_wire(I, xw, x): return mu0*I/(2*np.pi*(x - xw))   # y-tashkil etuvchi (ishora bilan)
I, d = 20, 0.1
for x in (0.05, 0.15, -0.05):
    B = B_wire(I, 0, x) + B_wire(I, d, x)
    print(f"x = {x*100:5.1f} sm:  B = {B*1e6:7.1f} mkT")""",
 ["Magnit maydon qanday manbalardan hosil bo‘ladi?", "Parma qoidasini tushuntiring.", "Nima uchun magnit kuch elektr kuchdan kichik?", "Amper birligi 2019-yildan qanday ta’riflanadi?"])

_a(14, 9, "biot", ["TN2", "TN3", "TN9"], r"Bio–Savar–Laplas qonuni va uning tatbiqi",
 r"Bio–Savar–Laplas qonuni yordamida chekli to‘g‘ri tok, doiraviy tok, ramka va yoy shaklidagi o‘tkazgichlar maydonini hisoblash.",
 r"""<p>\(dB=\dfrac{\mu_0}{4\pi}\dfrac{Idl\sin\alpha}{r^2}\). Chekli to‘g‘ri tok: \(B=\dfrac{\mu_0I}{4\pi r_0}(\cos\alpha_1-\cos\alpha_2)\). Doiraviy tok markazida \(\mu_0I/2R\), o‘qida \(\mu_0IR^2/2(R^2+x^2)^{3/2}\). Yoy (burchak \(\theta\)) markazida \(B=\dfrac{\mu_0I\theta}{4\pi R}\).</p>""",
 [("Kvadrat ramka", r"Tomoni 10 sm kvadrat ramkadan 5 A tok o‘tmoqda. Markazdagi induksiya?", r"Har bir tomon: \(r_0=a/2\), \(\alpha_1=45^\circ\), \(\alpha_2=135^\circ\): \(B_1=\frac{\mu_0I}{4\pi(a/2)}\sqrt2\). To‘rttasi: \(B=\frac{2\sqrt2\mu_0I}{\pi a}=56{,}6\) mkT."),
  ("Doiraviy o‘ram o‘qida", r"\(R=10\) sm, \(I=5\) A. Markazda va \(x=10\) sm da?", r"31,4 mkT va 11,1 mkT."),
  ("Yarim aylana va to‘g‘ri qismlar", r"Sim yarim aylana (\(R=5\) sm) va unga urinma ikki uzun to‘g‘ri qismdan iborat (U shakl), \(I=10\) A. Markazdagi induksiya?", r"Yarim aylana: \(\mu_0I/4R=62{,}8\) mkT. Har bir yarim cheksiz to‘g‘ri qism: \(\mu_0I/4\pi R=20\) mkT. Jami \(102{,}8\) mkT (barchasi bir yo‘nalishda).")],
 [(r"Ikki koaksial o‘ram (Gelmgols g‘altaklari) \(R\) masofada: o‘rtadagi maydon (\(N\) o‘ram, \(I\))?", r"\(B=(4/5)^{3/2}\mu_0NI/R\)"),
  (r"Muntazam oltiburchak ramka (tomon \(a\)) markazida \(B\)?", r"\(B=\frac{\sqrt3\mu_0I}{\pi a}\)"),
  (r"Doiraviy tok o‘qida \(B\) qayerda maksimal?", "markazda"),
  (r"Doiraviy o‘ramdan uzoqda (\(x\gg R\)) o‘qdagi \(B(x)\) qonuniyati?", r"\(B\approx\mu_0IR^2/2x^3\propto1/x^3\)")],
 r"""import numpy as np
mu0 = 4e-7*np.pi
def biot_savart(path, I, P, N=4000):
    B = np.zeros(3)
    for a, b in zip(path[:-1], path[1:]):
        t = np.linspace(0, 1, N)[:, None]; pts = a + (b - a)*t
        mid = (pts[1:] + pts[:-1])/2; dl = pts[1:] - pts[:-1]; r = P - mid
        B += mu0*I/(4*np.pi)*np.sum(np.cross(dl, r)/np.linalg.norm(r, axis=1)[:, None]**3, axis=0)
    return B
a = 0.1
sq = np.array([[-a/2, -a/2, 0], [a/2, -a/2, 0], [a/2, a/2, 0], [-a/2, a/2, 0], [-a/2, -a/2, 0]])
print(f"Kvadrat markazi: B = {np.linalg.norm(biot_savart(sq, 5, np.zeros(3)))*1e6:.2f} mkT, formula {2*np.sqrt(2)*mu0*5/(np.pi*a)*1e6:.2f}")
phi = np.linspace(0, 2*np.pi, 721); ring = np.stack([0.1*np.cos(phi), 0.1*np.sin(phi), 0*phi], 1)
print(f"Halqa markazi: {np.linalg.norm(biot_savart(ring, 5, np.zeros(3), 50))*1e6:.2f} mkT, formula {mu0*5/0.2*1e6:.2f}")""",
 ["Bio–Savar–Laplas qonunida vektor ko‘paytma nimani anglatadi?", "Chekli tok formulasidan cheksiz tok formulasini keltirib chiqaring.", "Gelmgols g‘altaklari nima uchun ishlatiladi?", "Superpozitsiyani magnit maydonga qo‘llash mumkinmi?"])

_a(15, 11, "ampere", ["TN3", "TN4", "TN9"], r"Amper qonuni. Amper qonuniga misollar. Magnit maydon kuchlarining ishi",
 r"Tokli o‘tkazgichga ta’sir etuvchi Amper kuchini, tokli ramkaga ta’sir etuvchi momentni va magnit maydon kuchlarining ishini hisoblash.",
 r"""<p>\(F=IBl\sin\alpha\) (chap qo‘l qoidasi). Parallel toklar: \(F/l=\mu_0I_1I_2/2\pi d\). Ramka: \(M=p_mB\sin\alpha\), \(p_m=NIS\). Ish: \(A=I\Delta\Phi\) (o‘tkazgich ko‘chganda kesib o‘tgan oqim). Bir jinsli maydonda yopiq konturga natijaviy kuch nol, faqat moment ta’sir qiladi.</p>""",
 [("Sterjenni muallaq ushlash", r"Massasi 10 g, uzunligi 20 sm gorizontal sterjen \(B=0{,}25\) T gorizontal maydonda (sterjenga tik). Og‘irlikni muvozanatlash uchun tok?", r"\(IBl=mg\) ⇒ \(I=mg/(Bl)=1{,}96\) A."),
  ("Ramka momenti", r"100 o‘ramli, yuzasi 4 sm² ramkada 0,5 A, \(B=0{,}2\) T. Maksimal moment?", r"\(M=NISB=100\cdot0{,}5\cdot4\cdot10^{-4}\cdot0{,}2=4\) mN·m."),
  ("Ko‘chirish ishi", r"Uzunligi 0,5 m, toki 10 A o‘tkazgich \(B=0{,}4\) T maydonda kuchga parallel 20 sm siljidi. Ish?", r"\(A=IBl\Delta x=0{,}4\) J (\(=I\Delta\Phi\)).")],
 [(r"Tokli o‘tkazgich maydon chiziqlariga parallel joylashgan. Kuch?", "0"),
  (r"Parallel simlar 4 mm masofada, toklar 2 A va 3 A. 1 m ga kuch?", "0,3 mN"),
  (r"Doiraviy tok (\(R=5\) sm, \(I=2\) A) \(B=0{,}1\) T da: maksimal moment?", r"\(1{,}57\) mN·m"),
  (r"Ramka barqaror muvozanatda bo‘lishi uchun \(\vec p_m\) qanday yo‘nalgan?", r"\(\vec B\) bo‘ylab")],
 r"""import numpy as np
mu0 = 4e-7*np.pi
m, l, B, g = 0.01, 0.2, 0.25, 9.81
print(f"Muallaq ushlash toki: {m*g/(B*l):.3f} A")
for d in (0.002, 0.005, 0.01):
    print(f"d = {d*1e3:.0f} mm: F/l = {mu0*2*3/(2*np.pi*d)*1e3:.3f} mN/m")""",
 ["Chap qo‘l qoidasini tushuntiring.", "Elektr dvigatelda moment qanday hosil bo‘ladi?", "Nima uchun bir jinsli maydonda yopiq konturga natijaviy kuch nol?", "Magnit kuchlar ishi va Lorens kuchi ish bajarmasligi qanday moslashadi?"])

_a(16, 11, "lorentzf", ["TN3", "TN4", "TN9"], r"Lorens kuchi. Zaryadlangan zarralarning elektr maydondagi harakati",
 r"Zaryadli zarralarning bir jinsli elektr maydonda tezlashishi va og‘ishini (ossillograf trubkasi, kondensator) hisoblash, Lorens kuchini qo‘llash.",
 r"""<p>\(\vec F=q\vec E+q\vec v\times\vec B\). Bo‘ylama maydonda: \(qU=mv^2/2\). Ko‘ndalang maydonda (kondensator uzunligi \(l\)): \(t=l/v_0\), \(y=\dfrac{qEl^2}{2mv_0^2}\), og‘ish burchagi \(\operatorname{tg}\theta=\dfrac{qEl}{mv_0^2}\). Elektron: \(e/m=1{,}76\cdot10^{11}\) C/kg.</p>""",
 [("Kondensatorda og‘ish", r"Elektron \(v_0=10^7\) m/s tezlik bilan uzunligi 5 sm kondensatorga plastinalarga parallel uchib kirdi, \(E=10^4\) V/m. Chiqishdagi og‘ish?", r"\(y=eEl^2/(2mv_0^2)=1{,}602\cdot10^{-19}\cdot10^4\cdot0{,}0025/(2\cdot9{,}109\cdot10^{-31}\cdot10^{14})=2{,}2\) sm; \(\operatorname{tg}\theta=0{,}88\)."),
  ("Proton tezlatkichi", r"Proton tinch holatdan 1 kV potensiallar farqida tezlashdi. Tezligi?", r"\(v=\sqrt{2eU/m_p}=4{,}38\cdot10^5\) m/s."),
  ("Milliken tomchisi", r"Massasi \(3{,}2\cdot10^{-15}\) kg moy tomchisi 4 mm oraliqli kondensatorda 98 V da muallaq turibdi. Zaryadi?", r"\(qU/d=mg\) ⇒ \(q=mgd/U=1{,}28\cdot10^{-18}\) C \(=8e\).")],
 [(r"Elektron 1 kV da tezlashdi. Energiyasi va tezligi?", r"1 keV, \(1{,}88\cdot10^7\) m/s"),
  (r"Alfa-zarra va proton bir xil potensiallar farqida tezlashsa, energiyalari nisbati?", "2"),
  (r"Elektronni to‘xtatish uchun 5 eV energiyada qanday tormozlovchi kuchlanish kerak?", "5 V"),
  (r"Zarra maydonga perpendikulyar uchib kirsa, trayektoriya?", "parabola")],
 r"""import numpy as np
e, m = 1.602e-19, 9.109e-31
v0, l, E = 1e7, 0.05, 1e4
y = e*E*l**2/(2*m*v0**2); th = np.degrees(np.arctan(e*E*l/(m*v0**2)))
print(f"Og'ish y = {y*100:.2f} sm, burchak = {th:.1f} gradus")
# Sonli tekshiruv
x, yy, vx, vy, dt = 0.0, 0.0, v0, 0.0, 1e-12
while x < l: vy += e*E/m*dt; x += vx*dt; yy += vy*dt
print(f"Sonli: y = {yy*100:.2f} sm")""",
 ["Elektr maydon zarra energiyasini o‘zgartiradimi?", "Ossillograf trubkasida nur qanday og‘diriladi?", "Milliken tajribasi nimani isbotladi?", "Zaryadning massaga nisbati nima uchun muhim?"])

_a(17, 11, "lorentzf", ["TN3", "TN4", "TN9"], r"Zaryadlangan zarralarning magnit maydondagi harakati. Xoll effekti",
 r"Zaryadli zarralarning bir jinsli magnit maydonda aylana va vint chiziq bo‘ylab harakatini, massa-spektrometr va siklotron prinsipini hamda Xoll effektini hisoblash.",
 r"""<p>\(r=\dfrac{mv_\perp}{|q|B}\), \(T=\dfrac{2\pi m}{|q|B}\), vint qadami \(h=v_\parallel T\). Massa-spektrometr: \(m=\dfrac{qB^2r^2}{2U}\). Xoll: \(U_H=\dfrac{IB}{nqd}\) ⇒ \(n=\dfrac{IB}{qdU_H}\), harakatchanlik \(\mu=\sigma R_H\).</p>""",
 [("Vint chiziq", r"Proton \(10^6\) m/s tezlik bilan \(B=0{,}2\) T maydonga 30° burchak ostida uchib kirdi. Radius va qadam?", r"\(r=mv\sin30^\circ/(eB)=2{,}61\) sm; \(h=2\pi mv\cos30^\circ/(eB)=28{,}4\) sm."),
  ("Yarimo‘tkazgichda Xoll effekti", r"Qalinligi 0,5 mm plastina, \(I=1\) mA, \(B=0{,}5\) T, \(U_H=5\) mV. Tashuvchilar konsentratsiyasi?", r"\(n=IB/(edU_H)=10^{-3}\cdot0{,}5/(1{,}602\cdot10^{-19}\cdot5\cdot10^{-4}\cdot5\cdot10^{-3})=1{,}25\cdot10^{21}\) m⁻³ — metallarnikidan \(10^7\) marta kam."),
  ("Siklotron", r"Siklotronda \(B=1\) T. Protonlar uchun tezlatuvchi kuchlanish chastotasi? Radius 0,5 m bo‘lsa, chiqish energiyasi?", r"\(f=eB/2\pi m=15{,}2\) MGs. \(E=(eBR)^2/2m=1{,}92\cdot10^{-12}\) J \(=12\) MeV.")],
 [(r"Elektron (1 keV) \(B=1\) mT da: radius?", "10,7 sm"),
  (r"Ikki izotop (massalari 20 va 22 a.b.) massa-spektrometrda: radiuslar nisbati (bir xil \(U\))?", r"\(\sqrt{22/20}=1{,}049\)"),
  (r"Mis plastina (\(d=0{,}1\) mm, \(I=10\) A, \(B=1\) T) da \(U_H\)?", "7,3 mkV"),
  (r"Elektron va proton bir xil tezlikda: radiuslar nisbati?", r"\(m_p/m_e=1836\)")],
 r"""import numpy as np
q, m, B = 1.602e-19, 1.673e-27, 0.2
v = 1e6; a = np.radians(30)
r = m*v*np.sin(a)/(q*B); h = 2*np.pi*m*v*np.cos(a)/(q*B)
print(f"r = {r*100:.2f} sm, qadam h = {h*100:.1f} sm")
# Boris integratori bilan tekshirish
vel = np.array([v*np.cos(a), v*np.sin(a), 0.0]); pos = np.zeros(3); Bv = np.array([B, 0, 0])
T = 2*np.pi*m/(q*B); dt = T/2000
for _ in range(2000):
    t = q*Bv/m*dt/2; s = 2*t/(1 + t@t); vp = vel + np.cross(vel, t); vel = vel + np.cross(vp, s); pos += vel*dt
print(f"Bir davrdan keyin x = {pos[0]*100:.1f} sm (qadam), y, z = {pos[1]*100:.3f}, {pos[2]*100:.3f} sm")""",
 ["Nima uchun siklotron davri tezlikka bog‘liq emas?", "Xoll effekti bilan tashuvchi ishorasi qanday aniqlanadi?", "Magnit tuzoq (probka) qanday ishlaydi?", "Relyativistik tezliklarda siklotron nima uchun ishlamaydi?"])

_a(18, 13, "rl", ["TN2", "TN4", "TN9"], r"Elektromagnit induksiya. O‘zaroinduksiya. O‘zinduksiya. Tokning qaror topishi. Magnit maydon energiyasi",
 r"Induksiya EYuK, induktivlik, RL zanjirdagi o‘tish jarayonlari va magnit maydon energiyasini hisoblash.",
 r"""<p>\(\mathcal E=-N\,d\Phi/dt\); harakatdagi sterjen \(Bvl\); aylanuvchi ramka \(\mathcal E_0=NBS\omega\). \(L=\mu_0\mu N^2S/l\); \(M=\mu_0\mu N_1N_2S/l\) (koaksial solenoidlar). RL: \(I=\frac{\mathcal E}{R}(1-e^{-t/\tau})\), \(\tau=L/R\). \(W=LI^2/2\), \(w=B^2/2\mu_0\mu\).</p>""",
 [("Generator", r"100 o‘ramli, yuzasi 200 sm² ramka \(B=0{,}1\) T maydonda sekundiga 50 marta aylanadi. EYuK amplitudasi?", r"\(\mathcal E_0=NBS\omega=100\cdot0{,}1\cdot0{,}02\cdot314=62{,}8\) V."),
  ("RL zanjir", r"\(L=0{,}2\) H, \(R=4\) Ω, \(\mathcal E=12\) V. Ulangandan 0,1 s keyingi tok?", r"\(\tau=0{,}05\) s; \(I=3(1-e^{-2})=2{,}59\) A."),
  ("O‘zaro induktivlik", r"Uzunligi 50 sm, kesimi 10 sm² solenoid ustiga 100 o‘ramli ikkinchi g‘altak o‘ralgan; birinchisida 1000 o‘ram. \(M\)? Birinchisida tok 0,01 s da 2 A ga tekis o‘zgarsa, ikkinchisida EYuK?", r"\(M=\mu_0N_1N_2S/l=0{,}251\) mH; \(\mathcal E_2=M\Delta I/\Delta t=50\) mV.")],
 [(r"Samolyot (qanot 40 m) 900 km/soat tezlikda, Yer maydoni vertikal tashkil etuvchisi 50 mkT. Qanot uchlari orasidagi EYuK?", "0,5 V"),
  (r"\(L=2\) H g‘altakda 3 A tok. Energiya?", "9 J"),
  (r"RL zanjirda tok \(0{,}9I_\infty\) ga yetish vaqti?", r"\(\tau\ln10=2{,}3\tau\)"),
  (r"\(B=1\) T maydon energiyasi zichligi (havoda)?", r"\(4\cdot10^5\) J/m³")],
 r"""import numpy as np
L, R, E = 0.2, 4.0, 12.0
tau = L/R; dt = 1e-5; I = 0.0
for k in range(int(0.1/dt)):
    I += (E - R*I)/L*dt              # Eyler usuli: L dI/dt = E - R I
print(f"Sonli I(0.1 s) = {I:.3f} A, analitik = {E/R*(1 - np.exp(-0.1/tau)):.3f} A")
print(f"Generator: E0 = {100*0.1*0.02*2*np.pi*50:.1f} V")""",
 ["Lens qoidasini energiya saqlanishi bilan bog‘lang.", "Nima uchun katta induktivlikli zanjirni uzish xavfli?", "O‘zaro induktivlik nimalarga bog‘liq?", "Magnit maydon energiyasi qayerda joylashgan?"])

_a(19, 14, "rlc", ["TN2", "TN4", "TN9"], r"Xususiy so‘nmas va so‘nuvchi elektromagnit tebranishlar. Majburiy tebranishlar",
 r"Tebranish konturida xususiy chastota, so‘nish koeffitsiyenti, logarifmik dekrement, asllik va energiya almashinuvini hisoblash; majburiy tebranishlar va rezonansni tahlil qilish.",
 r"""<p>\(\omega_0=1/\sqrt{LC}\), \(T=2\pi\sqrt{LC}\). Energiya: \(\frac{CU_m^2}2=\frac{LI_m^2}2\) ⇒ \(I_m=U_m\sqrt{C/L}\). So‘nish: \(\beta=R/2L\), \(\omega=\sqrt{\omega_0^2-\beta^2}\), log. dekrement \(\delta=\beta T\), asllik \(Q=\pi/\delta\approx\frac1R\sqrt{L/C}\). Majburiy: rezonans \(\omega=\omega_0\) da tok amplitudasi \(U_0/R\).</p>""",
 [("Radiopriyomnik konturi", r"\(C=500\) pF. 1 MGs chastotaga sozlash uchun \(L\)?", r"\(L=1/(4\pi^2f^2C)=50{,}7\) mkH."),
  ("So‘nuvchi kontur", r"\(L=1\) mH, \(C=0{,}1\) mkF, \(R=10\) Ω. \(\omega_0\), \(\beta\), \(\delta\), \(Q\)?", r"\(\omega_0=10^5\) rad/s; \(\beta=5000\) s⁻¹; \(\delta=2\pi\beta/\omega=0{,}315\); \(Q=\sqrt{L/C}/R=10\)."),
  ("Energiya almashinuvi", r"Shu konturda kondensatordagi maksimal kuchlanish 10 V. Maksimal tok (so‘nishni hisobga olmay)?", r"\(I_m=U_m\sqrt{C/L}=10\cdot\sqrt{10^{-4}}=0{,}1\) A.")],
 [(r"Kondensator sig‘imi 4 marta oshsa, davr?", "2 marta ortadi"),
  (r"Kritik qarshilik (\(L=1\) mH, \(C=0{,}1\) mkF)?", "200 Ω"),
  (r"Amplituda \(e\) marta kamayish vaqti (\(\beta=5000\) s⁻¹)?", "0,2 ms"),
  (r"\(Q=10\) bo‘lsa, rezonans egri chizig‘i kengligi (\(\omega_0=10^5\))?", r"\(\Delta\omega=\omega_0/Q=10^4\) rad/s")],
 r"""import numpy as np
L, C, R = 1e-3, 1e-7, 10.0
w0 = 1/np.sqrt(L*C); beta = R/(2*L); w = np.sqrt(w0**2 - beta**2)
print(f"w0 = {w0:.0f} rad/s, beta = {beta:.0f} 1/s, delta = {2*np.pi*beta/w:.3f}, Q = {np.sqrt(L/C)/R:.1f}")
q, i, dt = C*10, 0.0, 1e-8         # boshlang'ich U = 10 V
Umax = 0.0; T = 2*np.pi/w
for k in range(int(2e-4/dt)):
    i += (-q/C - R*i)/L*dt; q += i*dt
    if k*dt > 2e-4 - T and abs(q/C) > Umax: Umax, tp = abs(q/C), k*dt
print(f"t = {tp*1e3:.3f} ms dagi cho'qqi: {Umax:.3f} V (nazariy 10*exp(-beta*t) = {10*np.exp(-beta*tp):.3f} V)")""",
 ["LC konturni mexanik mayatnik bilan taqqoslang.", "Nima uchun real konturda tebranishlar so‘nadi?", "Asllik nimani ko‘rsatadi?", "Radiopriyomnik stansiyani qanday tanlaydi?"])

_a(20, 15, "ac", ["TN3", "TN4", "TN9"], r"O‘zgaruvchan tok quvvati, effektiv qiymat. Aktiv, induktiv va sig‘im qarshiliklar. To‘liq qarshilik. Vektor diagrammalar",
 r"O‘zgaruvchan tok zanjirlarida reaktiv qarshiliklar, to‘liq qarshilik, tok, faza siljishi va quvvatni hisoblash, vektor diagrammalar qurish.",
 r"""<p>\(X_L=\omega L\), \(X_C=1/\omega C\), \(Z=\sqrt{R^2+(X_L-X_C)^2}\), \(\operatorname{tg}\varphi=(X_L-X_C)/R\), \(P=UI\cos\varphi=I^2R\). Vektor diagramma: tok vektori gorizontal, \(U_R\) u bilan bir yo‘nalishda, \(U_L\) yuqoriga, \(U_C\) pastga; \(\vec U=\vec U_R+\vec U_L+\vec U_C\).</p>""",
 [("RLC zanjir", r"\(R=30\) Ω, \(X_L=80\) Ω, \(X_C=40\) Ω, \(U=100\) V. \(Z\), \(I\), \(\cos\varphi\), \(P\), elementlardagi kuchlanishlar?", r"\(Z=\sqrt{30^2+40^2}=50\) Ω; \(I=2\) A; \(\cos\varphi=0{,}6\) (\(\varphi=53^\circ\), induktiv); \(P=120\) W; \(U_R=60\), \(U_L=160\), \(U_C=80\) V — \(U_L>U\)!"),
  ("Lampa va kondensator", r"110 V, 60 W lampani 220 V, 50 Gs tarmoqqa kondensator orqali ulash kerak. Sig‘im?", r"\(I=0{,}545\) A, \(R=202\) Ω; \(Z=220/0{,}545=403\) Ω; \(X_C=\sqrt{403^2-202^2}=349\) Ω ⇒ \(C=9{,}1\) mkF. Rezistordan farqli, kondensator issiqlik ajratmaydi."),
  ("Effektiv qiymat", r"Tok \(i=5\sin314t\) A, \(R=20\) Ω. Effektiv tok va o‘rtacha quvvat?", r"\(I=3{,}54\) A; \(P=I^2R=250\) W.")],
 [(r"\(L=0{,}1\) H g‘altakning 50 Gs va 5 kGs dagi qarshiligi?", "31,4 Ω va 3,14 kΩ"),
  (r"\(C=10\) mkF ning 50 Gs dagi qarshiligi?", "318 Ω"),
  (r"G‘altak (\(R=10\) Ω, \(L=50\) mH) 50 Gs da \(\cos\varphi\)?", "0,54"),
  (r"Faqat L va C dan iborat zanjirda o‘rtacha quvvat?", "0")],
 r"""import numpy as np
R, XL, XC, U = 30, 80, 40, 100
Z = complex(R, XL - XC); I = U/abs(Z)
print(f"Z = {abs(Z):.1f} Ohm, I = {I:.2f} A, phi = {np.degrees(np.angle(Z)):.1f} deg, P = {I**2*R:.0f} W")
print(f"U_R = {I*R:.0f} V, U_L = {I*XL:.0f} V, U_C = {I*XC:.0f} V")
# Kompleks usul: 220 V, 50 Hz RLC
w = 2*np.pi*50; Z2 = 100 + 1j*(w*0.5 - 1/(w*10e-6))
print(f"Ma'ruza misoli: |Z| = {abs(Z2):.1f} Ohm, I = {220/abs(Z2):.3f} A, cos phi = {np.cos(np.angle(Z2)):.3f}")""",
 ["Effektiv qiymat qanday ta’riflanadi?", "Nima uchun induktiv qarshilik chastota bilan ortadi?", "Vektor diagramma qurish tartibi?", "Reaktiv quvvat nima va nima uchun zararli?"])

_a(21, 15, "trafo", ["TN3", "TN4", "TN9", "TN6"], r"Rezonansning ikki turi. Parallel zanjir. Transformatorlar",
 r"Kuchlanishlar va toklar rezonansini, parallel zanjirdagi toklarni, transformator parametrlarini va uch fazali tok kuchlanish va quvvatlarini hisoblash.",
 r"""<p>Ketma-ket rezonans: \(\omega_0=1/\sqrt{LC}\), \(I=U/R\), \(U_L=U_C=QU\). Parallel LC (ideal): \(I=U|\omega C-1/\omega L|\), rezonansda \(I\to0\), shoxobcha toklari \(I_L=I_C=U/\omega_0L\). Transformator: \(U_1/U_2=N_1/N_2=k\), \(I_1/I_2\approx1/k\). Uch fazali: yulduzda \(U_l=\sqrt3U_f\), quvvat \(P=3U_fI_f\cos\varphi=\sqrt3U_lI_l\cos\varphi\).</p>""",
 [("Transformator", r"220 V → 12 V transformator, birlamchi chulg‘am 1100 o‘ram. Ikkilamchi o‘ramlar soni? Ikkilamchi tok 2 A bo‘lsa, birlamchi tok (ideal)?", r"\(N_2=1100\cdot12/220=60\); \(I_1=I_2U_2/U_1=0{,}109\) A."),
  ("Uch fazali yuklama", r"Faza kuchlanishi 220 V, yulduz usulida har fazaga 22 Ω aktiv yuklama. Liniya kuchlanishi, faza toki, umumiy quvvat?", r"\(U_l=381\) V; \(I_f=10\) A; \(P=3\cdot220\cdot10=6{,}6\) kW; neytral simda tok 0."),
  ("Kuchlanishlar rezonansi", r"\(R=10\) Ω, \(L=0{,}1\) H, \(C=10\) mkF, \(U=10\) V. Rezonans chastotasi, tok va \(U_C\)?", r"\(f_0=159\) Gs; \(I=1\) A; \(Q=\sqrt{L/C}/R=10\); \(U_C=100\) V — manbadan 10 marta katta!")],
 [(r"Elektr uzatishda kuchlanish 10 marta oshirilsa, liniyadagi isrof?", "100 marta kamayadi"),
  (r"Uchburchak ulashda faza kuchlanishi 380 V, faza toki 5 A. Liniya toki?", "8,66 A"),
  (r"Parallel LC (\(L=0{,}1\) H, \(C=10\) mkF) rezonansda umumiy tok (ideal)?", "0"),
  (r"Transformator FIK 96 %, ikkilamchi quvvat 480 W. Birlamchi quvvat?", "500 W")],
 r"""import numpy as np
R, L, C, U = 10, 0.1, 10e-6, 10
f0 = 1/(2*np.pi*np.sqrt(L*C)); Q = np.sqrt(L/C)/R
print(f"f0 = {f0:.1f} Hz, Q = {Q:.1f}, I = {U/R:.1f} A, U_C = {Q*U:.0f} V")
for f in (100, 150, f0, 170, 250):
    w = 2*np.pi*f; Z = np.hypot(R, w*L - 1/(w*C))
    print(f"f = {f:6.1f} Hz: I = {U/Z:.3f} A")
Uf = 220; print(f"Yulduz: U_l = {Uf*np.sqrt(3):.0f} V, P = {3*Uf*Uf/22/1000:.1f} kW")""",
 ["Kuchlanishlar va toklar rezonansining farqi?", "Transformator o‘zgarmas tokda ishlaydimi?", "Uch fazali tizimning afzalliklari?", "Rezonans xavfli bo‘lishi mumkinmi?"])
