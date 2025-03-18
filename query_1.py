import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('users.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()

sql = """
SELECT round(avg(g.grade), 2) as avr_grade, s.student 
FROM grades as g 
LEFT JOIN students as s ON g.student_id = s.id
GROUP BY s.student
ORDER BY avr_grade DESC
LIMIT 5;
"""

print(execute_query(sql))
