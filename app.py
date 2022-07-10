import pandas as pd
import streamlit as st
st.set_page_config(layout="wide")
import numpy as np
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode, JsCode
st.subheader(" Index")
excel_file = 'country_capitals.xlsx'
sheet_name = 'Sheet1'

df = pd.read_excel(excel_file,
				   sheet_name=sheet_name,
				   usecols='A:E',
				   header=0)

with st.expander("Help on using the Index", expanded=True):
       st.write("""
        - This Index is interactive, and includes dummy links.
	- Using the column headings you can sort by clicking, rearrange columns and change column widths
	by clicking and dragging, and remove columns by dragging off the page.
	- Hover over a column heading and click on the three-bar menu that appears in the column 
	heading (or just long press on the heading with a tablet) to open the column search box.
	- Tap on the table rows anywhere (other than links!) to hide the column search boxes.
	- Change the theme to provide different colours and font sizes (also resets the table to the starting view).
	- Refresh the page to go back to the starting view of the index and theme.
	- Click on "Help on using the Index" above to open or close this help box.
     """)

hvar = """  <script>
			var elements = window.parent.document.querySelectorAll('.streamlit-expanderHeader');
			elements[0].style.fontWeight = 'bold';
	    </script>"""

components.html(hvar, height=0, width=0)

available_themes = ["streamlit", "light", "dark", "blue", "fresh", "material"]
selected_theme = st.selectbox("Choose a different color theme for the table below", available_themes)

gb = GridOptionsBuilder.from_dataframe(df)
#gb.configure_pagination(paginationAutoPageSize=True) #Add pagination
#gb.configure_side_bar()

gb.configure_column("TYPE",
                            headerName="TYPE",
                            cellRenderer=JsCode('''function(params) {return '<a href="https://www.google.com" target="_blank">'+ params.value+'</a>'}'''),
                            width=300)

gridOptions = gb.build()

grid_response = AgGrid(
    df,
    gridOptions=gridOptions,
    allow_unsafe_jscode=True,
    data_return_mode='AS_INPUT', 
    update_mode='MODEL_CHANGED', 
    fit_columns_on_grid_load=False,
    theme=selected_theme, #Add theme color to the table
    enable_enterprise_modules=False,
    height=500, 
    reload_data=True
)







