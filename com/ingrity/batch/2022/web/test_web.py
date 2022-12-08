import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode

def my_web():
    st.set_page_config(layout="wide")
    st.title("Batch 2022")
    df = pd.read_csv("D:\Support\snowflakedata\PersonDemographics\PersonDemographics2.csv")

    c = st.text_input("Gender")

    st.button("Submit")
    st.table(df)

    # gb = GridOptionsBuilder.from_dataframe(df)
    #
    # gb.configure_default_column(enablePivot=True, enableValue=True, enableRowGroup=True)
    #
    # gb.build()


if __name__ == "__main__":
    my_web()
