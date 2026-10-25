The Price of Finding a Certificate: Unsupported Pareto Points under Prefix Queries
Antonio Clim | SICOMP | KIT 04 — FIGURI EDITABILE | P42

1. FIȘIERELE CURENTE ȘI NUMEROTAREA

Deschide în LibreOffice Draw:
  odg/Fig1_Editable.odg — prefixul comun și cele două rute de achiziție;
  odg/Fig2_Editable.odg — regimurile analitice pentru benzile diagonale;
  odg/Fig3_Editable.odg — alfabetul fix și limitele asimptotice.

Fig1 este fosta figură introductivă Fig0 din P40. Fig2 este fosta Fig1,
iar Fig3 este fosta Fig2 din P37. Numerotarea curentă este folosită în
surse, legende, valori, inventare și metadatele exporturilor. Dosarul
history/P37/ conține rapoarte istorice nemodificate: numerotarea și hashurile
lor descriu baza de atunci, nu fișierele curente.

Toate cele trei pagini măsoară 5 × 6 in (12,7 × 15,24 cm). Conținutul
este alcătuit din obiecte native individuale, nu dintr-o imagine a paginii:
  Fig1: 46 casete de text, 13 forme vectoriale, fără grupuri;
  Fig2: 322 casete de text, 366 forme vectoriale, 341 grupuri;
  Fig3: 98 casete de text, 50 forme vectoriale, 117 grupuri.
Nu există draw:image, OLE sau SVG încapsulat în pagină. Miniatura de
previzualizare creată de LibreOffice nu este conținutul editabil al figurii.

reference_exports/ conține PDF/SVG/PNG pentru manuscris. Fig2 și Fig3 au
fost regenerate cu numerotarea curentă: SVG și PNG sunt identice octet cu
octet cu vechile Fig1 și Fig2. PDF-urile au metadatele renumerotate; imaginile
lor randate sunt identice cu baza P37. Fig1 păstrează exact desenul P40.
native_exports/ conține PDF/PNG obținute prin redeschiderea ODG în LibreOffice.
fodg/ este versiunea nativă XML lizibilă. values/ păstrează valorile exacte,
legendele și rapoartele de generare. verification/ conține verificările P41.

2. EDITARE PAS CU PAS — OPȚIONALĂ

A. Dezarhivează kitul într-un dosar; nu edita în ZIP. Fă o copie a ODG.
B. Instalează LibreOffice și, pentru redare stabilă, cele patru fonturi .ttf
   din source/fonts/. Folosește funcția de instalare a fonturilor sistemului;
   nu este necesară reinstalarea acelorași versiuni. Licența este inclusă.
C. Deschide copia în Draw. Folosește File > Save As pentru un nume nou,
   de exemplu Fig2_Editable_revizie_01.odg; păstrează formatul ODG.
D. Pentru Fig2/3, intră în grup cu dublu clic sau clic dreapta > Enter Group.
   F3 intră în grup; repetă când există grupuri imbricate. Fig1 nu cere
   acest pas. Navigator (F5) permite selectarea obiectelor după numele lor.
E. Selectează textul și apasă F2. Fontul, mărimea și culoarea sunt editabile.
   Formulele pot conține mai multe fragmente de text; acestea sunt texte
   reale, nu contururi de litere. Intră în grupul formulei pentru un fragment.
F. Pentru linii, marcaje, contururi și hașuri, selectează obiectul și schimbă
   Line/Area. F4 deschide Position and Size; F8 permite editarea punctelor.
G. Ieși prin Exit Group. Dacă este necesar, folosește meniul Ungroup.
   Ctrl+Shift+G grupează în Draw; nu îl folosi drept comandă de degrupare.
H. Salvează. Exportă o copie prin File > Export As > Export as PDF, pagina 1,
   fără schimbarea dimensiunii. Compară toate etichetele și valorile cu
   originalul, inclusiv la zoom mare. Pentru PNG: 1800 × 2160 pixeli, 360 dpi.

Instrucțiuni oficiale pentru comenzi și grupuri:
https://help.libreoffice.org/latest/en-GB/text/sdraw/04/01020000.html
https://documentation.libreoffice.org/assets/Uploads/Documentation/en/DG7.5/DG75-DrawGuide.pdf
Denumirile meniurilor diferă după versiune și limba interfeței.

3. VALORI ȘI SEMNIFICAȚIE CARE TREBUIE PĂSTRATE

Acestea sunt ilustrații matematice, nu măsurători sau intervale de încredere.
Fig1: prefix (2,3,1), șase înregistrări plătite; minimele C* sunt 8 și 7;
rutele costă (9,7) și (8,9). Probabilitățile 16/23 și 7/23 dau 25/23.
Cele două lumi sunt prezentate retrospectiv; politica nu primește o promisiune
că arhiva aparține acestei perechi. Raportul global folosește demonstrația
completă din Supplement S1.6, nu doar acest desen.
Fig2: N rămâne întreg, fără interpolare; 0<d<=1, iar d=0 este exclus.
Pragurile K=3 sunt d(N−1)=2 și 3, cu limite superioare incluse. Pentru
K>=3, regiunea exactă este 0<dN<=1 la prețuri unitare și setup zero.
Marcajul N=5,d=1 rămâne 71/67 randomizat și 15/14 determinist.
Fig3: N=12,q=3; U are A=(3/4,1/4), L=(5/12,5/12), R=(1,0);
V are A=(5/6,1/4), L=(1/2,1/2), R=(1,0). Intervalul central are lățimea
3/8800: nu îl lărgi artificial. Limitele sunt pentru puncte de acumulare;
convergența și constantele asimptotice exacte rămân nedemonstrate.

