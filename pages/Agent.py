import streamlit as st
import time
from style import set_style, set_sidebar

set_style()
set_sidebar()

st.title("🤖 Agent Ekonomi Informasi")

# COMMAND SELECT
command = st.selectbox(
    "Pilih Perintah",
    [
        "Tips Nilai Tinggi",
        "Analisis Performa Mahasiswa",
        "Konsep Ekonomi Informasi",
        "Ilustrasi Kehidupan Nyata",
        "Jadwal Kelas",
        "Motivasi Belajar",
        "Custom Query"
    ]
)

# Custom input
custom_query = ""
if command == "Custom Query":
    custom_query = st.text_area("Masukkan pertanyaan kamu")

# RUN AGENT
if st.button("Jalankan Agent"):

    # AI Thinking Simulation
    with st.spinner("Agent berpikir..."):
        st.write("🧐 Memahami pertanyaan...")
        time.sleep(0.6)

        st.write("📊 Mengakses knowledge ekonomi informasi...")
        time.sleep(0.6)

        st.write("⚙ Menyusun jawaban terbaik...")
        time.sleep(0.6)

    # DEFAULT RESPONSE
    def default_intro():
        st.info(
            "Yuk, belajar lebih rajin di mata kuliah Ekonomi Informasi 📚✨\n\n"
            "Sedikit demi sedikit kamu pasti paham, dan ini bakal kepake banget "
            "buat masa depan kamu di dunia data, bisnis, bahkan AI 🚀"
        )

    # COMMAND HANDLER
    # 🎯 TIPS NILAI
    if command == "Tips Nilai Tinggi":

        st.success("📈 Strategi Mendapat Nilai Tinggi")

        st.write("""
        - Duduk di baris depan (akses informasi lebih jelas)
        - Aktif bertanya dan menjawab
        - Catat poin penting (information retention)
        - Review materi setelah kelas
        - Terapkan konsep ke kehidupan nyata
        """)

        st.caption("Dalam ekonomi informasi, ini disebut meningkatkan kualitas sinyal akademik.")

    # 📊 ANALISIS
    elif command == "Analisis Performa Mahasiswa":

        st.success("📊 Insight Performa Mahasiswa")

        st.write("""
        - Mahasiswa dengan nilai M3 tinggi cenderung stabil.
        - Tren naik menunjukkan adaptasi belajar yang baik.
        - Penurunan nilai bisa jadi indikasi kurang memahami materi sebelumnya.
        """)

        st.info("Dalam ekonomi informasi, nilai adalah sinyal kualitas individu.")

    # 📚 KONSEP
    elif command == "Konsep Ekonomi Informasi":

        st.success("📘 Konsep Dasar")

        st.write("""
        Ekonomi informasi adalah cabang ekonomi yang mempelajari:

        - Bagaimana informasi mempengaruhi keputusan.
        - Asymmetric information (ketidakseimbangan informasi).
        - Signaling (memberi sinyal kualitas).
        - Screening (menilai kualitas berdasarkan data).
        """)

    # 🌍 ILUSTRASI
    elif command == "Ilustrasi Kehidupan Nyata":

        st.success("🌍 Contoh Nyata")

        st.write("""
        - Nilai mahasiswa → sinyal kemampuan.
        - CV → sinyal kualitas kandidat kerja.
        - Rating e-commerce → sinyal kualitas produk.
        - Followers & engagement → sinyal kredibilitas di media sosial.
        """)

    # 📍 JADWAL
    elif command == "Jadwal Kelas":

        st.success("📍 Ini Informasi Kelas Kita")

        st.write("""
        🏫 Lokasi: Bakrie Tower 42, Ruang 38  
        ⏰ Waktu: 07.30-10.00  
        👨‍🏫 Dosen: Pak Ben Rahman
        """)

    # MOTIVASI (UPGRADED HUMAN STYLE)
    elif command == "Motivasi Belajar":

        st.success("💛 Untuk Kamu...")

        st.write("""
        Hai kamuu 😊

        Semangat yaa, tinggal beberapa pertemuan lagi!

        Mungkin sekarang terasa agak berat atau membingungkan,
        tapi percaya deh, ekonomi informasi itu bakal jadi salah satu ilmu
        yang paling kepake di dunia kerja nanti.

        Kamu bakal ngerti:
        - Gimana data itu jadi kekuatan
        - Gimana orang ambil keputusan
        - Kenapa informasi itu bisa “mahal”.

        Pelan-pelan aja, yang penting kamu tetap jalan 💪  
        Kamu lagi investasi buat masa depanmu sendiri, bisa jadi auditor atau manager yang paham dunia ekonomi.

        Proud of you sudah sejauh ini ✨
        """)

    # 💬 CUSTOM QUERY (LEBIH FLEXIBLE)
    elif command == "Custom Query":

        if not custom_query:
            default_intro()

        else:
            q = custom_query.lower()

            if "tips" in q:
                st.success("📈 Tips Nilai Tinggi")
                st.write("Coba lebih aktif di kelas, catat poin penting, dan pahami konsepnya yaa ✨")

            elif "jadwal" in q:
                st.success("📍 Jadwal Kelas")
                st.write("Kelas di BT 42 ruang 38, jam 07.30 - 10.00 bersama Pak Ben Rahman")

            elif "konsep" in q:
                st.success("📘 Penjelasan Konsep")
                st.write("""
                Ekonomi informasi itu tentang bagaimana informasi mempengaruhi keputusan.

                Contohnya:
                orang beli produk karena lihat review → itu informasi
                """)

            elif "motivasi" in q or "semangat" in q:
                st.success("💛 Semangat untuk Kamu")

                st.write("""
                Haii 😊

                Kamu lagi belajar sesuatu yang nggak semua orang pahami loh.

                Sedikit capek itu wajar, tapi jangan berhenti ya.
                Nanti kamu bakal jadi orang yang ngerti data, ngerti keputusan,
                dan itu powerful banget 🚀

                Keep going yaa, aku dukung kamu 💪✨
                """)

            else:
                default_intro()