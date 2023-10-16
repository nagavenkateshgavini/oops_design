from single_inheritance import FuelCar

class Gasoline(FuelCar):
    def __init__(self, name, model, combust_type, gas_capacity):
        self.gas_capacity = gas_capacity
        FuelCar.__init__(self, name, model, combust_type)
    
    def get_gasoline_car(self):
        super().get_fuelcar()
        print(f"gas capacity is {self.gas_capacity}")

if __name__ == "__main__":
    g = Gasoline("Audi", "Q5", "gasoline", "30 liters")
    g.get_gasoline_car()