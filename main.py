import csv
from calculator import Calculator
import matplotlib.pyplot as plt

def analyze(a, b, h, y_0, file_name):
    columns = list()
    columns.append(Calculator.euler_method(a, b, h, y_0))
    columns.append(Calculator.improved_euler_method(a, b, h, y_0))
    columns.append(Calculator.runge_kutta_method(a, b, h, y_0))
    rows = list()
    rows.append(['X', 'Euler', 'Improved Euler', 'Runge Kutta'])
    x = 2
    for i in range(len(columns[0])):
        row = list()
        row.append(round(x, 2))
        for j in range(len(columns)):
            row.append(round(columns[j][i], 2))
        x += h
        rows.append(row)
    sw = csv.writer(open(file_name, 'w'))
    sw.writerows(rows)