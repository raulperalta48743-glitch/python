num = int(input("Dame un numero para armar el triangulo: "))

for i in range(1, num + 1):
    print(" " * (2 * (num - i)) + "🤪" * i)
