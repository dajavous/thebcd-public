import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image

st.set_page_config(page_title='Newsletter and Magazine Index')
st.header('BCD Newsletter and Magazine Index')
st.subheader('Sort and search for keywords and articles')

excel_file = 'Newsletter-and-Magazine-Index.xlsx'
sheet_name = 'Sheet1'

df = pd.read_excel(excel_file,
				sheet_name=sheet_name,
				usecols='A:E',
				header=0)

st.dataframe(df)






