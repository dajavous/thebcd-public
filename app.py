import pandas as pd
import js2py
import streamlit as st
st.set_page_config(layout="wide")
import numpy as np
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode

excel_file = 'Newsletter-and-Magazine-Index.xlsx'
sheet_name = 'Sheet1'

df = pd.read_excel(excel_file,
				sheet_name=sheet_name,
				usecols='A:E',
				header=0)

gb = GridOptionsBuilder.from_dataframe(df)

js = """
var output;
document = {
    write: function(value){
        output = value;
    }
}
function(params) {return `<a href=${params.value} target="_blank">${params.value}</a>`}"""

context = js2py.EvalJs()
cell_renderer = context.execute(js)

gb.configure_column("ISSUE", cellRenderer=cell_renderer)
gridOptions = gb.build()

gb.configure_pagination(paginationAutoPageSize=True) #Add pagination
gb.configure_side_bar() #Add a sidebar

grid_response = AgGrid(
    df,
    gridOptions=gridOptions,
    data_return_mode='AS_INPUT', 
    update_mode='MODEL_CHANGED', 
    fit_columns_on_grid_load=False,
    theme='blue', #Add theme color to the table
    enable_enterprise_modules=True,
    height=500, 
    reload_data=True
)







