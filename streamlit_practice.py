import streamlit as st
import numpy as np
import pandas as pd

st.title('Meningioma perfect prediction')

Age = st.sidebar.slider('Age', 10, 100)
st.sidebar.write('Age:', Age)