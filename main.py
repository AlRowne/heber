from analysis import group_by_exercise, progress_for_exercise
from loader import load_sets


def main():
    workout_sets = load_sets("liftosaur.csv")
    workout_dict = group_by_exercise(workout_sets)

    rdl_progress = progress_for_exercise(workout_dict, "Romanian Deadlift, Barbell")
    for day, e1rm in rdl_progress.items():
        print(f"Date: {day.date()}, RDL e1RM: {e1rm}")


if __name__ == "__main__":
    main()
