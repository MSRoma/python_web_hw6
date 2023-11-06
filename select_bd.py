import sqlite3


def execute_query(sql: str) -> list:

    with open(sql, 'r') as f:
        sql = f.read()


    with sqlite3.connect('salary.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        result = cur.fetchall()
        return print(result)
    
if __name__ == "__main__":
    execute_query("query_number1.sql")