import streamlit as st
import pandas as pd
import duckdb

df_beverages = pd.DataFrame({
    "beverage": [
        "Coffee", "Tea", "Orange Juice", "Soda", "Water",
        "Latte", "Cappuccino", "Iced Tea", "Lemonade", "Smoothie"
    ],
    "price": [3, 2, 4, 3, 1, 5, 5, 3, 4, 6]
})

df_food = pd.DataFrame({
    "food": [
        "Burger", "Pizza", "Salad", "Pasta", "Sandwich",
        "Fries", "Tacos", "Sushi", "Steak", "Wrap"
    ],
    "price": [10, 12, 8, 11, 7, 4, 9, 14, 18, 8]
})

answer= "SELECT * FROM df_food CROSS JOIN  df_beverages"
solution = duckdb.sql(answer).df()


with st.sidebar:
    option = st.selectbox(
        "What would you like to review?",
        ("Joins", "GroupBy", "Windows function"),
        placeholder="Select a theme"
    )
    st.write("You selected:", option)

st.title("SQL Playground 🚀")

st.header("enter your code here:")
sql_query = st.text_area(label="Input text", key="input1")

if sql_query:
    result = duckdb.query(sql_query).df()
    st.write(f"you entered the following query : {sql_query}")
    st.dataframe(result)

tab_1, tab_2 = st.tabs(["Tables", "Solution"])

with tab_1:
    st.write(df_beverages)
    st.write(df_food)
    st.write("expected:")
    st.dataframe(solution)

with tab_2:
    st.write(answer)