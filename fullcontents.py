import pandas as pd
import streamlit as st
#st.set_page_config(layout="wide")
import streamlit.components.v1 as components
import numpy as np
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode, JsCode
st.subheader("Full contents index - please wait for index to load")
excel_file = 'melling_mags.xlsx'
sheet_name = 'sheet1'

df = pd.read_excel(excel_file,
				   sheet_name=sheet_name,
				   usecols='A:D',
				   header=0)

gb = GridOptionsBuilder.from_dataframe(df)
gb.configure_pagination(paginationAutoPageSize=True) #Add pagination
#gb.configure_side_bar()



gridOptions = gb.build()

grid_response = AgGrid(
    df,
    gridOptions=gridOptions,
    allow_unsafe_jscode=True,
    reload_data=False,
    fit_columns_on_grid_load=False,
    theme='blue', #Add theme color to the table
    enable_enterprise_modules=False,
    height=650, 
)
