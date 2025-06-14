
operator = input("Choose from: Plus Minus Multiply Divide: ").strip().capitalize()


if operator not in ("Plus", "Minus", "Multiply", "Divide"):
    print("Invalid Operator")
    quit()

x = int(input("First number: "))
y = int(input("Second number: "))

if operator == "Plus":
    z = x + y
    print(z)
elif operator == "Minus":
    z = x - y
    print(z)
elif operator == "Multiply":
    z = x * y
    print(z)
else:# operator == "Divide":
    z = x / y
    print(z)



import os

print(os.path.abspath(__file__))

