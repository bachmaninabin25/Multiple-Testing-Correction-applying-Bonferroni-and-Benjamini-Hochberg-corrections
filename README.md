Multiple-Testing-Correction-applying-Bonferroni-and-Benjamini-Hochberg-corrections;

In this project, we took 20 stocks in a list, and then applied 10-15 signals, including mean reversion, momentum, bollinger, volatility etc.... and used the returns we get to calculate the information co-effecient from the alphas. We then took the information co-efficient and caulcate the p-values for further investigation

We used multipletests from statsmodel.stats and got normal p-value test ( < 0.05), bonferoni corrction and bh correction 

Our results were :- (near zuedio anna)




Signal                     IC    p-value   Naive   Bonf     BH
---------------------------------------------------------------
mom_5d              -0.0159     0.5979       ✗      ✗       ✗
mom_10d             +0.0109     0.7178       ✗      ✗       ✗
...
low_vol_21d         -0.0476     0.1166       ✗      ✗       ✗
---------------------------------------------------------------
Survivors                                    0      0        0

