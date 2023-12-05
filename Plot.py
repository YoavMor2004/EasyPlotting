from typing import Callable, Self

import matplotlib.pyplot as plt
import numpy as np
from numpy import ndarray
from scipy.stats import linregress

from EasyPlotting import plotters, util

AXES_TITLE_FONT_SIZE: int | None = None


default_plotter = plotters.small_scatter


class Plot:
    fig:        plt.Figure
    ax:         plt.Axes
    dir_path:   str | None
    plotter:    Callable[[plt.Axes, ndarray, ndarray, str | None], str]

    # noinspection SpellCheckingInspection
    def __init__(self, title: str, xlabel: str, ylabel: str, dir_path: str | None):
        self.fig, self.ax = plt.subplots()
        self.fig.tight_layout(rect=(0.1, 0.1, 1, 0.9))
        self.fig.suptitle(title)
        self.ax.set_xlabel(xlabel, fontsize=AXES_TITLE_FONT_SIZE)
        self.ax.set_ylabel(ylabel, fontsize=AXES_TITLE_FONT_SIZE)
        self.ax.grid()

        self.dir_path = dir_path

        self.plotter = default_plotter

    def plot(self, ch_x: ndarray, ch_y: ndarray, label: str = None) -> str:
        return self.plotter(self.ax, ch_x, ch_y, label=label)

    def dashed_line(self, slope: float, intercept: float, anchor_x: float, *, color: str | None = None) -> None:
        self.ax.axline((anchor_x, intercept + slope * anchor_x), slope=slope, ls='--', color=color)

    # noinspection SpellCheckingInspection
    def linregress(self, ch_x: np.ndarray, ch_y: np.ndarray, label: str = None) -> None:
        color: str

        linregress_result = linregress(ch_x, ch_y)

        color = self.plot(ch_x, ch_y, label)
        self.dashed_line(linregress_result.slope, linregress_result.intercept, float(ch_x[0]), color=color)
        self.set_axes_title(util.get_equation(linregress_result))

    def set_axes_title(self, title: str) -> None:
        self.ax.set_title(title)

    def save_fig(self, path: str) -> None:
        self.ax.legend()
        if self.dir_path is None:
            self.fig.savefig(path)
            return
        self.fig.savefig(rf'{self.dir_path}\{path}')

    def set_plotter(self, plotter: Callable[[plt.Axes, ndarray, ndarray, str | None], None]) -> Self:
        self.plotter = plotter
        return self
