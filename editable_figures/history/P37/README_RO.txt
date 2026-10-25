ARTICOL ASOCIAT — P36
The Price of Finding a Certificate: Unsupported Pareto Points under Prefix Queries
Autor: Antonio Clim

KIT 04 — FIGURI EDITABILE ÎN LIBREOFFICE DRAW (.ODG)
Antonio Clim | SICOMP | pachet local, fără publicare externă
Data verificării: 24 octombrie 2026

1. CE DESCHIZI

Pentru editare, deschide:
  odg/Fig1_Editable.odg
  odg/Fig2_Editable.odg

Fiecare fișier este un desen nativ de o pagină, 12,7 × 15,24 cm
(5 × 6 in). Nu este o imagine introdusă într-un document ODG.
Textele, axele, marcajele, contururile, benzile, liniile hașurii și
liniile de indicație sunt obiecte native distincte, selectabile.

Fig1: 322 casete de text, 366 forme vectoriale, 341 grupuri.
Fig2:  98 casete de text,  50 forme vectoriale, 117 grupuri.
Niciun draw:image, obiect OLE, imagine SVG încorporată sau bitmap
nu apare în conținutul paginii. LibreOffice poate păstra separat
miniatura de previzualizare a documentului; aceasta nu este figura.

reference_exports/ păstrează PDF/SVG/PNG originale P33, nemodificate.
native_exports/ conține PDF-urile exportate DUPĂ redeschiderea ODG și
PNG-urile de control la 360 dpi. Originalele rămân referința pentru
manuscrisul existent. Nu înlocui figurile din manuscris dacă nu ai
făcut o modificare intenționată și verificată.
fodg/ păstrează aceeași structură nativă în XML OpenDocument lizibil.
values/ conține valorile exacte, legendele și raportul original.
source/ conține generatorul, verificatoarele și fonturile licențiate.
verification/ conține rezultatele efectiv executate.

2. DESCHIDERE ȘI EDITARE, PAS CU PAS

A. Dezarhivează întregul kit într-un dosar normal. Nu edita în ZIP.
B. Instalează LibreOffice, dacă nu este deja instalat.
C. Pentru redare stabilă, instalează cele patru fișiere .ttf din
   source/fonts/ prin funcția de instalare a fonturilor a sistemului.
   Sunt DejaVu Sans regular, bold, oblique și bold-oblique, nemodificate.
   Licența lor este inclusă în source/fonts/LICENSE_DEJAVU.
   Dacă erau deja instalate aceleași fonturi, nu trebuie reinstalate.
D. Deschide odg/Fig1_Editable.odg sau Fig2_Editable.odg în Draw.
E. Folosește File > Save As și salvează o copie, de exemplu
   Fig2_Editable_revizie_01.odg. Păstrează extensia și formatul ODG.
F. Fă dublu clic pe grup sau clic dreapta > Enter Group (Intră în grup).
   F3 intră în grup. Repetă când obiectul este într-un grup imbricat.
   Grupurile păstrează structura: axes_1/axes_2, text_*, line2d_*,
   legend_*, patch_*; obiectele au și nume unice Fig1_... / Fig2_....
G. Pentru text, selectează caseta și apasă F2; poți folosi și dublu clic
   pe text după ce ai intrat în grupul potrivit. Modifică textul,
   fontul, dimensiunea sau culoarea în bara de formatare.
H. Formulele și unele etichete sunt alcătuite din mai multe fragmente
   sau chiar caractere editabile, pentru a conserva tipografia exactă.
   Intră în grupul etichetei și selectează fragmentul dorit. Nu sunt
   contururi de litere: fiecare fragment conține text real.
I. Pentru linie/marcaj/hașură, selectează obiectul și folosește
   proprietățile Line/Area (Linie/Suprafață) pentru grosime și culoare.
   F4 deschide Position and Size; F8 activează editarea punctelor
   pentru formele vectoriale. Fiecare linie de hașură poate fi editată.
J. Pentru a ieși, clic dreapta > Exit Group (Ieși din grup).
   Dacă dorești să desfaci un grup, clic dreapta > Ungroup.
   ATENȚIE: Ctrl+Shift+G grupează obiectele; nu este comanda de
   degrupare în Draw. Scurtătura de degrupare diferă între versiuni;
   folosește meniul dacă există dubii. Nu trebuie să desfaci toate
   grupurile pentru a edita un singur obiect.
K. Salvează ODG. Pentru o copie de publicare, File > Export As >
   Export as PDF; păstrează dimensiunea paginii și exportă pagina 1.
