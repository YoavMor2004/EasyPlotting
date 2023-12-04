from Plot import Plot


class AxesPlot(Plot):
    def __init__(self, title: str, xlabel: str, ylabel: str, dir_path: str | None = None):
        super().__init__(title, xlabel, ylabel, dir_path)

        self.ax.axvline(0, color='k')
        self.ax.axhline(0, color='k')
