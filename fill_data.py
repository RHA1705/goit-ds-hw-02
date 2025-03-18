'''Fill tabeles'''
from datetime import datetime
from random import randint, choice
import sqlite3
import faker


NUMBER_STUDENTS = 30
NUMBER_GROUPS = 3
LECTURES = ['Programming', 'Math', 'SQL', 'MatLab', 'Mechanics', 'ML']
NUMBER_LECTURERS = 3
NUMBER_GRADES = 20


def generate_fake_data(number_students, number_lecturers):
    '''generate data for database'''
    fake_students = []  # save student name
    fake_lecturers = [] # save lecturers names
    fake_data = faker.Faker()

    # Generyjemy listę studentów w ilości number_students
    for _ in range(number_students):
        fake_students.append(fake_data.name())

    for _ in range(number_lecturers):
        fake_lecturers.append(fake_data.name())

    return fake_students, fake_lecturers


def prepare_data(students, lecturers, groups, lectures, grades_number) -> tuple():
    '''prepare data for saving in database'''
    for_students = []
    for student in students:
        for_students.append((student, ))

    for_lecturers = []
    for lecturer in lecturers:
        for_lecturers.append((lecturer, ))

    for_groups = []
    for group in range(1, len(students) + 1):
        for_groups.append((randint(1, groups), group))

    for_lectures = []
    for lecture in lectures:
        for_lectures.append((lecture, randint(1, len(lecturers))))

    for_grades = []
    for _ in range(1, grades_number+1):
        grade_date = datetime(2023, randint(1, 12), randint(1, 28)).date()
        for student in range(1, len(students)+1):
            # Pętla za ilością studentów
            for_grades.append((randint(3, 5), grade_date, randint(1, 5), student))

    return for_students, for_lecturers, for_groups, for_lectures, for_grades


def insert_data_to_db(students, lecturers, groups, lectures, grades) -> None:
    # Створимо з'єднання з нашою БД та отримаємо об'єкт курсору для маніпуляцій з даними
    with sqlite3.connect('users.db') as con:

        cur = con.cursor()


        sql_to_students = """INSERT INTO students(student)
                               VALUES (?)"""
        cur.executemany(sql_to_students, students)


        sql_to_lecturers = """INSERT INTO lecturers(lecturer)
                               VALUES (?)"""
        cur.executemany(sql_to_lecturers, lecturers)


        sql_to_groups = """INSERT INTO groups(id, student_id)
                              VALUES (?, ?)"""
        cur.executemany(sql_to_groups, groups)


        sql_to_lectures = """INSERT INTO lectures(lecture, lecturer_id)
                              VALUES (?, ?)"""
        cur.executemany(sql_to_lectures, lectures)


        sql_to_grades = """INSERT INTO grades(grade, date_of, lecture_id, student_id)
                              VALUES (?, ?, ?, ?)"""
        cur.executemany(sql_to_grades, grades)

        # Фіксуємо наші зміни в БД
        con.commit()

if __name__ == '__main__':
    students, lecturers, groups, lectures, grades = prepare_data(*generate_fake_data(NUMBER_STUDENTS,
                                                                NUMBER_LECTURERS), NUMBER_GROUPS,
                                                                 LECTURES, NUMBER_GRADES)
    # print(companies)
    # print(employees)
    # print(posts)
    insert_data_to_db(students, lecturers, groups, lectures, grades)
