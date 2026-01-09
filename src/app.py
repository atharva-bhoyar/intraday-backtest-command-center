import streamlit as st
import pandas as pd
import plotly.express as px
import os

# -------------------------------
# Page setup
# -------------------------------
st.set_page_config(page_title="Trading Command Center", layout="wide")
st.title("📊 Trading Command Center")

# -------------------------------
# File paths
# -------------------------------
TRADES_PATH = "reports/trades.csv"
DAILY_PATH = "reports/daily_summary.csv"

# -------------------------------
# Check if files exist
# -------------------------------
if not os.path.exists(TRADES_PATH):
    st.error("❌ File not found: reports/trades.csv")
    st.stop()

if not os.path.exists(DAILY_PATH):
    st.error("❌ File not found: reports/daily_summary.csv")
    st.stop()

# -------------------------------
# Load data
# -------------------------------
trades = pd.read_csv(TRADES_PATH)
daily = pd.read_csv(DAILY_PATH)

st.success("✅ Reports loaded successfully")

# -------------------------------
# Top metrics
# -------------------------------
col1, col2, col3 = st.columns(3)

col1.metric("Total Trades", len(trades))
col2.metric("Total Days", len(daily))

if "equity" in daily.columns:
    total_return = (daily["equity"].iloc[-1] - 1) * 100
    col3.metric("Total Return %", f"{total_return:.2f}%")
else:
    col3.metric("Total Return %", "N/A")

st.divider()

# -------------------------------
# Equity Curve
# -------------------------------
st.subheader("📈 Equity Curve")

if "equity" not in daily.columns:
    st.error(f"❌ 'equity' column not found. Columns available: {list(daily.columns)}")
else:
    daily["date"] = pd.to_datetime(daily["date"])
    fig = px.line(
        daily,
        x="date",
        y="equity",
        title="Equity Curve"
    )
    st.plotly_chart(fig, use_container_width=True)

st.divider()

# -------------------------------
# Trades table
# -------------------------------
st.subheader("📄 Trades (Last 20)")

if trades.empty:
    st.warning("No trades found.")
else:
    st.dataframe(trades.tail(20), use_container_width=True)

# -------------------------------
# Debug section (optional)
# -------------------------------
with st.expander("🔍 Debug Info"):
    st.write("Daily columns:", list(daily.columns))
    st.write(daily.head())

st.success("🎉 Dashboard loaded successfully!")
