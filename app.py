import streamlit as st
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model

# Load model dan kelas
model = load_model('mobilenetv2.h5')  
classes = ['Bitu Agia', 'Junum Ese'] 

# Preprocessing gambar
def preprocess_image(img):
    img = img.resize((224, 224))
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

# Resize gambar untuk ditampilkan
def resize_display_image(img, max_size=300):
    img = img.copy()
    img.thumbnail((max_size, max_size))
    return img

st.set_page_config(page_title="Klasifikasi Noken", layout="centered")

st.title("Aplikasi Klasifikasi Noken")
st.markdown("Membantu pelestarian budaya Papua melalui teknologi")

tab1, tab2= st.tabs(["📚 Tentang Noken", "🏷️ Klasifikasi Noken"])

# ======================== TAB 1: EDUKASI NOKEN ========================
with tab1:
    st.header("📖 Apa itu Noken?")
    st.image("junum_ese.jpg", caption="Contoh Noken Tradisional")
    st.write("""
    **Noken** adalah tas tradisional masyarakat Papua yang terbuat dari serat kulit kayu.
    Noken bukan sekadar tas, tapi juga simbol budaya, identitas, dan kedewasaan bagi perempuan Papua.

    Pada 4 Desember 2012, Noken diakui oleh **UNESCO** sebagai *Warisan Budaya Takbenda Dunia*.
    """)

    st.markdown("🔗 [Baca selengkapnya di situs UNESCO](https://ich.unesco.org/en/RL/noken-multi-functional-handwoven-bag-carrying-knowledge-and-identity-00619)")

    with st.expander("🎯 Fakta Menarik tentang Noken"):
        st.markdown("""
        - ✅ Noken dibuat secara manual dari serat kulit kayu, dengan proses pemintalan dan perajutan yang rumit, memakan waktu berhari-hari hingga berminggu-minggu
        - 📦 Digunakan untuk membawa hasil kebun, barang, hingga bayi.
        - 🧵 Dibuat berbaga macam bahan alam, beberapa diataranya adalah pohon Ganemo atau Anggrek.
        """)

    with st.expander("🧪 Uji Pengetahuan Kamu!"):
        question = st.radio("Noken Junum Ese berasal dari daerah mana?", ["Sentani", "Asmat", "Arfak"])
        if st.button("Cek Jawaban"):
            if question == "Asmat":
                st.success("✅ Benar! Noken Junum Ese berasal dari Asmat.")
            else:
                st.error("❌ Salah! Jawaban yang benar: Asmat.")

# ======================== TAB 2: KLASIFIKASI ========================
with tab2:
    st.subheader("🔍 Klasifikasikan Jenis Noken")
    option = st.radio("Pilih metode input gambar:", ["📷 Ambil Foto", "📁 Upload Gambar"])

    image = None
    if option == "📁 Upload Gambar":
        uploaded_file = st.file_uploader("Upload gambar", type=["jpg", "jpeg", "png"])
        if uploaded_file:
            image = Image.open(uploaded_file).convert("RGB")

    elif option == "📷 Ambil Foto":
        camera_image = st.camera_input("Ambil foto menggunakan kamera")
        if camera_image:
            image = Image.open(camera_image).convert("RGB")

    if image:
        display_img = resize_display_image(image)
        st.image(display_img, caption="Gambar yang digunakan")

        input_array = preprocess_image(image)
        prediction = model.predict(input_array)[0][0]
        label = classes[1] if prediction > 0.5 else classes[0]
        confidence = prediction if prediction > 0.5 else 1 - prediction

        st.markdown(f"### ✅ Prediksi: `{label}`")
        st.markdown(f"**Akurasi**: {confidence:.2%}")



