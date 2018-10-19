from calculator import Calculator
from plot_builder import PlotBuilder
from tkinter import *


def is_number(line):
    if len(line) == 0:
        return False
    parts = line.split('.')
    if len(parts) > 2:
        return False
    if len(parts[0]) == 0:
        return False
    if line[0] == '-' and len(parts[0]) == 1:
        return False
    for c in line:
        if c != '-' and not c.isdigit() and c != '.':
            return False
    return True


def plot_button_clicked():
    a = a_entry.get()
    b = b_entry.get()
    h = h_entry.get()
    y0 = y0_entry.get()

    if not is_number(a):
        info_label.configure(text='Incorrect A.')
        return
    if not is_number(b):
        info_label.configure(text='Incorrect B.')
        return
    if not is_number(h):
        info_label.configure(text='Incorrect H.')
        return
    if not is_number(y0):
        info_label.configure(text='Incorrect Y0.')
        return
    info_label.configure(text='')

    show_plot()


def show_plot():
    curves = list()
    curves.append(Calculator.euler_method(float(a_entry.get()), float(b_entry.get()), float(h_entry.get()), float(y0_entry.get())))
    curves.append(Calculator.improved_euler_method(float(a_entry.get()), float(b_entry.get()), float(h_entry.get()), float(y0_entry.get())))
    curves.append(Calculator.runge_kutta_method(float(a_entry.get()), float(b_entry.get()), float(h_entry.get()), float(y0_entry.get())))
    PlotBuilder.build_plot('Result', curves, ['Euler', 'Improved Euler', 'Runge Kutta'])


window = Tk()

window.title("Plot builder")
window.geometry('170x260')

enter_a_label = Label(window, text='Enter A:', font=("Arial", 18))
enter_a_label.grid(column=0, row=0)

a_entry = Entry(window)
a_entry.grid(column=0, row=1)

enter_b_label = Label(window, text='Enter B:', font=("Arial", 18))
enter_b_label.grid(column=0, row=2)

b_entry = Entry(window)
b_entry.grid(column=0, row=3)

enter_h_label = Label(window, text='Enter H:', font=("Arial", 18))
enter_h_label.grid(column=0, row=4)

h_entry = Entry(window)
h_entry.grid(column=0, row=5)

enter_y0_label = Label(window, text='Enter Y0:', font=("Arial", 18))
enter_y0_label.grid(column=0, row=6)

y0_entry = Entry(window)
y0_entry.grid(column=0, row=7)

plot_button = Button(window, text='Plot', command=plot_button_clicked)
plot_button.grid(column=0, row=8)

info_label = Label(window, text='', font=("Arial", 18))
info_label.grid(column=0, row=9)

window.mainloop()