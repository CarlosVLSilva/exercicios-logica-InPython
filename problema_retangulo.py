import math

b = float(input("Base do retângulo: "))
a = float(input("Altura do retângulo: "))

area = b * a
perim = (2*b) + (2*a)
diagonal = math.sqrt(a**2 + b**2)

print(f"ÁREA = {area:.4f}")
print(f"PERÍMETRO = {perim:.4f}")
print(f"DIAGONAL = {diagonal:.4f}")