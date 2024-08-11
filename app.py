# app.py

import streamlit as st
from subgraph import get_top_pools_data, get_fee_analysis_data, get_comparative_analysis_data
from subgrounds.pagination import LegacyStrategy, ShallowStrategy

# Streamlit UI
st.title("Carina-Graph Dashboard")
st.write("Analyze top pools and their metrics using The Graph")

# Dropdown for pagination strategy
pagination_strategy = st.selectbox(
    "Select Pagination Strategy",
    options=["ShallowStrategy", "LegacyStrategy"]
)

# Convert selected strategy to appropriate object
pagination_strategy_class = ShallowStrategy if pagination_strategy == "ShallowStrategy" else LegacyStrategy

# Get and display top pools data
top_pools = get_top_pools_data(pagination_strategy_class)
st.subheader("Top Pools by Total Value Locked (USD)")
st.dataframe(top_pools)

# Get and display fee analysis data
fee_data = get_fee_analysis_data(pagination_strategy_class)
st.subheader("Fee Analysis of Top Pools")
st.dataframe(fee_data)

# Get and display comparative analysis data
comparative_analysis = get_comparative_analysis_data(pagination_strategy_class)
st.subheader("Comparative Analysis: Volume to Liquidity Ratio")
st.dataframe(comparative_analysis.sort_values(by='volume_to_liquidity_ratio', ascending=False))