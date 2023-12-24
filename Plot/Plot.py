from typing import Callable, Self, Optional

import matplotlib.pyplot as plt
import numpy as np
from numpy import ndarray
from scipy.optimize import curve_fit
from scipy.stats import linregress

from EasyPlotting import plotters, util

AXES_TITLE_FONT_SIZE: int | None = None


default_plotter = plotters.small_scatter


class Plot:
    fig:        plt.Figure
    ax:         plt.Axes
    dir_path:   Optional[str]
    plotter:    Callable[[plt.Axes, ndarray, ndarray, Optional[str], Optional[str]], str]
    fit_curve:  Optional[Callable[[float | ndarray, ...], float | ndarray]]
    curve_str:  Optional[str]

    # noinspection SpellCheckingInspection
    def __init__(self, title: str, xlabel: str, ylabel: str, dir_path: str | None):
        self.fig, self.ax = plt.subplots()
        self.fig.tight_layout(rect=(0.1, 0.1, 1, 0.9))
        self.fig.suptitle(title)
        self.ax.set_xlabel(xlabel, fontsize=AXES_TITLE_FONT_SIZE)
        self.ax.set_ylabel(ylabel, fontsize=AXES_TITLE_FONT_SIZE)
        self.ax.grid(which='both')

        self.dir_path = dir_path

        self.plotter = default_plotter
        self.fit_curve = None
        self.curve_str = None

    def plot(self, ch_x: ndarray, ch_y: ndarray, label: Optional[str] = None, color: Optional[str] = None) -> str:
        return self.plotter(self.ax, ch_x, ch_y, label, color)

    def dashed_line(self, slope: float, intercept: float, anchor_x: float, *, color: Optional[str] = None) -> None:
        self.ax.axline((anchor_x, intercept + slope * anchor_x), slope=slope, ls='--', color=color)

    def draw_line(self, slope: float, intercept: float, anchor_x: float, *,
                  label: Optional[str] = None, color: Optional[str] = None) -> None:
        self.ax.axline((anchor_x, intercept + slope * anchor_x), slope=slope, color=color, label=label)

    def draw_vertical_line(self, anchor_x: float, *, label: Optional[str] = None, color: Optional[str] = None) -> None:
        self.ax.axvline(anchor_x, label=label, color=color)

    def set_curve_fit(self, fit_curve: Callable[[float | ndarray, ...], float | ndarray], curve_str: str) -> Self:
        self.fit_curve = fit_curve
        self.curve_str = curve_str
        return self

    def reset_curve_fit(self) -> Self:
        self.fit_curve = None
        self.curve_str = None
        return self

    def curve_fit(self, ch_x: ndarray, ch_y: ndarray, label: Optional[str] = None) -> None:
        color: str
        parameter_values: list[float]
        prev_plotter: Callable[[plt.Axes, ndarray, ndarray, Optional[str], Optional[str]], str]

        if self.fit_curve is None:
            return self.linregress(ch_x, ch_y, label)

        prev_plotter = self.get_plotter()
        color = self.plot(ch_x, ch_y, label)
        parameter_values = curve_fit(self.fit_curve, ch_x, ch_y, maxfev=int(10e6))[0]
        print(parameter_values)
        ch_x = np.linspace(min(ch_x), max(ch_x), 1000)
        self.set_plotter(plotters.dashed_line_plot).plot(ch_x, self.fit_curve(ch_x, *parameter_values), label, color)
        self.set_axes_title(self.curve_str.format(*parameter_values))
        self.set_plotter(prev_plotter)


    def set_axes_title(self, title: str) -> None:
        self.ax.set_title(title)

    def save_fig(self, path: str) -> None:
        self.ax.legend()
        if self.dir_path is None:
            self.fig.savefig(path)
            return
        self.fig.savefig(rf'{self.dir_path}\{path}')

    def get_plotter(self) -> Callable[[plt.Axes, ndarray, ndarray, Optional[str], Optional[str]], str]:
        return self.plotter

    def set_plotter(self, plotter: Callable[[plt.Axes, ndarray, ndarray, str | None], str]) -> Self:
        self.plotter = plotter
        return self

    # noinspection SpellCheckingInspection
    def linregress(self, ch_x: np.ndarray, ch_y: np.ndarray, label: str = None) -> None:
        color: str

        linregress_result = linregress(ch_x, ch_y)

        color = self.plot(ch_x, ch_y, label)
        self.dashed_line(linregress_result.slope, linregress_result.intercept, float(ch_x[0]), color=color)
        self.set_axes_title(util.get_equation(linregress_result))
