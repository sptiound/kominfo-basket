import streamlit as st
import pandas as pd

# Konfigurasi Halaman
st.set_page_config(page_title="Portal Divisi Kominfo", page_icon="🏀", layout="wide")

# ==========================================
# INJEKSI CSS
# ==========================================
st.markdown("""
<style>
    /* Mengurangi jarak kosong di atas agar konten naik */
    .block-container {
        padding-top: 2rem !important; 
    }

    /* ========================================================= */
    /* 1. SIDEBAR KEMBALI KE DESAIN AWAL (MIDNIGHT BLUE) */
    /* ========================================================= */
    [data-testid="stSidebar"] {
        background-color: #0D47A1 !important;
    }
    
    [data-testid="stSidebar"] * {
        color: #FFFFFF !important;
    }

    /* ========================================================= */
    /* 2. TOMBOL LINK (KUNING SPARK) */
    /* ========================================================= */
    [data-testid="baseButton-link"] {
        background-color: #fec428 !important;
        color: #0D47A1 !important;
        border: 2px solid #fbde37 !important;
        border-radius: 8px !important;
        font-weight: 800 !important;
        transition: 0.3s;
    }
    
    [data-testid="baseButton-link"]:hover {
        background-color: #2196F3 !important; 
        color: #FFFFFF !important;
        border: 2px solid #2196F3 !important;
    }

    /* ========================================================= */
    /* 3. KOTAK NOTIFIKASI / ALERT (AZURE) */
    /* ========================================================= */
    [data-testid="stAlert"] {
        background-color: #4FC3F7 !important;
        border: none !important;
    }
    [data-testid="stAlert"] * {
        color: #0D47A1 !important;
    }

    /* ========================================================= */
    /* 4. EXPANDER / NOTULENSI (DIKEMBALIKAN KE BIRU MUDA) */
    /* ========================================================= */
    [data-testid="stExpander"] {
        background-color: #E1F5FE !important; /* Biru Muda */
        border: 1px solid #4FC3F7 !important;
        border-radius: 8px;
    }
    
    [data-testid="stExpander"] * {
        color: #0D47A1 !important; /* Teks biru tua agar kontras */
    }
</style>
""", unsafe_allow_html=True)

# Sidebar Navigasi
st.sidebar.title("📌 Menu Kominfo")
menu = st.sidebar.radio("Pilih Kategori:", 
    ["Dashboard", 
     "📂 Dokumentasi Kegiatan", 
     "📝 Notulensi Rapat", 
     "📅 Jobdesc & Hari Besar", 
     "🎨 Aset Canva"]
)

# 1. HALAMAN DASHBOARD
if menu == "Dashboard":
    st.title("Portal Divisi Kominfo 🏀")
    st.write("Selamat datang di pusat data internal Kominfo! Gunakan menu di sebelah kiri untuk mengakses dokumen, link desain, dan jadwal kegiatan.")
    st.info("Papan Pengumuman: membuat video demo dan konten open recruitment")

# 2. HALAMAN DOKUMENTASI KEGIATAN (GOOGLE DRIVE)
elif menu == "📂 Dokumentasi Kegiatan":
    st.title("📂 Link Dokumentasi (Google Drive)")
    st.write("Akses cepat ke folder dokumentasi foto dan video kegiatan.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Event Besar")
        st.link_button("📁 Dokumentasi Nusantara Cup", "https://drive.google.com/...")
    with col2:
        st.subheader("Lain-lain")
        st.link_button("📁 Folder Kegiatan UKM", "https://drive.google.com/drive/folders/1ZyfY7YMNB6OtJ8dDdPQzPuT6xW2QJ7gb?usp=sharing")
        st.link_button("📁 Folder Kegiatan Pengurus", "https://drive.google.com/drive/folders/1-B4rbPm1U3VAwq59HHNVk3YJF8mMw8oL?usp=drive_link")
        st.link_button("📁 Folder LOGO", "https://drive.google.com/drive/folders/1-9wwGgeyMSZCef787-L2ytpw8Fj8gFsL?usp=drive_link")

