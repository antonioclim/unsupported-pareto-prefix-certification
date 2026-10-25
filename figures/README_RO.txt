SURSE FIGURI — P46 — Antonio Clim

Numerotare: Fig1 = prefixul comun (fosta Fig0 P40); Fig2 = regimurile
analitice (fosta Fig1 P37); Fig3 = alfabetul fix și limitele (fosta Fig2 P37).
PDF/SVG/PNG gata pregătite sunt în generated/. Copiile folosite de LaTeX se află în kitul separat de submission,
02_Editable_Sources/source/. Toate au 5 × 6 in; inserează
la 5 in lățime fără plafon de înălțime mai mic. Fig3 folosește limita exactă candidate-census 12/11 și intervalul
unrestricted [23/22,12/11], cu diferența 1/22.

Nu este necesară rularea comenzilor pentru submission. Pentru reconstruire,
folosește o copie a dosarului și deschide terminalul în acest director.
Comenzile se rulează în terminal, nu se postează în chat.

Windows:
  py -m venv .venv
  .venv\Scripts\activate
  python -m pip install -r requirements-figures.txt
Linux/macOS:
  python3 -m venv .venv
  . .venv/bin/activate
  python -m pip install -r requirements-figures.txt

Instalează separat LibreOffice; fonturile DejaVu și licența sunt în fonts/.
O singură comandă reconstruiește toate cele trei figuri:
  python rebuild_figures.py --output-dir generated --soffice soffice
Rezultat așteptat: PASS și Fig1/2/3.pdf, .svg, .png, valorile și legendele.
Fig1 este exportată prin LibreOffice; Fig2/3 prin Matplotlib.
Verifică independent aritmetica:
  python check_figure_values.py generated/Figure_Exact_Values.json
Rezultat așteptat: PASS, 56 puncte de prag și amestecul rutelor verificat.

Dacă soffice nu este în PATH, folosește calea completă:
Windows:
  python rebuild_figures.py --output-dir generated --soffice "C:\Program Files\LibreOffice\program\soffice.exe"
macOS:
  python rebuild_figures.py --output-dir generated --soffice /Applications/LibreOffice.app/Contents/MacOS/soffice

Generatorul restrâns nu atinge Fig1 sau metadatele combinate:
  python make_figures.py --output-dir rebuilt_theorem_figures
El produce numai Fig2/3 și metadate Theorem_Figures_*. Nu confunda această
comandă restrânsă cu reconstruirea integrală prin rebuild_figures.py.

După modificări intenționate, inspectează toate figurile, inclusiv în gri,
apoi copiază cele trei PDF-uri din generated/ în dosarele figures/generated/
și source/ ale kitului 01/02_Editable_Sources. Recompilează Main și Supplement
conform ghidului principal; verifică numerele și trimiterile. Reconstruirea
nu păstrează editări manuale făcute în ODG. Pentru ODG-uri native și testele
lor complete folosește kitul separat 04_Figures_Editable_ODG.

Cod propriu: BSD-3-Clause; figuri și documentație proprie: CC BY 4.0,
în limita drepturilor lui Antonio Clim. DejaVu păstrează licența din fonts/.
Textele integrale și inventarul sunt în documentația de licențiere a kitului.
P46 este pregătit local, fără depunere sau publicare externă.

P49: textele din toate figurile sunt negre; culorile formelor, coordonatele, valorile și legendele rămân neschimbate. Exporturile au fost reconstruite și verificate.
