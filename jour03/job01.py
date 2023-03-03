class Ville:
    def __init__(self, nom, numhabitant):
        self.__nom = nom
        self.__numhabitant = numhabitant

    def recupnom(self):
        return self.__nom

    def recupnombhabitant(self):
        return self.__numhabitant

    def ajouter_habitant(self):
        self.__numhabitant += 1


class Personne:
    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville

    def ajoutPopulation(self):
        self.__ville.ajouter_habitant()


paris = Ville("Paris", 1000000)
marseille = Ville("Marseille", 861635)

print(f"Nombre d'habitants de {paris.recupnom()} : {paris.recupnombhabitant()}")
print(f"Nombre d'habitants de {marseille.recupnom()} : {marseille.recupnombhabitant()}")

john = Personne("John", 45, paris)
myrtille = Personne("Myrtille", 4, paris)
chloe = Personne("Chloé", 18, marseille)

john.ajoutPopulation()
myrtille.ajoutPopulation()
chloe.ajoutPopulation()

print(f"Nombre d'habitants de {paris.recupnom()} : {paris.recupnombhabitant()}")
print(f"Nombre d'habitants de {marseille.recupnom()} : {marseille.recupnombhabitant()}")