# 3. HALAMAN NOTULENSI RAPAT
elif menu == "📝 Notulensi Rapat":
    st.title("📝 Notulensi Rapat Divisi")
    st.write("Arsip hasil rapat rutin divisi Kominfo.")
    
    st.link_button("📄 Buka Google Docs Master Notulensi", "https://docs.google.com/...")
    
    with st.expander("PASSWORD"):
        st.markdown("""
            1. Email
               - basketnusantaraa@gmail.com Pw: Nusantarabasket2026
               - kominfoukmbasket@gmail.com Pw: Kominfobasket27
               - nusantarabasketball25.26@gmail.com Pw: Basketnusantara27
            2. Sosial Media
               ~ username: ukmbasketnusantara
                 - IG: \$UKMB4SK3T2627\$
                 - TIKTOK: #KominfoUKM27
            3. Canva login 
               - kominfoukmbasket@gmail.com : KominfoUKM27
        """)
        
    with st.expander("Rapat Divisi - 12 Agustus 2026"):
        st.markdown("""
            1. Proker rutin post sg ultah pj amin
                - buat gform (amin)
                - buat desain frame, desainnya disamakan semua (mei), yg memasukan foto di desain (teddy)
                - posting sg (fajar)
                - tema desain ulang tahun
            2. Proker post hari besar (??ngelu)
                - Pj fajar
                - yg edit seluruh anggota, jadwal sudah ditentukan
                - tema literasi digital dan inovasi 
            3. Proker RKT
                - Pj vella
                - buat after movie yg edit (teddy)
                - rkt dilist 
                - yg posting fajar
            4. Oprec ukm
                - buat konten oprec
                - desain poster oprec (teddy)
        """)

# 4. HALAMAN JOBDESC & HARI BESAR (SPREADSHEET)
elif menu == "📅 Jobdesc & Hari Besar":
    st.title("📅 Jobdesc & Kalender Hari Besar")
    st.write("Pembagian tugas dan jadwal posting perayaan hari besar.")
    
    st.link_button("📊 Buka Google Spreadsheet Jobdesc", "https://docs.google.com/spreadsheets/d/1GnljLZ0-A0Rba876XCtAcmU0nRoReO4AdxrB_rGVrWw/edit?usp=sharing")
    
    st.divider()
    
    st.subheader("Preview Jadwal Terdekat")
    
    data_hari_besar = pd.DataFrame({
        "Tanggal": [
            "14 Agustus", "17 Agustus 2026", "21 Agustus 2026", "25 Agustus 2026",
            "30 September 2026", "1 Oktober 2026", "28 Oktober 2026", "10 November 2026",
            "12 November 2026", "25 November 2026", "22 Desember 2026", "25 Desember 2026",
            "31 Desember 2026", "1 Januari 2027"
        ],
        "Hari Peringatan": [
            "Hari Pramuka", "Hari Kemerdekaan, Proklamasi", "Hari Maritim Nasional", 
            "Maulid Nabi Muhammad SAW.", "G30S/PKI", "Hari Kesaktian Pancasila", 
            "Hari Sumpah Pemuda", "Hari Pahlawan Nasional", "Hari Ayah Nasional", 
            "Hari Guru Nasional", "Hari Ibu", "Hari Natal", 
            "Malam Tahun Baru", "Tahun Baru"
        ],
        "Status Desain": [
            "Completed ✅", "Not started ⏳", "Not started ⏳", "Not started ⏳",
            "Not started ⏳", "Not started ⏳", "Not started ⏳", "Not started ⏳",
            "Not started ⏳", "Not started ⏳", "Not started ⏳", "Not started ⏳",
            "Not started ⏳", "Not started ⏳"
        ],
        "PIC": [
            "Amin", "Teddy", "Vella", "Mei",
            "Tia", "Amin", "Teddy", "Vella",
            "Mei", "Tia", "Amin", "Teddy",
            "Vella", "Mei"
        ],
        "Status Upload": [
            "Done ✅", "Not Upload Yet ❌", "Not Upload Yet ❌", "Not Upload Yet ❌",
            "Not Upload Yet ❌", "Not Upload Yet ❌", "Not Upload Yet ❌", "Not Upload Yet ❌",
            "Not Upload Yet ❌", "Not Upload Yet ❌", "Not Upload Yet ❌", "Not Upload Yet ❌",
            "Not Upload Yet ❌", "Not Upload Yet ❌"
        ]
    })
    
    st.dataframe(data_hari_besar, use_container_width=True, hide_index=True)
    
# 5. HALAMAN ASET CANVA
elif menu == "🎨 Aset Canva":
    st.title("🎨 Link Template & Desain Canva")
    st.write("Kumpulan link *master template* agar desain feeds dan story tetap konsisten.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.success("Template Feeds Instagram")
        st.link_button("🖼️ Template Feeds Utama", "https://canva.com/...")
        st.link_button("🖼️ Template Color Pallete", "https://canva.link/l2ysb1b7b89lv1n")
        st.link_button("🖼️ Template Open Recruitment", "https://canva.link/dd9scm76apd1ied")
    with col2:
        st.warning("Template Instagram Story")
        st.link_button("📱 Template Story Info Latihan", "https://canva.link/odclsjmj0na5tam")
        st.link_button("📱 Template Hari Besar", "https://canva.link/drmoy6yiw5msxlp")
