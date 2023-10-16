from vehicle import Vehicle

# along with fuel car class, electrical class is also extending the vehicle
class Electric(Vehicle):
    def __init__(self, name, model, battery_power):
        self.battery_power = battery_power
        Vehicle.__init__(self, name, model)
    
    def get_electric_car(self):
        super().get_name()
        print(f"battery power is {self.battery_power}")

if __name__ == "__main__":
    e = Electric("Tesla", "ModelX", "2000WH")
    e.get_electric_car()