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


def plot_multiple(progress_dicts: dict[str, dict[datetime, float]]):
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
