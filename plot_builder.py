import matplotlib.pyplot as plt


class PlotBuilder:

    @staticmethod
    def build_plot(curves, legend):
        plt.close()
        for points in curves:
            plt.plot(points[0], points[1])
        plt.ylabel('Y axis')
        plt.xlabel('X axis')
        plt.legend(legend, loc='upper left')
        plt.gcf().canvas.set_window_title('Result')
        plt.show()