La inserarea în manuscris, păstrează lățimea de 5 in fără o limită de
înălțime mai mică: etichete >=8,5 pt, linii esențiale >=1 pt. Culoarea,
hașura, formele marcajelor și legenda trebuie să rămână coerente.

4. RECONSTRUIRE OPȚIONALĂ, ÎNTR-O COPIE A KITULUI

Nu trebuie să rulezi nimic pentru a folosi fișierele deja pregătite.
Comenzile de mai jos se execută în terminal, din rădăcina kitului, nu în chat.
Reconstrucția suprascrie exporturile și rapoartele; nu păstrează modificările
manuale făcute în ODG. Păstrează o copie a modificărilor înainte de rulare.

Windows:
  py -m venv .venv
  .venv\Scripts\activate
  python -m pip install -r source/requirements_figures.txt
Linux/macOS:
  python3 -m venv .venv
  . .venv/bin/activate
  python -m pip install -r source/requirements_figures.txt

LibreOffice trebuie instalat separat. Comanda pentru toate cele trei
figuri de manuscris, pornind de la constante și fără acces la rețea:
  python source/rebuild_figures.py --output-dir reference_exports --soffice soffice
Apoi reconstruiește cele trei ODG și PDF-urile lor native:
  python source/build_editable_odg.py --convert --soffice soffice
Verifică structura, textele și geometria; reface și PNG-urile native:
  python source/verify_odg.py --render-previews
Previzualizări la dimensiunea finală, inclusiv tonuri de gri:
  python source/render_previews.py
Verifică separat valorile exacte:
  python source/check_figure_values.py reference_exports/Figure_Exact_Values.json
Rezultat așteptat: PASS, 56 puncte de prag și amestecul celor două rute verificat.
Test de editare programatică în copii temporare, pentru toate trei:
  python source/edit_roundtrip_probe.py --soffice soffice

Dacă soffice nu este în PATH, înlocuiește argumentul lui --soffice:
Windows: "C:\Program Files\LibreOffice\program\soffice.exe"
macOS: /Applications/LibreOffice.app/Contents/MacOS/soffice
De exemplu, pe Windows:
  python source/rebuild_figures.py --output-dir reference_exports --soffice "C:\Program Files\LibreOffice\program\soffice.exe"

Comanda restrânsă de mai jos reconstruiește NUMAI Fig2 și Fig3 într-un
alt dosar; nu scrie Fig1 și nu suprascrie metadatele comune celor trei:
  python source/make_figures.py --output-dir rebuilt_theorem_figures
Rapoartele ei încep cu Theorem_Figures_. Comanda pentru figura introductivă
produce SVG/FODG și aritmetica, fără export PDF sau ODG:
  python source/build_prefix_figure.py --output-dir rebuilt_prefix

Rulările scriu metadatele curente în dosarul de ieșire. Dacă faci o nouă
ediție a kitului, înlocuiește copiile din values/ cu noile fișiere JSON/TXT
și regenerează inventarele de licență și integritate înainte de distribuire.
Un manifest de integritate anterior nu descrie automat fișierele modificate.

5. VERIFICĂRI MOȘTENITE DIN P41 ȘI LIMITE

Toate cele trei ODG au fost salvate și redeschise headless în LibreOffice;
PDF-urile au câte o pagină 5 × 6 in, fără imagini raster. Cele 46/322/98
fragmente de text au fost păstrate exact. Inventarul caracterelor fără spații
din PDF corespunde SVG (584/378/498). Nicio etichetă nu depășește pagina;
fontul minim exportat este aproximativ 8,504 pt. Abaterea coordonatelor
verificate după salvare este sub 0,04 pt. Se includ previzualizări la
150 dpi pentru dimensiunea finală și versiuni în tonuri de gri.

Testul de editare schimbă un text și culoarea unei linii în copii temporare,
apoi verifică păstrarea lor după salvare și redeschidere. Este o probă
programatică; NU s-a efectuat editare manuală cu mouse-ul în interfața GUI.
Nu se pretinde identitate pixel cu pixel între LibreOffice și Matplotlib
sau între sisteme diferite. Verificările reprezentării nu demonstrează teoreme.
Fișierele verification/ conțin rezultatele efective și hashurile aferente.

6. LICENȚE ȘI STARE

Codul propriu nou: BSD-3-Clause. Documentația, tabelele și figurile proprii
noi: CC BY 4.0, în limita drepturilor lui Antonio Clim, conform autorizării
adoptate anterior. DejaVu păstrează termenii din source/fonts/LICENSE_DEJAVU,
inclusiv pentru subseturile încorporate. LICENSING.md și LICENSE_SCOPE.json
identifică exact componentele. Nicio licență a terților nu a fost înlocuită.

P42 este o pregătire locală, fără depunere la SICOMP, depozit public sau
publicare Zenodo. Această stare nu restrânge drepturile acordate prin licențe.

ACTUALIZARE P42
Cele trei figuri și sursele lor sunt identice cu versiunea P41 verificată.
S-au actualizat numai metadatele și documentația de livrare.
