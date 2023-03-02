class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def bonjour(self):
        print("Bonjour, je m'appelle", self.nom)


class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")
        self.age = 15  # redéfinition de l'âge à 15 ans


class Professeur(Personne):
    def enseigner(self):
        print("Le cours commence")


eleve1 = Eleve("Emilia", 13)
eleve1.bonjour()
eleve1.allerEnCours()

prof1 = Professeur("M. ligonet", 40)
prof1.bonjour()
prof1.enseigner()