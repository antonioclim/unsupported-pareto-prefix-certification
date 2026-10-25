# Historical manuscript retirement in the public P41 snapshot

The private P37 baseline retains the full historical manuscript and every
original archive unchanged. The public P41 snapshot omits
`legacy/p21/article/Manuscript_Paid_Prefix_Certification_P21_v10.md`.
Its recorded SHA-256 is
`58ce4a51a17d07f6572dcdcd65df256ec8af4e112935639346cc15b3dca84797`.

The original `legacy/p23/foundation/check_ordinal_foundation.py` performs finite
ordinal-posterior and Bellman calculations. It hashed four proof files for
provenance; it did not parse their mathematical content. One of those files was
the omitted manuscript. The original script, its output and its original
manifests remain unchanged historical evidence. The old standalone replayer
therefore still describes the earlier complete snapshot, not the current public
payload.

The current `checks/ordinal/check_ordinal_foundation_public.py` keeps the finite
arithmetic unchanged, hashes the three retained public proof inputs and records
the omitted manuscript's digest under `retained_historical_source`, with
`freshly_verified: false`. `provenance/Retired_Manuscript_P21.json` binds the
retirement to the exact old manifest entry. The replay requires the omitted path
to remain absent; it never substitutes a digest string for reading source bytes.

The current legacy wrapper copies the selected retained inputs to a temporary
workspace and executes the 26 scientific jobs in dependency order. It uses the
adapted ordinal checker for that single job. All 27 outputs must scientifically
match: 26 retain exact bytes; the adapted output must match the complete old JSON
after explicitly separating the original/adapted script hashes, the retired
source record and the remaining verified proof hashes. No arbitrary scientific
field is discarded. The new report labels this comparison rather than claiming
27 byte-identical outputs.

This is a public-package provenance change, not a theorem correction or a new
source verification. Old execution records remain truthful statements about
what was present when those runs occurred. The current report documents only
what the current public snapshot actually verifies.
