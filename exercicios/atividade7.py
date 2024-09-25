n=input("Digite um número inteiro menor que 1000: ")
x=int(n)    
if x>=100:
 centena= int(n[0])
 dezena= int(n[1])
 unidade= int(n[2])
 print(f"{centena} centenas,{dezena} dezenas, {unidade} unidades")
else:
 if x>=10 and x<99:
  dezena= int(n[0])
  unidade= int(n[1])
  print(f"{dezena} dezenas, {unidade} unidades")
 else:
   if x>=1 and x<9:
    unidade= int([0])
    print("unidades")
   else:
    print("inválido")
 