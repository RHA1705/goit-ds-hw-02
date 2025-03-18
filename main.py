import sqlite3
from random import randint
from datetime import datetime, date
from faker import Faker




NUMBER_STUDENTS = 30
NUMBER_GROUPS = 3

fake = Faker()

# Generowanie listy 20 nazw wykładów
# nazwy_wykladow = [fake.text(max_nb_chars=30) for _ in range(20)]
nazwy_wykladow = []

# Wyświetlenie wygenerowanych nazw
for _ in range(1, 6):
    nazwy_wykladow.append(fake.name())

def generate_groups(groups, students):
    for_groups = []
    for group in range(1, students + 1):
        for_groups.append((randint(1, groups), group))

    return for_groups

def generate_grades(number_students):
    for_grades = []
    for _ in range(20):
        grade_date = datetime(2023, randint(1, 12), randint(1, 28)).date()
        for student in range(1, number_students+1):
            # Pętla za ilością studentów
            for_grades.append((randint(3, 5), randint(1, 5), student, grade_date))

    return for_grades

if __name__ == '__main__':
    result = generate_groups(NUMBER_GROUPS, NUMBER_STUDENTS)
    result_2 = generate_grades(NUMBER_STUDENTS)
    print(result_2)
