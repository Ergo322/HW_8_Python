import csv
import os.path
import view

def find_surname(surname):
    if os.path.exists('data.csv'):
        with open('data.csv', 'r', encoding='utf-8') as dt:
            reader = csv.reader(dt)
            sum_list = []
            for row in reader:
                if len(row) != 0:
                    sum_list.append(row[0].split(';'))
            count = 0
            for item in sum_list:
                if surname == item[0]:
                    view.answer(item)
                    count+=1
            if count == 0:
                view.answer(f'{surname} не найден!')
    else:
        view.answer('Файл не найден!')

def find_name2(name):
    if os.path.exists('data.csv'):
        with open('data.csv', 'r', encoding='utf-8') as dt:
            reader = csv.reader(dt)
            sum_list = []
            for row in reader:
                if len(row) != 0:
                    sum_list.append(row[0].split(';'))
            count = 0
            for item in sum_list:
                if find_name2() == item[1]:
                    view.answer(item)
                    count+=1
            if count == 0:
                view.answer(f'Человек с  отчеством {find_name2()} не найден!')
    else:
        view.answer('Файл не найден!')

def find_occupation(occup):
    if os.path.exists('data.csv'):
        with open('data.csv', 'r', encoding='utf-8') as dt:
            reader = csv.reader(dt)
            sum_list = []
            for row in reader:
                if len(row) != 0:
                    sum_list.append(row[0].split(';'))
            count = 0
            for item in sum_list:
                if ocupp() == item[3]:
                    view.answer(item)
                    count+=1
            if count == 0:
                view.answer(f'Человек с должностью {occup} не найден!')
    else:
        view.answer('Файл не найден!')
