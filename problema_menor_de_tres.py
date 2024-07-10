print("Digite três valores: ")
x = int(input("Primeiro valor: "))
y = int(input("Segundo valor: "))
z = int(input("Teceiro valor: "))

print("MENOR: ", end="")
if x < y and x < z:
    print(x)
elif y < z:
    print(y)
else:
    print(z)