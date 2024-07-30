class User:
    
    def __init__(self, first_name, last_name):
        self.firstName = first_name
        self.lastName = last_name

    def sayFirstName(self):
        print("Имя: ", self.firstName)

    def sayLastName(self):
        print("Фамилия: ", self.lastName)

    def sayName(self):
        print("Имя и фамилия: ", self.firstName, self.lastName)



