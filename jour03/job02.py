class CompteBancaire:
    def __init__(self, numero_compte, nom, prenom, solde, decouvert=False):
        self.__numero_compte = numero_compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert

    def afficher(self):
        print(f"Numéro de compte: {self.__numero_compte}")
        print(f"Nom: {self.__nom}")
        print(f"Prénom: {self.__prenom}")
        print(f"Solde: {self.__solde}")
        print(f"Découvert autorisé: {self.__decouvert}")

    def afficherSolde(self):
        print(f"Le solde de votre compte est de {self.__solde}")

    def versement(self, montant):
        self.__solde += montant
        print(f"{montant} euro o éta verse sur votre compte.")
        self.afficherSolde()

    def retrait(self, montant):
        if self.__decouvert or self.__solde >= montant:
            self.__solde -= montant
            print(f"{montant} euros ont été débité  du compte.")
            self.afficherSolde()
        else:
            print("Opération impossible: vous êtes trop pauvre.")

    def agios(self, taux):
        if self.__solde < 0:
            agios = - self.__solde * taux
            self.__solde -= agios
            print(f"Des agios de {agios} euros ont été prélevés sur le compte.")
            self.afficherSolde()

    def virement(self, compte_destinataire, montant):
        if self.__solde >= montant:
            self.__solde -= montant
            compte_destinataire.versement(montant)
            print(f"Virement de {montant} euros effectué vers le compte {compte_destinataire.get_numero_compte()}.")
            self.afficherSolde()
        else:
            print("Opération impossible: solde insuffisant.")

    def get_numero_compte(self):
        return self.__numero_compte


compte1 = CompteBancaire("123456", "Dupont", "Jean", 1000)
compte2 = CompteBancaire("789101", "Durand", "Marie", -500, True)

compte1.afficher()
compte2.afficher()

compte1.afficherSolde()
compte1.versement(500)
compte1.retrait(200)
compte1.retrait(1500)
compte1.agios(0.05)
compte1.afficher()

compte1.virement(compte2, 300)
compte1.afficher()
compte2.afficher()