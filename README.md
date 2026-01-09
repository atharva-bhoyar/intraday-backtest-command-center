# 📈 Intraday Trading Strategy Backtesting & Trading Command Center

## Overview

This project is an end-to-end intraday trading analytics system designed to simulate, evaluate, and monitor systematic trading strategies using high-frequency market data. It focuses on clean data pipelines, robust backtesting logic, risk-adjusted performance evaluation, and real-time visualization — mirroring workflows used on quantitative trading desks.

The system ingests intraday price and volume data, applies rule-based trading strategies inspired by order flow and market microstructure concepts, and generates actionable performance insights via an interactive Streamlit-based command center dashboard.

## Key Objectives

Build reliable market data pipelines for intraday analysis

Backtest systematic trading strategies using production-style Python code

Compute PnL, drawdown, Sharpe ratio, and other risk metrics

Automate End-of-Day (EOD) reporting

Visualize live and historical strategy performance for rapid decision-making

## System Architecture
.
├── data/
│   ├── raw/              # Raw intraday price & volume data
│   ├── processed/        # Cleaned & feature-engineered datasets
│
├── src/
│   ├── data_pipeline.py  # Data ingestion, cleaning & validation
│   ├── strategy.py       # Trading logic & signal generation
│   ├── backtest.py       # Execution simulation & PnL calculation
│   ├── metrics.py        # Risk & performance metrics (Sharpe, DD)
│   └── reporting.py      # Automated EOD reporting
│
├── dashboard/
│   └── app.py            # Streamlit trading command center
│
├── notebooks/
│   └── exploratory.ipynb # Strategy research & signal exploration
│
├── requirements.txt
└── README.md

## Data Pipeline

Ingests intraday OHLCV market data from external sources (CSV / API-based feeds).

Cleans missing values, aligns timestamps, and validates trading hours.

Performs feature engineering including:

Volume-based indicators

Price–volume relationships

Intraday rolling statistics

Designed to be modular and extensible for additional data sources (options, macro indicators).

## Strategy Logic

Rule-based intraday trading strategies built using Pandas vectorized operations

Signal generation based on:

Volume expansion & contraction

Price momentum and mean-reversion patterns

Order-flow-inspired price–volume dynamics

Strategies are fully decoupled from execution logic to allow rapid experimentation and parameter tuning.

## Backtesting Framework

Simulates intraday trade execution with configurable parameters

Calculates:

Gross & Net PnL

Drawdown and peak-to-trough risk

Sharpe Ratio for risk-adjusted returns

Supports multiple strategies and walk-forward testing workflows

Backtests are designed to be reproducible and transparent, with all intermediate results logged.

## Performance Metrics

Daily & cumulative equity curves

Trade-level statistics (win rate, average R:R, holding time)

Risk metrics:

Maximum Drawdown

Volatility

Sharpe Ratio

Metrics are computed using standardized formulas aligned with industry practices.

# Trading Command Center (Streamlit Dashboard)

The Streamlit dashboard provides a centralized view of strategy performance:

Live & historical equity curves

Trade logs and signal timelines

Daily performance summaries

Strategy-level comparisons

Built to function as a desk-side monitoring tool rather than a static report.

## Automation

Automated End-of-Day (EOD) reporting pipeline

Generates daily performance summaries and exports reports for review

Designed to support future automation such as Morning Briefing dashboards

## Tech Stack

Python: Pandas, NumPy

Visualization: Streamlit

Data Storage: CSV / SQLite

Version Control: Git & GitHub

## How to Run
git clone https://github.com/atharvab07/intraday-trading-command-center.git
cd intraday-trading-command-center
pip install -r requirements.txt
streamlit run dashboard/app.py

Disclaimer

This project is for educational and research purposes only.
It does not constitute financial advice or live trading recommendations.
