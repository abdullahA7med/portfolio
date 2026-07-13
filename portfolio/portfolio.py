import streamlit as st
import os

# ============================================================
# CONFIG
# ============================================================
st.set_page_config(
    page_title="Abdullah ahmed | Data Analyst Portfolio",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# HIDE ALL DEFAULT ELEMENTS
# ============================================================
st.markdown("""
<style>
    #MainMenu {visibility: hidden !important;}
    footer {visibility: hidden !important;}
    header {visibility: hidden !important;}
    .stDeployButton {display: none !important;}
    [data-testid="stSidebar"] {display: none !important;}
    [data-testid="collapsedControl"] {display: none !important;}
    .stSidebar {display: none !important;}

    .block-container {
        padding: 0rem 2rem 2rem;
        max-width: 1200px;
        margin-left: auto !important;
        margin-right: auto !important;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================
# CSS - CLEAN PROFESSIONAL THEME
# ============================================================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;500;600;700;800;900&family=Inter:wght@300;400;500;600;700;800;900&display=swap');

    :root {
        --primary: #6366f1;
        --primary-light: #818cf8;
        --secondary: #a855f7;
        --accent: #ec4899;
        --bg: #0f0f23;
        --bg-card: #16162a;
        --bg-card-hover: #1e1e3a;
        --text: #f8fafc;
        --text-secondary: #94a3b8;
        --text-muted: #64748b;
        --border: rgba(99, 102, 241, 0.1);
        --border-hover: rgba(99, 102, 241, 0.3);
    }

    html, body, .stApp {
        background: var(--bg) !important;
        color: var(--text) !important;
        font-family: 'Inter', 'Cairo', sans-serif;
    }

    /* ===== HERO ===== */
    .hero {
        text-align: center;
        padding: 5rem 1rem 3rem;
        position: relative;
        overflow: hidden;
    }

    .hero::before {
        content: '';
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        width: 600px;
        height: 600px;
        background: radial-gradient(circle, rgba(99, 102, 241, 0.15) 0%, rgba(168, 85, 247, 0.08) 40%, transparent 70%);
        border-radius: 50%;
        animation: pulse 6s ease-in-out infinite;
        pointer-events: none;
    }

    @keyframes pulse {
        0%, 100% { opacity: 0.5; transform: translate(-50%, -50%) scale(1); }
        50% { opacity: 1; transform: translate(-50%, -50%) scale(1.15); }
    }

    .hero-name {
        font-size: 4.5rem;
        font-weight: 900;
        background: linear-gradient(135deg, #6366f1, #a855f7, #ec4899);
        background-size: 200% 200%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        animation: gradient 6s ease infinite;
        letter-spacing: -3px;
        margin-bottom: 0.5rem;
        position: relative;
        z-index: 1;
    }

    @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    .hero-role {
        font-size: 1.1rem;
        color: var(--text-secondary);
        font-weight: 500;
        letter-spacing: 5px;
        text-transform: uppercase;
        margin-bottom: 1.5rem;
        position: relative;
        z-index: 1;
    }

    .hero-desc {
        color: var(--text-muted);
        max-width: 500px;
        margin: 0 auto 2.5rem;
        line-height: 1.8;
        font-size: 1rem;
        position: relative;
        z-index: 1;
    }

    .hero-stats {
        display: flex;
        justify-content: center;
        gap: 5rem;
        position: relative;
        z-index: 1;
    }

    .hero-stat-num {
        font-size: 2.5rem;
        font-weight: 800;
        background: linear-gradient(135deg, #6366f1, #a855f7);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        line-height: 1;
    }

    .hero-stat-label {
        font-size: 0.7rem;
        color: var(--text-muted);
        text-transform: uppercase;
        letter-spacing: 3px;
        margin-top: 0.5rem;
    }

    /* ===== SECTIONS ===== */
    .section-title {
        font-size: 1.6rem;
        font-weight: 700;
        color: var(--text);
        margin: 3rem 0 1.2rem;
        padding-bottom: 0.6rem;
        border-bottom: 1px solid var(--border);
        display: flex;
        align-items: center;
        gap: 0.8rem;
    }

    .section-icon {
        width: 36px;
        height: 36px;
        background: linear-gradient(135deg, var(--primary), var(--secondary));
        border-radius: 10px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.1rem;
    }

    /* ===== SKILL TAGS ===== */
    .skills-grid {
        display: flex;
        flex-wrap: wrap;
        gap: 0.6rem;
        margin: 1rem 0 2rem;
    }

    .skill-tag {
        display: inline-block;
        background: var(--bg-card);
        border: 1px solid var(--border);
        border-radius: 8px;
        padding: 0.5rem 1.2rem;
        font-size: 0.85rem;
        color: var(--text-secondary);
        transition: all 0.3s ease;
    }

    .skill-tag:hover {
        border-color: var(--border-hover);
        color: var(--primary-light);
        background: var(--bg-card-hover);
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(99, 102, 241, 0.15);
    }

    /* ===== TABS ===== */
    .stTabs [data-baseweb="tab-list"] {
        gap: 6px;
        background: var(--bg-card);
        padding: 0.5rem;
        border-radius: 16px;
        border: 1px solid var(--border);
        margin-bottom: 1.5rem;
    }

    .stTabs [data-baseweb="tab"] {
        background: transparent;
        border-radius: 12px;
        padding: 0.7rem 2rem;
        color: var(--text-muted);
        font-weight: 600;
        font-size: 0.9rem;
        border: none;
    }

    .stTabs [data-baseweb="tab-highlight"] {
        background: linear-gradient(135deg, var(--primary), var(--secondary));
        border-radius: 12px;
        box-shadow: 0 4px 15px rgba(99, 102, 241, 0.3);
    }

    .stTabs [aria-selected="true"] {
        color: #fff !important;
        font-weight: 700;
    }

    .stTabs [data-baseweb="tab"]:hover:not([aria-selected="true"]) {
        color: var(--text-secondary);
        background: rgba(255,255,255,0.03);
    }

    /* ===== PROJECT CONTENT ===== */
    .project-content {
        padding: 1rem 0;
    }

    .project-header {
        display: flex;
        justify-content: space-between;
        align-items: flex-start;
        margin-bottom: 1rem;
        flex-wrap: wrap;
        gap: 1rem;
    }

    .project-title {
        font-size: 1.6rem;
        font-weight: 700;
        color: var(--text);
        margin: 0;
    }

    .project-badges {
        display: flex;
        gap: 0.5rem;
        flex-wrap: wrap;
    }

    .badge {
        background: rgba(99, 102, 241, 0.1);
        border: 1px solid rgba(99, 102, 241, 0.2);
        border-radius: 20px;
        padding: 0.3rem 1rem;
        font-size: 0.75rem;
        color: var(--primary-light);
        font-weight: 600;
    }

    .badge-purple {
        background: rgba(168, 85, 247, 0.1);
        border-color: rgba(168, 85, 247, 0.2);
        color: #c084fc;
    }

    .badge-pink {
        background: rgba(236, 72, 153, 0.1);
        border-color: rgba(236, 72, 153, 0.2);
        color: #f472b6;
    }

    .project-desc {
        color: var(--text-secondary);
        line-height: 1.8;
        margin-bottom: 1.5rem;
        font-size: 0.95rem;
        max-width: 700px;
    }

    /* ===== METRICS ===== */
    .metrics-row {
        display: flex;
        gap: 0.8rem;
        flex-wrap: wrap;
        margin: 1rem 0;
    }

    .metric-box {
        background: linear-gradient(145deg, rgba(99, 102, 241, 0.08), rgba(168, 85, 247, 0.05));
        border: 1px solid rgba(99, 102, 241, 0.12);
        border-radius: 14px;
        padding: 1rem 0.8rem;
        text-align: center;
        min-width: 90px;
        flex: 1;
        transition: all 0.3s;
    }

    .metric-box:hover {
        border-color: rgba(99, 102, 241, 0.3);
        background: linear-gradient(145deg, rgba(99, 102, 241, 0.12), rgba(168, 85, 247, 0.08));
    }

    .metric-value {
        font-size: 1.4rem;
        font-weight: 700;
        color: var(--primary-light);
        line-height: 1.2;
    }

    .metric-label {
        font-size: 0.65rem;
        color: var(--text-muted);
        margin-top: 0.3rem;
        text-transform: uppercase;
        letter-spacing: 1.5px;
    }

    /* ===== INSIGHTS ===== */
    .insight-box {
        background: rgba(34, 197, 94, 0.05);
        border-left: 3px solid #22c55e;
        padding: 0.8rem 1rem;
        border-radius: 0 10px 10px 0;
        margin: 0.5rem 0;
        color: var(--text-secondary);
        font-size: 0.9rem;
        line-height: 1.6;
    }

    .recommendation-box {
        background: rgba(245, 158, 11, 0.05);
        border-left: 3px solid #f59e0b;
        padding: 0.8rem 1rem;
        border-radius: 0 10px 10px 0;
        margin: 0.5rem 0;
        color: var(--text-secondary);
        font-size: 0.9rem;
        line-height: 1.6;
    }

    /* ===== GITHUB BUTTON ===== */
    .github-btn {
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        background: var(--bg-card);
        color: var(--text);
        padding: 0.7rem 1.5rem;
        border-radius: 10px;
        text-decoration: none;
        font-weight: 600;
        font-size: 0.85rem;
        border: 1px solid var(--border);
        transition: all 0.3s;
        margin-top: 1rem;
    }

    .github-btn:hover {
        background: var(--bg-card-hover);
        border-color: var(--border-hover);
        color: var(--primary-light);
    }

    /* ===== CONTACT ===== */
    .contact-section {
        text-align: center;
        padding: 4rem 2rem;
        margin-top: 3rem;
        background: linear-gradient(180deg, transparent, rgba(99, 102, 241, 0.02), transparent);
        border-radius: 24px;
    }

    .contact-btn {
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        background: linear-gradient(135deg, var(--primary), var(--secondary));
        color: #fff !important;
        padding: 0.9rem 2rem;
        border-radius: 12px;
        text-decoration: none !important;
        font-weight: 700;
        font-size: 0.95rem;
        margin: 0.3rem;
        transition: all 0.3s;
        border: none;
        box-shadow: 0 4px 15px rgba(99, 102, 241, 0.25);
    }

    .contact-btn:hover {
        transform: translateY(-2px) scale(1.02);
        box-shadow: 0 8px 25px rgba(99, 102, 241, 0.35);
        color: #fff !important;
    }

    /* ===== FOOTER ===== */
    .footer {
        text-align: center;
        padding: 2rem;
        color: var(--text-muted);
        border-top: 1px solid var(--border);
        margin-top: 3rem;
        font-size: 0.85rem;
    }

    /* ===== SCROLLBAR ===== */
    ::-webkit-scrollbar { width: 6px; }
    ::-webkit-scrollbar-track { background: var(--bg); }
    ::-webkit-scrollbar-thumb { background: var(--primary); border-radius: 3px; }

    /* ===== RESPONSIVE ===== */
    @media (max-width: 768px) {
        .hero-name { font-size: 3rem; }
        .hero-stats { gap: 2.5rem; }
        .project-title { font-size: 1.3rem; }
    }
</style>
""", unsafe_allow_html=True)

# ============================================================
# GITHUB LINKS - UPDATE THESE!
# ============================================================
GITHUB_REPOS = {
    "weather": "https://github.com/abdullahA7med/Data-Analysis-projects/tree/main/Weather_project",
    "sales": "https://github.com/abdullahA7med/Data-Analysis-projects/tree/main/Sales_analysis",
    "hr": "https://github.com/abdullahA7med/Data-Analysis-projects/tree/main/HR_analysis"
}

# ============================================================
# HERO SECTION
# ============================================================
st.markdown("""
<div class="hero">
    <div class="hero-name">Abdullah ahmed</div>
    <div class="hero-role">Data Analyst</div>
    <div class="hero-desc">
        Transforming raw data into actionable insights through analytics, 
        visualization, and machine learning.
    </div>
    <div class="hero-stats">
        <div>
            <div class="hero-stat-num">3+</div>
            <div class="hero-stat-label">Projects</div>
        </div>
        <div>
            <div class="hero-stat-num">5+</div>
            <div class="hero-stat-label">Tools</div>
        </div>
        <div>
            <div class="hero-stat-num">100%</div>
            <div class="hero-stat-label">Passion</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ============================================================
# ABOUT + SKILLS SECTION
# ============================================================
st.markdown("""
<div class="section-title">
    <div class="section-icon">🧑‍💼</div>
    <div>About Me</div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="color: #94a3b8; line-height: 1.8; max-width: 700px; margin-bottom: 0.5rem;">
Data Analyst passionate about turning raw data into actionable insights. 
Graduate of Social Service Institute with expertise in Python, Power BI, and data visualization.
</div>
""", unsafe_allow_html=True)

# Skills & Tools
st.markdown("""
<div class="section-title" style="margin-top: 2.5rem;">
    <div class="section-icon">🛠️</div>
    <div>Skills & Tools</div>
</div>
""", unsafe_allow_html=True)

skills = ["Python", "Pandas", "NumPy", "Matplotlib", "Seaborn", 
          "Streamlit", "Scikit-learn", "Power BI", "DAX", "Excel",
          "Data Visualization", "API Integration", "Data Cleaning", "EDA"]

skills_html = " ".join([f'<span class="skill-tag">{s}</span>' for s in skills])
st.markdown(f'<div class="skills-grid">{skills_html}</div>', unsafe_allow_html=True)

# ============================================================
# PROJECTS SECTION
# ============================================================
st.markdown("""
<div class="section-title">
    <div class="section-icon">📁</div>
    <div>Featured Projects</div>
</div>
""", unsafe_allow_html=True)

# Tabs
tab1, tab2, tab3 = st.tabs(["🌤️ Weather", "🛒 Sales", "👥 HR"])

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ==================== TAB 1: WEATHER ====================
with tab1:
    st.markdown('<div class="project-content">', unsafe_allow_html=True)

    st.markdown("""
    <div class="project-header">
        <div class="project-title">Egyptian Weather Dashboard</div>
        <div class="project-badges">
            <span class="badge">Python</span>
            <span class="badge badge-purple">Streamlit</span>
            <span class="badge badge-pink">API</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="project-desc">Real-time weather dashboard for Egyptian governorates with 7-day forecast, air quality monitoring, and interactive visualizations.</div>', unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1])
    with col1:
        st.write("**Key Features:**")
        st.write("- Real-time data via Weather API")
        st.write("- Multi-governorate support")
        st.write("- 7-day temperature forecast")
        st.write("- Air quality & rain probability")

        st.markdown('<div class="metrics-row">', unsafe_allow_html=True)
        c1, c2, c3, c4 = st.columns(4)
        with c1: st.markdown('<div class="metric-box"><div class="metric-value">4</div><div class="metric-label">Cities</div></div>', unsafe_allow_html=True)
        with c2: st.markdown('<div class="metric-box"><div class="metric-value">7</div><div class="metric-label">Days</div></div>', unsafe_allow_html=True)
        with c3: st.markdown('<div class="metric-box"><div class="metric-value">Live</div><div class="metric-label">Data</div></div>', unsafe_allow_html=True)
        with c4: st.markdown('<div class="metric-box"><div class="metric-value">API</div><div class="metric-label">Based</div></div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        st.link_button("🔗 View on GitHub", GITHUB_REPOS["weather"], type="secondary")

    with col2:
        st.image(os.path.join(BASE_DIR, "assets", "weather", "Weather_screen_shot.png"), use_container_width=True)

    st.markdown('</div>', unsafe_allow_html=True)

# ==================== TAB 2: SALES ====================
with tab2:
    st.markdown('<div class="project-content">', unsafe_allow_html=True)

    st.markdown("""
    <div class="project-header">
        <div class="project-title">E-Commerce Sales Analysis</div>
        <div class="project-badges">
            <span class="badge">Power BI</span>
            <span class="badge badge-purple">DAX</span>
            <span class="badge badge-pink">Modeling</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="project-desc">Comprehensive sales dashboard analyzing e-commerce performance across regions and product categories with actionable insights.</div>', unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1])
    with col1:
        st.write("**Key Metrics:**")
        st.markdown('<div class="metrics-row">', unsafe_allow_html=True)
        c1, c2, c3 = st.columns(3)
        with c1: st.markdown('<div class="metric-box"><div class="metric-value">126.9K</div><div class="metric-label">Revenue</div></div>', unsafe_allow_html=True)
        with c2: st.markdown('<div class="metric-box"><div class="metric-value">30</div><div class="metric-label">Orders</div></div>', unsafe_allow_html=True)
        with c3: st.markdown('<div class="metric-box"><div class="metric-value">4.23K</div><div class="metric-label">AOV</div></div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        st.write("**Insights:**")
        st.markdown('<div class="insight-box">Cairo dominates with largest revenue share</div>', unsafe_allow_html=True)
        st.markdown('<div class="insight-box">Sales decline Jan to Mar needs investigation</div>', unsafe_allow_html=True)
        st.markdown('<div class="insight-box">Electronics = 94 percent - Accessories need focus</div>', unsafe_allow_html=True)

        st.write("**Recommendations:**")
        st.markdown('<div class="recommendation-box">Review marketing for underperforming regions</div>', unsafe_allow_html=True)
        st.markdown('<div class="recommendation-box">Investigate monthly decline root cause</div>', unsafe_allow_html=True)

        st.link_button("🔗 View on GitHub", GITHUB_REPOS["sales"], type="secondary")

    with col2:
        st.image(os.path.join(BASE_DIR, "assets", "sales", "dashboard.png"), use_container_width=True)

    st.markdown('</div>', unsafe_allow_html=True)

# ==================== TAB 3: HR ====================
with tab3:
    st.markdown('<div class="project-content">', unsafe_allow_html=True)

    st.markdown("""
    <div class="project-header">
        <div class="project-title">HR Analytics Dashboard</div>
        <div class="project-badges">
            <span class="badge">Power BI</span>
            <span class="badge badge-purple">DAX</span>
            <span class="badge badge-pink">HR</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="project-desc">HR analytics for 50 employees across 5 departments. Turnover analysis, salary distribution, and retention insights.</div>', unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1])
    with col1:
        st.write("**Key Metrics:**")
        st.markdown('<div class="metrics-row">', unsafe_allow_html=True)
        c1, c2, c3, c4 = st.columns(4)
        with c1: st.markdown('<div class="metric-box"><div class="metric-value">50</div><div class="metric-label">Employees</div></div>', unsafe_allow_html=True)
        with c2: st.markdown('<div class="metric-box"><div class="metric-value">39</div><div class="metric-label">Active</div></div>', unsafe_allow_html=True)
        with c3: st.markdown('<div class="metric-box"><div class="metric-value">11</div><div class="metric-label">Resigned</div></div>', unsafe_allow_html=True)
        with c4: st.markdown('<div class="metric-box"><div class="metric-value">22%</div><div class="metric-label">Turnover</div></div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        st.write("**Insights:**")
        st.markdown('<div class="insight-box">Marketing: 40 percent turnover - critical risk</div>', unsafe_allow_html=True)
        st.markdown('<div class="insight-box">IT: Highest salary at 11.5K EGP</div>', unsafe_allow_html=True)
        st.markdown('<div class="insight-box">22 percent exceeds healthy benchmark (10-15 percent)</div>', unsafe_allow_html=True)

        st.write("**Recommendations:**")
        st.markdown('<div class="recommendation-box">Review incentive and reward systems</div>', unsafe_allow_html=True)
        st.markdown('<div class="recommendation-box">Evaluate Marketing work environment</div>', unsafe_allow_html=True)

        st.link_button("🔗 View on GitHub", GITHUB_REPOS["hr"], type="secondary")

    with col2:
        st.image(os.path.join(BASE_DIR, "assets", "hr", "dashboard-Screenshot.png"), use_container_width=True)

    st.markdown('</div>', unsafe_allow_html=True)

# ============================================================
# CONTACT
# ============================================================
st.markdown("---")
st.markdown("""
<div class="contact-section">
    <div class="section-title" style="justify-content:center; border:none; margin-bottom:1rem;">
        <div class="section-icon">📬</div>
        <div>Get In Touch</div>
    </div>
    <p style="color: #64748b; margin-bottom: 1.5rem;">
        Interested in collaborating? Let us connect and build something amazing.
    </p>
    <a href="mailto:abdullah.ahmed.saeed.alnoubi@email.com" class="contact-btn">📧 Email</a>
    <a href="www.linkedin.com/in/abdullah-ahmed-562503375" class="contact-btn">🔗 LinkedIn</a>
    <a href="https://github.com/abdullahA7med" class="contact-btn">🐙 GitHub</a>
</div>
""", unsafe_allow_html=True)

# ============================================================
# FOOTER
# ============================================================
st.markdown("""
<div class="footer">
    <p>Built with passion by Abdullah | Data Analyst Portfolio</p>
    <p style="font-size:0.75rem; margin-top:0.3rem;">2026 All Rights Reserved</p>
</div>
""", unsafe_allow_html=True)
