
import duckdb
import pandas as pd

con = duckdb.connect(database="data/exo_sql_tables.duckdb", read_only=False)


# ------------------------------------------------------------
# EXERCISES LIST
# ------------------------------------------------------------

data = {
    "theme": ["cross_joins","window_functions"],
    "exercise_name": ["beverages_and_food","simple_window"],
    "tables": [["beverages", "food"], "simple_window"],
    "last_reviewed": ["1980-01-01","1980-01-01"],
}
memory_state_df = pd.DataFrame(data)
con.execute("CREATE TABLE IF NOT EXISTS memory_state AS SELECT * FROM memory_state_df")


# ------------------------------------------------------------
# CROSS JOIN EXERCISES
# ------------------------------------------------------------

beverages = pd.DataFrame(
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
con.execute("CREATE TABLE IF NOT EXISTS beverages AS SELECT * FROM beverages")

food = pd.DataFrame(
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


con.execute("CREATE TABLE IF NOT EXISTS food AS SELECT * FROM food")
