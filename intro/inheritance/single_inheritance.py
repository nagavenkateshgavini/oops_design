from vehicle import Vehicle

class FuelCar(Vehicle):
    def __init__(self, name, model, combust_type):
        self.combust_type = combust_type
        Vehicle.__init__(self, name, model)
    
    def get_fuelcar(self):
        super().get_name()
        print(f"combust type is {self.combust_type}")
        
if __name__ == "__main__":
    f = FuelCar("Q5", "Audi", "Petrol")
    f.get_fuelcar()