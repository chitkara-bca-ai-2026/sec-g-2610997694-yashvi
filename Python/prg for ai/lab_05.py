import math

print("ENGINEERING CALCULATION TOOL")

value = float(input("Enter a numerical value: "))
exponent = float(input("Enter an exponent: "))
decimal_value = float(input("Enter a decimal measurement: "))

power = math.pow(value, exponent)
square_root = math.sqrt(value)
ceil_value = math.ceil(decimal_value)
floor_value = math.floor(decimal_value)

print("\nResults")
print("Value :", value)
print("Exponent :", exponent)
print("Power (pow) :", power)
print(f"Square Root (sqrt): {square_root:.4f}")
print("Decimal Value :", decimal_value)
print("Ceil Value :", ceil_value)
print("Floor Value :", floor_value)