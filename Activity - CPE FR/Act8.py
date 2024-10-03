# Simple Bingo Game

inputs = input("Input three numbers: ")

# Assign the three numbers
a, b, c = map(int, inputs.split())

status = ""

# Conditional Statement
if (a == b and a == c) or (b == c and b == a) or (c == a and c == b):
    status = "BINGO"
else:
    status = "TRY AGAIN"

# Display
print(f"Output: {status}")