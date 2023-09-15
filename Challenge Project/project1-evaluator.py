import streamlit as st
import pandas as pd
import numpy as np

team = st.selectbox('What is your team number?', ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10'))
option = st.radio('Select your classification level', ('Binary', 'Multiclass'))
input = st.file_uploader('Upload your pkl file', type='pkl')
if(input != None):
  st.write('Hi')
