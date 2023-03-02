class Student:
    def __init__(self, prenom, nom, student_id):
        self.__prenom = prenom
        self.__nom = nom
        self.__student_id = student_id
        self.__credits = 0
        self.__level = self.__studentEval()

    def add_credits(self, num_credits):
        if num_credits > 0:
            self.__credits += num_credits

    def __studentEval(self):
        if self.__credits >= 90:
            return "Excellent"
        elif self.__credits >= 80:
            return "Très bien"
        elif self.__credits >= 70:
            return "Bien"
        elif self.__credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"

    def Studentinfo(self):
        print("Nom: " + self.__nom)
        print("Prénom: " + self.__prenom)
        print("Identifiant: " + str(self.__student_id))
        print("Niveau: " + self.__level)

john_doe = Student("John", "Doe", 145)
john_doe.add_credits(20)
john_doe.add_credits(50)
john_doe.add_credits(30)

john_doe.Studentinfo()
