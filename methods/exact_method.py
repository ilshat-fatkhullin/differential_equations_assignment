from calculator import *


class ExactMethod:

    @staticmethod
    def get_result(x0, b, n, y0):
        x = x0
        step = (b - x0) / n

        x_rows = list()
        y_rows = list()

        while abs(b - x) >= abs(step):
            y = Calculator.get_general_solution(x, x0, y0)
            x_rows.append(x)
            y_rows.append(y)
            x += step

        return [x_rows, y_rows]
