# Regime-Aware Execution Strategy

## Overview
This repository contains a modular framework designed to optimize electronic execution via liquidity regime detection. The engine utilizes a Hidden Markov Model (HMM) to classify market states and adapt execution parameters dynamically based on Limit Order Book (LOB) signals.

## Key Performance Metrics
- **Out-of-Sample Implementation Shortfall:** [Insert Basis Points]
- **Hit Ratio (30s Forward Alpha):** [Insert Percentage]
- **Regime Stability Index:** [Insert Percentage]

## Methodology
- **Regime Detection:** Gaussian HMM applied to LOB spread and volatility features to isolate high-toxicity environments.
- **Signal Logic:** Order Book Imbalance (OBI) filtering to trigger aggressive entry during mean-reversion windows within identified liquidity states.
- **Validation:** Walk-forward out-of-sample testing to mitigate look-ahead bias and ensure generalizability.

## Project Structure
- /src: Core mathematical modules and evaluation logic.
- /notebooks: Research, visualization, and backtesting reports.
- /data: Sample microstructure datasets in Parquet format.

## Installation and Usage
1. Clone the repository.
2. Install dependencies: pip install -r requirements.txt
3. Execute the research notebook in /notebooks for full strategy analysis and visualization.