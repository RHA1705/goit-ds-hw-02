import sqlite3
import argparse


parser = argparse.ArgumentParser()

parser.add_argument('--domain', '-d', help='Please enter domain of user email')
args = vars(parser.parse_args())

domain = args.get("domain")

def execute_query(sql: str, domain) -> list:
    with sqlite3.connect('tasks.db') as con:
        cur = con.cursor()
        cur.execute(sql, (f"%{domain}",))
        return cur.fetchall()

sql = """
SELECT *
FROM tasks t 
    JOIN users u ON t.user_id = u.id
WHERE u.email LIKE ?
"""

print(execute_query(sql, domain))
