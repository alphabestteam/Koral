class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __str__(self): 
        return f'{self.x}, {self.y}'

    def __eq__(self, other_point):
        return self.x == other_point.x and self.y == other_point.y

    def __add__(self, other_point):
        return Point(self.x + other_point.x, self.y + other_point.y)