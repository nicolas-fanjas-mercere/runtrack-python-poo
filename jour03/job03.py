class Tache:
    def __init__(self, titre, description, statut="à faire"):
        self.titre = titre
        self.description = description
        self.statut = statut

    def __str__(self):
        return f"{self.titre} : {self.description} ({self.statut})"


class ListeDeTaches:
    def __init__(self):
        self.taches = []

    def ajouterTache(self, tache):
        self.taches.append(tache)

    def supprimerTache(self, tache):
        self.taches.remove(tache)

    def marquerCommeFinie(self, tache):
        tache.statut = "terminée"

    def afficherListe(self):
        for tache in self.taches:
            print(tache)

    def filterListe(self, statut):
        return [tache for tache in self.taches if tache.statut == statut]

# créer des tâches
tache1 = Tache("Faire les courses", "Acheter du lait et du pain")
tache2 = Tache("Apprendre le python", "Lire le livre 'Apprendre le python en 10 jours'")
tache3 = Tache("Faire du sport", "Aller à la salle de gym")

# créer une liste de tâches et ajouter les tâches
liste = ListeDeTaches()
liste.ajouterTache(tache1)
liste.ajouterTache(tache2)
liste.ajouterTache(tache3)

# afficher la liste des tâches
print("Liste des tâches :")
liste.afficherListe()

# marquer une tâche comme terminée
liste.marquerCommeFinie(tache1)

# afficher la liste des tâches à faire
print("Liste des tâches à faire :")
taches_a_faire = liste.filterListe("à faire")
for tache in taches_a_faire:
    print(tache)

# supprimer une tâche
liste.supprimerTache(tache2)

# afficher la liste des tâches
print("Liste des tâches :")
liste.afficherListe()