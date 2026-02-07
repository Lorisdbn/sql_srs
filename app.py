import streamlit as st
import pandas as pd
import duckdb


st.title("SQL Playground 🚀")

option = st.selectbox(
    "What would you like to review?",
    ("Joins", "GroupBy", "Windows function"),
    placeholder="Select a theme"
)

st.write("You selected:", option)

data = {
    "a": [1, 2, 3],
    "b": [4, 5, 6],
    "c": [7, 8, 9],
    "d": [10, 11, 12]
}

df=pd.DataFrame(data)

tab_1, tab_2 = st.tabs(["1er onglet", "2ème onglet"])

with tab_1:
    sql_query = st.text_area(label="Input text", key="input1")
    result = duckdb.query(sql_query).df()
    st.write(f"you entered the following query : {sql_query}")
    st.dataframe(result)


with tab_2:
    input_text = st.text_area(label="Input text", key="input2")
    st.write(input_text)