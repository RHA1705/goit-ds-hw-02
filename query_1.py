import sqlite3
import argparse


parser = argparse.ArgumentParser()

parser.add_argument('--name', '-n', help='Please enter username')
args = vars(parser.parse_args())

name = args.get("name")

def execute_query(sql: str, name) -> list:
    with sqlite3.connect('tasks.db') as con:
        cur = con.cursor()
        cur.execute(sql, (name,))
        return cur.fetchall()

sql = """
SELECT *
FROM tasks as t 
    LEFT JOIN users as u ON u.id = t.user_id
WHERE u.fullname LIKE ?
;
"""

print(execute_query(sql, name))