L. Redeschide PDF-ul rezultat și compară-l cu originalul, inclusiv la
   zoom mare. Verifică formulele, capetele intervalelor și toate
   legendele. Pentru o imagine PNG, exportă la 1800 × 2160 pixeli
   dacă păstrezi dimensiunea de 5 × 6 in și rezoluția de 360 dpi.

Straturile folosite sunt Editable labels și Analytic marks.
Selectarea unei regiuni complet albe poate selecta fundalul, nu textul;
revino în grup sau folosește Navigator (F5) și numele obiectului.

Ajutor oficial pentru F2/F3/F4/F5/F8 și comenzile Draw:
https://help.libreoffice.org/latest/en-GB/text/sdraw/04/01020000.html
Ghid pentru grupuri, meniuri și editarea obiectelor componente:
https://documentation.libreoffice.org/assets/Uploads/Documentation/en/DG7.5/DG75-DrawGuide.pdf
Consultate la 24 octombrie 2026. Denumirile meniurilor depind de limba UI.

3. CE NU TREBUIE MODIFICAT CA SIMPLĂ OPERAȚIE GRAFICĂ

Figurile sunt ilustrații analitice de teoreme, NU măsurători și NU
intervale de încredere. Schimbarea unei valori sau a unei coordonate
necesită o justificare matematică și actualizarea surselor și textului.

Fig1:
- N este întreg; coloanele rămân separate, fără interpolare.
- Domeniul este 0 < d <= 1; la d=0 clasa pozitivă este vidă.
- K=3: frontierele sunt d(N−1)=2 și d(N−1)=3, cu limite superioare
  incluse; aplică exact condițiile din Figure_Exact_Values.json.
- K>=3: regiunea exactă generală este 0 < dN <= 1, la prețuri
  unitare și setup zero.
- Marcajul N=5, d=1 păstrează 71/67 randomizat și 15/14 determinist.

Fig2:
- Alfabetul: (0,0), (1,0), (1,1); exemplul are N=12, q=3.
- U: A=(3/4,1/4), L=(5/12,5/12), R=(1,0).
- V: A=(5/6,1/4), L=(1/2,1/2), R=(1,0).
- Intervalele sunt [23/22,873/800], [12/11,873/800] și
  [12/11,3/(4*sqrt(2)-3)].
- Intervalul din mijloc are lățimea 3/8800; este foarte îngust pe
  scara figurii. Nu îl lărgi artificial pentru vizibilitate.
- Legenda precizează că sunt limite pentru puncte de acumulare;
  convergența și constantele asimptotice exacte rămân nedemonstrate.

După o schimbare strict estetică, păstrează fontul de minimum 8,5 pt
și liniile esențiale de minimum 1 pt la dimensiunea finală de 5 × 6 in.
Culoarea și hașura au rol semantic; schimbările trebuie sincronizate
între figură și legendă.

4. RECONSTRUIRE OPȚIONALĂ — NU ESTE NECESARĂ PENTRU EDITARE

Comenzile de mai jos se rulează într-un terminal deschis în rădăcina
acestui kit. Nu le posta în chat și nu trebuie executate pentru a
folosi ODG-urile deja pregătite. Folosește o COPIE a kitului: generatorul
rescrie fodg/, odg/, native_exports/ și unele rapoarte de verificare.
Reconstrucția pornește din SVG-urile de referință și NU păstrează
modificările făcute manual între timp în ODG.

Instalarea dependențelor într-un mediu virtual (Windows):
  py -m venv .venv
  .venv\Scripts\activate
  python -m pip install -r source/requirements_figures.txt

Instalarea dependențelor (Linux/macOS):
  python3 -m venv .venv
  . .venv/bin/activate
  python -m pip install -r source/requirements_figures.txt

Verificarea aritmeticii, fără LibreOffice sau biblioteci externe:
  python source/check_figure_values.py values/Figure_Exact_Values.json
Rezultat așteptat: status PASS; 56 puncte de prag verificate.

Refacerea FODG + ODG + PDF, dacă soffice este în PATH:
  python source/build_editable_odg.py --convert --soffice soffice

Pe Windows, dacă executabilul nu este în PATH:
  python source/build_editable_odg.py --convert --soffice "C:\Program Files\LibreOffice\program\soffice.exe"

Pe macOS, dacă executabilul nu este în PATH:
  python source/build_editable_odg.py --convert --soffice /Applications/LibreOffice.app/Contents/MacOS/soffice

