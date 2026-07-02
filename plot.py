import math
from datetime import datetime

import matplotlib.pyplot as plt

TOKYO_NIGHT = {
    "figure.facecolor": "#1a1b26",
    "axes.facecolor": "#1a1b26",
    "axes.edgecolor": "#414868",
    "axes.labelcolor": "#c0caf5",
    "axes.titlecolor": "#c0caf5",
    "text.color": "#c0caf5",
    "xtick.color": "#c0caf5",
    "ytick.color": "#c0caf5",
    "grid.color": "#414868",
    "grid.alpha": 0.3,
}
plt.rcParams.update(TOKYO_NIGHT)  # type: ignore[arg-type]


def plot_single(progress_dicts: dict[str, dict[datetime, float]]):
    fig, ax = plt.subplots(figsize=(12, 6))

    for exercise, progress_dict in progress_dicts.items():
        x = list(progress_dict.keys())
        y = list(progress_dict.values())
        ax.plot(x, y, marker="o", linewidth=2, label=exercise)  # pyright: ignore

    ax.set_title("Progress")
    ax.set_xlabel("Date")
    ax.set_ylabel("e1RM (kg)")
    ax.grid(True)
    ax.legend()

    fig.autofmt_xdate()
    fig.tight_layout()
    plt.show()


def plot_grid(progress_dicts: dict[str, dict[datetime, float]]):
    n = len(progress_dicts)
    ncols = 1 if n == 1 else 2
    nrows = math.ceil(n / ncols)

    fig, axes = plt.subplots(nrows=nrows, ncols=ncols, squeeze=False)

    for ax, (exercise, progress_dict) in zip(axes.flatten(), progress_dicts.items()):
        x = list(progress_dict.keys())
        y = list(progress_dict.values())

        ax.plot(x, y, marker="o", label=exercise)
        ax.set_title(exercise)
        ax.set_xlabel("Date")
        ax.set_ylabel("e1RM (kg)")
        ax.grid(True)
        ax.tick_params(axis="x", rotation=45)

    for ax in axes.flatten()[n:]:
        ax.set_visible(False)

    fig.tight_layout()
    plt.show()
