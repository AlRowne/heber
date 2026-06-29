from dataclasses import dataclass
from datetime import datetime


@dataclass
class WorkoutSet:
    date: datetime
    program: str
    day_name: str
    exercise: str
    reps: int
    weight_kg: float
    target_muscles: str
    synergist_muscles: str

    @property
    def e1rm(self) -> float:
        return self.weight_kg * (1 + self.reps / 30)
