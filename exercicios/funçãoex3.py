dicio={"0":12, "1":15, "2":18, "3":20, "4":22}

print("Tipo do cômodo potência(watts)")
print("0 - 12 watts\n1 - 15 watts\n2 - 18 watts\n3 - 20 watts\n4 - 22 watts")

def calculo(l,c,tipo):
    if tipo in dicio:
        watts_valor=dicio[tipo]
        x=(l*c) * (watts_valor/60)
        calc= round(x)
        print("----------------------------------")
        print(f"Resultado: {calc} lâmpadas")
        print("Obrigado por usar nosso sistema :)")
        print("----------------------------------")

while True:
    tipo = input("Digite o tipo do cômodo (ou -1 para sair): ")
    if tipo=="-1":
        break

    l=float(input("Digite a largura do cômodo: "))
    c=float(input("Digite o comprimento do cômodo: "))


    calculo(l,c,tipo)
print("----------------------------------")
print("Obrigado por usar nosso sistema :)")
print("----------------------------------") 