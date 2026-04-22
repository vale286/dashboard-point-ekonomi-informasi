import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

from style import set_style, set_sidebar


# MAIN FUNCTION
def main():

    set_style()
    set_sidebar()

    st.title("📊 Analisis Nilai Mahasiswa")

    uploaded_file = st.file_uploader("Upload file CSV/XLSX", type=["csv", "xlsx"])

    # HYBRID MODEL
    def hybrid_pred(row):
        M1, M2, M3 = row["M1"], row["M2"], row["M3"]

        trend = (-2/3 * M1) + (1/3 * M2) + (4/3 * M3)
        wma = (0.2 * M1) + (0.3 * M2) + (0.5 * M3)

        return max(0, min(10, 0.4 * trend + 0.6 * wma))

    # LOAD DATA
    if uploaded_file:

        try:
            df = pd.read_excel(uploaded_file) if uploaded_file.name.endswith("xlsx") else pd.read_csv(uploaded_file)
        except:
            st.error("❌ File tidak bisa dibaca. Pastikan format benar.")
            return

        # VALIDASI KOLOM
        required_cols = ["M1", "M2", "M3", "M4"]
        if not all(col in df.columns for col in required_cols):
            st.error("❌ Data harus memiliki kolom: M1, M2, M3, M4")
            return

        st.subheader("📋 Data Awal")
        st.dataframe(df)

        # MISSING VALUE
        st.subheader("🧼 Missing Value Check")
        missing = df.isnull().sum()
        st.write(missing)

        if missing.sum() == 0:
            st.success("✅ Tidak ada missing value, data bersih")
        else:
            st.warning("⚠ Terdapat missing value, bisa mempengaruhi hasil analisis")

        # FEATURE ENGINEERING
        df["Prediksi_Hybrid"] = df.apply(hybrid_pred, axis=1)
        df["Total_Nilai"] = df[["M1", "M2", "M3", "M4"]].sum(axis=1)

        # MACHINE LEARNING
        X = df[["M1", "M2", "M3"]]
        y = df["M4"]

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        model = RandomForestRegressor(random_state=42)
        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)

        # ======================
        # EVALUASI MODEL (UPGRADE)
        # ======================
        mae = mean_absolute_error(y_test, y_pred)
        rmse = np.sqrt(mean_squared_error(y_test, y_pred))
        r2 = r2_score(y_test, y_pred)

        st.subheader("🤖 Evaluasi Model (Machine Learning)")

        st.write(f"MAE (Mean Absolute Error): **{mae:.2f}**")
        st.write(f"RMSE: **{rmse:.2f}**")
        st.write(f"R² Score: **{r2:.2f}**")

        # Insight gabungan
        if mae < 1 and r2 > 0.8:
            st.success("🔥 Model sangat akurat dan stabil")
        elif mae < 2 and r2 > 0.6:
            st.warning("⚠ Model cukup akurat, masih bisa ditingkatkan")
        else:
            st.error("❌ Model kurang akurat, perlu data lebih baik")

        st.caption("MAE = rata-rata error, RMSE = error sensitif, R² = kemampuan model menjelaskan data")

        st.info(f"""
        Model mampu menjelaskan sekitar **{r2*100:.1f}% variasi nilai mahasiswa**.

        Artinya model dapat digunakan sebagai **alat bantu prediksi awal performa mahasiswa**.
        """)

        # ======================
        # TOP MAHASISWA
        # ======================
        st.subheader("🏆 Top 5 Mahasiswa")
        top = df.sort_values("Total_Nilai", ascending=False).head(5)
        st.dataframe(top)

        st.info(f"""
        Mahasiswa dengan performa tertinggi memiliki total nilai hingga **{top['Total_Nilai'].max()}**.
        Ini menunjukkan konsistensi performa akademik.
        """)

        # ======================
        # DISTRIBUSI NILAI
        # ======================
        st.subheader("📊 Distribusi Nilai Mahasiswa")
        fig = px.histogram(df, x="Total_Nilai")
        st.plotly_chart(fig, use_container_width=True)

        avg = df["Total_Nilai"].mean()
        st.info(f"""
        Rata-rata nilai mahasiswa adalah **{avg:.2f}**.
        Ini menunjukkan performa umum kelas secara keseluruhan.
        """)

        # ======================
        # SCATTER ANALYSIS
        # ======================
        st.subheader("🔍 Hubungan Antar Nilai")

        fig1 = px.scatter(df, x="M1", y="M4", title="Hubungan M1 vs M4")
        st.plotly_chart(fig1, use_container_width=True)

        st.info("""
        Jika pola titik cenderung naik, berarti mahasiswa dengan nilai awal tinggi
        cenderung mempertahankan performa hingga akhir.
        """)

        fig2 = px.scatter(df, x="M2", y="M3", title="Hubungan M2 vs M3")
        st.plotly_chart(fig2, use_container_width=True)

        st.info("""
        Jika titik menyebar, berarti performa mahasiswa tidak konsisten antar minggu.
        """)

        # ======================
        # CORRELATION
        # ======================
        st.subheader("📈 Analisis Korelasi")
        corr = df[["M1", "M2", "M3", "M4"]].corr()
        st.dataframe(corr)

        strongest = corr["M4"].drop("M4").idxmax()

        st.success(f"""
        Variabel yang paling berpengaruh terhadap nilai akhir (M4) adalah **{strongest}**.
        """)

        # ======================
        # EKONOMI INFORMASI
        # ======================
        st.subheader("Insight Ekonomi Informasi")

        st.write("""
        Dalam perspektif ekonomi informasi:

        - Nilai mahasiswa = Sinyal kualitas individu dalam belajar.
        - Model prediksi = Alat bantu pengambilan keputusan.
        - Data historis = Dasar analisis performa.

        Semakin lengkap informasi yang tersedia,
        semakin baik keputusan yang dapat diambil oleh dosen maupun mahasiswa.
        """)

    else:
        st.info("Silakan upload file untuk mulai analisis 📂")


# WAJIB JALANIN
main()