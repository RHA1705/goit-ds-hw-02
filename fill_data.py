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
    fake_emails = []
    fake_tasks = []
    actions = ["Fix", "Install", "Update", "Configure", "Verify", "Develop", "Test", "Optimize", "Prepare", "Implement"]
    objects = ["server", "database", "application", "software", "network", "login system", "administration panel",
               "payment module", "API", "reporting system"]
    fake_data = faker.Faker()

    for _ in range(number_users):
        fake_users.append(fake_data.name())
        fake_emails.append(fake_data.email())

    for _ in range(number_tasks):
        task = f"{random.choice(actions)} {random.choice(objects)}"
        fake_tasks.append(task)

    return fake_users, fake_emails, fake_tasks


def prepare_data(users, emails, tasks, status) -> tuple():
    '''prepare data for saving in database'''
    for_users = []
    for user, email in users:
        for_users.append((user, email, ))

    for_lecturers = []
    for task in tasks:
        for_lecturers.append((task, ))

    for_groups = []
    for group in range(1, len(students) + 1):
        for_groups.append((randint(1, groups), group))

    for_lectures = []
    for lecture in lectures:
        for_lectures.append((lecture, randint(1, len(lecturers))))



    return for_students, for_lecturers, for_groups, for_lectures, for_grades


def insert_data_to_db(users, emails, tasks, status) -> None:

    with sqlite3.connect('users.db') as con:

        cur = con.cursor()


        sql_to_users = """INSERT INTO users(user, email)
                               VALUES (?, ?)"""
        cur.executemany(sql_to_users, users, emails)


        sql_to_tasks = """INSERT INTO lecturers(task)
                               VALUES (?)"""
        cur.executemany(sql_to_tasks, tasks)


        sql_to_status = """INSERT INTO groups(status)
                              VALUES (?)"""
        cur.executemany(sql_to_status, status)


        sql_to_lectures = """INSERT INTO lectures(lecture, lecturer_id)
                              VALUES (?, ?)"""
        cur.executemany(sql_to_lectures, lectures)


        sql_to_grades = """INSERT INTO grades(grade, date_of, lecture_id, student_id)
                              VALUES (?, ?, ?, ?)"""
        cur.executemany(sql_to_grades, grades)

        # Фіксуємо наші зміни в БД
        con.commit()

if __name__ == '__main__':
    users, emails, tasks, status = prepare_data(*generate_fake_data(NUMBER_USERS, NUMBER_TASKS), STATUS)
    # print(companies)
    # print(employees)
    # print(posts)w
    insert_data_to_db(users, status, tasks)
