class Operation:
    def __init__(self, nombre1=0, nombre2=0):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def __str__(self):
        return f"Nombre 1 : {self.nombre1}, Nombre 2 : {self.nombre2}"


operation = Operation()
print(operation)