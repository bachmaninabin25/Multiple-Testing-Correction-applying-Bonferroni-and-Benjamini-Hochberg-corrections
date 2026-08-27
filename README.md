Multiple-Testing-Correction-applying-Bonferroni-and-Benjamini-Hochberg-corrections;


Signal validation framework applying multiple testing corrections to a universe of 10 quantitative signals, demonstrating why naive p-value thresholds produce false discoveries in systematic strategy research.

## Overview

When testing many signals simultaneously, the probability of finding at least one spurious result by chance grows rapidly. This project tests 10 signals on 20 stocks, computes IC-derived p-values, and applies Bonferroni and Benjamini-Hochberg corrections to show how many signals survive rigorous statistical scrutiny.

## Signals Tested

| Signal | Description |
|---|---|
| `mom_5d` | 5-day momentum |
| `mom_10d` | 10-day momentum |
| `mom_21d` | 21-day momentum |
| `mom_63d` | 63-day momentum |
| `meanrev_5d` | 5-day mean reversion |
| `meanrev_10d` | 10-day mean reversion |
| `bb_zscore_10d` | Bollinger Band z-score (10-day) |
| `bb_zscore_21d` | Bollinger Band z-score (21-day) |
| `rsi_14d` | 14-day RSI |
| `low_vol_21d` | Low volatility factor (21-day) |

## Methodology

- **Universe:** 20 US equities
- **IC Calculation:** Spearman correlation of each signal vs forward 1-day returns, aggregated across the full sample
- **P-value derivation:** From IC distribution
- **Corrections applied via `statsmodels.stats.multitest.multipletests`:**
  - Naive: α = 0.05
  - Bonferroni: α / n_tests (controls FWER)
  - Benjamini-Hochberg: controls FDR at 5%

## Results

| Signal | IC | p-value | Naive | Bonferroni | BH |
|---|---|---|---|---|---|
| mom_5d | −0.0159 | 0.5979 | ✗ | ✗ | ✗ |
| mom_10d | +0.0109 | 0.7178 | ✗ | ✗ | ✗ |
| mom_21d | +0.0240 | 0.4284 | ✗ | ✗ | ✗ |
| mom_63d | +0.0017 | 0.9563 | ✗ | ✗ | ✗ |
| meanrev_5d | +0.0159 | 0.5979 | ✗ | ✗ | ✗ |
| meanrev_10d | −0.0109 | 0.7178 | ✗ | ✗ | ✗ |
| bb_zscore_10d | −0.0012 | 0.9679 | ✗ | ✗ | ✗ |
| bb_zscore_21d | −0.0042 | 0.8905 | ✗ | ✗ | ✗ |
| rsi_14d | +0.0008 | 0.9783 | ✗ | ✗ | ✗ |
| low_vol_21d | −0.0476 | 0.1166 | ✗ | ✗ | ✗ |

**Survivors: 0 / 10 across all three methods.**

## Interpretation

Zero signals survive even the naive threshold — this is actually the correct result, not a failure. Standard technical signals on large-cap US equities over a 3-year sample are well-documented to have near-zero predictive power after transaction costs, consistent with Harvey, Liu & Zhu (2016) who argue the true significance threshold for financial factors should be t > 3.0, not the conventional 1.96. The result demonstrates that apparent signal performance in backtests is often illusory without rigorous multiple testing correction — particularly when testing correlated signals on the same universe.

> Harvey, C., Liu, Y., & Zhu, H. (2016). "… and the Cross-Section of Expected Returns." *Review of Financial Studies*, 29(1), 5–68.

## Stack

```
Python 3.x | pandas | numpy | yfinance | scipy | statsmodels
```

## Files

| File | Description |
|---|---|
| `project4.py` | Signal construction, IC computation, p-value derivation, Bonferroni and BH correction, results table |
del.stats and got normal p-value test ( < 0.05), bonferoni corrction and bh correction 

Our results were :-

Signal                       IC    p-value   Naive    Bonf      BH
------------------------------------------------------------------
mom_5d              IC=-0.0159     0.5979       ✗       ✗       ✗
mom_10d             IC=+0.0109     0.7178       ✗       ✗       ✗
mom_21d             IC=+0.0240     0.4284       ✗       ✗       ✗
mom_63d             IC=+0.0017     0.9563       ✗       ✗       ✗
meanrev_5d          IC=+0.0159     0.5979       ✗       ✗       ✗
meanrev_10d         IC=-0.0109     0.7178       ✗       ✗       ✗
bb_zscore_10d       IC=-0.0012     0.9679       ✗       ✗       ✗
bb_zscore_21d       IC=-0.0042     0.8905       ✗       ✗       ✗
rsi_14d             IC=+0.0008     0.9783       ✗       ✗       ✗
low_vol_21d         IC=-0.0476     0.1166       ✗       ✗       ✗
------------------------------------------------------------------
Survivors                                       0       0       0


This is consistent with Harvey,Liu and Zhoue (2016),which demonstrates that more rigorous signal validation is more reliable thatnaive p-value testing is not always reliable
