from exercise1 import Exercise

import datetime

class Project: 

    def __init__(self, description: str, start_date: datetime, exercises_not_finished = [] , exercises_finished = [], list_of_exercises = [], list_of_developers = []) -> None:
        self.description = description
        self.start_time = start_date
        self.list_of_exercises = list_of_exercises
        self.list_of_developers = list_of_developers
        self.exercises_not_finished = exercises_not_finished
        self.end_time = self._generate_end_time()
        self.exercises_finished = exercises_finished
        self._cost = self._cost_of_project()
        self._finished = self._project_finished()


    def get_description(self):
        return self.description
      
    def set_description(self, value):
        self.description = value

    def get_start_date(self):
        return self.start_date
      
    def set_start_date(self, value):
        self.start_date = value

    def get_list_of_exercises(self):
        return self.list_of_exercises
      
    def set_list_of_exercises(self, value):
        self.list_of_exercises = value

    def get_list_of_developers(self):
        return self.list_of_developers
      
    def set_list_of_developers(self, value):
        self.list_of_developers = value

    def get_exercises_not_finished(self):
        return self.description
      
    def set_exercises_not_finished(self, value):
        self.exercises_not_finished = value

    def get_end_time(self):
        return self.end_time
      
    def set_end_time(self, value):
        self.end_time = value

    def get_exercises_finished(self):
        return self.exercises_finished
      
    def set_exercises_finished(self, value):
        self.exercises_finished = value

    def get_cost(self):
        return self._cost
      
    def set_cost(self, value):
        self._cost = value

    def get_finished(self):
        return self._finished
      
    def set(self, value):
        self._finished = value


    def _generate_end_time(self) -> datetime:
        # The function will return the end date for the project

        year = self.start_time.year
        month = self.start_time.month
        day = self.start_time.day

        length_of_days = 0

        for exercise in self.exercises_not_finished:
            length_of_days += exercise.days_of_work

        sum_of_days = day + length_of_days

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



    def _project_finished(self) -> bool:
        # The function will return True is there isn't any exercises left to get done, otherwise, False
        if self.exercises_not_finished == None or len(self.exercises_not_finished) == 0:
            return True
        return False

    

    def _cost_of_project(self) -> float:
        # The function will calculate the cost of the overall project by the rewards of each exercise

        cost = 0

        for exercise in self.exercises_finished:
            cost += exercise.get_reward()

        return cost



    def add_exercise(self, exercise: Exercise) -> None:
        # The function will add a new exercise to the list of exercises and to the list of exercises to be done

        if exercise.project.description != self.description:
            raise Exception("Can't Add The Exercise! Already In Another Project!")

        if exercise in self.list_of_exercises:
            raise Exception("Can't Add The Exercise! Already In The Current projects Exercises List!")
        
        self.list_of_exercises.insert(exercise)
        self.exercises_not_finished.insert(exercise)

        if exercise.get_which_dev() not in self.list_of_developers:
            self.list_of_developers.insert(exercise.get_which_dev())

        for devs in self.list_of_developers:
            devs.get_exercises_to_be_done().insert(exercise)

        
    
    def remove_exercise(self, exercise: Exercise) -> None:
        # The function will remove an exercise if its not finished

        if exercise in self.exercises_finished:
            raise Exception("Can't Remove A Finished Exercise!")

        self.exercises_not_finished.remove(exercise)
        self.list_of_exercises.remove(exercise)

        for devs in self.list_of_developers:
            devs.get_exercises_to_be_done().remove(exercise)


    
    def find_project_by_description(self, description: str) -> Exercise or None:
        # The function will return the exercises by their description

        for exercise in self.list_of_exercises:
            if exercise.get_description() == description:
                return(exercise)
        return None
        