import pandas as pd
import yfinance as yf
import numpy as np
from statsmodels.stats.multitest import multipletests
import scipy as sc

ics = []
pval = []

tickers = ['AAPL', 'AVGO', 'AMD', 'INTC', 'JPM', 'BAC', 'GS', 'JNJ', 'UNH', 'PFE', 'CAT', 'DE', 'HON', 'UPS', 'WMT', 'PG', 'KO', 'PEP', 'MCD', 'NKE', 'SBUX']
stocks = yf.download(start='2020-01-01', end='2024-06-01', tickers=tickers)
prices = stocks['Close']
returns = prices.pct_change().dropna()

mom_5d        = returns.rolling(5).mean().mean(axis=1)
mom_10d       = returns.rolling(10).mean().mean(axis=1)
mom_21d       = returns.rolling(21).mean().mean(axis=1)
mom_63d       = returns.rolling(63).mean().mean(axis=1)
meanrev_5d    = -returns.rolling(5).mean().mean(axis=1)
meanrev_10d   = -returns.rolling(10).mean().mean(axis=1)
bb_zscore_10d = -((prices - prices.rolling(10).mean()) / prices.rolling(10).std()).mean(axis=1)
bb_zscore_21d = -((prices - prices.rolling(21).mean()) / prices.rolling(21).std()).mean(axis=1)

def compute_rsi(ret_series, period=14):
    gain = ret_series.clip(lower=0).rolling(period).mean()
    loss = (-ret_series.clip(upper=0)).rolling(period).mean()
    rs   = gain / (loss + 1e-9)
    return 100 - (100 / (1 + rs))

rsi_14d     = 50 - returns.apply(compute_rsi).mean(axis=1)
low_vol_21d = -returns.rolling(21).std().mean(axis=1)

signals = [mom_5d, mom_10d, mom_21d, mom_63d, meanrev_5d, meanrev_10d, bb_zscore_10d, bb_zscore_21d, rsi_14d, low_vol_21d]

fwd = returns.mean(axis=1).shift(-1) 

for i in signals:
    combined = pd.concat([i, fwd], axis=1).dropna()
    ic, p = sc.stats.spearmanr(combined.iloc[:, 0], combined.iloc[:, 1])
    ics.append(ic)
    pval.append(p)

bonf_pass, _, _, _ = multipletests(pval, alpha=0.05, method='bonferroni')
bh_pass,   _, _, _ = multipletests(pval, alpha=0.05, method='fdr_bh')
naive_pass          = [p < 0.05 for p in pval]


signal_names = ['mom_5d', 'mom_10d', 'mom_21d', 'mom_63d', 'meanrev_5d', 'meanrev_10d', 'bb_zscore_10d', 'bb_zscore_21d', 'rsi_14d', 'low_vol_21d']

for name, ic, p, naive, bonf, bh in zip(signal_names, ics, pval, naive_pass, bonf_pass, bh_pass):
    print(f"{name:<20} IC={ic:+.4f}  p={p:.4f}  naive={str(naive):<5}  bonf={str(bonf):<5}  bh={str(bh):<5}")


print(f"Bonferroni : {sum(bonf_pass)}/{len(pval)}")
print(f"BH (5% FDR): {sum(bh_pass)}/{len(pval)}")
print(f"Naive      : {sum(naive_pass)}/{len(pval)}")