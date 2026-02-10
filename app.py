import io

import duckdb
import pandas as pd
import streamlit as st

df_beverages = pd.DataFrame(
    {
        "beverage": [
            "Coffee",
            "Tea",
            "Orange Juice",
            "Soda",
            "Water",
            "Latte",
            "Cappuccino",
            "Iced Tea",
            "Lemonade",
            "Smoothie",
        ],
        "price": [3, 2, 4, 3, 1, 5, 5, 3, 4, 6],
    }
)

df_food = pd.DataFrame(
    {
        "food": [
            "Burger",
            "Pizza",
            "Salad",
            "Pasta",
            "Sandwich",
            "Fries",
            "Tacos",
            "Sushi",
            "Steak",
            "Wrap",
        ],
        "price": [10, 12, 8, 11, 7, 4, 9, 14, 18, 8],
    }
)

answer_str = "SELECT * FROM df_food CROSS JOIN  df_beverages"
solution_df = duckdb.sql(answer_str).df()


with st.sidebar:
    option = st.selectbox(
        "What would you like to review?",
        ("Joins", "GroupBy", "Windows function"),
        placeholder="Select a theme",
    )
    st.write("You selected:", option)

st.title("SQL Playground 🚀")

st.header("enter your code here:")
sql_query = st.text_area(label="Input text", key="input1")

if sql_query:
    result = duckdb.query(sql_query).df()
    st.write(f"you entered the following query : {sql_query}")
    st.dataframe(result)

try:
    result = result[solution_df.columns]
    st.dataframe(result.compare(solution_df))
except KeyError:
    st.write("Columns number does not match")

tab_1, tab_2 = st.tabs(["Tables", "solution_df"])

with tab_1:
    st.write(df_beverages)
    st.write(df_food)
    st.write("expected:")
    st.dataframe(solution_df)

with tab_2:
    st.write(answer_str)
