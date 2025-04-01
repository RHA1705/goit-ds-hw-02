import sqlite3
import argparse


parser = argparse.ArgumentParser()

parser.add_argument('--status', '-s', help='Please enter task status')
args = vars(parser.parse_args())

status = args.get("status")

def execute_query(sql: str, status) -> list:
    with sqlite3.connect('tasks.db') as con:
        cur = con.cursor()
        cur.execute(sql, (status,))
        return cur.fetchall()

sql = """
SELECT *
FROM tasks
WHERE status_id IN (SELECT id 
                    FROM status 
                    WHERE name = ?)
;
"""

print(execute_query(sql, status))
