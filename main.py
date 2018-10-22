from calculator import Calculator
from plot_builder import PlotBuilder
from tkinter import *


# returns True, if input parameter is number and False otherwise
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


# event handler on play button click
def on_plot_button_clicked():
    # getting values from input fields
    a = a_entry.get()
    b = b_entry.get()
    h = step_entry.get()
    y0 = y0_entry.get()

    # checking input fields completeness
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

    # if all inputs are in correct form, then show the plot
    show_plot()


# show window with plot, which is built from input parameters
def show_plot():
    # initializing list of graphs
    graphs = list()
    # appending graphs of each computation method
    graphs.append(Calculator.euler_method(float(a_entry.get()), float(b_entry.get()), float(step_entry.get()), float(y0_entry.get())))
    graphs.append(Calculator.improved_euler_method(float(a_entry.get()), float(b_entry.get()), float(step_entry.get()), float(y0_entry.get())))
    graphs.append(Calculator.runge_kutta_method(float(a_entry.get()), float(b_entry.get()), float(step_entry.get()), float(y0_entry.get())))
    # building the plot of obtained graphs and printing it as a separate window
    PlotBuilder.build_plot(graphs, ['Euler', 'Improved Euler', 'Runge Kutta'])


# creating a GUI window
window = Tk()

# filling GUI with necessary fields

window.title("Plot builder")
window.geometry('170x260')

enter_a_label = Label(window, text='Enter x0:', font=("Arial", 18))
enter_a_label.grid(column=0, row=0)

a_entry = Entry(window)
a_entry.grid(column=0, row=1)

enter_b_label = Label(window, text='Enter x:', font=("Arial", 18))
enter_b_label.grid(column=0, row=2)

b_entry = Entry(window)
b_entry.grid(column=0, row=3)

enter_y0_label = Label(window, text='Enter y0:', font=("Arial", 18))
enter_y0_label.grid(column=0, row=4)

y0_entry = Entry(window)
y0_entry.grid(column=0, row=5)

enter_step_label = Label(window, text='Enter step:', font=("Arial", 18))
enter_step_label.grid(column=0, row=6)

step_entry = Entry(window)
step_entry.grid(column=0, row=7)

plot_button = Button(window, text='Plot', command=on_plot_button_clicked)
plot_button.grid(column=0, row=8)

info_label = Label(window, text='', font=("Arial", 18))
info_label.grid(column=0, row=9)

window.mainloop()