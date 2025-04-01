import sqlite3
import argparse


parser = argparse.ArgumentParser()

parser.add_argument('--email', '-e', help='Please enter email address')
args = vars(parser.parse_args())

email = args.get("email")

def execute_query(sql: str, email) -> list:
    with sqlite3.connect('tasks.db') as con:
        cur = con.cursor()
        cur.execute(sql, (email,))
        return cur.fetchall()

sql = """
SELECT *
FROM users
WHERE email = ?
;
"""

print(execute_query(sql, email))
