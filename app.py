import streamlit as st
import numpy as np
from PIL import Image
import tensorflow as tf
# from tensorflow.keras.models import load_model
st.markdown("💡 Bergabung sebagai Duta Noken adalah langkah kecil untuk dampak budaya yang besar.")


@st.cache(allow_output_mutation=True)
def load_model():
  model=tf.keras.models.load_model('mobilenetv2.h5')
  return model
with st.spinner('Model is being loaded..'):
  model=load_model()
  
  
# classes = ['Bitu Agia', 'Junum Ese']  # Sesuaikan dengan kelas kamu

# # Preprocessing gambar
# def preprocess_image(img):
#     img = img.resize((224, 224))
#     img_array = np.array(img) / 255.0
#     img_array = np.expand_dims(img_array, axis=0)
#     return img_array

# # Resize gambar untuk ditampilkan
# def resize_display_image(img, max_size=300):
#     img = img.copy()
#     img.thumbnail((max_size, max_size))
#     return img

# # Konfigurasi halaman
# st.set_page_config(page_title="Klasifikasi Noken", layout="centered")

# # Judul utama
# st.title("Aplikasi Klasifikasi Noken")
# st.markdown("Membantu pelestarian budaya Papua melalui teknologi AI.")

# Navigasi menggunakan tab
tab1, tab2, tab3 = st.tabs(["🏷️ Klasifikasi Noken", "📚 Tentang Noken", "🧶 Duta Noken"])

# # ======================== TAB 1: KLASIFIKASI ========================
# with tab1:
#     st.subheader("🔍 Klasifikasikan Jenis Noken")
#     option = st.radio("Pilih metode input gambar:", ["📷 Ambil Foto", "📁 Upload Gambar"])

#     image = None
#     if option == "📁 Upload Gambar":
#         uploaded_file = st.file_uploader("Upload gambar", type=["jpg", "jpeg", "png"])
#         if uploaded_file:
#             image = Image.open(uploaded_file).convert("RGB")

#     elif option == "📷 Ambil Foto":
#         camera_image = st.camera_input("Ambil foto menggunakan kamera")
#         if camera_image:
#             image = Image.open(camera_image).convert("RGB")

#     if image:
#         display_img = resize_display_image(image)
#         st.image(display_img, caption="Gambar yang digunakan", use_container_width=True)

#         input_array = preprocess_image(image)
#         prediction = model.predict(input_array)[0][0]
#         label = classes[1] if prediction > 0.5 else classes[0]
#         confidence = prediction if prediction > 0.5 else 1 - prediction

#         st.markdown(f"### ✅ Prediksi: `{label}`")
#         st.markdown(f"**Confidence**: {confidence:.2%}")

#         if st.button("💾 Simpan Hasil"):
#             st.success("✅ Hasil klasifikasi disimpan! (simulasi)")

# # ======================== TAB 2: EDUKASI NOKEN ========================
# with tab2:
#     st.header("📖 Apa itu Noken?")
#     st.image("junum_ese.jpg", caption="Contoh Noken Tradisional", use_container_width=True)
#     st.write("""
#     **Noken** adalah tas tradisional masyarakat Papua yang terbuat dari serat kulit kayu.
#     Noken bukan sekadar tas, tapi juga simbol budaya, identitas, dan kedewasaan bagi perempuan Papua.

#     Pada 4 Desember 2012, Noken diakui oleh **UNESCO** sebagai *Warisan Budaya Takbenda Dunia*.
#     """)

#     st.markdown("🔗 [Baca selengkapnya di situs UNESCO](https://ich.unesco.org/en/RL/noken-multi-functional-handwoven-bag-carrying-knowledge-and-identity-00619)")

#     with st.expander("🎯 Fakta Menarik tentang Noken"):
#         st.markdown("""
#         - ✅ Noken dibuat oleh lelaki dan perempuan Papua.
#         - 📦 Digunakan untuk membawa hasil kebun, barang, hingga bayi.
#         - 🧵 Dibuat dari serat pohon seperti pohon Ganemo atau Anggrek.
#         """)

#     with st.expander("🧪 Uji Pengetahuan Kamu!"):
#         question = st.radio("Apa bahan utama pembuatan Noken?", ["Plastik", "Serat kulit kayu", "Benang wol"])
#         if st.button("Cek Jawaban"):
#             if question == "Serat kulit kayu":
#                 st.success("✅ Benar! Noken dibuat dari kulit kayu.")
#             else:
#                 st.error("❌ Salah! Jawaban yang benar: Serat kulit kayu.")

# # ======================== TAB 3: DUTA NOKEN ========================
# with tab3:
#     st.header("🧶 Duta Noken")
#     st.write("""
#     **Duta Noken** adalah individu atau perwakilan yang berperan dalam meningkatkan kesadaran, pelestarian,
#     dan promosi budaya Papua melalui edukasi dan aktivitas komunitas, khususnya seputar Noken.
#     """)

#     st.markdown("""
#     ### 📌 Peran Duta Noken:
#     - 🧑‍🏫 Mengedukasi masyarakat tentang nilai budaya Noken.
#     - 📸 Mendokumentasikan proses pembuatan Noken.
#     - 🧵 Mengadakan workshop dan pameran bersama pengrajin lokal.
#     """)

#     st.markdown("### 📬 Tertarik bergabung?")
#     st.write("""
#     Hubungi kami di:
#     - 📧 Email: **duta@noken.id**
#     - 📱 Instagram: [@dutanoken](https://instagram.com/dutanoken)
#     - 🌐 Website: [www.nokenpapua.id](https://www.nokenpapua.id) _(simulasi)_
#     """)

#     st.markdown("💡 Bergabung sebagai Duta Noken adalah langkah kecil untuk dampak budaya yang besar.")
