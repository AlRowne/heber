import typer

from analysis import group_by_exercise, progress_for_exercise
from loader import load_sets
from plot import plot_progress


def main(exercise: str, csv_path: str = "liftosaur.csv"):
    workout_sets = load_sets(csv_path)
    workout_dict = group_by_exercise(workout_sets)
    progress = progress_for_exercise(workout_dict, exercise)
    # rdl_progress = progress_for_exercise(workout_dict, "Romanian Deadlift, Barbell")
    # for day, e1rm in rdl_progress.items():
    #     print(f"Date: {day.date()}, RDL e1RM: {e1rm}")

    plot_progress(progress, f"{exercise} Progress")


if __name__ == "__main__":
    typer.run(main)
