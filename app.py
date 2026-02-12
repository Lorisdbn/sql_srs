
import streamlit as st
import duckdb
import ast

con = duckdb.connect(database="data/exo_sql_tables.duckdb", read_only=False)

with st.sidebar:
    theme = st.selectbox(
        "What would you like to review?",
        ("cross_joins", "GroupBy", "window_functions"),
        placeholder="Select a theme",
    )
    st.write("You selected:", theme)

    exercise=con.execute(f"SELECT * FROM memory_state WHERE theme ='{theme}'").df()
    st.write(exercise)

    exercise_name = exercise.loc[0, "exercise_name"]
    with open(f"answers/{exercise_name}.sql","r") as f:
        answer = f.read()

    solution_df = con.execute(answer).df()

st.title("SQL Playground 🚀")

st.header("enter your code here:")
sql_query = st.text_area(label="Input text", key="input1")

if sql_query:
    result = con.execute(sql_query).df()
    st.dataframe(result)

try:
    result = result[solution_df.columns]
    st.dataframe(result.compare(solution_df))
except KeyError:
    st.write("Columns number does not match")


n_lines_difference = result.shape[0] - solution_df.shape[0]

if n_lines_difference != 0:
    st.write(
        f"Your result has a {n_lines_difference} lines difference with the solution_df"
    )


tab_2, tab_3 = st.tabs(["Tables", "Solution"])

with tab_2:
    exercise_table= ast.literal_eval(exercise.loc[0, "tables"])
    for table in exercise_table:
        st.write(f"table :{table}")
        df_table = con.execute(f"SELECT * FROM {table}").df()
        st.dataframe(df_table)

with tab_3:
    st.write(answer)
