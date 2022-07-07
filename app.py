import pandas as pd
import streamlit as st
st.set_page_config(layout="wide")
import numpy as np
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode, JsCode

excel_file = 'Newsletter-and-Magazine-Index.xlsx'
sheet_name = 'Sheet1'

df = pd.read_excel(excel_file,
				sheet_name=sheet_name,
				usecols='A:E',
				header=0)

gb = GridOptionsBuilder.from_dataframe(df)
gb.configure_pagination(paginationAutoPageSize=True) #Add pagination
gb.configure_side_bar(filters_panel=True, columns_panel=False)

gb.configure_column("ISSUE",
                            headerName="ISSUE",
                            cellRenderer=JsCode('''function(params) {return '<a href="https://thebcd.co.uk/bcd_members_only/issue_' + params.value + '" target="_blank">'+ params.value+'</a>'}'''),
                            width=300)
gridOptions = gb.build()

grid_response = AgGrid(
    df,
    gridOptions=gridOptions,
    allow_unsafe_jscode=True,
    data_return_mode='AS_INPUT', 
    update_mode='MODEL_CHANGED', 
    fit_columns_on_grid_load=False,
    theme='blue', #Add theme color to the table
    enable_enterprise_modules=True,
    height=500, 
    reload_data=True
)






