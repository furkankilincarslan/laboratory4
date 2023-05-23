X = int(input("Enter the base (X): "))
Y = int(input("Enter the exponent (Y): "))

result = 1

for _ in range(Y):
    result *= X

print(f"The result of {X}^{Y} is: {result}")
