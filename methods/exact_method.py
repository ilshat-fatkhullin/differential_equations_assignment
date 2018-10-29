from calculator import *


class ExactMethod:

    @staticmethod
    def get_result(x0, b, n, y0):
        x = x0
        points = []
        step = (b - x0) / n

        while abs(b - x) >= abs(step):
            try:
                y = Calculator.get_general_solution(x, x0, y0)
            except UndefinedDomainException:
                x += step
                continue
            points.append((x, y))
            x += step

        undefined_points = ExactMethod.get_undefined_points(x0, b)
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
    def get_undefined_points(x0, b):
        start = min(x0, b)
        end = max(x0, b)
        k_start = int(math.ceil(start / math.pi))
        k_end = int(math.floor(end / math.pi))
        points = []
        for k in range(k_start, k_end + 1):
            points.append((k * math.pi + math.pi / 2, math.inf))

        return points
