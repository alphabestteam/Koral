from project1 import Project
from exercise1 import Exercise

import datetime

class Developer:
    
    def __init__(self, name: str, list_exercises_done: list, exercises_to_be_done: list, seniority = 1, reward = 0 ) -> None:
        self.name = name
        self._amount_exercises_done = list_exercises_done
        self._days_of_work = self.generate_days_of_work()
        self.seniority = self.generate_seniority()
        self._reward = reward
        self.exercises_to_be_done = exercises_to_be_done
        

    def get_name(self):
        return self.name
      
    def set_name(self, value):
        self.name = value

    def get_amount_exercises_done(self):
        return self._amount_exercises_done
      
    def set_amount_exercises_done(self, value):
        self._amount_exercises_done = value

    def get_days_of_work(self):
        return self._days_of_work
      
    def set_seniority(self, value):
        self.seniority = value

    def get_seniority(self):
        return self.seniority
      
    def set_days_of_work(self, value):
        self.days_of_work = value

    def get_reward(self):
        return self._reward
      
    def set_reward(self, value):
        self._reward = value

    def get_exercises_to_be_done(self):
        return self.exercises_to_be_done
      
    def set_exercises_to_be_done(self, value):
        self.exercises_to_be_done = value


    def generate_days_of_work(self) -> int:
        # The function will calculate the amount of days the worker worked
        days = 0
        
        for exercise in self.list_exercises_done:
            days += exercise.get_days_of_work()

        for exercise in self.exercises_to_be_done:

            if self.exercises_to_be_done == None or len(self.exercises_to_be_done) == 0:
                return days
            
            elif datetime.date.now() > exercise.get_start_date():
                days += datetime.date.now() - exercise.get_start_date()

        return days



    def generate_seniority(self) -> int:
        # The function will generate the seniority of the worker according to the complexity of the tasks he finished , and will update his reward by that exercise
        
        seniority = 0

        for exercise in self.list_exercises_done:
            seniority += exercise.get_complexity()
            self.reward += exercise.get_reward()

        return seniority


