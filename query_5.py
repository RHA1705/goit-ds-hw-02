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
SELECT l.lecture, lr.lecturer
FROM lectures l
	JOIN lecturers lr ON l.lecturer_id = lr.id
WHERE lr.lecturer = ?
;
"""

print(execute_query(sql, lecturer))
