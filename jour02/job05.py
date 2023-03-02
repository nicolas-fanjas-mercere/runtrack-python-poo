class Voiture:
    def __init__(self, marque, modele, annee, kilometrage):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__en_marche = False
        self.__reservoir = 50

    def set_marque(self, marque):
        self.__marque = marque

    def set_modele(self, modele):
        self.__modele = modele

    def set_annee(self, annee):
        self.__annee = annee

    def set_kilometrage(self, kilometrage):
        self.__kilometrage = kilometrage

    def set_en_marche(self, en_marche):
        self.__en_marche = en_marche

    def set_reservoir(self, reservoir):
        self.__reservoir = reservoir

    def get_marque(self):
        return self.__marque

    def get_modele(self):
        return self.__modele

    def get_annee(self):
        return self.__annee

    def get_kilometrage(self):
        return self.__kilometrage

    def get_en_marche(self):
        return self.__en_marche

    def get_reservoir(self):
        return self.__reservoir

    def demarrer(self):
        if self.__verifier_plein() and not self.__en_marche:
            self.__en_marche = True
            print("La voiture démarre.")
        else:
            print("Impossible de démarrer la voiture.")

    def arreter(self):
        if self.__en_marche:
            self.__en_marche = False
            print("La voiture s'arrête.")
        else:
            print("La voiture est déjà arrêtée.")

    def __verifier_plein(self):
        if self.__reservoir > 5:
            return True
        else:
            return False

ma_voiture = Voiture("fiat", "multiplat", 2009, 0)
ma_voiture.set_marque("Peugeot")
modele_voiture = ma_voiture.get_modele()
ma_voiture.demarrer()

