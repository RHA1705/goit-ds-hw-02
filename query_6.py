import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('tasks.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()

sql = """
SELECT *
FROM tasks
WHERE status_id IN (SELECT id FROM status WHERE name NOT LIKE 'complete')
;
"""

print(execute_query(sql))
