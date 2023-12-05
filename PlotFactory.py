from typing import Self

from EasyPlotting import Plot, AxesPlot


class PlotFactory:
    dir_path: str
    axes: bool

    def __init__(self, dir_path: str, axes: bool = False):
        self.dir_path = dir_path
        self.axes = axes

    def set_axes(self, axes: bool) -> Self:
        self.axes = axes
        return self

    def get_plot(self, title: str, xlabel: str, ylabel: str) -> Plot:
        if self.axes:
            return AxesPlot(title, xlabel, ylabel, self.dir_path)
        return Plot(title, xlabel, ylabel, self.dir_path)
