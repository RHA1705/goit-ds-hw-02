import sqlite3
import argparse


parser = argparse.ArgumentParser()

parser.add_argument('--old', '-o', help='Please enter user old name')
parser.add_argument('--new', '-n', help='Please enter user new name')
args = vars(parser.parse_args())

old_name = args.get("old")
new_name = args.get("new")

def execute_query(sql: str, old_name, new_name) -> list:
    with sqlite3.connect('tasks.db') as con:
        cur = con.cursor()
        cur.execute(sql, (new_name, old_name))
        return cur.fetchall()

sql = """
UPDATE users
SET fullname = ?
WHERE fullname = ?
;
"""

print(execute_query(sql, old_name, new_name))
