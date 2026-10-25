# APEX parameter-table erratum and this secondary analysis

The APEX authors' erratum corrects the paper's rank-threshold values to
`1.5, 3, 6`; the values `4, 8, 12, 16` belong to a different parameter. The
retained RPL data contain `_RANK_THRESHOLD` values `192, 384, 768`, which give
`1.5, 3, 6` on division by 128. The archived replay groups actual parameter records
and does not hardcode the erroneous table enumeration. Its declared numerical
transforms are latency/(latency+100) and one minus reliability.

Consequently this erratum does not change the frozen input bytes, selected
computation or retained results. The secondary analysis still reports no
observation saving on its 41 positive tasks, and its 1,536 overlapping tasks are not
independent replications. This is not a reimplementation or validation of the
APEX framework.

Primary author erratum:
https://www.carloalbertoboano.com/documents/hydher25tosn_errata.pdf

Associated article: https://doi.org/10.1145/3770918

Retained dataset: https://doi.org/10.3217/3dhx0-2k125
