import matplotlib.pyplot as plt


class PlotBuilder:

    @staticmethod
    def set_plot(curves, legend, window_id, title):
        plt.figure(window_id)
        for points in curves:
            plt.plot(points[0], points[1])
        plt.ylabel('Y axis')
        plt.xlabel('X axis')
        plt.legend(legend, loc='upper left')
        plt.gcf().canvas.set_window_title(title)

    @staticmethod
    def set_plot_of_results(curves, legend):
        plt.close(1)
        PlotBuilder.set_plot(curves, legend, 1, 'Results')

    @staticmethod
    def set_plot_of_errors(curves, legend):
        if curves is None:
            raise Exception('\'Curves\' argument is none')
        if legend is None:
            raise Exception('\'Legend\' argument is none')
        if len(curves) < len(legend):
            raise Exception('Not enough legend for curves')
        if len(curves) > len(curves):
            raise Exception('Not enough curves for legend')

        plt.close(2)

        if len(curves) == 0:
            return

        PlotBuilder.set_plot(curves, legend, 2, 'Errors')

    @staticmethod
    def show_plots():
        plt.show()