lis_consul = []
hist = []

while True:
    print("M - Médico")
    print("U - Usuário")
    inform = input("Informe se você é um Médico ou Usuário: ")

    if inform == "U" or inform == "u":
        print("1 - Marcar consulta\n2 - Verificar Histórico de Consultas")
        user = int(input("Digite o número da função que deseja: "))

        if user == 1:
            d = {}
            d["nome"] = input("Digite seu nome: ")
            d["cpf"] = float(input("Digite seu CPF: "))
            d["idade"] = float(input("Digite sua idade: "))
            d["horario"] = float(input("Digite o horário da consulta: "))
            lis_consul.append(d)
            print("Consulta Marcada com Sucesso!!")

        elif user == 2:
            hist_name = input("Digite o seu nome para ver o histórico: ")
            for consulta in lis_consul:
                if consulta["nome"] == hist_name:
                    print(consulta)
                    break
            else:
                print("Histórico não encontrado")

    elif inform == "M" or inform == "m":
        while True:
            print("1 - Ver listas de consultas\n2 - Realizar consulta\n3 - Sair")
            consul = int(input("Informe qual função deseja: "))

            if consul == 1:
                print(lis_consul)
            elif consul == 2:
                realizar = input("Digite o nome do paciente para realizar a consulta: ")
                for i in range(len(lis_consul)):
                    consulta = lis_consul[i]
                    if consulta["nome"] == realizar:
                        del lis_consul[i]
                        print("Consulta realizada")
                        break
                else:
                    print("Consulta não encontrada")
            elif consul == 3:
                break
