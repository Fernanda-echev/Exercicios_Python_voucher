est = []
car = []
carpreco = []
total_impost = 0.0
qtd = ()
remv_preco = []

while True:
    print("F - Funcionário")
    print("C - Cliente")
    usuario = input("Informe se você é um funcionário ou cliente: ")

    if usuario == "F" or usuario == "f":
        f = input("Informe sua matrícula: ")
        f = input("Informe seu nome: ")
        f = input("Informe sua data de nascimento: ")
        f = input("Informe seu cpf: ")
        print()
        print("Seja bem-vindo ao Sistema do Funcionário")
        print("=========================================")
        while True:
            print("1 - Consultar estoque")
            print("2 - Adicionar produtos")
            print("3 - Remover produtos")
            print("4 - Atualizar")
            print("5 - Alterar preços")
            print("0 - Voltar")
            func = int(input("Informe qual função deseja realizar: "))
            print("................................................")
            if func == 0:
                break
            if func == 1:
                for produto in est:
                    print(f"{produto[0]} - {produto[3]} R$ - {produto[4]} - {produto[5]} unidades")
            

            elif func == 2:
                nome = input("Digite o Nome do produto que deseja adicionar: ")
                tipo = input("Digite o Tipo abaixo \nalimento\nhigiene\nlimpeza: ")
                subtipo = input("Digite o Subtipo abaixo \ncarne\nlegumes\ncabelo\npele\nroupas\ncasa): ")
                preco = float(input("Digite o preço: R$ "))
                codigo = input("Digite o código do produto: ")
                qtd = int(input("Digite a quantidade que quer adicionar: "))
                est.append([nome, tipo, subtipo, preco, codigo, qtd])
                print("Produto adicionado ao estoque")
                print("-------------------------------")
            elif func == 3:
                print(est)
                nome_remv = input("Digite o nome do produto que deseja remover: ")
                est = [produto for produto in est if produto[0] != nome_remv]
                print("Produto removido do estoque")
                print("-----------------------------")
            elif func == 4:
                print("Atualizar quantidade de produto no estoque")
                print(est)
                nome_prod = input("Digite o nome do produto que deseja atualizar a quantidade: ")
                qtd_add = int(input("Digite a quantidade a adicionar: "))
                for produto in est:
                    if produto[0] == nome_prod:
                        produto[5] += qtd_add
                        print(f"Quantidade do produto {produto[0]} atualizada para {produto[5]} unidades")
                        break
            elif func == 5:
                print(est)
                nome_alt = input("Digite o nome do produto que deseja alterar o preço: ")
                novo_preco = float(input("Digite o novo preço: R$ "))
                for produto in est:
                    if produto[0] == nome_alt:
                        produto[3] = novo_preco
                        print("Preço alterado")
                        break

    elif usuario == "C" or usuario == "c":
        while True:
            nome_cliente = input("Informe seu nome: ")
            cpf_cliente = input("Informe seu CPF: ")
            while True:
                print("Seja bem-vindo ao nosso sistema")
                print("1 - Alimento")
                print("2 - Higiene")
                print("3 - Limpeza")
                print("4 - Remover produto do carrinho")
                print("0 - Finalizar compra")
                func = int(input("Informe a seção pelo número: "))
                if func == 1:
                    print("Produtos de Alimento:")
                    for produto in est:
                        if produto[1] == "alimento":
                            print(f"{produto[0]} - {produto[3]} R$ - {produto[2]} - {produto[5]} unidades")

                    escolha = input("Digite o nome do produto que deseja adicionar ao carrinho: ")
                    for produto in est:
                        if produto[0] == escolha:
                            car.append(produto[0])
                            carpreco.append(produto[3])
                            produto[5] -= 1
                            print("Produto adicionado ao carrinho")
                            break

                elif func == 2:
                    print("Produtos de Higiene:")
                    for produto in est:
                        if produto[1] == "higiene":
                            print(f"{produto[0]} - {produto[3]} R$ - {produto[2]} - {produto[5]} unidades")

                    escolha = input("Digite o nome do produto que deseja adicionar ao carrinho: ")
                    for produto in est:
                        if produto[0] == escolha:
                            car.append(produto[0])
                            carpreco.append(produto[3])
                            produto[5] -= 1  
                            print("Produto adicionado ao carrinho")
                            break

                elif func == 3:
                    print("Produtos de Limpeza:")
                    for produto in est:
                        if produto[1] == "limpeza":
                            print(f"{produto[0]} - {produto[3]} R$ - {produto[2]} - {produto[5]} unidades")

                    escolha = input("Digite o nome do produto que deseja adicionar ao carrinho: ")
                    for produto in est:
                        if produto[0] == escolha:
                            car.append(produto[0])
                            carpreco.append(produto[3])
                            produto[5] -= 1
                            print("Produto adicionado ao carrinho")
                            break

                elif func == 4:
                    print("Produtos no Carrinho:")
                    i = 1
                    for produto in car:
                        print(f"{i} - {produto} - {carpreco[i-1]} R$")
                        i += 1
                    remv = int(input("Digite o número do produto que deseja remover ou 0 para sair: "))
                    if remv == 0:
                        break
                    remv -= 1
                    if 0 <= remv < len(car):
                        print(f"Produto {car[remv]} removido do carrinho")
                        nome_prod = car[remv]
                        for produto in est:
                            if produto[0] == nome_prod:
                                produto[5] += 1 
                        del car[remv]
                        del carpreco[remv]
                    else:
                        print("Produto não encontrado no carrinho")
                        
                elif func == 0:
                    break
            print(car)
            soma = sum(carpreco)
            impost_nac = 0.05 * soma
            impost_estad = 0.08 * soma
            impost_mun = 0.12 * soma
            total_impost = soma + impost_nac + impost_estad + impost_mun

            print(f"Total: {total_impost:.2f} R$")
            print("---------------------------")
            print("Formas de Pagamento")
            print("1 - Dinheiro")
            print("2 - Pix")
            print("3 - Cartão")

            pag = int(input("Digite sua forma de pagamento: "))
            if pag == 1:
                din = float(input("Qual o valor a ser entregue: R$ "))
                if din >= total_impost:
                    print(f"Total da compra: R${soma:.2f}")
                    print(f"Imposto Nacional (5%): R$ {impost_nac:.2f}")
                    print(f"Imposto Estadual (8%): R$ {impost_estad:.2f}")
                    print(f"Imposto Municipal (12%): R$ {impost_mun:.2f}")
                    print(f"Total da compra com impostos: R$ {total_impost:.2f}")
                    print(f"Troco: R$ {din - total_impost:.2f}")
                    print("Compra finalizada com sucesso!!!")
                    break
                else:
                    print("Dinheiro insuficiente, tente novamente")
            elif pag == 2:
                pix = float(input("Informe o saldo existente: R$ "))
                if pix >= total_impost:
                    print(f"Total da compra: R${soma:.2f}")
                    print(f"Imposto Nacional (5%): R$ {impost_nac:.2f}")
                    print(f"Imposto Estadual (8%): R$ {impost_estad:.2f}")
                    print(f"Imposto Municipal (12%): R$ {impost_mun:.2f}")
                    print(f"Total da compra com impostos: R$ {total_impost:.2f}")
                    print("Compra finalizada com sucesso!!!")
                    break
                else:
                    print("Saldo insuficiente, tente novamente")
            elif pag == 3:
                print("1 - Débito")
                print("2 - Crédito")
                print("3 - Voucher")
                tipo = int(input("Informe o tipo de cartão: "))
                saldo = float(input("Digite o saldo disponível no cartão: R$ "))
                if saldo >= total_impost:
                    print(f"Total da compra: R${soma:.2f}")
                    print(f"Imposto Nacional (5%): R$ {impost_nac:.2f}")
                    print(f"Imposto Estadual (8%): R$ {impost_estad:.2f}")
                    print(f"Imposto Municipal (12%): R$ {impost_mun:.2f}")
                    print(f"Total da compra com impostos: R$ {total_impost:.2f}")
                    print("Compra finalizada com sucesso!!!")
                    print("---------------------------------")
                    break
                else:
                    print("Saldo insuficiente, tente novamente")
            break
