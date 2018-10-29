from calculator import *


class ImprovedEulerMethod:

    @staticmethod
    def get_result(x0, b, n, y0):
        return Calculator.compute_by_method(x0, b, n, y0, ImprovedEulerMethod.function)

    @staticmethod
    def get_error(x0, b, n, y0):
        return Calculator.compute_error(x0, b, n, y0, ImprovedEulerMethod.get_result)

    @staticmethod
    def function(x, y, step):
        return y + (step / 2) * (Calculator.get_derivative(x, y) + Calculator.get_derivative(x + step,
                                                                                             y + step * Calculator.get_derivative(
                                                                                                 x, y)))
