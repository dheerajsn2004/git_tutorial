# Simple Calculator

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    return "Cannot divide by zero"

if __name__ == "__main__":
    print("Simple Calculator")
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Sum:", add(a, b))
    print("Difference:", subtract(a, b))
    print("Product:", multiply(a, b))
    print("Division:", divide(a, b))
    print("Hello")
    