Verificarea structurii ODG, textelor, geometriei și PDF-ului:
  python source/verify_odg.py --render-previews
Rezultat așteptat: status PASS; zero imagini în pagină; o pagină
5 × 6 in pentru fiecare figură. Se actualizează și previzualizările PNG.

Test opțional de editare și redeschidere, fără modificarea figurilor:
  python source/edit_roundtrip_probe.py --soffice soffice
Se schimbă un text și culoarea unei linii într-o copie temporară,
se salvează ODG, se redeschide FODG și se verifică ambele schimbări.
Nu se generează PDF și nu se modifică figurile finale.

Pentru refacerea originalelor Matplotlib într-un dosar SEPARAT:
  python source/make_figures.py --output-dir rebuilt_reference
Nu copia automat aceste rezultate peste reference_exports/. Compară
întâi valorile și aspectul; versiunile bibliotecilor pot modifica redarea.

5. VERIFICĂRI EFECTUATE ȘI LIMITE REALE

- Ambele ODG au fost salvate și apoi redeschise efectiv de LibreOffice
  pentru a exporta PDF. Versiunea: LibreOfficeDev 26.8.0.0.alpha0,
  build 2c87e51eeaa2b413ff4ae097b2705eea1995d8e5.
- Structura ZIP/XML a fost inspectată: obiecte și texte native,
  fără imagine introdusă în pagină, SVG încapsulat sau obiect OLE.
- Toate cele 322/98 fragmente de text au supraviețuit exact salvării.
- Inventarul caracterelor vizibile din PDF corespunde SVG: 378/498
  caractere fără spații; nu lipsesc etichete matematice.
- Coordonatele obiectelor native au fost comparate după roundtrip;
  eroarea maximă este sub 0,04 pt, datorată unităților interne Draw.
- Titlurile Fig2 sunt pe un singur rând; liniile legendei se opresc
  înaintea textului. S-a inspectat vizual fiecare figură la 5 × 6 in.
- Testul de editare a unui text și a culorii unei linii a trecut la
  salvare ODG și redeschidere. Testul este programatic; nu pretindem
  o sesiune manuală de editare cu mouse-ul în interfața desktop.
- Nu promitem identitate pixel cu pixel: LibreOffice, Matplotlib și
  sistemele de operare pot avea diferențe de rasterizare, fonturi și
  poziționare subpixel. ODG urmează pozițiile SVG originale; originalul
  PDF și SVG au deja mici diferențe de metrică pentru text multilinie.
- Capetele liniilor de hașură sunt retrase cu o fracțiune de punct
  pentru a păstra grosimea de 1 pt în interiorul conturului benzii.
- Verificările figurilor nu înlocuiesc demonstrațiile din articol.

Detalii verificabile: verification/Native_ODG_Verification.json,
Object_Inventory.json, Exact_Values_Check.json și Edit_Roundtrip_Probe.json.

6. DREPTURI ȘI STAREA PACHETULUI P36

Antonio Clim a adoptat, la 24 octombrie 2026, BSD-3-Clause pentru codul
propriu nou și CC BY 4.0 pentru documentația, tabelele și figurile proprii
noi, în limita drepturilor sale. Licențele sunt aplicate în acest kit;
nu mai sunt propuneri. Textele integrale sunt în LICENSES/, iar
LICENSING.md și LICENSE_SCOPE.json precizează componentele acoperite.

Fonturile DejaVu păstrează separat termenii și notificările din
source/fonts/LICENSE_DEJAVU. Nu sunt relicențiate ca operă proprie.
Fișierele ODG, exporturile și valorile matematice nu au fost modificate
prin această actualizare de licențiere. Rapoartele din verification/
consemnează verificările native executate în P34; nu sunt prezentate ca
rulări noi P36.

Nu s-a creat depozit public, nu s-a rezervat DOI și nu s-a trimis nimic
revistei. Autorul a autorizat actualizarea kiturilor locale, nu o acțiune
externă. Această limită descrie mandatul asistentului și nu adaugă
restricții la drepturile acordate destinatarilor prin licențe.

ACTUALIZAREA TITLULUI — P36
Titlul articolului este sincronizat cu documentele de submission și metadatele
curente. Fișierele ODG, FODG și exporturile își păstrează titlurile descriptive
proprii figurilor; nu conțin titlul anterior al articolului. Conținutul grafic,
valorile, obiectele editabile și verificările native P34 sunt păstrate neschimbate.
Licențele adoptate în P35 rămân aplicabile în limitele LICENSING.md.
