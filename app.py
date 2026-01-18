import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# --- CONFIGURATION ---
st.set_page_config(page_title="Portfolio Construction AI", layout="wide")

# --- CLASS: ROBO ADVISOR ENGINE ---
class RoboAdvisorAI:
    def __init__(self):
        # Asset Classes and their expected annual returns/volatility (Simulated)
        self.assets = {
            'US Stocks (S&P 500)': {'return': 0.10, 'risk': 0.15},
            'Intl Stocks (Developed)': {'return': 0.08, 'risk': 0.18},
            'Emerging Markets': {'return': 0.12, 'risk': 0.22},
            'Corporate Bonds': {'return': 0.05, 'risk': 0.05},
            'Government Bonds': {'return': 0.03, 'risk': 0.02},
            'Real Estate (REITs)': {'return': 0.07, 'risk': 0.12},
            'Gold/Commodities': {'return': 0.04, 'risk': 0.10}
        }

    def calculate_risk_score(self, age, income, horizon, risk_tolerance):
        # Logic for Investor Classification
        score = 0
        
        # Age Factor
        if age < 30: score += 20
        elif age < 50: score += 10
        else: score += 5
        
        # Horizon Factor
        if horizon > 15: score += 20
        elif horizon > 5: score += 10
        else: score += 5
        
        # Financial Strength
        if income > 100000: score += 20
        elif income > 50000: score += 10
        else: score += 5
        
        # Psychology (User Input)
        score += (risk_tolerance * 8) # Scale 1-5 to 40 points max

        return min(score, 100)

    def generate_allocation(self, risk_score):
        # Rule-Based AI Allocation Engine
        if risk_score >= 80:
            profile = "Aggressive Growth"
            alloc = {'US Stocks (S&P 500)': 40, 'Emerging Markets': 20, 'Intl Stocks (Developed)': 20, 'Real Estate (REITs)': 10, 'Corporate Bonds': 5, 'Gold/Commodities': 5, 'Government Bonds': 0}
        elif risk_score >= 60:
            profile = "Growth"
            alloc = {'US Stocks (S&P 500)': 30, 'Intl Stocks (Developed)': 20, 'Emerging Markets': 10, 'Real Estate (REITs)': 10, 'Corporate Bonds': 20, 'Gold/Commodities': 5, 'Government Bonds': 5}
        elif risk_score >= 40:
            profile = "Balanced"
            alloc = {'US Stocks (S&P 500)': 20, 'Intl Stocks (Developed)': 15, 'Emerging Markets': 5, 'Real Estate (REITs)': 5, 'Corporate Bonds': 30, 'Government Bonds': 20, 'Gold/Commodities': 5}
        else:
            profile = "Conservative"
            alloc = {'US Stocks (S&P 500)': 10, 'Intl Stocks (Developed)': 5, 'Emerging Markets': 0, 'Real Estate (REITs)': 0, 'Corporate Bonds': 30, 'Government Bonds': 50, 'Gold/Commodities': 5}
        
        return profile, alloc

    def rebalance_check(self, current_portfolio, target_alloc, total_value):
        # Tax-Efficient Rebalancing Algorithm
        recommendations = []
        drift_log = []
        
        for asset, target_pct in target_alloc.items():
            current_val = current_portfolio.get(asset, 0)
            current_pct = (current_val / total_value) * 100
            drift = current_pct - target_pct
            
            drift_log.append({'Asset': asset, 'Target %': target_pct, 'Current %': round(current_pct, 2), 'Drift %': round(drift, 2)})
            
            # Rebalancing Threshold (5%)
            if abs(drift) > 5:
                if drift > 0:
                    action = "SELL"
                    amount = (drift / 100) * total_value
                    tax_note = "Warning: Capital Gains Tax may apply."
                else:
                    action = "BUY"
                    amount = abs(drift / 100) * total_value
                    tax_note = "Tax-efficient: Use new deposits if possible."
                    
                recommendations.append(f"{action} ${amount:,.2f} of {asset}. ({tax_note})")
                
        return pd.DataFrame(drift_log), recommendations

# --- INITIALIZE APP ---
ai = RoboAdvisorAI()

# --- SIDEBAR: INPUTS ---
st.sidebar.title("👤 Client Profile")
age = st.sidebar.number_input("Age", 18, 90, 30)
income = st.sidebar.number_input("Annual Income ($)", 0, 1000000, 60000)
horizon = st.sidebar.slider("Investment Horizon (Years)", 1, 40, 15)
risk_tolerance = st.sidebar.slider("Risk Tolerance (1=Low, 5=High)", 1, 5, 3)

# --- MAIN PAGE ---
st.title("🤖 Portfolio Construction AI")
st.markdown("### Automated Robo-Advisor & Investment Engine")

# 1. RISK PROFILING
risk_score = ai.calculate_risk_score(age, income, horizon, risk_tolerance)
profile_name, allocation = ai.generate_allocation(risk_score)

col1, col2 = st.columns(2)
with col1:
    st.info(f"**Investor Type:** {profile_name}")
with col2:
    st.metric("AI Risk Score", f"{risk_score}/100")

# 2. PORTFOLIO VISUALIZATION
st.subheader("1. Recommended Portfolio Allocation")
df_alloc = pd.DataFrame(list(allocation.items()), columns=['Asset Class', 'Percentage'])
fig = px.pie(df_alloc, values='Percentage', names='Asset Class', title=f'Target Allocation for {profile_name} Profile', hole=0.4)
st.plotly_chart(fig, use_container_width=True)

# 3. WEALTH PROJECTION (Goal Based)
st.subheader("2. Wealth Projection Engine")
initial_inv = st.number_input("Initial Investment Amount ($)", 1000, 1000000, 10000)
monthly_contrib = st.number_input("Monthly Contribution ($)", 0, 50000, 500)

years = list(range(horizon + 1))
values = []
current_val = initial_inv
avg_return = 0.08 # Simplified avg return for projection

for y in years:
    values.append(current_val)
    current_val = (current_val + (monthly_contrib * 12)) * (1 + avg_return)

fig_proj = px.line(x=years, y=values, title="Projected Portfolio Growth (Goal Visualization)", labels={'x': 'Years', 'y': 'Portfolio Value ($)'})
st.plotly_chart(fig_proj, use_container_width=True)

# 4. REBALANCING ENGINE
st.subheader("3. Tax-Efficient Rebalancing Module")
st.write("Simulate your current portfolio to see AI recommendations.")

# Simulation inputs
with st.expander("Input Current Portfolio Holdings"):
    current_holdings = {}
    for asset in allocation.keys():
        current_holdings[asset] = st.number_input(f"Current Value of {asset} ($)", 0, 1000000, 0)

total_holdings_val = sum(current_holdings.values())

if total_holdings_val > 0:
    drift_df, actions = ai.rebalance_check(current_holdings, allocation, total_holdings_val)
    
    st.table(drift_df)
    
    if actions:
        st.error("⚠️ Rebalancing Required")
        for action in actions:
            st.write(f"- {action}")
    else:
        st.success("✅ Portfolio is Balanced.")
else:
    st.warning("Please enter current holdings to run the Rebalancing Engine.")