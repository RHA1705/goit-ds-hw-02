import sqlite3
import argparse


parser = argparse.ArgumentParser()

parser.add_argument('--lecture', '-l', help='Please enter lecture from the list: Programming, Math, SQL, MatLab, Mechanics, ML')
parser.add_argument('--group', '-g', help='Please enter group number')
args = vars(parser.parse_args())

lecture = args.get("lecture")
group = args.get("group")

def execute_query(sql: str, lecture, group) -> list:
    with sqlite3.connect('users.db') as con:
        cur = con.cursor()
        cur.execute(sql, (lecture, group, ))
        return cur.fetchall()

sql = """
SELECT g.grade, l.lecture, gr.id as gr, s.student
FROM grades g 
	JOIN lectures l ON g.lecture_id = l.id
	JOIN groups gr ON g.student_id = gr.student_id
	JOIN students s ON g.student_id = s.id
WHERE l.lecture = ? AND gr.id = ?
;
"""

print(execute_query(sql, lecture, group))
