salarioatual=int(input("Digite seu salario atual"))
if salarioatual<500:
    calculo=((15/100)*salarioatual)+salarioatual
    print(f"Seu salário reajustado é {calculo}")
elif salarioatual<1000:
    calculo=((10/100)*salarioatual)+salarioatual
    print(f"Seu salário reajustado é {calculo}")
else:
    calculo=((5/100)*salarioatual)+salarioatual
    print(f"Seu salário reajustado é {calculo}")