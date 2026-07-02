from datetime import datetime
from typing import Annotated

import questionary
import typer

from analysis import group_by_exercise, progress_for_exercise
from loader import load_sets
from plot import plot_multiple

style = questionary.Style(
    [
        ("qmark", "#7aa2f7 bold"),
        ("question", "#c0caf5 bold"),
        ("selected", "#2ac3de bold"),
        ("pointer", "#bb9af7 bold"),
    ]
)


def main(
    csv_path: Annotated[str, typer.Argument()] = "liftosaur.csv",
):
    workout_sets = load_sets(csv_path)
    workout_dict = group_by_exercise(workout_sets)
    list_of_exercises = sorted(workout_dict)

    exercises = questionary.checkbox(
        "Which exercise do you want to visualize?",
        choices=list_of_exercises,
        style=style,
    ).ask()

    if not exercises:
        raise typer.Exit(1)

    progress_dicts: dict[str, dict[datetime, float]] = {}
    for e in exercises:
        progress_dicts[e] = progress_for_exercise(workout_dict, e)

    plot_multiple(progress_dicts)


if __name__ == "__main__":
    typer.run(main)
