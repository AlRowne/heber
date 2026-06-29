from typing import Annotated

import questionary
import typer
from prompt_toolkit.shortcuts.prompt import CompleteStyle
from rich import print

from analysis import group_by_exercise, progress_for_exercise
from loader import load_sets
from plot import plot_progress

style = questionary.Style(
    [
        ("completion-menu.completion", "bg:#292e42"),
        ("completion-menu.completion.current", "bg:#7aa2f7 #1a1b26 bold"),
        ("completion-menu.meta.completion", "bg:#414868 #a9b1d6"),
        ("scrollbar.button", "bg:#565f89"),
        ("scrollbar.background", "bg:#414868"),
        ("qmark", "#7aa2f7 bold"),
        ("question", "#c0caf5 bold"),
        ("answer", "#c0caf5 bold"),
        ("selected", "fg:#1a1b26 bold"),
        ("pointer", "#bb9af7"),
    ]
)


def main(
    csv_path: Annotated[str, typer.Argument()] = "liftosaur.csv",
):
    workout_sets = load_sets(csv_path)
    workout_dict = group_by_exercise(workout_sets)
    list_of_exercises = sorted(workout_dict)

    exercise = questionary.autocomplete(
        "Which exercise do you want to visualize?",
        choices=list_of_exercises,
        validate=lambda x: x in list_of_exercises,
        complete_style=CompleteStyle.MULTI_COLUMN,
        style=style,
    ).ask()

    if exercise is None:
        raise typer.Exit(1)

    progress = progress_for_exercise(workout_dict, exercise)
    plot_progress(progress, f"{exercise} Progress")


if __name__ == "__main__":
    typer.run(main)
