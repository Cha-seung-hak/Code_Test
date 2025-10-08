class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num 
        return self.result
    
    def minus(self, num):
        self.result -= num
        return self.result
    
    def multiply(self, num):
        self.result *= num
        return self.result
    
    def divide(self, num):
        self.result /= num
        return self.result
    

cal1 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal1.minus(4))
print(cal1.multiply(4))
print(cal1.divide(4))