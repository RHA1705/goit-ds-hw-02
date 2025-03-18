import sqlite3
import argparse


parser = argparse.ArgumentParser()

parser.add_argument('--name', '-n',
                    help='Please enter student full name')
args = vars(parser.parse_args())

student = args.get("name")

def execute_query(sql: str, student) -> list:
    with sqlite3.connect('users.db') as con:
        cur = con.cursor()
        cur.execute(sql, (student,))
        return cur.fetchall()

sql = """
SELECT l.lecture
FROM lectures l 
	JOIN grades g ON g.lecture_id = l.id
	JOIN students s ON g.student_id = s.id
WHERE s.student = ?
GROUP BY g.lecture_id
;
"""

print(execute_query(sql, student))
