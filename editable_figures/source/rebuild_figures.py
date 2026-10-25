#!/usr/bin/env python3
"""Rebuild all three manuscript figures from exact constants, without network access.

BSD-3-Clause, Antonio Clim. Figures and own documentation: CC BY 4.0.
Figure 1 is exported by LibreOffice; Figures 2 and 3 by Matplotlib.
This command replaces generated files; it cannot preserve manual ODG edits.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir', type=Path,
                        default=Path(__file__).resolve().parent / 'generated')
    parser.add_argument('--soffice', default=shutil.which('soffice'))
    args = parser.parse_args()
    if not args.soffice:
        parser.error('LibreOffice soffice is required to export Figure 1; use --soffice PATH')
    out = args.output_dir.resolve()
    out.mkdir(parents=True, exist_ok=True)
    source = Path(__file__).resolve().parent
    subprocess.run([sys.executable, str(source/'make_figures.py'),
                    '--output-dir', str(out)], check=True)
    with tempfile.TemporaryDirectory(prefix='sicomp_prefix_figure_') as temporary:
        temp = Path(temporary)
        subprocess.run([sys.executable, str(source/'build_prefix_figure.py'),
                        '--output-dir', str(temp)], check=True)
        for input_file, directory, format_name in [
                (temp/'Fig1_Editable.fodg', temp/'saved', 'odg'),
                (temp/'saved/Fig1_Editable.odg', temp/'export', 'pdf:draw_pdf_Export')]:
            directory.mkdir(exist_ok=True)
            subprocess.run([args.soffice, '-env:UserInstallation='+(temp/'profile').as_uri(),
                            '--headless', '--convert-to', format_name, '--outdir',
                            str(directory), str(input_file)], check=True)
        shutil.copy2(temp/'Fig1.svg', out/'Fig1.svg')
        shutil.copy2(temp/'export/Fig1_Editable.pdf', out/'Fig1.pdf')
        import fitz
        document = fitz.open(out/'Fig1.pdf')
        document[0].get_pixmap(matrix=fitz.Matrix(5, 5)).save(out/'Fig1.png')
        prefix = json.loads((temp/'Fig1_Exact_Values.json').read_text())
        caption = (temp/'Fig1_Caption.txt').read_text().strip()
        for name in ['Fig1_Exact_Values.json', 'Fig1_Caption.txt']:
            shutil.copy2(temp/name, out/name)
    values = json.loads((out/'Theorem_Figures_Exact_Values.json').read_text())
    values['schema'] = 'sicomp-three-analytic-figures-p44-v1'
    values['Fig1'] = prefix
    values['captions'] = {'Fig1': caption.removeprefix('Fig1. '), **values['captions']}
    values['proof_locations']['Fig1'] = 'Supplement S1.6; the pair is illustrative, not a two-world promise'
    (out/'Figure_Exact_Values.json').write_text(json.dumps(values, ensure_ascii=False, indent=2)+'\n')
    (out/'Figure_Captions.txt').write_text('\n\n'.join(k+'. '+v for k,v in values['captions'].items())+'\n')
    theorem_record = json.loads((out/'Theorem_Figures_Build_Record.json').read_text())
    record = {
        'schema': 'sicomp-three-figure-build-p44-v1', 'revision': 'P44',
        'finished_at_utc': datetime.now(timezone.utc).isoformat(), 'status': 'PASS',
        'figure_order': ['Fig1', 'Fig2', 'Fig3'],
        'mapping': {'P40 Fig0': 'Fig1', 'P37 Fig1': 'Fig2', 'P37 Fig2': 'Fig3'},
        'prefix_arithmetic': prefix,
        'theorem_figure_generation': theorem_record,
        'generators_sha256': {name: sha(source/name) for name in
            ['rebuild_figures.py', 'make_figures.py', 'build_prefix_figure.py', 'build_editable_odg.py']},
        'values_sha256': sha(out/'Figure_Exact_Values.json'),
        'exports': [{'file': p.name, 'bytes': p.stat().st_size, 'sha256': sha(p)}
                    for i in range(1,4) for ext in ['pdf','svg','png']
                    for p in [out/f'Fig{i}.{ext}']],
        'new_measurements': False, 'network_calls': False, 'GUI_interaction_executed': False,
        'scope': 'Exact displayed arithmetic and generated representation; not a proof of manuscript theorems.',
        'final_insertion_requirement': 'Use 5 inch width, without a smaller height limit; all labels are at least 8.5 pt.'
    }
    (out/'Figure_Build_Record.json').write_text(json.dumps(record, ensure_ascii=False, indent=2)+'\n')
    subprocess.run([sys.executable, str(source/'check_figure_values.py'),
                    str(out/'Figure_Exact_Values.json')], check=True)
    print('PASS: rebuilt Fig1, Fig2 and Fig3; see Figure_Build_Record.json')

if __name__ == '__main__':
    main()
