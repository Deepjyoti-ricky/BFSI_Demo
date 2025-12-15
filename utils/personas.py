"""
Persona Configuration for Wealth 360 Analytics Platform

Defines the different user personas and maps their specific insights
from each section of the application.

Author: Deepjyoti Dev, Senior Data Cloud Architect, Snowflake GXC Team
"""

# Persona Definitions
PERSONAS = {
    "chief_investment_officer": {
        "name": "Chief Investment Officer (CIO)",
        "role": "CIO",
        "description": "Strategic oversight of investment decisions and portfolio performance",
        "icon": "chart_with_upwards_trend",
        "color": "#1f4e79",
        "focus_areas": [
            "Portfolio Performance",
            "Risk Management",
            "Asset Allocation",
            "Market Intelligence",
        ],
    },
    "relationship_manager": {
        "name": "Relationship Manager (RM)",
        "role": "RM",
        "description": "Client relationship management and advisory services",
        "icon": "handshake",
        "color": "#2e7dd2",
        "focus_areas": [
            "Client Engagement",
            "Churn Prevention",
            "Cross-sell Opportunities",
            "Life Event Triggers",
        ],
    },
    "compliance_officer": {
        "name": "Compliance Officer",
        "role": "Compliance",
        "description": "Regulatory compliance and risk monitoring",
        "icon": "shield",
        "color": "#28a745",
        "focus_areas": [
            "Suitability Alerts",
            "KYC/KYB Status",
            "Regulatory Breaches",
            "Audit Readiness",
        ],
    },
    "wealth_advisor": {
        "name": "Wealth Advisor",
        "role": "Advisor",
        "description": "Direct client advisory and portfolio recommendations",
        "icon": "user_tie",
        "color": "#6f42c1",
        "focus_areas": [
            "Client 360 View",
            "Next Best Actions",
            "Portfolio Optimization",
            "Client Briefings",
        ],
    },
    "operations_manager": {
        "name": "Operations Manager",
        "role": "Operations",
        "description": "Operational efficiency and process optimization",
        "icon": "cog",
        "color": "#fd7e14",
        "focus_areas": [
            "Transaction Anomalies",
            "Process Automation",
            "Advisor Productivity",
            "Cash Sweep Operations",
        ],
    },
    "executive": {
        "name": "C-Suite Executive",
        "role": "Executive",
        "description": "Enterprise-wide strategic oversight and decision making",
        "icon": "building",
        "color": "#dc3545",
        "focus_areas": [
            "AUM Growth",
            "Revenue Optimization",
            "Client Acquisition",
            "Market Position",
        ],
    },
}


