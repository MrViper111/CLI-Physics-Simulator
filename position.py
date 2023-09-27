from plane import Plane


class Position:
    plane: Plane
    x: int
    y: int

    def __init__(self, plane, x: int, y: int):
        self.plane = plane
        self.x = x
        self.y = y

    def place(self, string: str):
        self.plane.place(string, self.plane.size - self.y - 1, self.plane.size - self.x)
