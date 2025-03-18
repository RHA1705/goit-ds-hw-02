import sqlite3
import argparse


parser = argparse.ArgumentParser()

parser.add_argument('--lecture', '-l', help='Please enter lecture from the list: Programming, Math, SQL, MatLab, Mechanics, ML')
args = vars(parser.parse_args())

lecture = args.get("lecture")

def execute_query(sql: str, lecture) -> list:
    with sqlite3.connect('users.db') as con:
        cur = con.cursor()
        cur.execute(sql, (lecture,))
        return cur.fetchall()

sql = """
SELECT ROUND(AVG(g.grade), 2) as avg_grade, l.lecture, s.student
FROM grades g 
	JOIN lectures l ON g.lecture_id = l.id 
	JOIN students s ON g.student_id = s.id 
WHERE l.lecture = ?
GROUP BY s.student 
ORDER BY avg_grade DESC 
LIMIT 1
;
"""

print(execute_query(sql, lecture))
