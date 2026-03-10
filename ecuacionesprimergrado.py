print("Resolviendo una ecuación de primer grado")

A = int(input("Ingrese el coeficiente A: "))

while A == 0:
    print("A no puede ser 0")
    A = int(input("Ingrese nuevamente el coeficiente A: "))

B = int(input("Ingrese el coeficiente B: "))

resultado = -B / A

print("El resultado es:", resultado)
