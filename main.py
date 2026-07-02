from datetime import datetime
from typing import Annotated

import questionary
import typer

from analysis import group_by_exercise, progress_for_exercise
from loader import load_sets
from plot import plot_grid, plot_single

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
        "Which exercise(s) do you want to visualize?",
        choices=list_of_exercises,
        style=style,
    ).ask()
    if not exercises:
        raise typer.Exit(1)

    plot_style = questionary.select(
        "Which plot style do you want to show?",
        choices=[
            questionary.Choice(title="Single Axis (overlay)", value="single"),
            questionary.Choice(title="Grid (one per exercise)", value="grid"),
        ],
        style=style,
    ).ask()
    if plot_style is None:
        raise typer.Exit(1)

    progress_dicts: dict[str, dict[datetime, float]] = {}
    for e in exercises:
        progress_dicts[e] = progress_for_exercise(workout_dict, e)

    if plot_style == "single":
        plot_single(progress_dicts)
    elif plot_style == "grid":
        plot_grid(progress_dicts)


if __name__ == "__main__":
    typer.run(main)
