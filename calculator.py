import math
from calculation_exceptions import UndefinedDomainException


class Calculator:

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
    def f(x, y):
        if math.cos(x) == 0:
            raise UndefinedDomainException()
        return (y ** 4) * math.cos(x) + y * math.tan(x)

    @staticmethod
    def F(x, x0, y0):
        if Calculator.is_particular_case(y0):
            return 0

        if Calculator.is_undefined_case(x, x0, y0):
            raise UndefinedDomainException()

        return 1 / Calculator.F_denominator(x, x0, y0)

    @staticmethod
    def is_particular_case(y0):
        return y0 == 0

    @staticmethod
    def is_undefined_case(x, x0, y0):
        if math.cos(x0) == 0:
            return True

        if math.tan(x) + Calculator.constant(x0, y0) == 0:
            return True

        return False

    @staticmethod
    def constant(x0, y0):
        return 1 / (Calculator.cube_degree(y0) * Calculator.cube_degree(math.cos(x0))) + 3 * math.tan(x0)

    @staticmethod
    def F_denominator(x, x0, y0):
        return Calculator.cube_root(
            Calculator.constant(x0, y0) * Calculator.cube_degree(math.cos(x)) - 3 * math.sin(
                x) * Calculator.square_degree(math.cos(x)))

    @staticmethod
    def compute_by_method(x_0, b, step, y_0, method_function):
        x_rows = list()
        y_rows = list()
        y = y_0
        x = x_0
        while x <= b:
            x_rows.append(x)
            y_rows.append(y)
            try:
                y = method_function(x, y, step)
            except UndefinedDomainException:
                return [x_rows, y_rows]
            except OverflowError:
                return [x_rows, y_rows]
            x += step
        x_rows.append(x)
        y_rows.append(y)
        return [x_rows, y_rows]

    @staticmethod
    def euler_method(x0, b, step, y0):
        return Calculator.compute_by_method(x0, b, step, y0, Calculator.euler_function)

    @staticmethod
    def euler_function(x, y, step):
        return y + step * Calculator.f(x, y)

    @staticmethod
    def improved_euler_method(x0, b, step, y0):
        return Calculator.compute_by_method(x0, b, step, y0, Calculator.improved_euler_function)

    @staticmethod
    def improved_euler_function(x, y, step):
        return y + (step / 2) * (Calculator.f(x, y) + Calculator.f(x + step, y + step * Calculator.f(x, y)))

    @staticmethod
    def runge_kutta_method(x0, b, step, y0):
        return Calculator.compute_by_method(x0, b, step, y0, Calculator.runge_kutta_function)

    @staticmethod
    def runge_kutta_function(x, y, step):
        k_1 = Calculator.f(x, y)
        k_2 = Calculator.f(x + step / 2, y + (step / 2) * k_1)
        k_3 = Calculator.f(x + step / 2, y + (step / 2) * k_2)
        k_4 = Calculator.f(x + step, y + step * k_3)
        return y + (step / 6) * (k_1 + 2 * k_2 + 2 * k_3 + k_4)

    @staticmethod
    def exact_method(x0, b, step, y0):
        x = x0
        points = []

        while x <= b:
            try:
                y = Calculator.F(x, x0, y0)
            except UndefinedDomainException:
                x += step
                continue
            points.append((x, y))
            x += step

        undefined_points = Calculator.get_undefined_points(x0, b, y0)
        for p in undefined_points:
            points.append(p)

        points.sort()

        x_rows = list()
        y_rows = list()

        for p in points:
            x_rows.append(p[0])
            y_rows.append(p[1])

        return [x_rows, y_rows]

    @staticmethod
    def get_undefined_points(x0, b, y0):
        k_start = int(math.ceil(x0 / (math.pi / 2)))
        k_end = int(math.floor(b / (math.pi / 2)))
        points = []
        for k in range(k_start, k_end + 1):
            points.append((k * (math.pi / 2), math.inf))

        if Calculator.is_particular_case(y0):
            return points

        offset = math.atan(Calculator.constant(x0, y0) / 3)
        k_start = int(math.ceil(x0 / math.pi))
        k_end = int(math.floor(b / math.pi))
        for k in range(k_start, k_end + 1):
            points.append((k * math.pi + offset, math.inf))

        return points
