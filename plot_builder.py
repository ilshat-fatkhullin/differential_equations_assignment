import matplotlib.pyplot as plt


class PlotBuilder:

    @staticmethod
    def build_plot(title, points):
        plt.plot(points[0], points[1])
        plt.ylabel('Y axis')
        plt.xlabel('X axis')
        plt.title(title)
        plt.show()