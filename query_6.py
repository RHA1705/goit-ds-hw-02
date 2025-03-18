import sqlite3
import argparse


parser = argparse.ArgumentParser()

parser.add_argument('--group', '-g',
                    help='Please enter group number')
args = vars(parser.parse_args())

group = args.get("group")

def execute_query(sql: str, group) -> list:
    with sqlite3.connect('users.db') as con:
        cur = con.cursor()
        cur.execute(sql, (group,))
        return cur.fetchall()

sql = """
SELECT s.student
FROM groups g
	JOIN students s ON g.student_id = s.id
WHERE g.id = ?
;
"""

print(execute_query(sql, group))
