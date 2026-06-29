from datetime import datetime

import matplotlib.pyplot as plt


def plot_progress(progress_dict: dict[datetime, float], title: str):
    x = list(progress_dict.keys())
    y = list(progress_dict.values())

    plt.plot(x, y)  # type: ignore[arg-type]
    plt.title(title)
    plt.xlabel("Date")
    plt.ylabel("e1RM (kg)")
    plt.show()
