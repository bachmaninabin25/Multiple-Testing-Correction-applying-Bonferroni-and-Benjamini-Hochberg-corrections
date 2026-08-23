Multiple-Testing-Correction-applying-Bonferroni-and-Benjamini-Hochberg-corrections;

In this project, we took 20 stocks in a list, and then applied 10-15 signals, including mean reversion, momentum, bollinger, volatility etc.... and used the returns we get to calculate the information co-effecient from the alphas. We then took the information co-efficient and caulcate the p-values for further investigation

We used multipletests from statsmodel.stats and got normal p-value test ( < 0.05), bonferoni corrction and bh correction 

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
