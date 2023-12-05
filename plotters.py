import numpy as np
from matplotlib import pyplot as plt


def small_scatter(ax: plt.Axes, ch_x: np.ndarray, ch_y: np.ndarray, label: str) -> None:
    ax.plot(ch_x, ch_y, marker='.', ls='', label=label)


def big_scatter(ax: plt.Axes, ch_x: np.ndarray, ch_y: np.ndarray, label: str) -> None:
    ax.plot(ch_x, ch_y, marker='o', ls='', label=label)


def line_plot(ax: plt.Axes, ch_x: np.ndarray, ch_y: np.ndarray, label: str) -> None:
    ax.plot(ch_x, ch_y, label=label)
