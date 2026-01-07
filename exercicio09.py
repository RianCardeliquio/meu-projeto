## 🎯 Objetivo
#Nesta atividade, você irá desenvolver um **sistema simples de cadastro e gerenciamento em Python**, executado no terminal.  
#O objetivo é praticar e consolidar os **conceitos básicos da linguagem**, aplicando-os em um projeto único e funcional.
#função para opções

def startingProgram():
    print("\n[1] Adicionar contato")
    print("[2] Ver todos")
    print("[3] Buscar")
    print("[4] Ver total de contatos salvos")
    print("[5] Sair")
    selectOptionm = input("Escolha uma opção:\n")
    return selectOptionm

#função para registro de nome e cidade
def registerLetters(x):
    if x == 1:
        registerName = input("Nome: ")
        while not registerName.isalpha():
            print("Digite apenas letras.")
            registerName = input("Nome: ")
        return registerName

    else:
        registerCity = input("Cidade: ")
        while not registerCity.isalpha():
            print("Digite apenas letras.")
            registerCity = input("Nome: ")
            registerCity = registerCity.capitalize()
        return registerCity

#função para registro de número telefone
def registerNumber():
    while True:
        try:
            registerNumber = int(input("Telefone: "))
            return registerNumber
        except ValueError:
            print("Digíte apenas números")
#Função para  procurar nome especifico na lista com dicionários
def searchUser(nome):
    resultados = []
    for user in register:
        if nome.lower() in user['nome'].lower():
            resultados.append(user)
    return resultados

#Inicio do Programa
print("Olá, Bem vindo, este programa registra seus contatos!")
register = []
while True:
    option = startingProgram()
    if option == "1":
        name= registerLetters(1)
        number = registerNumber()
        city = registerLetters(2)

#Criando uma dicionário com as informações do contato e add a lista
        person = {
        "nome": name,
        "telefone": number,
        "cidade": city
        }
        register.append(person)
        print(f"Contato '{name}' adicionado!")

#Verficando todos os registrados na lista
    if option == "2":
        if len(register) == 0:
            print("Não há registros!\n")
        else:
            print("\n---- Contatos da Lista ----")
            for registred in range(len(register)):
                print(f"{registred+1}.")
                print(f"  Nome: {person['nome']}")
                print(f"  Telefone: {person['telefone']}")
                print(f"  Cidade: {person['cidade']}")

#Procurando contato na Lista:
    elif option == "3":
        if len(register) == 0:
            print("\n Não há contatos registrados ainda!\n")
        else:
            search = input("Digite o nome que deseja buscar: ")
            resultados = searchUser(search)  # CORREÇÃO: passar o parâmetro
            
            if resultados:
                print(f"\n Encontrado(s) {len(resultados)} contato(s):\n")
                for i, pessoa in enumerate(resultados, 1):
                    print(f"{i}.")
                    print(f"  Nome: {pessoa['nome']}")
                    print(f"  Telefone: {pessoa['telefone']}")
                    print(f"  Cidade: {pessoa['cidade']}")
                    print("-" * 30)
            else:
                print(f"\n Nenhum contato encontrado com '{search}'\n")

#Contar quantos contatos tem registrado
    elif option == "4":
        print(f"Você tem {len(register)} em sua lista de conta")
    
#Encerramento do programa
    elif option == "5":
        print("Programa encerrado!")
        break

#Verificação de comando invalido
    else:
        print("Comando Inválido, tente novamente!")