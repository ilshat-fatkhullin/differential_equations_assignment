import matplotlib.pyplot as plt


class PlotBuilder:

    @staticmethod
    def build_plot(title, curves, legend):
        for points in curves:
            plt.plot(points[0], points[1])
        plt.ylabel('Y axis')
        plt.xlabel('X axis')
        plt.legend(legend, loc='upper left')
        plt.title(title)
        plt.show()