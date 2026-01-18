# Project Report: Portfolio Construction AI
**Timeline:** 15 Days | **Role:** AI Financial Architect

## 1. Executive Summary
This project outlines the development of a "Robo-Advisor," an automated investment platform. The system uses algorithmic logic to assess investor risk, construct optimal portfolios based on Modern Portfolio Theory (MPT), and provide tax-efficient rebalancing suggestions. The platform was built using Python and visualized using Streamlit.

## 2. Architecture & Design (Part 1)
The application follows a modular architecture:
1.  **Input Layer:** Collects client data (Age, Income, Risk Tolerance, Horizon).
2.  **Processing Layer (The AI Engine):**
    * *Risk Module:* Quantifies user data into a score (0-100).
    * *Allocation Module:* Maps scores to a pre-defined asset mix (Equities, Bonds, Real Estate).
3.  **Visualization Layer:** Uses Plotly and Streamlit to render dynamic charts.

## 3. Core Features Implementation
### A. Risk Profiling (Part 2)
We implemented a scoring algorithm that weighs 'Time Horizon' and 'Age' heavily.
* *Score Formula:* Risk Capacity (Financials) + Risk Tolerance (Psychology).
* *Output:* Classifications ranging from "Conservative" to "Aggressive Growth."

### B. Goal-Based Construction (Part 3)
The engine projects future wealth using Compound Annual Growth Rate (CAGR) formulas, incorporating monthly contributions to simulate real-world goal planning.

### C. Tax-Efficient Rebalancing (Part 4)
The system detects "Drift" (when an asset deviates >5% from its target).
* *Algorithm:* It calculates the delta between Current% and Target%.
* *Tax Efficiency:* The system prioritizes "Buying" underweight assets using new deposits over "Selling" overweight assets, thereby avoiding immediate Capital Gains Tax events.

## 4. Testing & Validation (Part 7)
The system was tested against various user profiles:
* **Case A (25-year-old, High Income):** System correctly identified "Aggressive Growth" and allocated 80% to Equities.
* **Case B (60-year-old, Low Risk):** System correctly identified "Conservative" and allocated 80% to Bonds/Safety.
* **Rebalancing Test:** Simulated a market crash in Tech stocks; the system correctly triggered a "BUY" signal for the underweight asset class.

## 5. Conclusion
The Portfolio Construction AI successfully automates the role of a traditional financial advisor. It provides transparent, logic-based investment advice and dynamic visualization, fulfilling all project requirements.