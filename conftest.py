from datetime import datetime

import pytest

from workoutset import WorkoutSet


@pytest.fixture
def make_set():
    """WorkoutSet factory with defaults"""

    def _make(exercise="Squat", reps=5, weight_kg=100.0, date=None):
        return WorkoutSet(
            date=date or datetime(2026, 1, 1),
            program="TestProgram",
            day_name="TestDay",
            exercise=exercise,
            reps=reps,
            weight_kg=weight_kg,
            target_muscles="Quads",
            synergist_muscles="Glutes",
        )

    return _make
