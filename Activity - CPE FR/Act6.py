# Color Display

color = input("Enter color initial: ")
colorDisplay = ""

# Conditional Statement
if color == "r" or color == "R":
    colorDisplay = "RED"
elif color == "g" or color == "G":
    colorDisplay = "GREEN"
elif color == "b" or color == "B":
    colorDisplay = "BLUE"
else:
    colorDisplay = "BLACK"

# Display
print(f"Display color: {colorDisplay}")