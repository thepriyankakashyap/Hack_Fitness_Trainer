import streamlit as st
from PIL import Image

st.title('Hack Fitness Trainer')

image = Image.open('demo.jpg')

st.image(image, caption='Hack Fitness Trainer')
