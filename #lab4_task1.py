#lab4_task1

height = float(input("Enter your height in cm: "))
weight = float (input("Enter your weight in kg: "))

BMI = weight / (height/100)**2

print(f"You BMI is {BMI}")

if BMI < 16:
    print("You are starvation.")
elif BMI <=16.99:
    print("You are emaciation.")
elif BMI <= 18.49:
    print("You are underweight.")
elif BMI <= 24.99:
    print("You are correct weight.")
elif BMI <= 29.99:
    print("You are overweight.")

elif BMI <= 34.99:
    print("You are first degree obesity.")

elif BMI <= 39.99:
    print("You are second degree obesity (clinical).")

elif BMI >=40:
    print("You are severely third degree obesity (extreme).")
