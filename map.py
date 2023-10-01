from enum import Enum
from typing import List
from dataclasses import dataclass


@dataclass
class DirectionItem:
    title: str


@dataclass
class EnvironmentItem:
    title: str


class Environment(Enum):
    FOREST = EnvironmentItem(title="Лес")
    DESERT = EnvironmentItem(title="Пустыня")


class Direction(Enum):
    NORTH = DirectionItem(title="Север")
    SOUTH = DirectionItem(title="Юг")
    EAST = DirectionItem(title="Восток")
    WEST = DirectionItem(title="Запад")


ENV_TO_RUS = {
    Environment.FOREST: "Лес",
    Environment.DESERT: "Пустыня",
}


class Location:

    def __init__(self, environment: Environment):
        self.environment = environment


class Point:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Map:

    def __init__(self):
        self.map_size = 2
        self.zones: List[List[Location]] = [
            [Location(Environment.FOREST),
             Location(Environment.DESERT),
             ],
            [Location(Environment.FOREST),
             Location(Environment.DESERT),
             ]
        ]
        self.position = Point(0, 0)

    def get_current_environment(self) -> str:
        x = self.position.x
        y = self.position.y
        env = self.zones[y][x].environment
        return env.value.title

    def get_passages(self) -> dict[Direction, Environment]:
        passages: dict[Direction, Environment] = {}

        x = self.position.x
        y = self.position.y
        north_y = y - 1
        south_y = y + 1
        west_x = x - 1
        east_x = x + 1

        if west_x >= 0:
            west_env = self.zones[y][west_x].environment
            passages[Direction.WEST] = west_env

        if east_x < self.map_size:
            east_env = self.zones[y][east_x].environment
            passages[Direction.EAST] = east_env

        if north_y >= 0:
            north_env = self.zones[north_y][x].environment
            passages[Direction.NORTH] = north_env

        if south_y < self.map_size:
            south_env = self.zones[south_y][x].environment
            passages[Direction.SOUTH] = south_env

        return passages
