import pandas as pd
import streamlit as st
st.set_page_config(layout="wide")
import numpy as np
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode, JsCode

excel_file = 'country_capitals.xlsx'
sheet_name = 'Sheet1'

df = pd.read_excel(excel_file,
				sheet_name=sheet_name,
				usecols='A:E',
				header=0)

gb = GridOptionsBuilder.from_dataframe(df)
gb.configure_pagination(paginationAutoPageSize=True) #Add pagination
gb.configure_side_bar()



gridOptions = gb.build()

grid_response = AgGrid(
    df,
    gridOptions=gridOptions,
    allow_unsafe_jscode=True,
    data_return_mode='AS_INPUT', 
    update_mode='MODEL_CHANGED', 
    fit_columns_on_grid_load=False,
    theme='blue', #Add theme color to the table
    enable_enterprise_modules=False,
    height=500, 
    reload_data=True
)






