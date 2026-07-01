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


def plot_progress(progress_dict: dict[datetime, float], title: str):
    x = list(progress_dict.keys())
    y = list(progress_dict.values())
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(x, y, marker="o", color="#7aa2f7", markerfacecolor="#bb9af7", linewidth=2)  # type: ignore
    ax.set_title(title)
    ax.set_xlabel("Date")
    ax.set_ylabel("e1RM (kg)")
    ax.grid(True)

    fig.autofmt_xdate()
    fig.tight_layout()
    plt.show()
