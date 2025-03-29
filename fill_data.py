'''Fill tabeles'''
from datetime import datetime
from random import randint, choice
import sqlite3
import faker
import random


NUMBER_USERS = 30
NUMBER_TASKS = 50
STATUS = ['new', 'in progress', 'completed']


def generate_fake_data(number_users, number_tasks):
    '''generate data for database'''
    fake_users = []
    fake_tasks = []
    actions = ["Fix", "Install", "Update", "Configure", "Verify", "Develop", "Test", "Optimize", "Prepare", "Implement"]
    objects = ["server", "database", "application", "software", "network", "login system", "administration panel",
               "payment module", "API", "reporting system"]

    fake_data = faker.Faker()

    for user in range(number_users):

        fake_users.append((fake_data.name(), fake_data.email()))


    for _ in range(number_tasks):
        task_title = f"{random.choice(actions)} {random.choice(objects)}"
        fake_tasks.append(task_title)

    return fake_users, fake_tasks


def prepare_data(users, tasks, status) -> tuple():
    '''prepare data for saving in database'''
    descriptions = ["Requires post-completion testing.",
                    "Log check required after implementation.",
                    "Changes should be consulted with the IT team.",
                    "Possible compatibility issues, requires thorough analysis.",
                    "Urgent task - high risk of failure."]
    for_users = []
    for user in users:
        for_users.append((user, ))

    for_tasks = []
    for task in tasks:
        for_tasks.append((task, choice(descriptions), randint(0, len(STATUS)+1), randint(1, NUMBER_USERS)+1), )

    for_status = []
    for s in status:
        for_status.append((s,))

    print(for_users)
    print(for_tasks)
    return for_users, for_tasks, for_status


def insert_data_to_db(users, tasks, status) -> None:

    with sqlite3.connect('tasks.db') as con:

        cur = con.cursor()


        sql_to_users = """INSERT INTO users(fullname, email)
                               VALUES (?, ?)"""
        cur.executemany(sql_to_users, users)


        sql_to_tasks = """INSERT INTO tasks(title, description, status_id, user_id)
                               VALUES (?, ?, ?, ?)"""
        cur.executemany(sql_to_tasks, tasks)


        sql_to_status = """INSERT INTO status(name)
                              VALUES (?)"""
        cur.executemany(sql_to_status, status)

        # Фіксуємо наші зміни в БД
        con.commit()

if __name__ == '__main__':
    users, tasks, status = prepare_data(*generate_fake_data(NUMBER_USERS, NUMBER_TASKS), STATUS)
    # print(companies)
    # print(employees)
    # print(posts)w
    insert_data_to_db(users, tasks, status)
