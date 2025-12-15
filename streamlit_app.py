"""
BFSI Wealth 360 Analytics Platform - Main Application

Professional Banking, Financial Services, and Insurance (BFSI) analytics platform
leveraging Snowflake's wealth management dataset with multi-page architecture.

Author: Deepjyoti Dev, Senior Data Cloud Architect, Snowflake GXC Team
Contact: deepjyoti.dev@snowflake.com | +917205672310
Version: 2.0.0 (Multi-Page Architecture)
License: MIT
"""

import streamlit as st

from utils.data_functions import get_global_kpis, get_snowflake_session
from utils.personas import (
    get_all_section_insights,
    get_persona_info,
    get_persona_list,
    get_section_insights,
)

# Configure page
st.set_page_config(
    page_title="BFSI Wealth 360 Analytics",
    page_icon=None,
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS for professional styling
st.markdown(
    """
<style>
    .main-header {
        background: linear-gradient(90deg, #1f4e79, #2e7dd2);
        padding: 24px;
        border-radius: 12px;
        margin-bottom: 20px;
        color: white;
        text-align: center;
        box-shadow: 0 4px 14px rgba(0,0,0,0.12);
    }
    .card {
        background: #ffffff;
        border: 1px solid #e9ecef;
        border-radius: 12px;
        padding: 18px 18px 8px 18px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.04);
    }
    .metric-row .stMetric {
        background: #ffffff;
        border: 1px solid #e9ecef;
        border-radius: 12px;
        padding: 12px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.04);
    }
    .section-title {
        margin-top: 6px;
        margin-bottom: 10px;
    }
    .sidebar-section {
        background: #f8f9fa;
        padding: 10px;
        border-radius: 8px;
        margin: 10px 0;
        border: 1px solid #e9ecef;
    }
    .persona-card {
        background: linear-gradient(135deg, var(--persona-color) 0%, var(--persona-color-light) 100%);
        padding: 15px;
        border-radius: 10px;
        color: white;
        margin-bottom: 15px;
    }
    .insight-card {
        background: #f8f9fa;
        border-left: 4px solid var(--accent-color, #2e7dd2);
        padding: 12px 15px;
        margin: 8px 0;
        border-radius: 0 8px 8px 0;
    }
    .data-source-tag {
        display: inline-block;
        background: #e9ecef;
        padding: 2px 8px;
        border-radius: 12px;
        font-size: 12px;
        margin: 2px;
    }
</style>
""",
    unsafe_allow_html=True,
)

# Main header
st.markdown(
    """
<div class="main-header">
    <h1>BFSI Wealth 360 Analytics Platform</h1>
    <p>Powered by Snowflake | Multi-Page Architecture | 12 Advanced Use Cases</p>
</div>
""",
    unsafe_allow_html=True,
)

# Sidebar configuration
with st.sidebar:
    st.markdown("## **Wealth 360** Control Center")

    # Validate connection silently
    try:
        session = get_snowflake_session()
        st.success("**Connected to Snowflake**")
    except Exception as e:
        st.error("**Snowflake Connection Failed**")
        error_str = str(e)
        if "secrets" in error_str.lower() or "no configuration needed" in error_str:
            st.info(
                """
            **For Streamlit in Snowflake:**
            - No configuration needed!
            - Try refreshing the page.

            **For Local Development:**
            - Configure `.streamlit/secrets.toml`
            """
            )
        else:
            st.exception(e)
        st.stop()

    st.divider()

    # Persona Selection
    st.markdown("### **Select Your Role**")
    persona_options = get_persona_list()
    persona_keys = [p[0] for p in persona_options]
    persona_names = [p[1] for p in persona_options]

    selected_persona_name = st.selectbox(
        "I am a:",
        persona_names,
        index=persona_names.index("C-Suite Executive"),
        help="Select your role to see personalized insights",
    )

    # Get the key for the selected persona
    selected_persona_key = persona_keys[persona_names.index(selected_persona_name)]
    persona_info = get_persona_info(selected_persona_key)

    # Store in session state
    st.session_state.selected_persona = selected_persona_key
    st.session_state.persona_info = persona_info

    # Display persona info
    st.markdown(
        f"""
    <div style="background: {persona_info['color']}; padding: 12px; border-radius: 8px; color: white; margin: 10px 0;">
        <strong>{persona_info['name']}</strong><br>
        <small>{persona_info['description']}</small>
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.divider()

    # Focus Areas for selected persona
    st.markdown("### **Your Focus Areas**")
    for area in persona_info["focus_areas"]:
        st.markdown(f"• {area}")

    st.divider()

    # Global Filters
    st.markdown("### **Global Filters**")

    # Wealth Segments
    wealth_segments = st.multiselect(
        "Wealth Segments:",
        ["Ultra HNW", "Very HNW", "HNW", "Emerging HNW", "Mass Affluent"],
        default=["Ultra HNW", "Very HNW", "HNW"],
    )

    # Risk Tolerance
    risk_tolerance = st.multiselect(
        "Risk Tolerance:",
        ["Conservative", "Moderate", "Balanced", "Growth", "Aggressive Growth"],
        default=["Conservative", "Moderate", "Balanced", "Growth", "Aggressive Growth"],
    )

    # Time Windows
    st.markdown("**Time Windows:**")
    col1, col2 = st.columns(2)
    with col1:
        engagement_days = st.number_input(
            "Engagement (days)", min_value=30, max_value=365, value=180, step=30
        )
    with col2:
        advisor_window = st.number_input(
            "Advisor Activity", min_value=30, max_value=365, value=90, step=15
        )

    # Thresholds
    st.markdown("**Thresholds:**")
    hnw_threshold = st.number_input(
        "HNW Minimum (USD)",
        min_value=100000,
        value=1_000_000,
        step=100000,
        format="%d",
    )

    concentration_pct = st.slider(
        "Concentration Alert (%)", min_value=5, max_value=80, value=30, step=5
    )

    st.divider()

    # Quick Actions
    st.markdown("### **Quick Actions**")

    if st.button("Generate Executive Report", use_container_width=True):
        st.info("Executive report generated!")

    if st.button("Check Alerts", use_container_width=True):
        st.warning("23 items need attention")

    if st.button("Refresh All Data", use_container_width=True):
        st.success("Data refreshed!")

    st.divider()

    # Analytics Summary
    st.markdown("### **Quick Stats**")
    try:
        quick_stats = get_global_kpis()
        if quick_stats and len(quick_stats) > 0:
            st.metric("Total Clients", f"{quick_stats.get('num_clients', 'N/A'):,}")
            st.metric("Total AUM", f"${quick_stats.get('aum', 0):,.0f}")
            avg_portfolio = quick_stats.get("aum", 0) / max(
                quick_stats.get("num_clients", 1), 1
            )
            st.metric("Avg Portfolio", f"${avg_portfolio:,.0f}")
        else:
            st.info("Loading analytics...")
    except Exception:
        st.info("Quick stats unavailable")

# Store filters in session state for use across pages
st.session_state.wealth_segments = wealth_segments
st.session_state.risk_tolerance = risk_tolerance
st.session_state.engagement_days = engagement_days
st.session_state.advisor_window = advisor_window
st.session_state.hnw_threshold = hnw_threshold
st.session_state.concentration_threshold = concentration_pct / 100.0

# Main content area
st.markdown(f"## **Welcome, {persona_info['role']}**")

# Persona-specific welcome message
st.markdown(
    f"""
<div class="insight-card" style="border-left-color: {persona_info['color']};">
    <strong>Personalized Dashboard</strong><br>
    This view is optimized for your role as <strong>{persona_info['name']}</strong>.
    The insights and metrics shown are tailored to your focus areas:
    {', '.join(persona_info['focus_areas'])}.
</div>
""",
    unsafe_allow_html=True,
)

# Get persona-specific insights for home section
home_insights = get_section_insights("home", selected_persona_key)

# Executive Snapshot (center metrics)
with st.container():
    st.markdown(
        "<div class='section-title'><h4>Executive Snapshot</h4></div>",
        unsafe_allow_html=True,
    )

    # Show persona-specific primary metrics
    if home_insights.get("primary_metrics"):
        st.caption(
            f"**Your Key Metrics:** {', '.join(home_insights['primary_metrics'])}"
        )

    m1, m2, m3, m4 = st.columns(4)
    try:
        kpis = get_global_kpis()
        total_clients = f"{kpis.get('num_clients', 0):,}"
        total_aum = f"${kpis.get('aum', 0):,.0f}"
        avg_portfolio_val = 0
        if kpis.get("num_clients", 0):
            avg_portfolio_val = kpis.get("aum", 0) / max(kpis.get("num_clients", 1), 1)
        avg_portfolio = f"${avg_portfolio_val:,.0f}"
        ytd = kpis.get("ytd_growth_pct")
        ytd_text = (
            f"{ytd*100:.2f}%"
            if isinstance(ytd, (int, float)) and ytd is not None
            else "N/A"
        )
        with m1:
            st.metric("Total Clients", total_clients)
        with m2:
            st.metric("Total AUM", total_aum)
        with m3:
            st.metric("Avg Portfolio", avg_portfolio)
        with m4:
            st.metric("YTD Growth", ytd_text)
    except Exception:
        with m1:
            st.metric("Total Clients", "—")
        with m2:
            st.metric("Total AUM", "—")
        with m3:
            st.metric("Avg Portfolio", "—")
        with m4:
            st.metric("YTD Growth", "—")

# Persona-specific Key Insights
st.markdown("---")
st.markdown(f"## **Key Insights for {persona_info['role']}**")

if home_insights.get("key_insights"):
    insight_cols = st.columns(len(home_insights["key_insights"]))
    for i, insight in enumerate(home_insights["key_insights"]):
        with insight_cols[i]:
            st.markdown(
                f"""
            <div class="insight-card" style="border-left-color: {persona_info['color']};">
                {insight}
            </div>
            """,
                unsafe_allow_html=True,
            )

# Data Sources
if home_insights.get("data_sources"):
    st.markdown(
        "**Data Sources:** "
        + " ".join([f"`{ds}`" for ds in home_insights["data_sources"]])
    )

# Quick Navigation buttons
st.markdown("\n")
navc1, navc2, navc3, navc4, navc5 = st.columns([1, 1, 1, 1, 1])
with navc1:
    if st.button("Business Overview", use_container_width=True):
        st.switch_page("pages/01_Business_Overview.py")
with navc2:
    if st.button("AI Insights", use_container_width=True):
        st.switch_page("pages/02_AI_Powered_Insights.py")
with navc3:
    if st.button("Analytics Deep Dive", use_container_width=True):
        st.switch_page("pages/03_Analytics_Deep_Dive.py")
with navc4:
    if st.button("Real-Time Intelligence", use_container_width=True):
        st.switch_page("pages/04_Real_Time_Intelligence.py")
with navc5:
    if st.button("Advanced Capabilities", use_container_width=True):
        st.switch_page("pages/05_Advanced_Capabilities.py")

st.markdown("\n")

# Persona Insights by Section
st.markdown("---")
st.markdown("## **Your Insights Across Platform Sections**")

all_insights = get_all_section_insights(selected_persona_key)

# Create expandable sections for each page
for section_key, section_data in all_insights.items():
    if section_key == "home":
        continue  # Already shown above

    with st.expander(
        f"**{section_data.get('section_title', section_key)}**", expanded=False
    ):
        col1, col2 = st.columns([2, 1])

        with col1:
            st.markdown("**Key Insights:**")
            for insight in section_data.get("key_insights", []):
                st.markdown(f"• {insight}")

        with col2:
            st.markdown("**Primary Metrics:**")
            for metric in section_data.get("primary_metrics", []):
                st.markdown(f"• {metric}")

            st.markdown("**Data Sources:**")
            sources = section_data.get("data_sources", [])
            st.markdown(" ".join([f"`{s}`" for s in sources]))

# Two-card intro
st.markdown("---")
intro_left, intro_right = st.columns(2)
with intro_left:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown(
        """
        ### **Getting Started**

        This AI-native application showcases Snowflake Cortex capabilities:

        - **Business Overview**: AI-powered executive dashboard with Cortex insights
        - **AI-Powered Insights**: Live Snowflake Cortex AI demonstrations
        - **Analytics Deep Dive**: Advanced portfolio and risk analytics
        - **Real-Time Intelligence**: Live monitoring and automated workflows
        - **Advanced Capabilities**: Geospatial analytics and predictive models
        """
    )
    st.markdown("</div>", unsafe_allow_html=True)

with intro_right:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown(
        """
        ### **Cortex AI Capabilities**

        - **AI_COMPLETE**: Natural language business queries, risk assessment
        - **AI_CLASSIFY**: Automatic categorization and risk-level tagging
        - **AI_SENTIMENT**: Real-time feedback and complaint routing
        - **AI_SUMMARIZE_AGG**: Cross-document summaries and market analysis
        """
    )
    st.markdown("</div>", unsafe_allow_html=True)

# Platform Overview
st.markdown("---")
st.markdown("## **Platform Overview**")

overview_col1, overview_col2, overview_col3 = st.columns([2, 2, 1])

with overview_col1:
    st.markdown(
        """
        **Enterprise Wealth Management Platform**

        The Wealth 360 Analytics Platform represents the next generation of **BFSI analytics**,
        combining **Snowflake Data Cloud** capabilities with **Cortex AI** to deliver unprecedented
        insights for wealth management operations.

        **Key Capabilities:**
        - Real-time AI-powered insights with Snowflake Cortex
        - 360-degree client analytics and portfolio management
        - Geospatial risk analysis with climate intelligence
        - Advanced predictive modeling and automation
        - Regulatory compliance and risk monitoring
        """
    )

with overview_col2:
    st.markdown(
        """
        **Business Value Delivered**

        - **$47M AUM** protected through AI-driven risk alerts
        - **23% improvement** in client retention rates
        - **67% faster** compliance reporting cycles
        - **85% reduction** in manual portfolio rebalancing
        - **Real-time monitoring** of 450+ client portfolios

        **Platform Navigation:**

        Navigate through our **5 core modules** designed for different stakeholder needs.
        """
    )

with overview_col3:
    st.markdown("**System Status**")
    st.success("AI Engine: Online")
    st.success("Data Pipeline: Active")
    st.success("Real-time Feeds: Connected")
    st.info("Last Updated: just now")

    st.markdown("**Live Metrics**")
    st.metric("Active Sessions", "127", "+12")
    st.metric("AI Queries/min", "43", "+7")
    st.metric("System Load", "23%", "-5%")

# Use Case Catalog
with st.expander(
    "**Complete Use Case Catalog** - Click to see all 12 advanced capabilities",
    expanded=False,
):
    st.markdown(
        """
    | Use Case | Why It Matters | Key Tables | KPIs | Complexity/TTV |
    |----------|----------------|------------|------|----------------|
    | **Customer 360 & Segmentation** | Single view across balances, portfolios, behavior | CLIENTS, ACCOUNTS, TRANSACTIONS, PORTFOLIOS | AUM/NTB growth, segment coverage | Low / 1-2 wks |
    | **Next Best Action (cross/upsell)** | Recommend actions for portfolio optimization | CLIENTS, TRANSACTIONS, INTERACTIONS, PORTFOLIOS | Offer CTR, conversion, AUM lift | Med / 2-4 wks |
    | **Attrition/Churn Early Warning** | Catch balance flight & engagement drop | INTERACTIONS, ADVISOR_CLIENT_RELATIONSHIPS | Churn rate, save rate, time-to-contact | Med / 2-4 wks |
    | **Suitability & Risk Drift Alerts** | Ensure portfolio aligns to risk tolerance | CLIENTS (RISK_TOLERANCE), PORTFOLIOS, POSITION_HISTORY | Suitability breaches, time-to-remediate | Med / 3-5 wks |
    | **Portfolio Drift & Rebalance** | Alert on asset-class drift vs strategy | PORTFOLIOS, POSITION_HISTORY | Drift % over threshold, rebalance yield | Med / 3-5 wks |
    | **Idle Cash / Cash-Sweep** | Monetize idle balances | POSITION_HISTORY | Cash ratio, NII uplift | Low / 1-2 wks |
    | **Trade & Transaction Anomaly Detection** | Catch unusual patterns and outliers | TRANSACTIONS | Transaction integrity, operational risk | Med / 2-4 wks |
    | **Advisor Productivity & Coverage** | Improve book management & cadences | ADVISOR_CLIENT_RELATIONSHIPS, INTERACTIONS | Coverage %, last-contact SLA | Low / 1-2 wks |
    | **Event-Driven Outreach** | Timely, contextual nudge at life/market events | CLIENTS (LIFE_EVENT), MARKET_EVENTS, INTERACTIONS | Engagement rate, booked meetings | Low / 1-2 wks |
    | **Complaint/Sentiment Intelligence** | Mine notes for issues & intent | INTERACTIONS (OUTCOME_NOTES) | NPS proxy, time-to-resolution | Low / 1-2 wks |
    | **Wealth Narrative & Client Briefing** | Auto-generate client summaries | CLIENTS, PORTFOLIOS, POSITION_HISTORY, INTERACTIONS | Prep time saved, call quality | Low / 1-2 wks |
    | **KYB/KYC Ops Copilot** | Speed up checks & documentation Q&A | CLIENTS/ACCOUNTS + external docs | Cycle time, touchless rate | Med / 3-6 wks |
    | **Geospatial Analytics & Climate Risk** | Location-based insights and weather risk | CLIENTS + Weather/POI data | Geographic AUM, climate exposure | Med / 3-5 wks |
    """
    )

st.markdown("---")
st.markdown(
    "### **Navigate to specific pages using the sidebar to explore detailed analytics**"
)

# Footer
st.markdown(
    """
<div style='text-align: center; color: #666; padding: 20px;'>
    <p>BFSI Wealth 360 Analytics Platform |
    Built with Streamlit & Snowflake |
    Author: Deepjyoti Dev, Senior Data Cloud Architect</p>
</div>
""",
    unsafe_allow_html=True,
)
