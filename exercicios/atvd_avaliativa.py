taref = []

def marcar_concl():
    print()
    if len(taref) > 0:
        for i in range(len(taref)):
            print(f"{i + 1}. {taref[i]['descricao']} - {taref[i]['status']}")
        cod = int(input("Digite o código da tarefa para concluir ou não: ")) - 1
        if 0 <= cod < len(taref):
            taref[cod]["status"] = "Concluída"
            print("\nTarefa concluída :)")
            print(".......................")

def add():
    d = {}
    d["descricao"] = input("Dê a descrição da tarefa: ")
    d["status"] = input("Digite o status(Digite não concluído): ")
    taref.append(d)
    print("\nTarefa adicionada :)")
    print("......................")

def remv():
        if menu==4:
            print(taref)
            nome_taref = input("Digite a descrição da tarefa que deseja remover: ")
            for i in range(len(taref)):
                if taref[i]["descricao"] == nome_taref:
                    taref.pop(i)
                    print("\nTarefa removida :)")
                    print("....................")
                    break

while True:
    print("\n1 - Adicionar Tarefas\n2 - Listar Tarefas\n3 - Marcar como concluída\n4 - Remover Tarefa\n5 - Sair")
    menu = int(input("Digite qual função deseja executar: "))
    
    if menu == 1:
        add()
    elif menu == 2:
        if len(taref) > 0:
            for i in range(len(taref)):
                print(f"{i + 1}. {taref[i]['descricao']} - {taref[i]['status']}")
    elif menu == 3:
        marcar_concl()
    elif menu == 4:
        remv()
    elif menu == 5:
        break