info=[]
maior=0
for i in range(4):
    print(i)
    d={}
    d["nome"]=input("Digite seu nome: ")
    d["funcao"]=input("Digite sua função: ")
    d["salario"]=float(input("Digite seu salario: "))
    info.append(d)

    if  d["salario"] > maior:
        maior = d["salario"]
    info.append(d)

for pessoa in info:
    if pessoa["salario"]==maior:
        print(f"A Pessoa com maior salário é {pessoa ["nome"]} ")
