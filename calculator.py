class Calculator:

    # string representation of function, which is used in computation methods
    function_string = '((y * (2 * x + 1)) / x) - x'

    @staticmethod
    def f(x, y):
        return eval(Calculator.function_string)

    @staticmethod
    def euler_method(a, b, step, y_0):
        x_rows = list()
        y_rows = list()
        y = y_0
        x = a
        while x <= b:
            x_rows.append(x)
            y_rows.append(y)
            y += step * Calculator.f(x, y)
            x += step
        x_rows.append(x)
        y_rows.append(y)
        return [x_rows, y_rows]

    @staticmethod
    def improved_euler_method(a, b, step, y_0):
        x_rows = list()
        y_rows = list()
        y = y_0
        x = a
        while x <= b:
            x_rows.append(x)
            y_rows.append(y)
            y += (step / 2) * (Calculator.f(x, y) + Calculator.f(x + step, y + step * Calculator.f(x, y)))
            x += step
        x_rows.append(x)
        y_rows.append(y)
        return [x_rows, y_rows]

    @staticmethod
    def runge_kutta_method(a, b, step, y_0):
        x_rows = list()
        y_rows = list()
        y = y_0
        x = a
        while x <= b:
            x_rows.append(x)
            y_rows.append(y)
            k_1 = Calculator.f(x, y)
            k_2 = Calculator.f(x + step / 2, y + (step / 2) * k_1)
            k_3 = Calculator.f(x + step / 2, y + (step / 2) * k_2)
            k_4 = Calculator.f(x + step, y + step * k_3)
            y += (step / 6) * (k_1 + 2 * k_2 + 2 * k_3 + k_4)
            x += step
        x_rows.append(x)
        y_rows.append(y)
        return [x_rows, y_rows]