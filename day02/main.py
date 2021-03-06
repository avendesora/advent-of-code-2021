from dataclasses import dataclass
from enum import Enum

from helpers import clean_line, Point2D


class Direction(Enum):
    FORWARD = "forward"
    DOWN = "down"
    UP = "up"


@dataclass
class Command:
    direction: Direction
    distance: int


def read_input(filename: str) -> list[Command]:
    input_commands: list[Command] = []

    with open(filename, "r", encoding="utf-8") as lines:
        for line in lines:
            direction_string, distance_string = clean_line(line).split(" ")
            input_commands.append(
                Command(Direction(direction_string), int(distance_string))
            )

    return input_commands


def plot_movement(input_commands: list[Command]) -> Point2D:
    current_location: Point2D = Point2D(0, 0)

    for command in input_commands:
        if command.direction == Direction.FORWARD:
            current_location.x += command.distance
        elif command.direction == Direction.DOWN:
            current_location.y -= command.distance
        elif command.direction == Direction.UP:
            current_location.y += command.distance

    return current_location


def plot_movement_with_aim(input_commands: list[Command]) -> Point2D:
    current_location: Point2D = Point2D(0, 0)
    aim: int = 0

    for command in input_commands:
        if command.direction == Direction.FORWARD:
            current_location.x += command.distance
            current_location.y += command.distance * aim
        elif command.direction == Direction.DOWN:
            aim += command.distance
        elif command.direction == Direction.UP:
            aim -= command.distance

    return current_location


if __name__ == "__main__":
    # Part One
    commands: list[Command] = read_input("input.txt")
    end_location: Point2D = plot_movement(commands)
    print(
        f"Final horizontal position x final depth = {abs(end_location.x * end_location.y)}"
    )

    # Part Two
    end_location_with_aim: Point2D = plot_movement_with_aim(commands)
    print(
        f"Using aim, final horizontal position x final depth = {abs(end_location_with_aim.x * end_location_with_aim.y)}"
    )
