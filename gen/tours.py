"""Interaktiv modellar uchun ovozli avtomatik namoyish ssenariylari.
Har bir qadam: (parametrlar, izoh). Tanlov (select) uchun qiymat '#indeks' ko'rinishida beriladi."""

T = {
 "coulomb": [
  ({"q1": 2, "q2": -3, "r": 0.3, "eps": 1}, "Bu model Kulon qonunini ko‘rsatadi. Ikki mikrokulon va minus uch mikrokulon zaryadlar o‘ttiz santimetr masofada. Ular nol butun olti nyuton kuch bilan tortishadi."),
  ({"r": 0.6}, "Masofani ikki marta oshiramiz. Kuch to‘rt marta kamaydi: Kulon kuchi masofa kvadratiga teskari proporsional."),
  ({"q2": 3}, "Ikkinchi zaryad ishorasini almashtiramiz. Endi bir xil ishorali zaryadlar itariladi, kuch yo‘nalishi teskari bo‘ldi."),
  ({"r": 0.3, "eps": 81}, "Zaryadlarni suvga tushiramiz. Suvning dielektrik singdiruvchanligi sakson bir, shuning uchun kuch sakson bir marta kamaydi."),
  ({"q1": 2, "q2": -3, "r": 0.3, "eps": 1}, "Namoyish tugadi. Endi zaryadlar va masofani o‘zingiz o‘zgartirib ko‘ring.")],
 "field": [
  ({"cfg": "#0", "k": -1, "px": 0, "py": 0}, "Bu model elektr maydon kuch chiziqlarini ko‘rsatadi. Musbat va manfiy zaryad — dipol. Kuch chiziqlari musbat zaryaddan chiqib, manfiyga kiradi. O‘rtadagi kuchlanganlik uch ming ikki yuz volt metrga yaqin."),
  ({"py": 20}, "Sinov nuqtasini o‘rta perpendikulyar bo‘ylab yigirma santimetr yuqoriga ko‘taramiz. Maydon zaryadlarni tutashtiruvchi chiziqqa parallel va olti yuz to‘qson volt metrga teng — ishlangan misoldagi javob."),
  ({"k": 1, "py": 0}, "Ikkala zaryadni musbat qilamiz. O‘rtada kuch chiziqlari bir-biridan qochadi va kuchlanganlik nolga teng bo‘ladi."),
  ({"cfg": "#2", "px": 0, "py": 0}, "Kvadrat uchlaridagi to‘rt zaryad. Superpozitsiya prinsipi bo‘yicha markazda maydonlar vektor sifatida qo‘shiladi va besh ming volt metrdan oshadi."),
  ({"cfg": "#0", "k": -1, "px": 0, "py": 20}, "Namoyish tugadi. Sinov nuqtasini surib, maydon qanday o‘zgarishini o‘zingiz kuzating.")],
 "gauss": [
  ({"mode": "#0", "Q": 10, "R": 10, "r": 5}, "Bu model Gauss teoremasi yordamida simmetrik maydonlarni ko‘rsatadi. Bir jinsli zaryadlangan shar ichida kuchlanganlik markazdan masofaga chiziqli o‘sadi."),
  ({"r": 20}, "Gauss sirtini shardan tashqariga chiqaramiz. Endi butun zaryad sirt ichida, maydon masofa kvadratiga teskari kamayadi, xuddi nuqtaviy zaryaddagidek."),
  ({"mode": "#1", "r": 5}, "Sferik qobiqni tanlaymiz. Ichkarida zaryad yo‘q, shuning uchun kuchlanganlik nolga teng. Faradey qafasi shu prinsipda ishlaydi."),
  ({"mode": "#3", "r": 20}, "Cheksiz tekislik maydoni masofaga bog‘liq emas: grafik tashqarida gorizontal chiziq."),
  ({"mode": "#0", "Q": 10, "R": 10, "r": 5}, "Namoyish tugadi. Boshqa taqsimotlarni o‘zingiz sinab ko‘ring.")],
 "potential": [
  ({"cfg": "#0", "q": 4, "d": 30}, "Bu model potensial xaritasini ko‘rsatadi. Pushti — musbat, ko‘k — manfiy potensial. Oq chiziqlar — ekvipotensial chiziqlar, ular kuch chiziqlariga perpendikulyar."),
  ({"cfg": "#0"}, "Dipol o‘rtasida potensial nolga teng, lekin pastki grafikka qarang: kuchlanganlik nol emas. Potensial nol bo‘lishi maydon yo‘qligini bildirmaydi."),
  ({"cfg": "#1"}, "Ikki musbat zaryad: o‘rtada kuchlanganlik nolga teng, potensial esa musbat va katta."),
  ({"cfg": "#2"}, "Zaryadlar teng bo‘lmaganda ekvipotensial chiziqlar nosimmetrik bo‘ladi, nol potensialli chiziq kichik zaryadni o‘rab oladi."),
  ({"cfg": "#0", "q": 4, "d": 30}, "Namoyish tugadi.")],
 "dielectric": [
  ({"eps": 1, "s": 1, "a": 45}, "Bu model dielektrikdagi maydonni ko‘rsatadi. Hozir singdiruvchanlik birga teng — oraliq havo bilan to‘lgan."),
  ({"eps": 4}, "To‘rtga teng dielektrik kiritamiz. Uning sirtlarida bog‘langan zaryadlar paydo bo‘ldi, ichkaridagi maydon to‘rt marta kamaydi. Induksiya vektori esa o‘zgarmadi."),
  ({"eps": 8}, "Singdiruvchanlikni oshirsak, bog‘langan zaryadlar ko‘payadi va maydon yanada susayadi."),
  ({"eps": 4, "a": 30}, "O‘ngda kuch chiziqlarining chegarada sinishi: dielektrikda chiziqlar normaldan uzoqlashadi, burchaklar tangenslari nisbati singdiruvchanliklar nisbatiga teng."),
  ({"eps": 4, "s": 1, "a": 45}, "Namoyish tugadi.")],
 "capacitor": [
  ({"S": 100, "d": 1, "eps": 1, "U": 100}, "Bu model yassi kondensatorni ko‘rsatadi. Yuza yuz kvadrat santimetr, oraliq bir millimetr. Sig‘im sakson sakkiz pikofarad."),
  ({"d": 2}, "Oraliqni ikki marta oshiramiz. Sig‘im ikki marta kamaydi, bir xil kuchlanishda zaryad va energiya ham kamaydi."),
  ({"d": 1, "eps": 5}, "Besh singdiruvchanlikli dielektrik kiritamiz. Sig‘im besh marta ortdi."),
  ({"eps": 1, "U": 500}, "Kuchlanishni besh marta oshiramiz. Energiya kuchlanish kvadratiga proporsional, ya’ni yigirma besh marta ortdi."),
  ({"S": 100, "d": 1, "eps": 1, "U": 100}, "Namoyish tugadi.")],
 "ohm": [
  ({"E": 12, "r": 0.5, "R": 5.5}, "Bu model to‘la zanjir uchun Om qonunini ko‘rsatadi. EYuK o‘n ikki volt, ichki qarshilik yarim om, yuklama besh yarim om. Tok ikki amper, foydali quvvat yigirma ikki vatt."),
  ({"R": 0.5}, "Yuklamani ichki qarshilikka tenglashtiramiz. Foydali quvvat maksimal — yetmish ikki vatt, lekin foydali ish koeffitsiyenti atigi ellik foiz."),
  ({"R": 20}, "Katta yuklamada FIK yuqori, ammo quvvat kichik."),
  ({"R": 0.1}, "Qisqa tutashuvga yaqin holat: tok juda katta, energiyaning deyarli hammasi manbaning o‘zida issiqlikka aylanadi."),
  ({"E": 12, "r": 0.5, "R": 5.5}, "Namoyish tugadi.")],
 "kirchhoff": [
  ({"E1": 12, "E2": 6, "R1": 2, "R2": 4, "R3": 6}, "Bu model Kirxgof qoidalari bilan ikki manbali zanjirni hisoblaydi. Birinchi manba orqali bir butun to‘qson bir amper, o‘rtadagi qarshilik orqali bir butun o‘ttiz olti amper tok o‘tadi."),
  ({}, "Ikkinchi manbadagi tok manfiy chiqdi. Demak u yerda tok teskari yo‘nalgan va olti voltli manba zaryadlanmoqda. O‘ngdagi quvvat balansiga qarang."),
  ({"E2": 10}, "Ikkinchi EYuKni o‘n voltga oshiramiz. Endi ikkala manba ham energiya beradi."),
  ({"E2": 6, "R3": 1}, "O‘rtadagi qarshilikni kamaytiramiz: undagi tok keskin ortdi. Har qanday holatda manbalar quvvati rezistorlardagi issiqlikka teng."),
  ({"E1": 12, "E2": 6, "R1": 2, "R2": 4, "R3": 6}, "Namoyish tugadi.")],
 "biot": [
  ({"mode": "#0", "I": 10, "x": 5}, "Bu model Bio–Savar–Laplas qonunini ko‘rsatadi. O‘n amperli to‘g‘ri tokdan besh santimetrda induksiya qirq mikrotesla — Yer maydoniga yaqin."),
  ({"x": 10}, "Masofani ikki marta oshiramiz: induksiya ham ikki marta kamaydi."),
  ({"mode": "#1", "I": 5, "R": 10, "x": 0}, "Doiraviy o‘ram markazida induksiya o‘ttiz bir butun to‘rt mikrotesla. O‘q bo‘ylab uzoqlashganda u tez kamayadi."),
  ({"mode": "#2", "I": 2, "N": 500, "x": 0}, "Solenoid o‘rtasida maydon deyarli bir jinsli va mu nol n I ga teng. Uchlarida esa ikki marta kichik."),
  ({"mode": "#0", "I": 10, "x": 5}, "Namoyish tugadi.")],
 "ampere": [
  ({"I1": 20, "I2": 20, "d": 10}, "Bu model ikki parallel tokni ko‘rsatadi. Toklar bir yo‘nalishda: o‘rtada maydonlar bir-birini yo‘qotadi, simlar esa tortishadi."),
  ({"I2": -20}, "Ikkinchi tok yo‘nalishini almashtiramiz. O‘rtada maydon bir yuz oltmish mikroteslaga teng bo‘ldi, simlar endi itariladi."),
  ({"d": 5}, "Masofani ikki marta kamaytiramiz: birlik uzunlikka kuch ikki marta ortdi."),
  ({"I1": 20, "I2": 20, "d": 10}, "Birinchi sim atrofidagi uzuq aylana — sirkulyatsiya konturi. Uning bo‘ylab induksiya sirkulyatsiyasi faqat o‘ralgan tokka bog‘liq. Namoyish tugadi.")],
 "lorentzf": [
  ({"p": "#0", "v": 10, "B": 100, "E": 0, "a": 90}, "Bu model Lorens kuchini ko‘rsatadi. Proton magnit maydonga perpendikulyar uchib kirdi va aylana bo‘ylab harakatlanmoqda."),
  ({"v": 20}, "Tezlikni ikki marta oshiramiz: radius ham ikki marta ortdi, lekin aylanish davri o‘zgarmadi. Siklotron shu xossaga asoslangan."),
  ({"v": 10, "a": 45}, "Tezlik maydonga burchak ostida bo‘lsa, zarra vint chiziq bo‘ylab harakatlanadi. O‘ngda yondan ko‘rinish."),
  ({"a": 90, "E": 20}, "Elektr maydonni qo‘shamiz. Zarra endi maydonlarga perpendikulyar yo‘nalishda siljiydi — bu E kesishgan B dreyfi."),
  ({"p": "#0", "v": 10, "B": 100, "E": 0, "a": 90}, "Namoyish tugadi.")],
 "hyster": [
  ({"mode": "#0", "Hm": 1000, "Hc": 150, "Ms": 1.2}, "Bu model ferromagnetikning gisterezis sirtmog‘ini ko‘rsatadi. Tashqi maydon davriy o‘zgaradi, domenlar burilib, magnitlanish to‘yinishga chiqadi."),
  ({"Hc": 500}, "Koersitiv kuchni oshiramiz — qattiq ferromagnetik. Sirtmoq kengaydi, bir siklda isrof ortdi. Bunday materiallar doimiy magnitlarda ishlatiladi."),
  ({"Hc": 30}, "Yumshoq ferromagnetik: sirtmoq tor, isrof kichik — transformator o‘zaklari uchun."),
  ({"mode": "#1"}, "Paramagnetikda magnitlanganlik maydonga chiziqli va juda kichik, gisterezis yo‘q."),
  ({"mode": "#0", "Hm": 1000, "Hc": 150, "Ms": 1.2}, "Namoyish tugadi.")],
 "rl": [
  ({"mode": "#0", "E": 10, "R": 10, "L": 0.5}, "Bu model RL zanjirda tokning qaror topishini ko‘rsatadi. Vaqt doimiysi ellik millisekund. Shu vaqtda tok barqaror qiymatining oltmish uch foiziga yetadi."),
  ({"L": 1.5}, "Induktivlikni uch marta oshiramiz: jarayon uch marta sekinlashdi."),
  ({"L": 0.5, "R": 30}, "Qarshilikni oshirsak, vaqt doimiysi kamayadi, barqaror tok ham kamayadi."),
  ({"mode": "#1", "R": 10}, "Uzish jarayoni: o‘zinduksiya EYuK tokni ushlab turishga harakat qiladi, tok eksponensial kamayadi."),
  ({"mode": "#0", "E": 10, "R": 10, "L": 0.5}, "Namoyish tugadi.")],
 "wave": [
  ({"E0": 100, "f": 100, "n": 1}, "Bu model elektromagnit to‘lqinni ko‘rsatadi. Sariq — elektr maydon, havorang — magnit maydon. Ular bir-biriga va tarqalish yo‘nalishiga perpendikulyar va bir fazada tebranadi."),
  ({"f": 200}, "Chastotani ikki marta oshiramiz: to‘lqin uzunligi ikki marta qisqardi."),
  ({"f": 100, "n": 2}, "Sindirish ko‘rsatkichi ikkiga teng muhitda to‘lqin tezligi va uzunligi ikki marta kamayadi."),
  ({"n": 1, "E0": 200}, "Amplitudani ikki marta oshirsak, intensivlik to‘rt marta ortadi."),
  ({"E0": 100, "f": 100, "n": 1}, "Namoyish tugadi.")],
 "ac": [
  ({"R": 100, "L": 0.5, "C": 10, "f": 50, "U": 220}, "Bu model o‘zgaruvchan tok zanjirini ko‘rsatadi. Ellik gersda sig‘im qarshilik induktiv qarshilikdan katta, tok kuchlanishdan oldinda, quvvat koeffitsiyenti nol butun ellik uch."),
  ({"f": 71}, "Chastotani yetmish bir gersga yaqinlashtiramiz. Bu kuchlanishlar rezonansi: induktiv va sig‘im qarshiliklar teng, tok maksimal va kuchlanish bilan bir fazada."),
  ({"R": 20}, "Qarshilikni kamaytiramiz: rezonans egri chizig‘i keskinlashdi, g‘altak va kondensatordagi kuchlanishlar tarmoq kuchlanishidan bir necha marta oshib ketdi."),
  ({"R": 100, "f": 150}, "Rezonansdan yuqori chastotada zanjir induktiv xarakterga ega, tok kuchlanishdan orqada."),
  ({"R": 100, "L": 0.5, "C": 10, "f": 50, "U": 220}, "Namoyish tugadi.")],
 "rc": [
  ({"mode": "#0", "U": 10, "R": 1, "C": 100}, "Bu model kondensatorning zaryadlanishini ko‘rsatadi. Vaqt doimiysi nol butun bir sekund."),
  ({}, "O‘ng grafikka qarang: manba bergan energiyaning aniq yarmi kondensatorda to‘planadi, yarmi rezistorda issiqlikka aylanadi."),
  ({"R": 5}, "Qarshilikni besh marta oshiramiz: zaryadlanish sekinlashdi, lekin energiyalar nisbati baribir yarmiga teng."),
  ({"mode": "#1", "R": 1}, "Razryad: kondensator energiyasi to‘liq rezistorda issiqlikka aylanadi."),
  ({"mode": "#0", "U": 10, "R": 1, "C": 100}, "Namoyish tugadi.")],
 "rlc": [
  ({"mode": "#0", "L": 10, "C": 1, "R": 20}, "Bu model tebranish konturini ko‘rsatadi. Xususiy chastota bir ming besh yuz to‘qson gers, asllik beshga teng. Tebranishlar so‘nmoqda."),
  ({}, "O‘ng grafikda energiya kondensatordan g‘altakka va qaytib o‘tib turadi, umumiy energiya qarshilikda kamayadi."),
  ({"R": 0}, "Qarshilik nol bo‘lsa, tebranishlar so‘nmaydi."),
  ({"R": 250}, "Qarshilik kritik qiymatdan katta bo‘lsa, tebranish bo‘lmaydi — aperiodik razryad."),
  ({"mode": "#1", "R": 20}, "Majburiy tebranishlar: rezonans chastotasida tok amplitudasi maksimal. Namoyish tugadi.")],
 "trafo": [
  ({"N1": 1100, "N2": 60, "Rl": 6, "eta": 96, "Uf": 220}, "Bu model transformatorni ko‘rsatadi. Bir ming bir yuz va oltmish o‘ramda ikki yuz yigirma volt o‘n ikki voltga pasayadi. Ikkilamchi tok ikki amper."),
  ({"N2": 2000}, "Ikkilamchi o‘ramlarni ko‘paytirsak, transformator kuchaytiruvchi bo‘ladi: kuchlanish ortadi, tok kamayadi."),
  ({"N2": 60, "Rl": 2}, "Yuklama qarshiligini kamaytirsak, ikkilamchi va birlamchi toklar ortadi."),
  ({"Rl": 6}, "O‘ngda uch fazali tok: uch sinusoida yuz yigirma gradusga siljigan. Yulduz ulashda liniya kuchlanishi uch ildizi marta katta — uch yuz sakson volt. Namoyish tugadi.")],
}
