import sqlite3
import argparse


parser = argparse.ArgumentParser()

parser.add_argument('--id', type=int, required=True, help='Please enter task id')
args = vars(parser.parse_args())

task_id = args.get("id")

def execute_query(sql: str, task_id: int):
    with sqlite3.connect('tasks.db') as con:
        cur = con.cursor()
        cur.execute(sql, (task_id,))
        con.commit()
        print("Task deleted successfully")

sql = """
DELETE FROM tasks
WHERE id = ?
;
"""

print(execute_query(sql, task_id))
