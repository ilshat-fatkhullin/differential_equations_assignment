import math


# contains information about differential equation, such as derivative function and general solution, and computes all
# computation methods by implemented pattern
class Calculator:

    # returns derivative in given point
    @staticmethod
    def get_derivative(x, y):
        return -2 * y + 4 * x

    # returns constant in given point
    @staticmethod
    def constant(x0, y0):
        return (y0 - 2 * x0 + 1) / (math.e ** (-2 * x0))

    # returns set of point as a result of computation by given method
    @staticmethod
    def compute_by_method(x0, b, n, y0, method_function):
        x_rows = list()
        y_rows = list()
        y = y0
        x = x0
        step = (b - x0) / n
        while abs(b - x) >= abs(step):
            x_rows.append(x)
            y_rows.append(y)
            try:
                y = method_function(x, y, step)
            except OverflowError:
                y = y0
            x += step
        x_rows.append(x)
        y_rows.append(y)
        return [x_rows, y_rows]

    # returns set of point as a result of error computation by given method
    @staticmethod
    def compute_error(x0, b, n, y0, method):
        method_values = method(x0, b, n, y0)
        x_rows = method_values[0]
        y_rows = method_values[1]
        for i in range(len(x_rows)):
            y = Calculator.get_general_solution(x_rows[i], x0, y0)
            y_rows[i] = abs(y_rows[i] - y)
        return [x_rows, y_rows]

    # returns general solution in given point with given initial value
    @staticmethod
    def get_general_solution(x, x0, y0):
        return Calculator.constant(x0, y0) * (math.e ** (-2 * x)) + 2 * x - 1
