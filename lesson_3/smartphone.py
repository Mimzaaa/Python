class Smartphone:

    def __init__(self, phone, model, sub_number):
        self.brand = phone
        self.model = model
        self.sub_number = sub_number

    def __str__(self):
        return f"{self.brand} - {self.model}. {self.sub_number}"