class Forme:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    def aire(self):
        return self.longueur * self.largeur


class Cercle(Forme):
    def __init__(self, radius):
        self.radius = radius

    def aire(self):
        return 3.14 * self.radius ** 2

rectangle = Forme(5, 10)
print("Aire du rectangle :", rectangle.aire())

cercle = Cercle(7)
print("Aire du cercle :", cercle.aire())