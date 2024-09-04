class Vector2():
    x = 0
    y = 0

    def __init__(self, xy_array : set|list, limit_x:int=None, limit_y:int=None) -> None:
        self.x = xy_array[0]
        self.y = xy_array[1]
        if (limit_y and limit_y<=0) or (limit_x and limit_x <= 0):
            raise ValueError
        self.limit_x = limit_x
        self.limit_y = limit_y

    def __len__(self):
        return (self.x**2 + self.y**2) ** 0.5

    def __add__(self, inp):
        return Vector2((self.x+inp.x, self.y+inp.y))

    def __sub__(self, tmp):
        return Vector2((self.x-tmp.x, self.y-tmp.y))

    def __neg__(self):
        return Vector2((-self.x, -self.y))

    def __eq__(self, inp: object) -> bool:
        return self.coords() == inp.coords()

    def __mul__(self, k : int):
        return Vector2((self.x*k, self.y*k))

    def coords(self):
        x = self.x
        y = self.y
        if self.limit_x:
            x %= self.limit_x
        if self.limit_y:
            y %= self.limit_y
        return (x, y)

