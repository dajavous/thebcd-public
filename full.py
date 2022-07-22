import pandas as pd
import streamlit as st
#st.set_page_config(layout="wide")
import streamlit.components.v1 as components
import numpy as np
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode, JsCode
st.subheader("Dummy Full contents index - please wait for index to load")
excel_file = 'melling_mags.csv'
sheet_name = 'sheet1'

df = pd.read_csv(excel_file)

with st.expander("Help on using the Index", expanded=True):
       st.write("""
	- Hover over a column heading and click on the three-bar menu that appears in the column 
	  heading (or just long press on the heading with a tablet) to open the column search box.
	- Tap on the table rows anywhere (other than links!) to hide the column search boxes.
	- Click on "Help on using the Index" above to open or close this help box.
     """)

hvar = """  <script>
			var elements = window.parent.document.querySelectorAll('.streamlit-expanderHeader');
			elements[0].style.fontSize = 'large';
			elements[0].style.fontWeight = 'bold';
	    </script>"""

components.html(hvar, height=0, width=0)

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
