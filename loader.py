import csv
from datetime import datetime

from workoutset import WorkoutSet


def load_sets(csv_path: str) -> list[WorkoutSet]:

    workout_list: list[WorkoutSet] = []
    with open(csv_path, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if (
                row["Is Warmup Set?"] == "1"
                or row["Completed Reps"] == ""
                or row["Completed Weight Value"] == ""
            ):
                continue
            date = datetime.fromisoformat(row["Workout DateTime"])
            program: str = row["Program"]
            day_name: str = row["Day Name"]
            exercise: str = row["Exercise"]
            reps: int = int(row["Completed Reps"])
            if row["Required Weight Unit"] == "lb":
                weight_kg = float(row["Completed Weight Value"]) * 0.4536
            else:
                weight_kg = float(row["Completed Weight Value"])
            target_muscles: str = row["Target Muscles"]
            synergist_muscles: str = row["Synergist Muscles"]

            workout_set = WorkoutSet(
                date=date,
                program=program,
                day_name=day_name,
                exercise=exercise,
                reps=reps,
                weight_kg=weight_kg,
                target_muscles=target_muscles,
                synergist_muscles=synergist_muscles,
            )
            workout_list.append(workout_set)

    return workout_list
