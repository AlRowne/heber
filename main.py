from typing import Annotated

import typer
from rich import print

from analysis import group_by_exercise, progress_for_exercise
from loader import load_sets
from plot import plot_progress


def main(
    exercise: Annotated[str | None, typer.Argument()] = None,
    csv_path: Annotated[str, typer.Argument()] = "liftosaur.csv",
):
    workout_sets = load_sets(csv_path)
    workout_dict = group_by_exercise(workout_sets)
    list_of_exercises = sorted(workout_dict)

    if exercise not in list_of_exercises:
        if exercise is None:
            print("No exercise provided, use one of these:")
        else:
            print("Exercise not found, use one of these:")
        print(list_of_exercises)
        raise typer.Exit(code=1)

    progress = progress_for_exercise(workout_dict, exercise)
    plot_progress(progress, f"{exercise} Progress")


if __name__ == "__main__":
    typer.run(main)
