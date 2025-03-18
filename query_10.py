import sqlite3
import argparse


parser = argparse.ArgumentParser()

parser.add_argument('--student', '-s',
                    help='Please enter student full name')
parser.add_argument('--lecturer', '-l',
                    help='Please enter lecturer full name')
args = vars(parser.parse_args())

student = args.get("student")
lecturer = args.get("lecturer")

def execute_query(sql: str, student, lecturer) -> list:
    with sqlite3.connect('users.db') as con:
        cur = con.cursor()
        cur.execute(sql, (student, lecturer,))
        return cur.fetchall()

sql = """
SELECT l.lecture
FROM lectures l 
	JOIN grades g ON g.lecture_id = l.id
	JOIN students s ON g.student_id = s.id
	JOIN lecturers lr ON l.lecturer_id = lr.id
WHERE s.student = ? AND lr.lecturer = ?
GROUP BY l.lecture
;
"""

print(execute_query(sql, student, lecturer))
