class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def get_longueur(self):
        return self.__longueur

    def set_longueur(self, longueur):
        self.__longueur = longueur

    def get_largeur(self):
        return self.__largeur

    def set_largeur(self, largeur):
        self.__largeur = largeur

    def afficher(self):
        print("Longueur :", self.__longueur)
        print("Largeur :", self.__largeur)

# Créer un rectangle avec une longueur de 10 et une largeur de 5
mon_rectangle = Rectangle(10, 5)

# Afficher les attributs de mon_rectangle
mon_rectangle.afficher()

# Modifier la longueur et la largeur
mon_rectangle.set_longueur(15)
mon_rectangle.set_largeur(8)

# Afficher les attributs modifiés de mon_rectangle
mon_rectangle.afficher()