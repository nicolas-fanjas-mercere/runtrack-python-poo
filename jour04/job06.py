class Vehicule:
    def __init__(self, marque, annee, prix):
        self.marque = marque
        self.annee = annee
        self.prix = prix

    def informationsVehicule(self):
        print(f"Marque : {self.marque}")
        print(f"Année : {self.annee}")
        print(f"Prix : {self.prix} €")

    def demarrer(self):
        print("Attention, je roule.")


class Voiture(Vehicule):
    def __init__(self, marque, annee, prix, portes=4):
        super().__init__(marque, annee, prix)
        self.portes = portes

    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Nombre de portes : {self.portes}")

    def demarrer(self):
        print("Je démarre ma voiture.")


class Moto(Vehicule):
    def __init__(self, marque, annee, prix, roue=2):
        super().__init__(marque, annee, prix)
        self.roue = roue

    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Nombre de roues : {self.roue}")

    def demarrer(self):
        print("Je démarre ma moto.")


voiture = Voiture("Renault", 2022, 20000)
voiture.informationsVehicule()

moto = Moto("Yamaha", 2022, 10000)
moto.informationsVehicule()

voiture.demarrer()
moto.demarrer()