import numpy as np
from matplotlib import pyplot as plt


def small_scatter(ax: plt.Axes, ch_x: np.ndarray, ch_y: np.ndarray, label: str | None) -> str:
    return ax.plot(ch_x, ch_y, marker='.', ls='', label=label)[0].get_color()


def big_scatter(ax: plt.Axes, ch_x: np.ndarray, ch_y: np.ndarray, label: str | None) -> str:
    return ax.plot(ch_x, ch_y, marker='o', ls='', label=label)[0].get_color()


def line_plot(ax: plt.Axes, ch_x: np.ndarray, ch_y: np.ndarray, label: str | None) -> str:
    return ax.plot(ch_x, ch_y, label=label)[0].get_color()


def dashed_line_plot(ax: plt.Axes, ch_x: np.ndarray, ch_y: np.ndarray, label: str | None) -> str:
    return ax.plot(ch_x, ch_y, ls='--', label=label)[0].get_color()
