from methods.euler_method import EulerMethod
from methods.exact_method import ExactMethod
from methods.improved_euler_method import ImprovedEulerMethod
from methods.runge_kutta_method import RungeKuttaMethod
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
    x0 = x0_entry.get()
    x = x_entry.get()
    n = n_entry.get()
    y0 = y0_entry.get()

    # checking input fields completeness
    if not is_number(x0):
        info_label.configure(text='Incorrect X0.')
        return
    if not is_number(x):
        info_label.configure(text='Incorrect X.')
        return
    if not is_number(n):
        info_label.configure(text='Incorrect N.')
        return
    if not is_number(y0):
        info_label.configure(text='Incorrect Y0.')
        return
    info_label.configure(text='')

    methods = list()

    if euler_method_flag.get():
        methods.append('Euler')
    if improved_euler_method_flag.get():
        methods.append('Improved Euler')
    if runge_kutta_method_flag.get():
        methods.append('Runge Kutta')
    if exact_method_flag.get():
        methods.append('Exact')

    if len(methods) == 0:
        info_label.configure(text='Select at least one method.')
        return

    # if all inputs are in correct form, then show the plot
    show_plot(methods)


# show window with plot, which is built from input parameters
def show_plot(methods):
    # initializing list of graphs
    result_graphs = list()
    error_graphs = list()

    # appending graphs of chosen computation methods
    for method in methods:
        if method == 'Euler':
            result_graphs.append(
                EulerMethod.get_result(float(x0_entry.get()), float(x_entry.get()), float(n_entry.get()),
                                                                    float(y0_entry.get())))
            error_graphs.append(
                EulerMethod.get_error(float(x0_entry.get()), float(x_entry.get()), float(n_entry.get()),
                                                       float(y0_entry.get())))
        elif method == 'Improved Euler':
            result_graphs.append(
                ImprovedEulerMethod.get_result(float(x0_entry.get()), float(x_entry.get()), float(n_entry.get()),
                                                            float(y0_entry.get())))
            error_graphs.append(
                ImprovedEulerMethod.get_error(float(x0_entry.get()), float(x_entry.get()), float(n_entry.get()),
                                              float(y0_entry.get())))
        elif method == 'Runge Kutta':
            result_graphs.append(
                RungeKuttaMethod.get_result(float(x0_entry.get()), float(x_entry.get()), float(n_entry.get()),
                                                         float(y0_entry.get())))
            error_graphs.append(
                RungeKuttaMethod.get_error(float(x0_entry.get()), float(x_entry.get()), float(n_entry.get()),
                                           float(y0_entry.get())))
        elif method == 'Exact':
            result_graphs.append(
                ExactMethod.get_result(float(x0_entry.get()), float(x_entry.get()), float(n_entry.get()),
                                        float(y0_entry.get())))

    # building the plot of obtained graphs and printing it as a separate window
    PlotBuilder.set_plot_of_results(result_graphs, methods)
    if 'Exact' in methods:
        methods.remove('Exact')
    PlotBuilder.set_plot_of_errors(error_graphs, methods)
    PlotBuilder.show_plots()


# creating a GUI window
window = Tk()

# filling GUI with necessary fields

window.title("Plot builder")
window.geometry('400x300')

info_label = Label(window, text='', font=("Arial", 18), fg="red")
info_label.grid(column=0, row=0, sticky="W", columnspan=2)

enter_x0_label = Label(window, text='X0:', font=("Arial", 18))
enter_x0_label.grid(column=0, row=1, sticky="W")

x0_entry = Entry(window)
x0_entry.grid(column=0, row=2, sticky="W")

enter_x_label = Label(window, text='X:', font=("Arial", 18))
enter_x_label.grid(column=0, row=3, sticky="W")

x_entry = Entry(window)
x_entry.grid(column=0, row=4, sticky="W")

enter_y0_label = Label(window, text='Y0:', font=("Arial", 18))
enter_y0_label.grid(column=0, row=5, sticky="W")

y0_entry = Entry(window)
y0_entry.grid(column=0, row=6, sticky="W")

enter_n_label = Label(window, text='N:', font=("Arial", 18))
enter_n_label.grid(column=0, row=7, sticky="W")

n_entry = Entry(window)
n_entry.grid(column=0, row=8, sticky="W")

mathods_label = Label(window, text='Methods:', font=("Arial", 18))
mathods_label.grid(column=1, row=1, sticky="W")

euler_method_flag = BooleanVar()
euler_check_button = Checkbutton(window, text='Euler', font=("Arial", 18), variable=euler_method_flag)
euler_check_button.grid(column=1, row=2, sticky="W")

improved_euler_method_flag = BooleanVar()
improved_euler_check_button = Checkbutton(window, text='Improved Euler', font=("Arial", 18),
                                          variable=improved_euler_method_flag)
improved_euler_check_button.grid(column=1, row=3, sticky="W")

runge_kutta_method_flag = BooleanVar()
runge_kutta_check_button = Checkbutton(window, text='Runge Kutta', font=("Arial", 18), variable=runge_kutta_method_flag)
runge_kutta_check_button.grid(column=1, row=4, sticky="W")

exact_method_flag = BooleanVar()
exact_method_check_button = Checkbutton(window, text='Exact', font=("Arial", 18), variable=exact_method_flag)
exact_method_check_button.grid(column=1, row=5, sticky="W")

plot_button = Button(window, text='Plot', font=("Arial", 18), command=on_plot_button_clicked)
plot_button.grid(column=1, row=8, sticky="E")

window.mainloop()