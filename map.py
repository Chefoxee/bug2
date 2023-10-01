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


class Location:

    def __init__(self, environment: Environment):
        self.environment = environment

    @classmethod
    def from_env_title(cls, title: str) -> 'Location':
        for env in Environment:
            if env.value.title == title:
                return cls(environment=env)
        raise ValueError


class Point:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def dump(self) -> dict:
        return {"x": self.x, "y": self.y}

    @classmethod
    def load(cls, data: dict) -> 'Point':
        return cls(x=data["x"], y=data["y"])


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

    def dump(self):
        return {
            "position": self.position.dump(),
            "zones": [[location.environment.value.title for location in row] for row in self.zones],
        }

    @classmethod
    def load(cls, data: dict) -> 'Map':
        map = Map()
        map.position = Point.load(data["position"])
        map.zones = [[Location.from_env_title(env_title) for env_title in row] for row in data["zones"]]
        map.map_size = len(data["zones"])
        return map

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
