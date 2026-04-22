import streamlit as st

# GLOBAL STYLE
def set_style():
    st.markdown("""
    <style>

    .stApp {
        background: linear-gradient(135deg, #e0f2fe, #ccfbf1);
        color: #0f172a;
    }

    section[data-testid="stSidebar"] {
        background: rgba(255,255,255,0.9);
    }

    div[data-testid="metric-container"] {
        background: rgba(255,255,255,0.7);
        border-radius: 12px;
        padding: 15px;
    }

    .stPlotlyChart {
        background-color: white !important;
        border-radius: 10px;
        padding: 10px;
    }

    button[kind="primary"] {
        background-color: #10b981 !important;
        color: white !important;
        border-radius: 8px;
    }

    </style>
    """, unsafe_allow_html=True)


# SIDEBAR GLOBAL
def set_sidebar():
    st.sidebar.image("logo_ubakrie.png", width=120)
    st.sidebar.markdown("---")
    st.sidebar.caption("Dibuat oleh:")
    st.sidebar.caption("Baptista Yohana Vallen")
    st.sidebar.caption("1232002032 | Sistem Informasi 2023")