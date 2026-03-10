print("\nAño bisiesto")

a = int(input("\nIngresa un año: "))

if a % 400 == 0:
    print("El año es bisiesto.")
elif a % 4 == 0 and a % 100 != 0:
    print("E we si we, ya cheque bein we, el año si es bisiesto año es bisiesto.")
else:
    print("Oye, no we, ya cheque bien we y no we el año no es bisiesto.")

