<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/header-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/header-light.svg">
  <img alt="Chien-Cheng (Eric) Chu: quantitative research, machine learning, derivatives pricing" src="assets/header-dark.svg" width="100%">
</picture>

<p align="center">
  <a href="mailto:eric07310115@gmail.com"><img alt="Email" src="https://img.shields.io/badge/email-eric07310115%40gmail.com-0d1117?style=flat-square&logo=gmail&logoColor=58a6ff&labelColor=0d1117"></a> <a href="https://www.linkedin.com/in/eric-chu-b1394a2a1/"><img alt="LinkedIn" src="https://img.shields.io/badge/linkedin-eric--chu-0d1117?style=flat-square&logo=linkedin&logoColor=58a6ff&labelColor=0d1117"></a> <a href="https://medium.com/@eric07310115"><img alt="Medium" src="https://img.shields.io/badge/medium-%40eric07310115-0d1117?style=flat-square&logo=medium&logoColor=58a6ff&labelColor=0d1117"></a>
</p>

I work on quantitative research where machine learning meets financial structure: models that stay consistent with pricing theory, use only point-in-time information, and survive transaction costs.

```yaml
name: Chien-Cheng (Eric) Chu
based_in: Taipei, Taiwan
education: B.S. Information Management and Finance, NYCU (2025)
thesis: Constrained Deep Learning for Option Pricing
research:
  - structure-aware neural networks for derivatives pricing
  - cross-sectional equity alpha with walk-forward machine learning
  - reinforcement learning and market microstructure for intraday trading
  - differentiable optimization layers
principles:
  - decisions at time t use information up to t-1, nothing later
  - transaction costs and market impact belong in the first backtest, not the last
  - the final test period is touched once
  - every model is compared with a naive baseline before anything is built on it
```

## `01` Research focus

| Area | Problem | Methods |
|---|---|---|
| **Constrained deep learning for derivatives** | Option-pricing networks that remain consistent with pricing theory | Black–Scholes PDE residual penalties, positivity- and monotonicity-constrained layers, ConvLSTM and Transformer encoders, moneyness and temporal positional encodings |
| **Cross-sectional equity alpha** | Point-in-time factor research and return ranking | Technical, fundamental, behavioral and cross-sectional factors; dynamic universe masking; per-date OLS neutralization against size and sector; walk-forward LightGBM classifier–ranker ensembles; Optuna; portfolios under turnover and position limits |
| **Regime modeling** | Risk and position scaling without look-ahead | Hidden Markov models on returns, volatility, market breadth and relative volume |
| **Event-driven and probabilistic signals** | Post-announcement return prediction | Autoregressive residuals, Wasserstein distance for distributional drift, dealer gamma exposure, clustering-based momentum, Gaussian-process regression, gradient boosting |
| **Automated alpha discovery** | Searching the space of formulaic signals | Expression trees, Transformer generator–predictor loop |
| **Reinforcement learning for trading** | Regime-aware hierarchical agents on minute-level data | MacroHFT, soft–hard expert routing with Gumbel–Softmax, Rainbow DQN, QR-DQN |
| **Market microstructure** | Exchange simulation and short-horizon signals | Asynchronous matching engine, limit-order-book reconstruction, order-book imbalance, inventory-aware market making |
| **Differentiable optimization** | Optimization problems as network layers | OptNet quadratic-programming layers, KKT implicit differentiation, primal–dual interior-point methods |

## `02` Selected work

