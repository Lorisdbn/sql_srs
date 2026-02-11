
import streamlit as st
import duckdb

con = duckdb.connect(database="data/exo_sql_tables.duckdb", read_only=False)
# answer_str = "SELECT * FROM df_food CROSS JOIN  df_beverages"
# solution_df = duckdb.sql(answer_str).df()


with st.sidebar:
    theme = st.selectbox(
        "What would you like to review?",
        ("cross_joins", "GroupBy", "window_functions"),
        placeholder="Select a theme",
    )
    st.write("You selected:", theme)

    exercise=con.execute(f"SELECT * FROM memory_state WHERE theme ='{theme}'").df()
    st.write(exercise)

st.title("SQL Playground 🚀")

st.header("enter your code here:")
sql_query = st.text_area(label="Input text", key="input1")

# if sql_query:
#     result = duckdb.query(sql_query).df()
#     st.write(f"you entered the following query : {sql_query}")
#     st.dataframe(result)
#
# try:
#     result = result[solution_df.columns]
#     st.dataframe(result.compare(solution_df))
# except KeyError:
#     st.write("Columns number does not match")
#
# tab_1, tab_2 = st.tabs(["Tables", "solution_df"])
#
# with tab_1:
#     st.write(df_beverages)
#     st.write(df_food)
#     st.write("expected:")
#     st.dataframe(solution_df)
#
# with tab_2:
#     st.write(answer_str)