# Section-to-Persona Insights Mapping
SECTION_INSIGHTS = {
    "home": {
        "title": "Platform Home",
        "insights": {
            "chief_investment_officer": {
                "primary_metrics": ["Total AUM", "YTD Growth", "Portfolio Performance"],
                "key_insights": [
                    "Real-time AUM tracking across all portfolios",
                    "AI-powered growth forecasting with Cortex",
                    "Market positioning relative to benchmarks",
                ],
                "data_sources": ["ACCOUNTS", "ACCOUNT_HISTORY", "PORTFOLIOS"],
            },
            "relationship_manager": {
                "primary_metrics": [
                    "Total Clients",
                    "Engagement Score",
                    "Churn Alerts",
                ],
                "key_insights": [
                    "Client engagement trends and patterns",
                    "Priority outreach recommendations",
                    "Relationship health indicators",
                ],
                "data_sources": [
                    "CLIENTS",
                    "INTERACTIONS",
                    "ADVISOR_CLIENT_RELATIONSHIPS",
                ],
            },
            "compliance_officer": {
                "primary_metrics": ["Compliance Rate", "Open Alerts", "KYC Status"],
                "key_insights": [
                    "Suitability compliance dashboard",
                    "Regulatory alert summary",
                    "Audit trail accessibility",
                ],
                "data_sources": ["CLIENTS", "ACCOUNTS", "PORTFOLIOS"],
            },
            "wealth_advisor": {
                "primary_metrics": ["My Clients", "Pending Actions", "Revenue Impact"],
                "key_insights": [
                    "Personal book overview",
                    "AI-recommended next actions",
                    "Client meeting preparation",
                ],
                "data_sources": [
                    "CLIENTS",
                    "ADVISOR_CLIENT_RELATIONSHIPS",
                    "INTERACTIONS",
                ],
            },
            "operations_manager": {
                "primary_metrics": [
                    "Active Advisors",
                    "Process Efficiency",
                    "Automation Rate",
                ],
                "key_insights": [
                    "Advisor productivity metrics",
                    "Workflow automation status",
                    "Operational bottleneck identification",
                ],
                "data_sources": [
                    "ADVISORS",
                    "ADVISOR_CLIENT_RELATIONSHIPS",
                    "TRANSACTIONS",
                ],
            },
            "executive": {
                "primary_metrics": [
                    "Total AUM",
                    "Client Count",
                    "Revenue",
                    "Growth Rate",
                ],
                "key_insights": [
                    "Enterprise-wide performance summary",
                    "Strategic growth opportunities",
                    "Competitive market positioning",
                ],
                "data_sources": ["ACCOUNTS", "CLIENTS", "PORTFOLIOS", "TRANSACTIONS"],
            },
        },
    },
    "business_overview": {
        "title": "Business Overview",
        "insights": {
            "chief_investment_officer": {
                "primary_metrics": [
                    "Portfolio Drift",
                    "Risk Exposure",
                    "Asset Allocation",
                ],
                "key_insights": [
                    "Investment strategy alignment analysis",
                    "Risk-adjusted return optimization",
                    "Sector and asset class performance",
                ],
                "data_sources": ["PORTFOLIOS", "POSITION_HISTORY"],
            },
            "relationship_manager": {
                "primary_metrics": [
                    "Client Satisfaction",
                    "Retention Rate",
                    "NPS Score",
                ],
                "key_insights": [
                    "Client sentiment trends from interactions",
                    "At-risk client identification",
                    "Engagement improvement opportunities",
                ],
                "data_sources": [
                    "CLIENTS",
                    "INTERACTIONS",
                    "ADVISOR_CLIENT_RELATIONSHIPS",
                ],
            },
            "compliance_officer": {
                "primary_metrics": [
                    "Suitability Breaches",
                    "Concentration Alerts",
                    "KYC Expiry",
                ],
                "key_insights": [
                    "Portfolio concentration risk monitoring",
                    "Suitability mismatch detection",
                    "Regulatory deadline tracking",
                ],
                "data_sources": ["CLIENTS", "PORTFOLIOS", "ACCOUNTS"],
            },
            "wealth_advisor": {
                "primary_metrics": [
                    "Book Value",
                    "Client Growth",
                    "Revenue per Client",
                ],
                "key_insights": [
                    "Personal performance benchmarking",
                    "High-value client opportunities",
                    "Cross-sell conversion tracking",
                ],
                "data_sources": ["ADVISOR_CLIENT_RELATIONSHIPS", "CLIENTS", "ACCOUNTS"],
            },
            "operations_manager": {
                "primary_metrics": [
                    "Transaction Volume",
                    "Processing Time",
                    "Error Rate",
                ],
                "key_insights": [
                    "Operational throughput analysis",
                    "Process efficiency metrics",
                    "Automation opportunity identification",
                ],
                "data_sources": ["TRANSACTIONS", "ACCOUNTS"],
            },
            "executive": {
                "primary_metrics": ["Revenue Growth", "Market Share", "Cost-to-Income"],
                "key_insights": [
                    "Enterprise financial performance",
                    "Strategic initiative progress",
                    "Competitive landscape analysis",
                ],
                "data_sources": ["ACCOUNTS", "CLIENTS", "TRANSACTIONS"],
            },
        },
    },
    "ai_insights": {
        "title": "AI-Powered Insights",
        "insights": {
            "chief_investment_officer": {
                "primary_metrics": [
                    "AI Risk Score",
                    "Prediction Accuracy",
                    "Market Signals",
                ],
                "key_insights": [
                    "Cortex-powered market forecasting",
                    "AI-driven risk assessment",
                    "Predictive portfolio optimization",
                ],
                "data_sources": ["PORTFOLIOS", "POSITION_HISTORY", "MARKET_EVENTS"],
            },
            "relationship_manager": {
                "primary_metrics": [
                    "Churn Probability",
                    "Next Best Action",
                    "Sentiment Score",
                ],
                "key_insights": [
                    "AI-predicted client churn risk",
                    "Personalized engagement recommendations",
                    "Sentiment analysis from interactions",
                ],
                "data_sources": [
                    "CLIENTS",
                    "INTERACTIONS",
                    "ADVISOR_CLIENT_RELATIONSHIPS",
                ],
            },
            "compliance_officer": {
                "primary_metrics": [
                    "Risk Classification",
                    "Anomaly Detection",
                    "Compliance Score",
                ],
                "key_insights": [
                    "AI_CLASSIFY for risk categorization",
                    "Transaction anomaly detection",
                    "Automated compliance monitoring",
                ],
                "data_sources": ["TRANSACTIONS", "CLIENTS", "ACCOUNTS"],
            },
            "wealth_advisor": {
                "primary_metrics": [
                    "Client Briefing",
                    "Talking Points",
                    "Meeting Prep",
                ],
                "key_insights": [
                    "AI-generated client narratives",
                    "Automated meeting preparation",
                    "Personalized conversation starters",
                ],
                "data_sources": ["CLIENTS", "PORTFOLIOS", "INTERACTIONS"],
            },
            "operations_manager": {
                "primary_metrics": [
                    "Process Automation",
                    "Efficiency Score",
                    "Bottleneck ID",
                ],
                "key_insights": [
                    "AI-identified process improvements",
                    "Workflow optimization recommendations",
                    "Resource allocation suggestions",
                ],
                "data_sources": ["ADVISORS", "TRANSACTIONS", "INTERACTIONS"],
            },
            "executive": {
                "primary_metrics": [
                    "AI Confidence",
                    "Forecast Accuracy",
                    "Strategic Insights",
                ],
                "key_insights": [
                    "AI-powered strategic recommendations",
                    "Enterprise-wide predictive analytics",
                    "Competitive intelligence synthesis",
                ],
                "data_sources": ["ACCOUNTS", "CLIENTS", "PORTFOLIOS", "MARKET_EVENTS"],
            },
        },
    },
    "analytics_deep_dive": {
        "title": "Analytics Deep Dive",
        "insights": {
            "chief_investment_officer": {
                "primary_metrics": [
                    "Alpha Generation",
                    "Sharpe Ratio",
                    "Drawdown Analysis",
                ],
                "key_insights": [
                    "Detailed portfolio attribution analysis",
                    "Risk-adjusted performance metrics",
                    "Factor exposure decomposition",
                ],
                "data_sources": ["PORTFOLIOS", "POSITION_HISTORY", "ACCOUNT_HISTORY"],
            },
            "relationship_manager": {
                "primary_metrics": [
                    "Client Lifetime Value",
                    "Engagement Depth",
                    "Wallet Share",
                ],
                "key_insights": [
                    "Client segmentation analytics",
                    "Behavioral pattern analysis",
                    "Revenue optimization by segment",
                ],
                "data_sources": ["CLIENTS", "ACCOUNTS", "TRANSACTIONS"],
            },
            "compliance_officer": {
                "primary_metrics": [
                    "Breach History",
                    "Resolution Time",
                    "Risk Trending",
                ],
                "key_insights": [
                    "Historical compliance analysis",
                    "Risk pattern identification",
                    "Remediation effectiveness tracking",
                ],
                "data_sources": ["CLIENTS", "PORTFOLIOS", "ACCOUNTS"],
            },
            "wealth_advisor": {
                "primary_metrics": [
                    "Client Performance",
                    "Goal Progress",
                    "Rebalancing Needs",
                ],
                "key_insights": [
                    "Individual client portfolio analysis",
                    "Goal-based planning metrics",
                    "Tax optimization opportunities",
                ],
                "data_sources": ["CLIENTS", "PORTFOLIOS", "POSITION_HISTORY"],
            },
            "operations_manager": {
                "primary_metrics": [
                    "SLA Compliance",
                    "Cost per Transaction",
                    "Capacity Utilization",
                ],
                "key_insights": [
                    "Operational cost analysis",
                    "Service level monitoring",
                    "Capacity planning insights",
                ],
                "data_sources": [
                    "TRANSACTIONS",
                    "ADVISORS",
                    "ADVISOR_CLIENT_RELATIONSHIPS",
                ],
            },
            "executive": {
                "primary_metrics": [
                    "Segment Profitability",
                    "Channel Efficiency",
                    "Market Penetration",
                ],
                "key_insights": [
                    "Segment-level P&L analysis",
                    "Distribution channel performance",
                    "Growth opportunity mapping",
                ],
                "data_sources": ["CLIENTS", "ACCOUNTS", "TRANSACTIONS", "ADVISORS"],
            },
        },
    },
    "real_time_intelligence": {
        "title": "Real-Time Intelligence",
        "insights": {
            "chief_investment_officer": {
                "primary_metrics": [
                    "Live Market Data",
                    "Position Changes",
                    "Risk Alerts",
                ],
                "key_insights": [
                    "Real-time portfolio monitoring",
                    "Market event impact analysis",
                    "Dynamic risk threshold alerts",
                ],
                "data_sources": ["PORTFOLIOS", "POSITION_HISTORY", "MARKET_EVENTS"],
            },
            "relationship_manager": {
                "primary_metrics": [
                    "Live Interactions",
                    "Client Activity",
                    "Alert Queue",
                ],
                "key_insights": [
                    "Real-time client engagement tracking",
                    "Immediate outreach triggers",
                    "Activity-based prioritization",
                ],
                "data_sources": [
                    "INTERACTIONS",
                    "CLIENTS",
                    "ADVISOR_CLIENT_RELATIONSHIPS",
                ],
            },
            "compliance_officer": {
                "primary_metrics": [
                    "Active Breaches",
                    "Real-time Alerts",
                    "Escalation Status",
                ],
                "key_insights": [
                    "Live compliance monitoring",
                    "Immediate breach notification",
                    "Real-time escalation tracking",
                ],
                "data_sources": ["TRANSACTIONS", "PORTFOLIOS", "CLIENTS"],
            },
            "wealth_advisor": {
                "primary_metrics": ["Client Alerts", "Market Updates", "Action Items"],
                "key_insights": [
                    "Client-specific event notifications",
                    "Market-driven opportunity alerts",
                    "Priority action queue",
                ],
                "data_sources": ["CLIENTS", "PORTFOLIOS", "MARKET_EVENTS"],
            },
            "operations_manager": {
                "primary_metrics": [
                    "Transaction Queue",
                    "Processing Status",
                    "System Health",
                ],
                "key_insights": [
                    "Real-time transaction monitoring",
                    "System performance tracking",
                    "Bottleneck identification",
                ],
                "data_sources": ["TRANSACTIONS", "ACCOUNTS"],
            },
            "executive": {
                "primary_metrics": ["Live AUM", "Active Users", "Critical Alerts"],
                "key_insights": [
                    "Enterprise dashboard overview",
                    "Real-time business metrics",
                    "Critical issue escalation",
                ],
                "data_sources": ["ACCOUNTS", "CLIENTS", "ADVISORS"],
            },
        },
    },
    "advanced_capabilities": {
        "title": "Advanced Capabilities",
        "insights": {
            "chief_investment_officer": {
                "primary_metrics": [
                    "Climate Risk",
                    "Geospatial AUM",
                    "Predictive Models",
                ],
                "key_insights": [
                    "ESG and climate risk analysis",
                    "Geographic concentration risk",
                    "ML-powered investment insights",
                ],
                "data_sources": ["CLIENTS", "PORTFOLIOS", "POSITION_HISTORY"],
            },
            "relationship_manager": {
                "primary_metrics": [
                    "Geographic Coverage",
                    "Regional Performance",
                    "Local Events",
                ],
                "key_insights": [
                    "Regional client distribution",
                    "Local market opportunities",
                    "Geographic engagement patterns",
                ],
                "data_sources": ["CLIENTS", "ADVISOR_CLIENT_RELATIONSHIPS"],
            },
            "compliance_officer": {
                "primary_metrics": [
                    "Regional Compliance",
                    "Jurisdiction Risk",
                    "Cross-border",
                ],
                "key_insights": [
                    "Multi-jurisdiction compliance",
                    "Regional regulatory mapping",
                    "Cross-border transaction monitoring",
                ],
                "data_sources": ["CLIENTS", "TRANSACTIONS", "ACCOUNTS"],
            },
            "wealth_advisor": {
                "primary_metrics": [
                    "Client Locations",
                    "Meeting Planning",
                    "Travel Optimization",
                ],
                "key_insights": [
                    "Client geographic clustering",
                    "Meeting route optimization",
                    "Regional client concentration",
                ],
                "data_sources": ["CLIENTS", "ADVISOR_CLIENT_RELATIONSHIPS"],
            },
            "operations_manager": {
                "primary_metrics": [
                    "Branch Performance",
                    "Regional Efficiency",
                    "Resource Allocation",
                ],
                "key_insights": [
                    "Branch-level analytics",
                    "Regional resource optimization",
                    "Capacity planning by location",
                ],
                "data_sources": ["ADVISORS", "CLIENTS", "TRANSACTIONS"],
            },
            "executive": {
                "primary_metrics": [
                    "Market Expansion",
                    "Regional P&L",
                    "Growth Corridors",
                ],
                "key_insights": [
                    "Geographic growth opportunities",
                    "Regional profitability analysis",
                    "Expansion strategy insights",
                ],
                "data_sources": ["CLIENTS", "ACCOUNTS", "ADVISORS"],
            },
        },
    },
}


def get_persona_list():
    """Return a list of persona names for selection."""
    return [(key, persona["name"]) for key, persona in PERSONAS.items()]


def get_persona_info(persona_key):
    """Get detailed information for a specific persona."""
    return PERSONAS.get(persona_key, PERSONAS["executive"])


def get_section_insights(section_key, persona_key):
    """Get insights for a specific section and persona combination."""
    section = SECTION_INSIGHTS.get(section_key, {})
    insights = section.get("insights", {}).get(persona_key, {})
    return {
        "section_title": section.get("title", "Section"),
        **insights,
    }


def get_all_section_insights(persona_key):
    """Get all section insights for a specific persona."""
    results = {}
    for section_key, section_data in SECTION_INSIGHTS.items():
        insights = section_data.get("insights", {}).get(persona_key, {})
        results[section_key] = {
            "section_title": section_data.get("title", "Section"),
            **insights,
        }
    return results
