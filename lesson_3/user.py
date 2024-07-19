class User:

    def __init__(self, first_name, last_name):
        self.f_name = first_name
        self.l_name = last_name

    def sayFName(self):
        print("Ваше имя:", self.f_name)
    
    def sayLName(self):
        print("Ваша фаша фамилия:", self.l_name)

    def sayFLName(self):
        print("Ваше имя и фамилия:", self.f_name, self.l_name)

