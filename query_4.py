import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('tasks.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()

sql = """
SELECT *
FROM users
WHERE id NOT IN (SELECT user_id FROM tasks) 
;
"""

print(execute_query(sql))
