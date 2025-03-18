import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('users.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()

sql = """
SELECT round(avg(g.grade), 2) as avr_grade 
FROM grades as g 
;
"""
result = execute_query(sql)[0]
result = list(result)
print(f'Avarage grade = {result[0]}')
