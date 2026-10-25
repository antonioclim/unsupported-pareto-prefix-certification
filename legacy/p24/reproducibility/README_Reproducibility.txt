P24 SELECTED SCIENTIFIC REPLAY

Purpose and selection
---------------------
This companion preserves and replays a declared selection of the existing
scientific evidence. It does not claim to rerun every historical experiment.
The P24 orchestrator runs the unchanged P21, P22 and P23 replayers and the
unchanged author-written P17 APEX subcatalogue replay in temporary copies.

Stage         Scientific programs   Deterministic scientific outputs
P21                   6                          6
P22                  11                         11
P23                   8                          8
P17 wireless          1                          2
Total                26                         27

The three inherited phase replayers, P24 orchestrator and inventory builder
are administrative programs, not additional scientific-program counts.
The P23 independent universal-upper checker runs only after the associated
producer succeeds. The P22 N5 independent checker imports the included own
check_band_independent.py. All other imports are Python standard-library
modules. No package installation or network access is needed.

Run it
------
1. Extract the final companion without changing its internal paths. The
   extraction directory must contain p9, p17, p20, p21, p22, p23 and p24.
2. Open a terminal in that directory. Use an existing Python 3 interpreter
   on Linux or a Windows Subsystem for Linux environment. The retained byte
   comparisons were tested on Linux. Frozen scripts use their original text
   output defaults; native Windows newline/encoding conversion may prevent
   byte identity. Do not edit those scripts to compensate.
3. Run this exact command:

   python3 p24/reproduce_p24.py --record p24/review/P24_Local_Replay.json

   An absolute script path also works from any current directory. In that
   case an explicitly supplied relative --record path is relative to the
   terminal's current directory. A separate report avoids overwriting the
   retained P24 execution record.
4. The runner prints one JSON status line per stage and a final status line.
   Success requires status PASS, scientific_programs_executed 26,
   scientific_outputs_byte_identical 27, and
   original_inputs_and_retained_outputs_unchanged true. A nonzero process
   exit code indicates failure. Read the saved JSON report for the failing
   stage and error. Missing or modified frozen inputs are rejected before
   execution; restore the original companion instead of editing checksums.

The runner verifies every manifest input by SHA-256 and size before running,
then hashes all originals again after running. Its own source and all old
sources, retained scientific results, licences and historical records remain
unchanged. Generated scientific outputs live only in temporary directories;
their hashes and byte comparisons are retained in the new report. Timings,
platform details and execution-report bytes can vary between machines.

Input and output inventory
--------------------------
Replay_Input_Manifest.json is authoritative for the selected clean companion
input inventory. Every files[].path must be copied at precisely that path,
relative to the extraction root. It binds all 26 scientific scripts, the 27
expected outputs, every proof/hash dependency, three unchanged replayers,
the new orchestrator, original wireless input and provenance/licence records,
and the retained historical companion. The manifest's stages[].jobs list is
the explicit scientific output inventory, including the two wireless files.

The manifest itself, this README, the P24 execution/review records, and final
paper/supplement files are packaged in addition to its immutable input list.
Those final manuscript sources have separate final-source bindings. They do
not replace proof texts hashed by older scientific checks. The unchanged P21
manuscript is therefore included with both P23 correction/audit notes. This
retains historical byte provenance while making the repaired positive-
completion construction visible to readers.

build_replay_manifest.py is a release-maintainer inventory utility. It reads
the literal job lists from unchanged replayers and freezes existing files.
Readers should run reproduce_p24.py, not regenerate the manifest before
validation: rebuilding a manifest would redefine the frozen reference.

The minimal P22 input set contains the exact selected scripts and proof/hash
dependencies, not every historical review prose file. Its unchanged replayer
discovers the available Python/Markdown/text inputs, so its administrative
source inventory can be smaller than the retained original P22 report. All
eleven scientific outputs must nevertheless remain byte-identical.

Real wireless evidence
----------------------
The preserved inputs are two archived trial-summary files:

  p9/licence/apex_dataset/Crystal_results.json    27,901 bytes
  p9/licence/apex_dataset/RPL_results.json        78,910 bytes

Together they contain 312 trial rows from 16 Crystal and 36 RPL configurations
with six rows each. The fixed replay evaluates 128 SHA-ranked triples per
protocol, three candidate choices, and two disjoint three-row blocks:
1,536 candidate/block tasks, 98,304 prefix states and 9,216 policy paths.
Tasks overlap across subcatalogues; they are not independent physical trials.

The frozen transform uses latency/(latency+100 ms) and one minus reliability.
Its declared legal completion domain is the closed square. This is a
secondary audit relaxation; it is not validation of the triangular physical
model. The retained outcome is adverse to claims of practical savings: only
41 tasks are positive (33 Crystal, 8 RPL), every positive certificate costs
nine rows, and every compared policy costs nine rows. The 1,495 other tasks
are negative. No wireless disclosure saving is observed in this control.

No complete upstream archive is required: the two raw files total 106,811
bytes. Dataset README, attribution and CC BY 4.0 legal text accompany them.
The dataset DOI is 10.3217/3dhx0-2k125. Dataset attribution/licensing must not
be confused with the separate MIT software deposit or article. This package
preserves component licence information; it does not assign a new blanket
licence to every file. No new radio measurement, original framework/firmware
execution, hardware/testbed run or new data acquisition occurs here.

Retained history and proof limits
--------------------------------
p20/output/Research_Companion_Paid_Prefix_v1.zip is retained as a nested
historical scientific companion (791,647 bytes), together with its original
execution record. That record reports 31 historical jobs and 35 outputs,
including 30 byte-identical outputs and five declared metadata variations;
all 35 scientific contents matched. P24 does not rerun those 31 jobs. Only
the explicitly selected P17 wireless job is repeated in the current run.
No historical P12 main execution is added by this release.

Finite exact enumerations corroborate their declared finite cases. They do
not execute an infinite Ramsey proof or exhaust arbitrary continuous archive
classes. The two P23 universal-upper programs additionally reproduce exact
Bernstein certificates covering a continuous parameter cube, conditional on
the analytic policy and polynomial reduction. A successful replay establishes
reproduction of the declared computational evidence; it is not external peer
review, proof-assistant verification, priority certification or evidence of
new IoT/radio measurements.
