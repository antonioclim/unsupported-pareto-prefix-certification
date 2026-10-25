ANALYTIC MANUSCRIPT FIGURES — P46

The three figures display exact constructions and analytic bounds. They contain
no measured performance, fitted data or statistical confidence intervals.
Fig1 illustrates the common-prefix obstruction. Fig2 shows the band regimes.
Fig3 shows the fixed-alphabet worlds and the asymptotic bounds: 12/11 is the
exact candidate-census limit on the stated triangle and fixed-alphabet domains
with unit prices and zero setup cost. For unrestricted randomised policies,
23/22 and 12/11 remain lower and upper bounds; their gap is 1/22. Convergence
and the exact unrestricted constant remain open.

The ready-to-use PDF/SVG/PNG files, exact values and captions are in generated/.
The editable ODG/FODG files and their object-level checks are in
../editable_figures/. All exports have a 5 by 6 inch canvas. Insert at 5 inches
wide without imposing a smaller height cap. Text is at least 8.5 pt and essential
native strokes at least 1 pt at that size. Colour is redundant with labels,
markers, hatching and line styles.

OPTIONAL REPRODUCTION
Use a new copy of this directory. The commands run in a terminal, not in a chat.
Create a virtual environment and install requirements-figures.txt if needed.
Install LibreOffice separately. Then run:

  python3 rebuild_figures.py --output-dir regenerated --soffice soffice
  python3 check_figure_values.py regenerated/Figure_Exact_Values.json

The first command rebuilds all three numbered figures. Expected status: PASS.
Fig1 uses LibreOffice; Fig2 and Fig3 use Matplotlib. The second uses only Python's
standard library and checks exact figure semantics, including 56 threshold
points and the route mixture. It does not replace the universal proofs.

The narrower command below rebuilds ONLY Fig2 and Fig3, with metadata names
starting Theorem_Figures_; it does not create or overwrite Fig1:

  python3 make_figures.py --output-dir rebuilt_theorem_figures

Native ODG reconstruction, edit roundtrips and object inventory checks are
explained in ../editable_figures/README_RO.txt. Rebuilding does not preserve
manual ODG edits; retain a copy first. Dependency installation may need internet;
figure generation itself is offline. Fonts and their licence are in fonts/.

The P44 scientific exports and exact values are retained unchanged in P46.
Rendering bytes may depend on library versions, operating system and fonts.
Current provenance records identify the actual environment and source hashes.
The standard-library science replay does not require plotting dependencies.
Own new code is BSD-3-Clause; own new documentation and figures are CC BY 4.0
within the author's rights. Preserve all third-party terms.
