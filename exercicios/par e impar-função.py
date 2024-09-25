num=[1,2,3,4,5,6,7,8,9,10]
def verificar(num):
    calc_par=0
    calc_impar=0

    for i in num:
        if i % 2 == 0:
            calc_par+=i

        else:
            calc_impar+=i


    calc_par,calc_impar,  = verificar(num)       
    print(f"Números pares: ")
    print(f"Soma dos Pares: {calc_par}")
    print(f"Soma dos Ímpares: {calc_impar}")

verificar(num)
