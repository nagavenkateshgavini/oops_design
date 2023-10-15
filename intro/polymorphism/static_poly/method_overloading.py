class Math:
    def __init__(self):
        pass
    
    def add(self, a, b, c=0):
        s = a + b + c
        print(f"sum is: {s}")
    
if __name__ == "__main__":
    m = Math()
    m.add(1, 2)
    m.add(1, 2, 3) # method overloading
