class Vehicle:
    def __init__(self, name, model):
        self.name = name
        self.model = model

    def get_name(self):
        print(f"The car is a {self.name}, model {self.model}", end=", ")
