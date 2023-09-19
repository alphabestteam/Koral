from project import Project
from exercise import Exercise

class Developer:
    def __init__(self, name: str, amount_exercises_done: int, days_of_work: int, reword: int, exercises_to_be_done: list, seniority = 1) -> None:
        self.name = name
        self._amount_exercises_done = amount_exercises_done
        self._days_of_work = days_of_work
        self.reword = reword
        self.exercises_to_be_done = exercises_to_be_done
        self.seniority = seniority
        pass