import sqlite3
import json


def execute_query(sql: str) -> list:

    with open(sql, 'r') as f:
        sql = f.read()


    with sqlite3.connect('salary.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        result = cur.fetchall()
        return print(result)
    
if __name__ == "__main__":
    execute_query("query_1.sql")
    # execute_query("query_2.sql")
    # execute_query("query_3.sql")
    # execute_query("query_4.sql")
    # execute_query("query_5.sql")
    # execute_query("query_6.sql")
    # execute_query("query_7.sql")
    # execute_query("query_8.sql")
    # execute_query("query_9.sql")
    # execute_query("query_10.sql")
   