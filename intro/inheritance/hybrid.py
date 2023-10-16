from single_inheritance import FuelCar
from hierarchical import Electric

class Hybrid(FuelCar, Electric):
    def __init__(self, name, model, combust_type, battery_power):
        FuelCar.__init__(self, name, model, combust_type)
        Electric.__init__(self, name, model, battery_power)
        
    def get_hybrid_car(self):
        super().get_fuelcar()
        super().get_electric_car()
    
if __name__ == "__main__":
    h = Hybrid("Audi", "Q5", "petrol", "2000WH")
    h.get_hybrid_car()