# pyFuReA legacy source analysis

Local preserved snapshot:

- `src/legacy/`

Excluded from repo snapshot:

- `pyFuReA.pyc` — Python 2.7 bytecode, derived artifact.
- `disser.session.tar` — Spyder session/config artifact, not source code.

## Files

- `pyFuReA.py` — core f-regression implementation.
- `pw-data.py` — well-test / piecewise-analysis visualization script using `pyFuReA`.
- `test2.py` — unrelated Google Scholar/`scholarly` experiment for Philippe Smets; not part of f-regression core.
- `SPE 12777 Bourdet.csv` — 154-row well-test data, columns: `time,deltap,dp,s_time,s_deltap,s_dp`.
- `Rylsk-gas-consumption.csv` — 1064 rows, semicolon-separated `DATE;TMED;VOL1`.
- `house-prices.tsv` — 16 rows, 8 columns, demonstration dataset with price spread.
- `running-perf.tsv` — 15 rows, 7 columns, demonstration dataset.
- `consensus.xlsx`, `gas_production.xls` — spreadsheet datasets.
- `welltest_loglog_*.png` — generated/illustrative well-test log-log plots.

## Core model (`pyFuReA.py`)

The file implements fuzzy point geometry and line-fitting:

- `FuzzyPoint` — base point with apex, spreads, and exponential L-function `exp(-abs(u)**m)`.
- `Ppoint` — axis-aligned point membership/similarity.
- `Epoint` — elliptic point with interaction/rotation matrix `R`; computes similarity to a hyperplane and optional closest point.
- `WeightedPowerMean` — aggregation of point similarities. Handles multi-model aggregation via either probabilistic-sum style accumulation or max mode (max mode is private and currently never enabled).
- `LinearfRegression` — single linear f-regression estimator.
- `ClusteredLinearfRegression` — multi-line/clustered version, used for piecewise/multiple model fitting.

Dependencies used/imported:

- `numpy`
- `scipy.optimize.minimize`
- `sklearn.linear_model.LinearRegression` (imported but not used in the inspected code)

## Technical state

- The Python files pass Python 3 syntax compilation.
- Code style and APIs are legacy Python 2 era:
  - `rotation.iteritems()` will fail under Python 3 when rotation is non-empty.
  - `LinearfRegression.fit()` calls `basinhopping(...)`, but `basinhopping` is commented out in the import line; this method will fail unless fixed/imported.
  - `ClusteredLinearfRegression.fit()` uses `minimize(..., method='Nelder-Mead', options={'ftol': ...})`; modern SciPy may warn or prefer `xatol/fatol`.
  - `WeightedPowerMean.__init__` accepts `weights` but never assigns `self.weights = weights`; sample weights are effectively ignored unless set elsewhere.
  - `spreads_y` parameters are accepted by fit methods but not used.
  - `RotationMatrix` is a stub.

## Relation to papers/dissertation

- `pw-data.py` explicitly references the 2013 discussion: spreads should be calculated using domain considerations “as discussed in Izyumov, 2013”.
- The script reproduces/visualizes well-test log-log behavior around `SPE 12777 Bourdet.csv`, matching the oilfield/well-testing f-regression thread.
- The class names and algorithms correspond to the f-regression method: fuzzy points, similarity of points to model hyperplanes, aggregation by plausibility, and piecewise/clustered linear fitting.

## Immediate cleanup recommendations

1. Keep `src/legacy/` as immutable historical snapshot.
2. If modernizing, create a separate package (`src/f_regression/`) instead of editing the legacy file in place.
3. Add tests for:
   - `Ppoint.membership/similarity`;
   - `Epoint.similarity`;
   - `WeightedPowerMean` with explicit weights;
   - one simple line fit and one clustered/piecewise fit.
4. Fix Python 3 compatibility only in the modernized package, preserving the legacy source unchanged.
