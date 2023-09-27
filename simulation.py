import time
import os

from plane import Plane
from position import Position
from physics import Physics


class Simulation:
    plane: Plane
    initial_position: Position
    initial_x_velocity: int
    initial_y_velocity: int
    acceleration_x: int
    acceleration_y: int
    length: int

    def __init__(self, plane, initial_position, initial_x_velocity, initial_y_velocity, acceleration_x, acceleration_y, length):
        self.plane = plane
        self.initial_position = initial_position
        self.initial_x_velocity = initial_x_velocity
        self.initial_y_velocity = initial_y_velocity
        self.acceleration_x = acceleration_x
        self.acceleration_y = acceleration_y
        self.length = length + 1

    def start(self):
        for t in range(self.length):
            time.sleep(1)

            if os.name == "nt":
                os.system("cls")
            else:
                os.system("clear")

            x = Physics.getPosition(self.initial_position.x, self.initial_x_velocity, self.acceleration_x, t)
            y = Physics.getPosition(self.initial_position.y, self.initial_y_velocity, self.acceleration_y, t)
            position = Position(self.plane, x, y)

            if (self.plane.size < y) or (y < 0) or (self.plane.size < x) or (x < 0) or (t == self.length):
                print("\nSimulation over!")
                print(f"|  Total time: {t}s")
                print(f"|  Initial position: ({self.initial_position.x}, {self.initial_position.y})")
                print(f"|  Final position: ({position.x}, {position.y})")
                return

            print(f"Elapsed time: {t}s")
            print(f"Position: ({x}, {y})")

            position.place("X")
            self.plane.print()
