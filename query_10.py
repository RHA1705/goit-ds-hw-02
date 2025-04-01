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
SELECT COUNT(status_id) as Number_of_tasks, s.name
FROM tasks 
    JOIN status s ON s.id = tasks.status_id
WHERE s.name = ?
GROUP BY status_id;
"""

print(execute_query(sql, status))
