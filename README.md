# LOB-E: Regime-Aware Microstructure Execution Engine

## Performance Summary (Out-of-Sample)
| Metric | Result | Interpretation |
| :--- | :--- | :--- |
| **Implementation Shortfall** | **-36.73 bps** | Significant alpha vs. VWAP benchmark |
| **Hit Ratio (30s Alpha)** | **75.0%** | High predictive accuracy of OBI signals |
| **Regime Switch Ratio** | **9.80%** | Stable HMM states via feature smoothing |

## Technical Architecture
- **Feature Engineering:** Integrated a low-pass rolling filter to mitigate tick-noise and stabilize HMM transitions.
- **Regime Detection:** Utilized a 3-component Gaussian Hidden Markov Model to classify liquidity toxicity environments.
- **Execution Logic:** Opportunistic "Dip Sniping" triggered by Order Book Imbalance (OBI) thresholds during high-slippage regimes.

## Usage
1. `pip install -r requirements.txt`
2. Run `notebooks/Visuals.ipynb` for full backtesting analytics.
