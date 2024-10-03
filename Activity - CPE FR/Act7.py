# Water Range Selector

range = int(input("Input number within the range (1-3): "))

waterStatus = ""

# Conditional statement
if range == 1:
    waterStatus = "HOT"
elif range == 2:
    waterStatus = "LUKE WARM"
elif range == 3:
    waterStatus = "COLD"
else:
    waterStatus = "OUT OF RANGE"

# Display output
print(f"Output: {waterStatus}")