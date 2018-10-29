from calculator import Calculator


class EulerMethod:

    @staticmethod
    def get_result(x0, b, n, y0):
        return Calculator.compute_by_method(x0, b, n, y0, EulerMethod.function)

    @staticmethod
    def get_error(x0, b, n, y0):
        return Calculator.compute_error(x0, b, n, y0, EulerMethod.get_result)

    @staticmethod
    def function(x, y, step):
        return y + step * Calculator.get_derivative(x, y)
