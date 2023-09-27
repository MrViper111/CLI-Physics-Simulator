from plane import Plane
from position import Position
from simulation import Simulation


def main():
    plane = Plane(30, "•")

    Simulation(
        plane=Plane(30, "•"),
        initial_position=Position(plane, 0, 15),
        initial_x_velocity=4,
        initial_y_velocity=5,
        acceleration_x=0,
        acceleration_y=-2,
        length=6
    ).start()
    

if __name__ == "__main__":
    main()
