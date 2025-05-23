import sqlite3
import argparse


parser = argparse.ArgumentParser()

parser.add_argument('--title', '-t', help='Please enter task title')
parser.add_argument('--status', '-s', help='Please enter status name')
args = vars(parser.parse_args())

title = args.get("title")
status = args.get("status")

def execute_query(sql: str, title, status) -> list:
    with sqlite3.connect('tasks.db') as con:
        cur = con.cursor()
        cur.execute(sql, (status, title,))
        return cur.fetchall()

sql = """
UPDATE tasks
SET status_id = (SELECT id FROM status WHERE name = ?)
WHERE title = ?
;
"""

print(execute_query(sql, title, status))
