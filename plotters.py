from typing import Optional

import numpy as np
from matplotlib import pyplot as plt


def small_scatter(ax: plt.Axes, ch_x: np.ndarray, ch_y: np.ndarray, label: str | None, color: Optional[str]) -> str:
    return ax.plot(ch_x, ch_y, marker='.', ls='', label=label, color=color)[0].get_color()


def big_scatter(ax: plt.Axes, ch_x: np.ndarray, ch_y: np.ndarray, label: str | None, color: Optional[str]) -> str:
    return ax.plot(ch_x, ch_y, marker='o', ls='', label=label, color=color)[0].get_color()


def line_plot(ax: plt.Axes, ch_x: np.ndarray, ch_y: np.ndarray, label: str | None, color: Optional[str]) -> str:
    return ax.plot(ch_x, ch_y, label=label, color=color)[0].get_color()


def dashed_line_plot(ax: plt.Axes, ch_x: np.ndarray, ch_y: np.ndarray, label: str | None, color: Optional[str]) -> str:
    return ax.plot(ch_x, ch_y, ls='--', label=label, color=color)[0].get_color()


def null_plot(ax: plt.Axes, ch_x: np.ndarray, ch_y: np.ndarray, label: str | None, color: Optional[str]) -> str:
    if color is None:
        return 'k'
    return color
