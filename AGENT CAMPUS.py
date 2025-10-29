# =========================================================
# 🎓 AGENT KAMPUS CERDAS — HYBRID REASONING AGENT
# =========================================================

import streamlit as st
import pandas as pd
from datetime import datetime, date
import matplotlib.pyplot as plt
import os

st.set_page_config(page_title="Agent Kampus Cerdas", page_icon="🎓", layout="centered")

st.title("🎓 EDUPLANNER")
st.write("Sistem pintar yang membantu menentukan **prioritas tugas kuliah** kamu berdasarkan deadline, kesulitan, dan kebiasaan belajarmu.")

# =========================================================
# 1️⃣ DATA INISIALISASI
# =========================================================
DATA_FILE = "riwayat_tugas.csv"

if os.path.exists(DATA_FILE):
    df = pd.read_csv(DATA_FILE)
else:
    df = pd.DataFrame(columns=["Tugas", "Mata Kuliah", "Kesulitan", "Deadline", "Prioritas", "Status", "Feedback"])

# =========================================================
# 2️⃣ INPUT FORM
# =========================================================
st.subheader("📝 Tambahkan Data Tugas")
nama = st.text_input("Nama Tugas:")
mata_kuliah = st.text_input("Mata Kuliah:")
kesulitan = st.selectbox("Tingkat Kesulitan:", ["Mudah", "Sedang", "Sulit"])
deadline = st.date_input("Deadline Tugas:")

# =========================================================
# 3️⃣ RULE-BASED FORWARD CHAINING
# =========================================================
def tentukan_prioritas(kesulitan, deadline):
    hari_tersisa = (deadline - date.today()).days

    if hari_tersisa < 0:
        return "Terlambat"
    elif hari_tersisa <= 2:
        return "Sangat Tinggi"
    elif hari_tersisa <= 5 and kesulitan == "Sulit":
        return "Tinggi"
    elif kesulitan == "Mudah" and hari_tersisa > 2:
        return "Sedang"
    else:
        return "Rendah"

# =========================================================
# 4️⃣ TAMBAH DATA
# =========================================================
if st.button("💾 Tambahkan ke Daftar"):
    if nama and mata_kuliah:
        prioritas = tentukan_prioritas(kesulitan, deadline)
        new_row = pd.DataFrame([[nama, mata_kuliah, kesulitan, deadline, prioritas, "Belum", ""]],
                               columns=df.columns)
        df = pd.concat([df, new_row], ignore_index=True)
        df.to_csv(DATA_FILE, index=False)
        st.success(f"Tugas **{nama}** ditambahkan dengan prioritas **{prioritas}** ✅")
    else:
        st.warning("Mohon isi semua field sebelum menambahkan tugas.")

# =========================================================
# 5️⃣ TAMPILKAN DATA
# =========================================================
st.subheader("📋 Daftar Semua Tugas")
if not df.empty:
    df_sorted = df.sort_values(by="Prioritas", ascending=True)
    st.dataframe(df_sorted)

    # =====================================================
    # 6️⃣ VISUALISASI PRIORITAS
    # =====================================================
    st.subheader("📊 Distribusi Prioritas")
    fig, ax = plt.subplots()
    df["Prioritas"].value_counts().plot(kind="bar", ax=ax)
    ax.set_title("Jumlah Tugas Berdasarkan Prioritas")
    ax.set_ylabel("Jumlah")
    st.pyplot(fig)

    # =====================================================
    # 7️⃣ FEEDBACK / LEARNING ELEMENT
    # =====================================================
    st.subheader("📈 Evaluasi & Pembelajaran")
    tugas_pilih = st.selectbox("Pilih tugas yang sudah dikerjakan:", df["Tugas"])
    feedback = st.radio("Apakah urutan prioritas sesuai kenyataan?", ["Belum", "Ya", "Tidak"], horizontal=True)

    if st.button("✅ Simpan Feedback"):
        df.loc[df["Tugas"] == tugas_pilih, "Feedback"] = feedback
        df.loc[df["Tugas"] == tugas_pilih, "Status"] = "Selesai"
        df.to_csv(DATA_FILE, index=False)
        st.success("Feedback disimpan. Agen belajar dari perilaku kamu!")

        # Analisis sederhana dari feedback (learning)
        feedback_stat = df["Feedback"].value_counts()
        st.info(f"📊 Statistik Feedback: {dict(feedback_stat)}")

else:
    st.info("Belum ada tugas yang ditambahkan.")

# =========================================================
# 8️⃣ GOAL-BASED SUGGESTION
# =========================================================
st.subheader("🎯 Rekomendasi Harian (Goal-based)")

def evaluasi_feedback(df):
    """Analisis sederhana perilaku pengguna (learning agent)."""
    if df.empty:
        return "Belum ada data untuk dianalisis."
    selesai = len(df[df["Status"] == "Selesai"])
    terlambat = len(df[df["Prioritas"] == "Terlambat"])
    total = len(df)
    rasio = selesai / total if total else 0
    if rasio < 0.5:
        return f"⚠️ Kamu sering menunda tugas. Fokuslah ke tugas berprioritas tinggi! (Selesai: {selesai}/{total})"
    else:
        return f"✅ Hebat! Kamu menyelesaikan sebagian besar tugas tepat waktu. (Selesai: {selesai}/{total})"

if not df.empty:
    df_aktif = df[df["Status"] == "Belum"]
    if not df_aktif.empty:
        tugas_fokus = df_aktif.sort_values(by="Prioritas", ascending=True).iloc[0]
        st.success(f"💡 Rekomendasi: Fokus dulu pada **{tugas_fokus['Tugas']}** "
                   f"({tugas_fokus['Mata Kuliah']}) dengan prioritas **{tugas_fokus['Prioritas']}**.")
    else:
        st.info("Semua tugas sudah selesai! 🎉")

    # Feedback learning
    st.markdown("### 📈 Analisis Learning Agent")
    st.info(evaluasi_feedback(df))
else:
    st.info("Belum ada data untuk divisualisasikan.")

st.caption("Dibuat oleh: Slw Khair — Proyek UTS AI • 2025")
