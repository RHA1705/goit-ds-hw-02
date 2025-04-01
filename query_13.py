import sqlite3
import argparse


parser = argparse.ArgumentParser()

parser.add_argument('--status', '-s', help='Please enter status name')
args = vars(parser.parse_args())

status = args.get("status")

def execute_query(sql: str, status) -> list:
    with sqlite3.connect('tasks.db') as con:
        cur = con.cursor()
        cur.execute(sql, (status,))
        return cur.fetchall()

sql = """
SELECT u.fullname, t.title, s.name
FROM users u
INNER JOIN tasks t ON u.id = t.user_id
INNER JOIN status s ON s.id = t.status_id
WHERE s.name = ?
;
"""

print(execute_query(sql, status))
