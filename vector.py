class Vector2():
    x = 0
    y = 0
    
    def __init__(self, xy_array : set|list) -> None:
        self.x = xy_array[0]
        self.y = xy_array[1]
        
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
        return (self.x, self.y)
    