agenda = []

def novoContato():
    print("PREENCHA O NOVO CONTATO")
    nome = input("\nNome: ")
    if procurarNome(nome) == None:
       celular = input("Celular: ")
       email = input("E-mail: ")
       agenda.append([nome, celular, email])
       print("\nContato adcionado com sucesso!!!")
    else:
        print("\nNome de contato já presente na lista.")

def procurarNome(nomeContato):
    for ind, item in enumerate(agenda):
        if item[0].lower() == nomeContato.lower():
            return ind
    return None

def exibirContato():
    print("PROCURAR - DIGITE O NOME DO CONTATO")
    nome = input("\nNome: ")
    ind = procurarNome(nome)
    if ind != None:
        print(f"Nome: {agenda[ind][0]} \nCelular: {agenda[ind][1]} \nE-mail: {agenda[ind][2]}")
    else:
        print("Nome não encontrado.")

def editarContato():
    print("EDITAR - DIGITE O NOME DO CONTATO")
    nome = input("\nNome: ")
    ind = procurarNome(nome)
    if ind != None:
        print("Nome: ", nome)
        celular = input("\nCelular: ")
        email = input("E-mail: ")
        agenda[ind] = [nome, celular, email]
        print("Registro editado com sucesso!")
    else:
        print("Nome não encontrado.")

def listarContatos():
    print("CONTATOS DA AGENDA")
    for item in agenda:
        print(f"\nNome: {item[0]} \nCelular: {item[1]} \nE-mail: {item[2]}")
        print("--------------------------------------------")
    print("FIM DA AGENDA")

def apagarContato():
    print("EXCLUIR - DIGITE O NOME DO CONTATO")
    nome = input("\nNome: ")
    ind = procurarNome(nome)
    if ind == None:
        print("Nome não encontrado.")
    else:
        if confirmandoExclusao(nome):
           del agenda[ind]
           print("Registro excluido com sucesso!")
        else:
            print("Exclusão cancelada!")

def confirmandoExclusao(nomeContato):
    while True:
        print(F"Deseja realmente EXCLUIR {nomeContato} da agenda ?")
        resposta = input("[S]im ou [N]ão ? ")
        if resposta.lower() == "s":
           return True
        elif resposta.lower() == "n":
            return False
        else:
            print("Opcao Inválida!")


def menu(): 
    print("""
   1 - Adicionar novo contato
   2 - Editar um contato
   3 - Pesquisar contato
   4 - Lista de contatos
   5 - Apagar um contato
   6 - Sair
   """) 
    return validarEscolha()

def validarEscolha():
    while True:
        try:
            numeroMenu = int(input("\nEscolha uma opção: "))
            if numeroMenu >= 1 and numeroMenu <= 6:
                return (numeroMenu)
            else:
                return (0)
        except ValueError:
            print("Valor inválido, favor digitar entre 1 e 6")


while True: 
    opcao = menu()
    if opcao == 0:
        print("Opcao Inválida!")
    elif opcao == 6:
        break
    elif opcao == 1:
        novoContato()
    elif opcao == 2:
        editarContato()
    elif opcao == 3:
        exibirContato()
    elif opcao == 4:
        listarContatos()
    elif opcao == 5:
        apagarContato()