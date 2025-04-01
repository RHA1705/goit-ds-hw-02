import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('tasks.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()

sql = """
SELECT u.fullname, COUNT(t.user_id) as number_of_tasks
FROM users u 
    LEFT JOIN tasks t ON u.id = t.user_id
GROUP BY u.id
ORDER BY number_of_tasks DESC;
"""

print(execute_query(sql))
