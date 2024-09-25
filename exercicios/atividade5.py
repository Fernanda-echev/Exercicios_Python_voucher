print("equação do segundo grau: ax²+bx+c")

a = float(input("digite o valor a: "))
b = float(input("digite o valor b: "))
c = float(input("digite o valor c: "))
delta = (b ** 2) - 4 * a * c

if a == 0:
    print("Conta inválida")
elif delta < 0:
    print("sem raízes reais")
else:
    x1 = (-b + delta ** (1/2)) / (2 * a)
    x2 = (-b - delta ** (1/2)) / (2 * a)

    print(f"x1: {x1}, x2: {x2}")