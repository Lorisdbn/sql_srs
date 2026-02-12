
import streamlit as st
import duckdb
import os
import logging

if "data" not in os.listdir():
    logging.error(os.listdir())
    logging.error("creating data folder")
    os.mkdir("data")

if "exo_sql_tables.duckdb" not in os.listdir("data"):
    exec(open("init_db.py").read())




con = duckdb.connect(database="data/exo_sql_tables.duckdb", read_only=False)

with st.sidebar:
    available_themes_df = con.execute("SELECT DISTINCT theme FROM memory_state").df()
    theme = st.selectbox(
        "What would you like to review?",
        available_themes_df,
        placeholder="Select a theme",
    )

    if theme:
        st.write("You selected:", theme)
        exercise=(
        con.execute(f"SELECT * FROM memory_state WHERE theme ='{theme}'")
        .df()
        .sort_values("last_reviewed")
        .reset_index()
        )
    else:
        exercise = (
        con.execute(f"SELECT * FROM memory_state")
        .df()
        .sort_values("last_reviewed")
        .reset_index()
        )

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
    exercise_table= exercise.loc[0, "tables"]
    for table in exercise_table:
        st.write(f"table :{table}")
        df_table = con.execute(f"SELECT * FROM {table}").df()
        st.dataframe(df_table)

with tab_3:
    st.write(answer)
