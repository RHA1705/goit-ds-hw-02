import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('tasks.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()

sql = """
SELECT *
FROM tasks 
WHERE description IS NULL
;
"""

print(execute_query(sql))
