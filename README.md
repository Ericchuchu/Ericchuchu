# Chien-Cheng (Eric) Chu

Quantitative researcher based in Taipei. I build systematic equity strategies and study how machine learning can be made to respect financial structure: point-in-time data, realistic transaction costs, walk-forward validation, and no-arbitrage constraints.

- **Now:** Quantitative Researcher at Tachan Securities, working on factor research, walk-forward gradient-boosting ranking models, regime-aware risk scaling, and the research-to-execution pipeline.
- **Before:** Global Alpha Researcher at Trexquant Investment (remote); Quantitative Trading Program at Kronos Research (automated trading team); quantitative research intern at MMA Pan Asia Fund and Tachan Securities.
- **Education:** B.S. in Information Management and Finance, National Yang Ming Chiao Tung University (NYCU), 2025. Undergraduate thesis on constrained deep learning for option pricing, advised by Prof. Tian-Shyr Dai.

## Research interests

- Cross-sectional equity strategies: factor construction, neutralization, machine-learning ranking, portfolio construction under turnover and position limits
- Derivatives pricing with deep learning under PDE and no-arbitrage constraints
- Reinforcement learning and market microstructure for high-frequency trading
- Differentiable optimization layers (OptNet, KKT implicit differentiation)

## Selected projects

| Project | Summary | Methods |
|---|---|---|
| [taiex-option-pricing-dl](https://github.com/Ericchuchu/taiex-option-pricing-dl) | Undergraduate thesis code. One-day-ahead pricing of TAIEX index options from three-channel tensors; a dual-branch ConvLSTM + Transformer network with a Black–Scholes PDE penalty lowers the ConvLSTM baseline's test MSE by 48.7%. The README documents the evaluation protocol and its known weaknesses | PyTorch, ConvLSTM, MultiPatchFormer, FANformer, PDE-regularized loss, Kou / FFT benchmark |
| [MacroHFT](https://github.com/Ericchuchu/MacroHFT) (team project, fork) | Hierarchical reinforcement learning for minute-level ETHUSDT trading, extending MacroHFT (KDD 2024) with a regime-aware Dynamic Hybrid coordinator. My part: baseline strategies, the multi-patch temporal state encoder and the evaluation modules | PyTorch, DQN variants, regime-conditioned expert mixing |
| [twse-attention-stock-alerts](https://github.com/Ericchuchu/twse-attention-stock-alerts) | Bot that watches TWSE/MOPS disclosures of attention stocks, extracts EPS from free-form Chinese text, compares it with the previous quarter and pushes alerts to Telegram | Selenium, regular-expression parsing, Telegram Bot API, Docker |
| [bb-keltner-squeeze-sar](https://github.com/Ericchuchu/bb-keltner-squeeze-sar) | Rule-based squeeze-breakout strategy with next-bar execution and commissions, tuned by searching for parameter plateaus instead of single optima | TA-Lib, vectorbt, Optuna (NSGA-II), HiPlot |
| [tw-stock-rnn-trading](https://github.com/Ericchuchu/tw-stock-rnn-trading), [tw-stock-rnn-selection](https://github.com/Ericchuchu/tw-stock-rnn-selection) | 2024 study that turns GRU / LSTM / ConvLSTM price forecasts into trading rules, with a retrospective that reproduces the original backtests and measures how much of their profit came from look-ahead bias and missing costs | PyTorch, vectorbt, Optuna |

My current work is proprietary and is not hosted here. The repositories above are thesis, course and independent projects from 2024 to 2025; each README states its data, evaluation period and limitations.

## Writing

- [Deep Learning-Driven CTA Investment Decisions: Stock Price Prediction and Portfolio Management](https://medium.com/@eric07310115/deep-learning-driven-cta-investment-decisions-stock-price-prediction-and-portfolio-management-9b676da6d2f7) (Medium, 2024)
- [使用 Bollinger Bands – Keltner Squeeze 配合 SAR 指標的順勢交易策略](https://medium.com/@eric07310115/%E4%BD%BF%E7%94%A8-bollinger-bands-keltner-squeeze-%E9%85%8D%E5%90%88-sar-%E6%8C%87%E6%A8%99%E7%9A%84%E9%A0%86%E5%8B%A2%E4%BA%A4%E6%98%93%E7%AD%96%E7%95%A5-4c6ffab5b64c) (Medium, 2024, in Chinese): a trend-following strategy built on the Bollinger–Keltner squeeze with Parabolic SAR exits

## Tools

Python (NumPy, pandas, SciPy, PyTorch, scikit-learn, LightGBM, Optuna), C++, SQL, Git, Docker.

## Contact

[eric07310115@gmail.com](mailto:eric07310115@gmail.com) · [LinkedIn](https://www.linkedin.com/in/eric-chu-b1394a2a1/) · [Medium](https://medium.com/@eric07310115)
