import streamlit as st
import eda
import prediction
from PIL import Image


with st.sidebar:
    image = Image.open('eCentrixlogo.png')
    st.image(image, caption = 'eCentrix Solutions')

page = st.sidebar.selectbox('Pilih Halaman : ', ('Dashboard', 'Prediction'))

with st.sidebar:
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')

    st.subheader('Head Office')
    st.write('Jl. Nangka no 87. Tanjung Barat Jakarta Selatan 12530')


if page == 'Dashboard' : 
    eda.run()
else:
    prediction.run()