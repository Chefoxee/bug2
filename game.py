from map import Map
from player import Player


class Game:
    def __init__(self):
        self.map = Map()
        self.player = Player()
        # Записываем текущее состояние игры
        pass

    def dump(self) -> dict:
        return {
            "map": self.map.dump(),
            "player": {},
        }

    @classmethod
    def load(cls, data: dict) -> 'Game':
        game = Game()
        game.map = Map.load(data["map"])
        game.player = Player()
        return game

    def run(self):
        self.step()

    def step(self):
        self.display_actual_info()
        # Запрашиваем у игрока его решение
        # Применяем его решение
        pass

    def display_actual_info(self):
        print(f"Вы находиесь в локации: {self.map.get_current_environment()}")
        passages = self.map.get_passages()
        for direction, environment in passages.items():
            print(f"На {direction.value.title}е находится {environment.value.title}")