| Repository | What it is | Stack |
|---|---|---|
| [`Constrained-Deep-Learning-for-Option-Pricing`](https://github.com/Ericchuchu/Constrained-Deep-Learning-for-Option-Pricing) | Undergraduate thesis. One-day-ahead pricing of TAIEX index options; a dual-branch ConvLSTM + Transformer network with a Black–Scholes PDE penalty lowers the ConvLSTM baseline's test MSE by 48.7%. The README documents the evaluation protocol and its known weaknesses | PyTorch · ConvLSTM · MultiPatchFormer · FANformer · Kou / FFT benchmark |
| [`MacroHFT`](https://github.com/Ericchuchu/MacroHFT) (team project, fork) | Hierarchical reinforcement learning for minute-level ETHUSDT trading, extending MacroHFT (KDD 2024) with a regime-aware Dynamic Hybrid coordinator. My part: baseline strategies, the multi-patch temporal state encoder and the evaluation modules | PyTorch · DQN variants · expert mixing |
| [`twse-attention-stock-alerts`](https://github.com/Ericchuchu/twse-attention-stock-alerts) | Monitors exchange disclosures of attention stocks, extracts EPS from free-form Chinese text, compares it with the previous quarter and pushes alerts to Telegram | Selenium · regex parsing · Telegram Bot API · Docker |
| [`bb-keltner-squeeze-sar`](https://github.com/Ericchuchu/bb-keltner-squeeze-sar) | Rule-based squeeze-breakout strategy with next-bar execution and commissions, tuned by searching for parameter plateaus instead of single optima | TA-Lib · vectorbt · Optuna NSGA-II · HiPlot |
| [`tw-stock-rnn-trading`](https://github.com/Ericchuchu/tw-stock-rnn-trading) · [`tw-stock-rnn-selection`](https://github.com/Ericchuchu/tw-stock-rnn-selection) | 2024 study that turns GRU / LSTM / ConvLSTM forecasts into trading rules, with a retrospective that reproduces the original backtests and measures how much of their profit came from look-ahead bias and missing costs | PyTorch · vectorbt · Optuna |

Current research code is proprietary and is not hosted here. Each public repository states its data, evaluation period and limitations.

## `03` Stack

**Languages**&nbsp; ![Python](https://img.shields.io/badge/Python-21262d?style=for-the-badge&logo=python&logoColor=3776AB) ![C++](https://img.shields.io/badge/C%2B%2B-21262d?style=for-the-badge&logo=cplusplus&logoColor=00599C) ![SQL](https://img.shields.io/badge/SQL-21262d?style=for-the-badge)

**Modeling**&nbsp; ![PyTorch](https://img.shields.io/badge/PyTorch-21262d?style=for-the-badge&logo=pytorch&logoColor=EE4C2C) ![scikit-learn](https://img.shields.io/badge/scikit--learn-21262d?style=for-the-badge&logo=scikitlearn&logoColor=F7931E) ![LightGBM](https://img.shields.io/badge/LightGBM-21262d?style=for-the-badge) ![Optuna](https://img.shields.io/badge/Optuna-21262d?style=for-the-badge) ![qpth](https://img.shields.io/badge/qpth%20%2F%20OptNet-21262d?style=for-the-badge)

**Scientific computing**&nbsp; ![NumPy](https://img.shields.io/badge/NumPy-21262d?style=for-the-badge&logo=numpy&logoColor=4DABCF) ![pandas](https://img.shields.io/badge/pandas-21262d?style=for-the-badge&logo=pandas&logoColor=E70488) ![SciPy](https://img.shields.io/badge/SciPy-21262d?style=for-the-badge&logo=scipy&logoColor=8CAAE6)

**Backtesting and infrastructure**&nbsp; ![vectorbt](https://img.shields.io/badge/vectorbt-21262d?style=for-the-badge) ![TA-Lib](https://img.shields.io/badge/TA--Lib-21262d?style=for-the-badge) ![asyncio](https://img.shields.io/badge/asyncio%20%2F%20WebSocket-21262d?style=for-the-badge) ![Docker](https://img.shields.io/badge/Docker-21262d?style=for-the-badge&logo=docker&logoColor=2496ED) ![Git](https://img.shields.io/badge/Git-21262d?style=for-the-badge&logo=git&logoColor=F05032)

```text
mathematics    multivariable calculus · linear algebra · constrained optimization
               quadratic programming · Lagrangian duality · KKT conditions
               numerical methods · implicit differentiation
statistics     statistical inference · regression · autoregressive models · Gaussian processes
               hidden Markov models · time-series analysis
finance        option pricing · Black–Scholes PDE · factor modeling · portfolio construction
               exposure neutralization · transaction-cost modeling · market microstructure
               backtesting and walk-forward validation
```

## `04` Writing

- [Deep Learning-Driven CTA Investment Decisions: Stock Price Prediction and Portfolio Management](https://medium.com/@eric07310115/deep-learning-driven-cta-investment-decisions-stock-price-prediction-and-portfolio-management-9b676da6d2f7) (Medium, 2024)
- [使用 Bollinger Bands – Keltner Squeeze 配合 SAR 指標的順勢交易策略](https://medium.com/@eric07310115/%E4%BD%BF%E7%94%A8-bollinger-bands-keltner-squeeze-%E9%85%8D%E5%90%88-sar-%E6%8C%87%E6%A8%99%E7%9A%84%E9%A0%86%E5%8B%A2%E4%BA%A4%E6%98%93%E7%AD%96%E7%95%A5-4c6ffab5b64c) (Medium, 2024, in Chinese): a trend-following strategy built on the Bollinger–Keltner squeeze with Parabolic SAR exits
