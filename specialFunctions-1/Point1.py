class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        self.obj = (x, y)

        def __str__(self): 
            return(f"the value of x is: {self.x}\n the value of y is: {self.y}")

        def __eq__(self):
            return self.x == self.y

        def __add__(self):
            return self.x + self.y