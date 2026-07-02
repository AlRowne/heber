import pytest


def test_e1rm(make_set):
    workout_set = make_set(weight_kg=180, reps=9)
    assert workout_set.e1rm == pytest.approx(234)


def test_e1rm_single(make_set):
    ws = make_set(weight_kg=180, reps=1)
    assert ws.e1rm == pytest.approx(180 * (1 + 1 / 30))
