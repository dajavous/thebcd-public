import pandas as pd
import streamlit as st
st.set_page_config(layout="wide")
import streamlit.components.v1 as components
import numpy as np

st.subheader("Dummy full contents index - testing")
excel_file = 'melling_mags.xlsx'
sheet_name = 'sheet1'

df = pd.read_excel(excel_file,
				   sheet_name=sheet_name,
				   usecols='A:D',
				   header=0)

st.dataframe(df)

