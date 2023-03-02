class Operation:
    def __init__(self, nombre1=0, nombre2=0):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def addition(self):
        resultat = self.nombre1 + self.nombre2
        print(f"Le résultat de l'addition est : {resultat}")

    def __str__(self):
        return f"Nombre1 : {self.nombre1}, Nombre2 : {self.nombre2}"

operation = Operation(nombre1=10, nombre2=20)
print(operation)
operation.addition()