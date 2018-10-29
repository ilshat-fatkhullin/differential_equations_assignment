import math
from calculation_exceptions import UndefinedDomainException


# contains information about differential equation, such as derivative function and general solution, and computes all
# computation methods by implemented pattern
class Calculator:
    # if computation method's value goes outside of this range, it returns back to initial value
    clamping_range = 100

    # returns cubic root with correct sign
    @staticmethod
    def get_cubic_root(value):
        if value < 0:
            return -(-value) ** (1. / 3.)
        else:
            return value ** (1. / 3.)

    # returns cubic degree
    @staticmethod
    def get_cubic_degree(value):
        return value * value * value

    # returns square degree
    @staticmethod
    def get_square_degree(value):
        return value * value

    # returns derivative in given point
    @staticmethod
    def get_derivative(x, y):
        if math.cos(x) == 0:
            raise UndefinedDomainException()
        return (y ** 4) * math.cos(x) + y * math.tan(x)

    # returns constant in given point
    @staticmethod
    def constant(x0, y0):
        return 1 / (Calculator.get_cubic_degree(y0) * Calculator.get_cubic_degree(math.cos(x0))) + 3 * math.tan(x0)

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
                if abs(y) > Calculator.clamping_range:
                    y = y0
            except UndefinedDomainException:
                y = y0
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
            try:
                y = Calculator.get_general_solution(x_rows[i], x0, y0)
            except UndefinedDomainException:
                y_rows[i] = float('inf')
                continue
            y_rows[i] = abs(y_rows[i] - y)
        return [x_rows, y_rows]

    # returns general solution in given point with given initial value
    @staticmethod
    def get_general_solution(x, x0, y0):
        if Calculator.is_particular_case(y0):
            return 0

        if Calculator.is_discontinuity_point(x, x0, y0):
            raise UndefinedDomainException()

        return 1 / Calculator.get_cubic_root(
            Calculator.constant(x0, y0) * Calculator.get_cubic_degree(math.cos(x)) - 3 * math.sin(
                x) * Calculator.get_square_degree(math.cos(x)))

    # checks whether given initial value is particular case or not
    @staticmethod
    def is_particular_case(y0):
        return y0 == 0

    # checks whether given point yields discontinuity or not
    @staticmethod
    def is_discontinuity_point(x, x0, y0):
        if math.cos(x0) == 0:
            return True

        if math.tan(x) + Calculator.constant(x0, y0) == 0:
            return True

        return False
