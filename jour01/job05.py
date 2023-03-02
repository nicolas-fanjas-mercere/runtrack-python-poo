class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def afficherLesPoints(self):
        print(f"({self.x}, {self.y})")

    def afficherX(self):
        print(self.x)

    def afficherY(self):
        print(self.y)

    def changerX(self, nouveau_x):
        self.x = nouveau_x

    def changerY(self, nouveau_y):
        self.y = nouveau_y


p = Point(3, 4)

p.afficherLesPoints()

p.afficherX()
p.afficherY()

p.changerX(5)
p.changerY(6)

p.afficherX()
p.afficherY()