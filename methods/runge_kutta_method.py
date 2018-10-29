from calculator import *


class RungeKuttaMethod:

    @staticmethod
    def get_result(x0, b, n, y0):
        return Calculator.compute_by_method(x0, b, n, y0, RungeKuttaMethod.function)

    @staticmethod
    def get_error(x0, b, n, y0):
        return Calculator.compute_error(x0, b, n, y0, RungeKuttaMethod.get_result)

    @staticmethod
    def function(x, y, step):
        k_1 = Calculator.get_derivative(x, y)
        k_2 = Calculator.get_derivative(x + step / 2, y + (step / 2) * k_1)
        k_3 = Calculator.get_derivative(x + step / 2, y + (step / 2) * k_2)
        k_4 = Calculator.get_derivative(x + step, y + step * k_3)
        return y + (step / 6) * (k_1 + 2 * k_2 + 2 * k_3 + k_4)