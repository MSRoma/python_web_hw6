from datetime import datetime
import faker
import random
from random import randint, choice
import sqlite3

NUMBER_STUDENTS = 50
NUMBER_TEACHERS = 5
NUMBER_GROUPS = 3
NUMBER_SUBJECTS = 8
NUMBER_GRADES = 20

def generate_fake_data(number_students, number_teachers, number_groups,number_subjects,number_grades) -> tuple():
    fake_students = []  # тут зберігатимемо компанії
    fake_teachers = []  # тут зберігатимемо співробітників
    fake_groups = []  # тут зберігатимемо посади
    fake_subjects = []  # тут зберігатимемо посади
    fake_grades = []  # тут зберігатимемо посади
    '''Візьмемо три компанії з faker і помістимо їх у потрібну змінну'''
    fake_data = faker.Faker((['uk-UA']))

    # Створимо набір компаній у кількості number_companies
    for _ in range(number_students):
        fake_students.append(fake_data.name())

    # Згенеруємо тепер number_employees кількість співробітників'''
    for _ in range(number_teachers):
        fake_teachers.append(fake_data.name())

    # Та number_post набір посад
    for _ in range(number_groups):
        fake_groups.append(fake_data.safe_color_name())
    
    # Та number_post набір посад
    for _ in range(number_subjects):
        fake_subjects.append(fake_data.job())

    for _ in range(number_grades):
        fake_grades.append(fake_data.random_int(min=1,max = 5))

    return fake_students, fake_teachers, fake_groups, fake_subjects ,fake_grades

students, teachers, groups ,subjects, grades = generate_fake_data(NUMBER_STUDENTS, NUMBER_TEACHERS, NUMBER_GROUPS,NUMBER_SUBJECTS,NUMBER_GRADES)
print(students)
print(teachers)
print(groups)
print(subjects)
print(grades)

def prepare_data(students, teachers, groups ,subjects, grades) -> tuple():
    for_groups = []
    # Готуємо список кортежів назв компаній
    for group in groups:
        for_groups.append((group, ))

    for_students = []  # для таблиці employees

    for std in students:
        '''
        Для записів у таблицю співробітників нам потрібно додати посаду та id компанії. Компаній у нас було за замовчуванням
        NUMBER_COMPANIES, при створенні таблиці companies для поля id ми вказували INTEGER AUTOINCREMENT - тому кожен
        запис отримуватиме послідовне число збільшене на 1, починаючи з 1. Тому компанію вибираємо випадково
        у цьому діапазоні
        '''
        for_students.append((std, randint(1, NUMBER_GROUPS)))

    '''
    Подібні операції виконаємо й у таблиці payments виплати зарплат. Приймемо, що виплата зарплати у всіх компаніях
    виконувалася з 10 по 20 числа кожного місяця. Діапазон зарплат генеруватимемо від 1000 до 10000 у.о.
    для кожного місяця, та кожного співробітника.
    '''
    for_teachers = []

    for teach in teachers:
        for_teachers.append((teach, ))

    for_subjects = []

    for sub in subjects:
        for_subjects.append((sub, randint(1, NUMBER_TEACHERS) ))
    
    grades = []

    for i in range(NUMBER_STUDENTS+1):
        # Виконуємо цикл за місяцями'''
        for_grades = 
        for _ in range(20):
            start_date = datetime.date(year=2015, month=1, day=1)
            end_date = datetime.date(year=2016, month=1, day=1)
            fake_date = fake.date_between(start_date=start_date, end_date=end_date)
      
            # Виконуємо цикл за кількістю співробітників
            for_grades.append((i, payment_date, randint(1000, 10000)))

    return for_companies, for_employees, for_payments