class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        return (self.x, self.y)

    def move(self, x, y):
        self.x = x
        self.y = y

    def dist(self, p):
        return ((self.x - p.x) ** 2 + (self.y - p.y) ** 2) ** 0.5

p1 = Point(1, 2)
p2 = Point(4, 6)
print(p1.dist(p2))  
