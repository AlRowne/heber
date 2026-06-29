from collections import defaultdict
from datetime import datetime

from workoutset import WorkoutSet


def group_by_exercise(workout_list: list[WorkoutSet]) -> dict[str, list[WorkoutSet]]:
    exercise_dict = defaultdict(list)
    for workout_set in workout_list:
        exercise_dict[workout_set.exercise].append(workout_set)

    return exercise_dict


def progress_for_exercise(
    workout_dict: dict[str, list[WorkoutSet]], exercise: str
) -> dict[datetime, float]:
    exercise_dict: defaultdict[datetime, list[WorkoutSet]] = defaultdict(list)
    e1rm_dict: dict[datetime, float] = {}

    for workout_set in workout_dict[exercise]:
        exercise_dict[workout_set.date].append(workout_set)
    for day, workout_sets in exercise_dict.items():
        best_e1rm = max(s.e1rm for s in workout_sets)
        e1rm_dict[day] = round(best_e1rm, 1)

    return dict(sorted(e1rm_dict.items()))
