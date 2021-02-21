#miles per gallon calculator

#first solution
def mpg_calculator():
    miles = 0.0
    gas = 0.0
    mpg = 0.0
    
    miles = float(input("Enter miles driven: "))
    gas = float(input("Enter gallons of gas used: "))
    
    mpg = miles / gas
    
    print(f"The MPG of your car is {mpg}")

mpg_calculator()

#second solution ---class
class MpgCalculator:
    def __init__(self, miles, gas):
        self.miles = miles
        self.gas = gas
    
    def mpg(self):
        return self.miles / self.gas
    
a = float(input("Enter miles driven: "))
b = float(input("Enter gallons of gas used: "))

obj = MpgCalculator(a, b)

print(f"The MPG of your car is {obj.mpg()}")