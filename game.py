import json
from map import Direction, Map
from player import Player




class Game:
    def __init__(self):
        self.map = Map()
        self.player = Player()

    def save(self):
        with open("save.json", "w") as fh:
            json.dump(self.dump(), fh)





    def decision(self) -> 'Direction':
        # Запрос направления
        passages = self.map.get_passages()
        print(f"\nДвижение доступно на:\n")
        for direction, environment in passages.items():
            print(f"{direction.value.key} - {direction.value.title}")
        key = input(f"Выберите направление - ")
        dir = Direction.from_key(key)
        return dir

    def action(self, direction: Direction):
        if direction == Direction.NORTH:
            self.map.position.y -= 1
        if direction == Direction.SOUTH:
            self.map.position.y += 1
        if direction == Direction.EAST:
            self.map.position.x += 1
        if direction == Direction.WEST:
            self.map.position.x -= 1


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
        while True:
            self.save()
            self.step()

    def step(self):
        self.display_actual_info()
        decision = self.decision()
        self.action(decision)


    def display_actual_info(self):
        print(f"Вы находиесь в локации: {self.map.get_current_environment()}")
        passages = self.map.get_passages()
        for direction, environment in passages.items():
            print(f"На {direction.value.title}е находится {environment.value.title}")
