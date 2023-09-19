from project import Project
from developer import Developer

import datetime

class Exercise:

    def __init__(self, description: str, start_date: datetime, project: Project, days_of_work: int, complexity: int, which_dev = None) -> None:
        self.description = description
        self.start_date = start_date
        self.project = project
        self.days_of_work = days_of_work

        if complexity < 1 or complexity > 5 :
            raise Exception("The Complexity Need To Be Between 1 And 5 !")
        self.complexity = complexity

        self.complexity = self.complexity_is_validate()
        self.which_dev = which_dev
        self.finished = self.exercise_finished()
        self.reward = self._generate_reward()
        self.end_date = self._generate_end_time()


    def get_description(self):
        return self.description
      
    def set_description(self, value):
        self.description = value

    def get_start_date(self):
        return self.start_date
      
    def set_start_date(self, value):
        self.start_date = value

    def get_project(self):
        return self.project
      
    def set_project(self, value):
        self.project = value

    def get_days_of_work(self):
        return self.days_of_work
      
    def set_days_of_work(self, value):
        self.days_of_work = value

    def get_complexity(self):
        return self.complexity
      
    def set_complexity(self, value):
        self.complexity = value

    def get_which_dev(self):
        return self.which_dev
      
    def set_which_dev(self, value):
        self.which_dev = value

    def get_finished(self):
        return self.finished
      
    def set_finished(self, value):
        self.finished = value

    def get_reward(self):
        return self.reward
      
    def set_reward(self, value):
        self.reward = value

    def get_end_date(self):
        return self.end_date
      
    def set_end_date(self, value):
        self.end_date = value

        
    def __str__(self) -> str:
        return f"The exercise is: {self.description}"



    def _generate_end_time(self) -> datetime:
        # The function will return the end date for the project

        year = self.start_time.year
        month = self.start_time.month
        day = self.start_time.day

        sum_of_days = self.days_of_work + day

        if month == 2 and sum_of_days >= 28:

            if month + sum_of_days // 28 >= 12:
                if (month + sum_of_days) // 28 == 12:
                    year += 1
                else:
                    year += (month + sum_of_days // 28) // 12
            if sum_of_days == 28:
                month += 1
                day = 1
            if sum_of_days > 28:
                month += sum_of_days // 28
                day = sum_of_days - 28

        elif (month == 4 or month == 6 or month == 9 or month == 11) and sum_of_days >= 30:

            if month + sum_of_days // 30 >= 12:
                if (month + sum_of_days) // 30 == 12:
                    year += 1
                else:
                    year += (month + sum_of_days // 30) // 12
            if sum_of_days == 30:
                month += 1
                day = 1
            if sum_of_days > 30:
                month += sum_of_days // 30
                day = sum_of_days - 30

        elif (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12) and sum_of_days >= 31:
            if month + sum_of_days // 31 >= 12:
                if (month + sum_of_days) // 31 == 12:
                    year += 1
                else:
                    year += (month + sum_of_days // 31) // 12 

            if sum_of_days == 31:
                month += 1
                day = 1
            if sum_of_days > 31:
                month += sum_of_days // 31
                day = sum_of_days - 31

        return datetime.date(year, month, day)



    def _generate_reward(self) -> float:
        # The function will generate a reward

        if self.which_dev == None:
            return 0
        reward = self.which_dev.seniority * (self.complexity / self.days_of_work)
        return reward



    def add_dev(self, dev: Developer) -> None:
        # The function updates the current exercise with a developer 
        
        self.which_dev = dev



    def exercise_finished(self, dev: Developer) -> bool:
        # The function return True if the end date has passes and that the dev who tries to change the status of the exercise is permitted to that exercise, otherwise, False 
        if dev != self.which_dev:
            raise Exception("Only The Permitted Developer Can Define A Exercise As Finished!")
        
        if datetime.date.now() > self.end_date and dev == self.which_dev:
            return True
        
        return False
    