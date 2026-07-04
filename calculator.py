print("================================")
print(" SIMPLE MATHEMATICAL CALCULATOR ")
print("================================")

num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /, %, ^): ")
num2 = float(input("Enter second number: "))

if operator == "+":
    print("Answer =", num1 + num2)

elif operator == "-":
    print("Answer =", num1 - num2)

elif operator == "*":
    print("Answer =", num1 * num2)

elif operator == "/":
    if num2 != 0:
        print("Answer =", num1 / num2)
    else:
        print("Cannot divide by zero.")

elif operator == "%":
    print("Answer =", num1 % num2)

elif operator == "^":
    print("Answer =", num1 ** num2)

else:
    print("Invalid operator.")

print("\nThank you for using the calculator.")