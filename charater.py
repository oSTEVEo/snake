from vector import Vector2
# a = vector.Vector2((1, 2))

class Snake():
    #head_xy = [HEIGHT//2, WIDTH//2]
    # TODO hard-mode: death if touch border 
    def __init__(self, head_position_xy : set, hard_mode=False) -> None:
        self.head_pos = Vector2(head_position_xy)
        self.speed_vector = Vector2((1, 0))
        self.body = [Vector2((-1, 0))]
        self.status = 1
        # 0 - Game Over
        # 1 - Normal
        # 2 - Cake!
    
    def score(self) -> int:
        return len(self.body)
    
    def update(self, pg): # Update body
        # Movement
        if not self.status:
            return 0
        self.head_pos += self.speed_vector
        self.body = [-self.speed_vector] + self.body[:-1]   # Updating body like FIFO
        
        # Cheking collision                                                # TODO make real fifo by built-in lib 
        if self.head_pos == pg.fruit_pos:
            self.body = self.body + [self.body[0]]
            self.status = 2
        else: self.status = 1
        for snake in pg.snakes:
            ptr = snake.head_pos # global pointer for each snake's part
            if snake.status == 0: # skip dead snakes
                continue 
            for part in snake.body:
                ptr += part # change ptr
                if ptr == self.head_pos: # Checking head-body collisions
                    self.status = 0                    
        return self.status
    