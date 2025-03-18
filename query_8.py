import sqlite3
import argparse


parser = argparse.ArgumentParser()

parser.add_argument('--name', '-n',
                    help='Please enter lecturer full name')
args = vars(parser.parse_args())

lecturer = args.get("name")

def execute_query(sql: str, lecturer) -> list:
    with sqlite3.connect('users.db') as con:
        cur = con.cursor()
        cur.execute(sql, (lecturer,))
        return cur.fetchall()

sql = """
SELECT round(avg(g.grade), 2) avg_garde, l.lecture, lr.lecturer
FROM grades g 
	JOIN lectures l ON g.lecture_id = l.id
	JOIN groups gr ON g.student_id = gr.student_id
	JOIN lecturers lr ON l.lecturer_id = lr.id
WHERE lr.lecturer = ?
GROUP BY l.lecture
;
"""

print(execute_query(sql, lecturer))
