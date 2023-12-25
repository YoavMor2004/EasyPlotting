from typing import Optional, Callable

import numpy as np
from numpy import ndarray
from matplotlib import pyplot as plt


def small_scatter(ax: plt.Axes, ch_x: np.ndarray, ch_y: np.ndarray, label: str | None, color: Optional[str]) -> str:
    return ax.plot(ch_x, ch_y, marker='.', ls='', label=label, color=color)[0].get_color()


def line_plot(ax: plt.Axes, ch_x: np.ndarray, ch_y: np.ndarray, label: str | None, color: Optional[str]) -> str:
    return ax.plot(ch_x, ch_y, label=label, color=color)[0].get_color()


def dashed_line_plot(ax: plt.Axes, ch_x: np.ndarray, ch_y: np.ndarray, label: str | None, color: Optional[str]) -> str:
    return ax.plot(ch_x, ch_y, ls='--', label=label, color=color)[0].get_color()


def null_plot(ax: plt.Axes, ch_x: np.ndarray, ch_y: np.ndarray, label: str | None, color: Optional[str]) -> str:
    if color is None:
        return 'k'
    return color


def table_plotter(
        plotter: Callable[[plt.Axes, ndarray, ndarray, Optional[str], Optional[str]], str]
) -> Callable[[plt.Axes, ndarray, ndarray, Optional[str], Optional[str]], str]:
    def plot(ax: plt.Axes, ch_x: ndarray, ch_y: ndarray, label: Optional[str], color: Optional[str]) -> str:
        color: str

        color = plotter(ax, ch_x, ch_y, label, color)
        i: int
        for i in range(len(ch_x)):
            print(f'{ch_x[i]:f}\t{ch_y[i]:f}')
        print()
        return color

    return plot


def big_scatter(ax: plt.Axes, ch_x: np.ndarray, ch_y: np.ndarray, label: str | None, color: Optional[str]) -> str:
    return ax.plot(ch_x, ch_y, marker='o', ls='', label=label, color=color)[0].get_color()
