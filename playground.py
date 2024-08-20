from vector import Vector2
from charater import Snake
from random import randint

class Playgroud():
    snakes = []
    def __init__(self, height=64, width=48) -> None:
        self.height = height
        self.width = width
        # TODO custom fruit pos (needed?)
        self.fruit_pos = Vector2((self.height//2, self.width//2 + 3))
    
    def add_player(self) -> int:
        self.snakes.append(Snake((self.height//2, self.width//2)))
        return len(self.snakes)-1
        
    def update(self):
        # TODO maybe needed to make other update mekanism (see game of life)
        fruit_catched = False 
        for snake in self.snakes:
            if snake.update(self) == 2:
                fruit_catched = True
        if fruit_catched: self.generate_fruit()
        return fruit_catched
    
    def generate_fruit(self):
        # TODO playground overflow bug
        while True:
            pos = Vector2((randint(0, self.height), randint(0, self.width)))
            for snake in self.snakes:
                # skip dead snakes
                if snake.status == 0:
                    continue
                # check head-fruit and body-fruit collisions
                ptr = snake.head_pos
                for part in snake.body + [snake.head_pos]:
                    if ptr == pos:       
                        break
                    ptr += part
            break
        self.fruit_pos = pos
        return pos