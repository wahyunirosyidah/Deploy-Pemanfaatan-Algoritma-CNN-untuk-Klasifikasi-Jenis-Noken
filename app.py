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