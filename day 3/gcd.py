#GCD calculator using Eucliean algorithm

def gcd(a, b):
    
    if a==b:
        return a
    elif a > b:
        return gcd(a-b, b)
    else:
        return gcd(a, b-a) 
a, b = input("Enter two numbers separated by space: ").split()
a, b = int(a), int(b)

print(f"The GCD of {a} and {b} is {gcd(a, b)}")