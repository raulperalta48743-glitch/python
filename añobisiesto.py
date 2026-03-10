print("\nAño bisiesto")

a = int(input("\nIngresa un año: "))

if a % 400 == 0:
    print("El año es bisiesto.")
elif a % 4 == 0 and a % 100 != 0:
    print("El año es bisiesto.")
else:
    print("El año no es bisiesto.")
