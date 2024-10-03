# Simple Calculator

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
operation = input("Choose operation: ").upper()

result = 0
# Operation
if operation == "ADD":
    result = num1 + num2
elif operation == "SUBTRACT":
    result = num1 - num2
elif operation == "MULTIPLY":
    result = num1 * num2
else:
    if num2 == 0:
        result = "undefined"
    else:
        result = num1 / num2

# Display
print(f"Result: {result}")