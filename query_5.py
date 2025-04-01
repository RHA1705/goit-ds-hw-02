import sqlite3
import argparse


parser = argparse.ArgumentParser()

parser.add_argument('--task', '-t', help='Please enter task title')
parser.add_argument('--user', '-u', help='Please enter user name')
args = vars(parser.parse_args())

task_title = args.get("task")
user_fullname = args.get("user")

def execute_query(sql: str, task_title, user_fullname) -> list:
    with sqlite3.connect('tasks.db') as con:
        cur = con.cursor()
        cur.execute(sql, (task_title, user_fullname))
        return cur.fetchall()

sql = """
INSERT INTO tasks(title, description, status_id, user_id)
VALUES (?, 
        NULL, 
        NULL,
        (SELECT id FROM users WHERE fullname = ?))
;
"""

print(execute_query(sql, task_title, user_fullname))
