class Animal:
    def __init__(self):
        pass
    
    def print_animal(self):
        print("I am from animal class")
        
    def print_animal_two(self):
        print("I am from animal class")
        
class Lion(Animal):
    def print_animal(self): # method overriding
        print("I am from Lion class")

if __name__ == "__main__":
    lion = Lion()
    lion.print_animal()
    lion.print_animal_two()
