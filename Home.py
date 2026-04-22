import streamlit as st
from style import set_style

st.set_page_config(page_title="Ekonomi Informasi", layout="wide")
set_style()

# Sidebar (tanpa navigation)
st.sidebar.image("logo_ubakrie.png", width=120)

st.sidebar.markdown("---")
st.sidebar.caption("Dibuat oleh:")
st.sidebar.caption("Baptista Yohana Vallen")
st.sidebar.caption("1232002032 | Sistem Informasi 2023")

# Home content
st.title("👋 Selamat Datang di Dashboard Ekonomi Informasi")

st.markdown("""
Dashboard ini digunakan untuk menganalisis performa mahasiswa berdasarkan nilai M1-M4  
dengan pendekatan **Machine Learning + Hybrid Forecasting**.
""")

st.subheader("⚙️ Metode yang Digunakan")

st.markdown("""
### 📊 Hybrid Model:
- Trend Analysis (40%)
- Weighted Moving Average (60%)
- Machine Learning (Random Forest)

### 📐 Formula:
- Trend = (-2/3 × M1) + (1/3 × M2) + (4/3 × M3)
- WMA = (0.2 × M1) + (0.3 × M2) + (0.5 × M3)
- Final Score = 0.4 × Trend + 0.6 × WMA
""")

st.subheader("🔥 Semangat Belajar")

st.metric("Level Semangat", "1000%", "Tidak pernah turun 🚀")
st.progress(100)