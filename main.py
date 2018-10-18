from calculator import Calculator
from plot_builder import PlotBuilder
from tkinter import *


def plot_button_clicked():
    a = a_entry.get()
    b = b_entry.get()
    h = h_entry.get()
    y0 = y0_entry.get()

    if not a.isdigit():
        info_label.configure(text='Incorrect A.')
        return
    if not b.isdigit():
        info_label.configure(text='Incorrect B.')
        return
    if not h.isdigit():
        info_label.configure(text='Incorrect H.')
        return
    if not y0.isdigit():
        info_label.configure(text='Incorrect Y0.')
        return
    info_label.configure(text='')

    show_plot()


def show_plot():
    result = Calculator.euler_method(2, 4, 0.5, 0)
    PlotBuilder.build_plot('Euler method', result)


window = Tk()

window.title("Plot builder")
window.geometry('500x500')

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