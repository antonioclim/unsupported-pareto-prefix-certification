# APEX Dataset: Testbed Traces and Evaluation Results for Automated Parameter Exploration in Low-Power Wireless Protocols

This record contains the experimental data underlying the article:

> M. H. M. Hydher, M. Schuß, O. Saukh, K. Römer, C. A. Boano:
> "APEX: Automated Parameter Exploration for Low-Power Wireless Protocols",
> ACM Transactions on Sensor Networks 21(6), Article 59, 2025.
> DOI: 10.1145/3770918

DOI of this dataset: 10.3217/3dhx0-2k125
Companion software record (APEX framework, MIT licensed): 10.3217/ckwaw-z8h92
Development repository: http://iti.tugraz.at/APEX

Funding: This research was funded in whole, or in part, by the Austrian Science Fund (FWF) [10.55776/DFH5].

License: Creative Commons Attribution 4.0 International (CC BY 4.0).

## Contents

| File | Description |
|---|---|
| `Crystal_results.json` | Complete testbed ground truth for the Crystal protocol: 16 parameter settings, 6 trials each, 96 trials |
| `RPL_results.json` | Complete testbed ground truth for the RPL protocol: 36 parameter settings, 6 trials each, 216 trials |
| `evaluation_results.zip` | Replay evaluation results for both protocols, 9 optimization approaches, all application requirements, 1,000 independent runs each |
| `synthetic_data_5param.zip` | Synthetic five-parameter RPL dataset (243 configurations, 972 observations), the script that generated it, and its evaluation results |

All testbed experiments were executed on the D-Cube public testbed (Graz University of Technology, 48 nodes over two floors), at different times of the day and week.

## Ground truth traces

Each entry in `Crystal_results.json` and `RPL_results.json` is one testbed trial:

```json
{
  "id": 37155,               D-Cube job id of the trial
  "params": { ... },         protocol parameters, raw firmware values (see mapping below)
  "metrics": {
    "reliability": 0.674,    packet reception ratio (PRR), fraction between 0 and 1
    "latency": 602.13,       end-to-end latency in ms
    "energy": 191.13         total energy in J
  }
}
```

### Crystal: raw values to paper notation

| Recorded field | Values | Paper notation | Meaning |
|---|---|---|---|
| `n_tx_max` | 1, 2, 3, 4 | n_tx = 1, 2, 3, 4 | transmissions per flood |
| `tx_power` | 19, 23, 27, 31 | −5, −3, −1, 0 dBm | CC2420 PA_LEVEL register values |
| `n_empty_ta` | 1 (constant) | not tuned | fixed in all experiments |

### RPL: raw values to paper notation

RPL parameters are recorded in Contiki-NG units. Link metrics use the ETX × 128 fixed-point convention.

| Recorded field | Values | Paper notation | Meaning |
|---|---|---|---|
| `_MAX_LINK_METRIC` | 2048, 4096, 8192 | max_link_metric = 16, 32, 64 | worst link quality accepted as a parent (recorded value / 128) |
| `_RPL_DIO_INTERVAL_MIN` | 4, 8, 12, 16 | DIO_interval = 2⁴, 2⁸, 2¹², 2¹⁶ ms | exponent of the minimum DIO interval |
| `_RANK_THRESHOLD` | 192, 384, 768 | rank_threshold = 1.5, 3, 6 | how much better a new parent must be (recorded value / 128) |
| `_RPL_DAO_DELAY` | 512 (constant) | not tuned | |
| `_RPL_DIS_INTERVAL` | 3840 (constant) | not tuned | |
| `_RPL_PROBING_INTERVAL` | 11520 (constant) | not tuned | |

## Evaluation results

`evaluation_results.zip` is organized as `evaluation_results/<Protocol>/<Approach>/`, with Protocol in {Crystal, RPL} and Approach in {GP-LCB, EI, GEL, GER, GUC, RL-Step, RL-Any, RL-GP, SVM}. GP-LCB and EI are the APEX configurations; the rest are the baselines described in Section 6 of the article. Inside each approach there is one folder per application requirement, named `AR_<n>`.

Each requirement folder holds two files covering 1,000 independent optimization runs replayed against the recorded ground truth (the SVM files hold 1,002 runs):

- `AR_<n>_goal_value.json`: `{ "<run_id>": { "<trial>": best_goal_value_so_far, ... }, ... }`
- `AR_<n>_parameter_set.json`: `{ "<run_id>": { "<trial>": [parameter values of the current best], ... }, ... }`

For the model-fitting approaches (GP-LCB, EI, GEL, GER, GUC) trial numbering starts at 6, after a six-trial initialization phase; the reinforcement learning approaches and SVM start at trial 0. The Crystal GER AR3 files cover trials 6 to 95. Goal values are in the unit of the goal metric of that application requirement (J for energy goals, PRR fraction for reliability goals).

### Application requirements (AR)

| AR | Protocol | Goal | Constraint |
|---|---|---|---|
| AR1 | Crystal | minimize energy | PRR ≥ 65% |
| AR2 | Crystal | minimize energy | PRR ≥ 92% |
| AR3 | Crystal | minimize energy | PRR ≥ 96% |
| AR4 | Crystal | maximize PRR | energy ≤ 210 J |
| AR5 | Crystal | maximize PRR | energy ≤ 190 J |
| AR6 | Crystal | maximize PRR | energy ≤ 170 J |
| AR7 | RPL | minimize energy | PRR ≥ 65.5% |
| AR8 | RPL | minimize energy | PRR ≥ 88% |
| AR9 | RPL | minimize energy | PRR ≥ 93% |
| AR10 | RPL | maximize PRR | energy ≤ 2940 J |
| AR11 | RPL | maximize PRR | energy ≤ 2885 J |
| AR12 | RPL | maximize PRR | energy ≤ 2879 J |
| AR13 | Crystal | minimize energy | PRR ≥ 97.5% |
| AR14 | Crystal | maximize PRR | energy ≤ 168 J |
| AR15 | RPL | minimize energy | PRR ≥ 94.7% |
| AR16 | RPL | maximize PRR | energy ≤ 2872 J |

AR13 to AR16 are the very tight requirements used to evaluate finding any valid parameter set rather than the best one.

## Synthetic five-parameter dataset

`synthetic_data_5param.zip` contains the higher-dimensional scalability study of Section 6: RPL extended with DAO delay and DIS interval to five tuned parameters, three values each, 243 configurations, each evaluated four times for 972 observations. The archive includes:

- `Synthetic_data_creation_script.py`: the script that generated the data, using rule-based models and noise variances learned from the real testbed results
- `real_synthetic_combined_972_5.json` and `filtered_results_3_3_3_4.json`: the generated datasets
- `Evaluation_Results/`: replay evaluation results on this dataset, same file schema as above

## Reproducing the article's results

The APEX framework that produced and consumes this data is archived separately under DOI 10.3217/ckwaw-z8h92 and developed at http://iti.tugraz.at/APEX. Point its `RecordedTestEnvironment` at the ground truth files to replay optimizations; the configuration files in the software record show all knobs.
