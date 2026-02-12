
import duckdb
import pandas as pd

con = duckdb.connect(database="data/exo_sql_tables.duckdb", read_only=False)


# ------------------------------------------------------------
# EXERCISES LIST
# ------------------------------------------------------------

data = {
    "theme": ["cross_joins","cross_joins"],
    "exercise_name": ["beverages_and_food","sizes_and_trademark"],
    "tables": [["beverages", "food"], ["size", "trademark"]],
    "last_reviewed": ["1990-01-01","1970-01-01"],
}
memory_state_df = pd.DataFrame(data)
con.execute("DROP TABLE IF EXISTS memory_state")
con.execute("CREATE TABLE memory_state AS SELECT * FROM memory_state_df")



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

size = pd.DataFrame(
    {
        "size": ["XS","S","M","L","XL"]
    }
)

con.execute("CREATE TABLE IF NOT EXISTS size AS SELECT * FROM size")

trademark = pd.DataFrame(
    {
        "trademark": ["Nike","Abercrombie","Lewis","Asphalte"]
    }
)

con.execute("CREATE TABLE IF NOT EXISTS trademark AS SELECT * FROM trademark")

con.close()