class Calculator:

    @staticmethod
    def f(x, y):
        return ((y * (2 * x + 1)) / x) - x

    @staticmethod
    def euler_method(a, b, h, y_0):
        x_rows = list()
        y_rows = list()
        y = y_0
        x = a
        while x <= b:
            x_rows.append(x)
            y_rows.append(y)
            y += h * Calculator.f(x, y)
            x += h
        x_rows.append(x)
        y_rows.append(y)
        return [x_rows, y_rows]

    @staticmethod
    def improved_euler_method(a, b, h, y_0):
        rows = list()
        y = y_0
        x = a
        while x <= b:
            rows.append(y)
            y += (h / 2) * (Calculator.f(x, y) + Calculator.f(x + h, y + h * Calculator.f(x, y)))
            x += h
        rows.append(y)
        return rows

    @staticmethod
    def runge_kutta_method(a, b, h, y_0):
        rows = list()
        y = y_0
        x = a
        while x <= b:
            rows.append(y)
            k_1 = Calculator.f(x, y)
            k_2 = Calculator.f(x + h / 2, y + (h / 2) * k_1)
            k_3 = Calculator.f(x + h / 2, y + (h / 2) * k_2)
            k_4 = Calculator.f(x + h, y + h * k_3)
            y += (h / 6) * (k_1 + 2 * k_2 + 2 * k_3 + k_4)
            x += h
        rows.append(y)
        return rows