import pandas as pd
import streamlit as st

excel_file = 'Newsletter-and-Magazine-Index.xlsx'
sheet_name = 'Sheet1'

df = pd.read_excel(excel_file,
				sheet_name=sheet_name,
				usecols='A:E',
				header=0,
		  		index_col=None)

st.dataframe(df, width=1200, height=400)






