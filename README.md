# 🎓 **EDUPLANNER : Hybrid Reasoning Agent**
> _Sistem Cerdas Penentu Urutan Pengerjaan Tugas Mahasiswa_

---

## 👩‍💻 **Anggota Kelompok**
| NIM | Nama |
|-----|------|
| 4522210066 | **Salwa Khairu Mista** |
| 4522210037 | **Raihan Alfisa Saugi** |
| 4522210040 | **Daffa Abraar Sajuti** |

---

## 🧠 **Deskripsi Proyek**
**EDUPLANNER** adalah sistem **Hybrid Agent (Forward Chaining + Learning Agent)** yang membantu mahasiswa menentukan **prioritas tugas kuliah** berdasarkan:
- Deadline tugas   
- Tingkat kesulitan   
- Riwayat kebiasaan belajar  

Aplikasi ini dibuat menggunakan **Streamlit** sehingga berjalan interaktif di web, dengan penyimpanan lokal menggunakan file `riwayat_tugas.csv`.

---

## ⚙️ **Fitur Utama**
| Fitur | Deskripsi |
|-------|------------|
| 📝 **Input Tugas** | Menambahkan tugas baru dengan nama, mata kuliah, kesulitan, dan deadline |
| 🧩 **Forward Chaining (Rule-Based)** | Menentukan prioritas tugas otomatis berdasarkan aturan logika |
| 📊 **Visualisasi Data** | Menampilkan grafik distribusi tugas berdasarkan tingkat prioritas |
| ✅ **Feedback Learning Agent** | Sistem belajar dari feedback pengguna untuk menyesuaikan saran di masa depan |
| 🎯 **Goal-Based Suggestion** | Memberikan rekomendasi tugas yang paling penting untuk dikerjakan hari ini |

---

## 🧩 **Konsep Reasoning**
### 🔹 1. Forward Chaining (Data-Driven Reasoning)
Agen memulai dari **fakta-fakta awal** (deadline dan kesulitan tugas), lalu menurunkan **kesimpulan baru** berupa *prioritas tugas*.  
Contoh aturan sederhana:
`IF deadline ≤ 2 hari THEN prioritas = "Sangat Tinggi"
ELSE IF kesulitan = "Sulit" AND deadline ≤ 5 hari THEN prioritas = "Tinggi"
ELSE IF kesulitan = "Mudah" THEN prioritas = "Sedang"
ELSE prioritas = "Rendah"`

---

### 🔹 2. Learning Agent
Agen menganalisis feedback pengguna dari tugas yang sudah selesai:
- Jika banyak tugas terlambat → Agen memberi peringatan agar fokus ke prioritas tinggi.  
- Jika sebagian besar tugas selesai tepat waktu → Agen memberikan apresiasi.  

Konsep: **Belajar dari pengalaman pengguna** untuk menyesuaikan rekomendasi selanjutnya.

---


