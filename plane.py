
class Plane:
    size: int
    character: str

    def __init__(self, size, character):
        self.size = size
        self.character = character
        self.plane: list = [[f"\033[90m{self.character}\033[97m" for _ in range(self.size)] for _ in range(self.size)]

    def place(self, string: str, index_1: int, index_2: int):
        self.plane[index_1][-index_2] = string

    def print(self):
        for row in self.plane:
            print(" ".join(row))
