import math
from calculation_exceptions import UndefinedDomainException


class Calculator:
    clamp_range = 100

    @staticmethod
    def cube_root(value):
        if value < 0:
            return -(-value) ** (1. / 3.)
        else:
            return value ** (1. / 3.)

    @staticmethod
    def cube_degree(value):
        return value * value * value

    @staticmethod
    def square_degree(value):
        return value * value

    @staticmethod
    def get_derivative(x, y):
        if math.cos(x) == 0:
            raise UndefinedDomainException()
        return (y ** 4) * math.cos(x) + y * math.tan(x)

    @staticmethod
    def constant(x0, y0):
        return 1 / (Calculator.cube_degree(y0) * Calculator.cube_degree(math.cos(x0))) + 3 * math.tan(x0)

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
                if abs(y) > Calculator.clamp_range:
                    y = y0
            except UndefinedDomainException:
                y = y0
            except OverflowError:
                y = y0
            x += step
        x_rows.append(x)
        y_rows.append(y)
        return [x_rows, y_rows]

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

    @staticmethod
    def get_general_solution(x, x0, y0):
        if Calculator.is_particular_case(y0):
            return 0

        if Calculator.is_discontinuity_point(x, x0, y0):
            raise UndefinedDomainException()

        return 1 / Calculator.get_general_solution_denominator(x, x0, y0)

    @staticmethod
    def get_general_solution_denominator(x, x0, y0):
        return Calculator.cube_root(
            Calculator.constant(x0, y0) * Calculator.cube_degree(math.cos(x)) - 3 * math.sin(
                x) * Calculator.square_degree(math.cos(x)))

    @staticmethod
    def is_particular_case(y0):
        return y0 == 0

    @staticmethod
    def is_discontinuity_point(x, x0, y0):
        if math.cos(x0) == 0:
            return True

        if math.tan(x) + Calculator.constant(x0, y0) == 0:
            return True

        return False