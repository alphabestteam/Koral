class People:
    def __init__(self, list_of_names) -> None:
        self.list_of_names = list_of_names

    def __iter__(self):
        self.curr_index = 0
        return self
    
    def __next__(self):
        if self.curr_index + 1 >= len(self.list_of_names) + 1:
            del self.curr_index
            raise StopIteration
        self.curr_index += 1
        return self.list_of_names[self.curr_index - 1]

    def add_person(self, name_input) -> None:
        self.list_of_names.append(name_input)
