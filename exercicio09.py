## 🎯 Objetivo
#Nesta atividade, você irá desenvolver um **sistema simples de cadastro e gerenciamento em Python**, executado no terminal.  
#O objetivo é praticar e consolidar os **conceitos básicos da linguagem**, aplicando-os em um projeto único e funcional.
#função para opções

import json
from datetime import datetime 

# Função para salvar contatos no arquivo JSON
def salvar_contatos(lista_contatos):
    try:
        with open("contatos.json", "w", encoding="utf-8") as arquivo:
            json.dump(lista_contatos, arquivo, indent=4, ensure_ascii=False)
        print("✅ Contatos salvos com sucesso!")
    except Exception as erro:
        print(f"❌ Erro ao salvar: {erro}")
# Função para carregar contatos do arquivo JSON
def carregar_contatos():
    try:
        with open("contatos.json", "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        # Se o arquivo não existe, retorna lista vazia
        print("📁 Arquivo não encontrado. Iniciando lista vazia.")
        return []
    except Exception as erro:
        print(f"❌ Erro ao carregar: {erro}")
        return []
# Função para o menu
def startingProgram():
    print("\n[1] Adicionar contato")
    print("[2] Ver todos")
    print("[3] Buscar")
    print("[4] Ver total de contatos salvos")
    print("[5] Editar contato")
    print("[0] Sair")
    selectOption = input("Escolha uma opção:\n")
    return selectOption
# Função para registro de nome e cidade
def registerLetters(x):
    if x == 1:
        registerName = input("Nome: ")
        while not registerName.replace(" ", "").isalpha():
            print("Digite apenas letras.")
            registerName = input("Nome: ")
        return registerName.title()
    else:
        registerCity = input("Cidade: ")
        while not registerCity.replace(" ", "").isalpha():
            print("Digite apenas letras.")
            registerCity = input("Cidade: ")
        return registerCity.title()
# Função para registro de número telefone
def registerNumber():
    while True:
        try:
            registerNumber = input("Telefone: ")
            if not registerNumber.isdigit():
                raise ValueError
            return registerNumber
        except ValueError:
            print("Digite apenas números")
# Função para procurar nome específico na lista
def searchUser(nome, register):
    resultados = []
    for user in register:
        if nome.lower() in user['nome'].lower():
            resultados.append(user)
    return resultados
# ===== INÍCIO DO PROGRAMA =====
print("Olá, Bem vindo, este programa registra seus contatos!")
# CARREGAR CONTATOS DO ARQUIVO AO INICIAR
register = carregar_contatos()
print(f"📋 {len(register)} contato(s) carregado(s).")
while True:
    option = startingProgram()
#Registro de pessoas na lista de contatos  
    if option == "1":
        name = registerLetters(1)
        number = registerNumber()
        city = registerLetters(2)
    
        # Pegar data e hora atual
        agora = datetime.now()
        data_cadastro = agora.strftime("%d/%m/%Y às %H:%M:%S")

        person = {
            "nome": name,
            "telefone": number,
            "cidade": city,
            "cadastrado_em": data_cadastro  # ← NOVA LINHA
        }
        register.append(person)
        print(f"Contato '{name}' adicionado em {data_cadastro}!")
        salvar_contatos(register)
#Para ver todos os contatos na lista
    elif option == "2":
        if len(register) == 0:
            print("Não há registros!\n")
        else:
            print("\n---- Contatos da Lista ----")
            for i, pessoa in enumerate(register, 1):
                print(f"{i}.")
                print(f"  Nome: {pessoa['nome']}")
                print(f"  Telefone: {pessoa['telefone']}")
                print(f"  Cidade: {pessoa['cidade']}")
                print(f"  Cadastrado em: {pessoa.get('cadastrado_em', 'Não registrado')}") 
                print("-" * 30)
#Procurar contato específio na lista
    elif option == "3":
        if len(register) == 0:
            print("\nNão há contatos registrados ainda!\n")
        else:
            search = input("Digite o nome que deseja buscar: ")
            resultados = searchUser(search, register)
            
            if resultados:
                print(f"\nEncontrado(s) {len(resultados)} contato(s):\n")
                for i, pessoa in enumerate(resultados, 1):
                    print(f"{i}.")
                    print(f"  Nome: {pessoa['nome']}")
                    print(f"  Telefone: {pessoa['telefone']}")
                    print(f"  Cidade: {pessoa['cidade']}")
                    print(f"  Cadastrado em: {pessoa.get('cadastrado_em', 'Não registrado')}")  
                    if 'ultima_edicao' in pessoa:
                        print(f"  Última edição: {pessoa['ultima_edicao']}")
                    print("-" * 30)
            else:
                print(f"\nNenhum contato encontrado com '{search}'\n")
#Ver total de contatos salvos
    elif option == "4":
        print(f"Você tem {len(register)} contato(s) em sua lista")
#Procurar contado para Editar
    elif option == "5":
        if len(register) == 0:
            print("\nNão há contatos registrados ainda!\n")
        else:
            search = input("Digite o nome que deseja buscar: ")
            resultados = searchUser(search, register)
            
            if resultados:
                print(f"\nEncontrado(s) {len(resultados)} contato(s):\n")

                # Mostrar todos os resultados
                for i, pessoa in enumerate(resultados, 1):
                    print(f"{i}.")
                    print(f"  Nome: {pessoa['nome']}")
                    print(f"  Telefone: {pessoa['telefone']}")
                    print(f"  Cidade: {pessoa['cidade']}")
                    print("-" * 30)

                # Caso haja mais de 1, escolha de qual editar
                if len(resultados) > 1:
                    while True:
                        try:
                            escolha_pessoa = int(input(f"Qual contato deseja editar? (1-{len(resultados)}): "))
                            if 1 <= escolha_pessoa <= len(resultados):
                                pessoa_selecionada = resultados[escolha_pessoa - 1]
                                break
                            else:
                                print(f"Digite um número entre 1 e {len(resultados)}")
                        except ValueError:
                            print("Digite apenas números!")
                else:
                    # Se houver apenas um resultado
                    pessoa_selecionada = resultados[0]


                print("Digite [1] para alterar número")
                print("Digíte [2] para alterar a cidade")
                while True:
                    escolhaAlterar = input("Escolha uma opção:\n")
                    if escolhaAlterar == "1":   
                        print("Digite o novo Telefone")                     
                        novoNumero = registerNumber()
                        pessoa["telefone"] = novoNumero       
                        print(f"Contato '{pessoa['nome']}' teve o telefone alterado para {novoNumero}!")
                        break

                    elif escolhaAlterar == "2":
                        novaCidade = registerLetters(2)
                        pessoa["cidade"] = novaCidade
                        print(f"Contato '{pessoa['nome']}' teve a cidade alterada para {novaCidade}!")
                        break

                    else:
                        print("Comando Inválido, tente novamente!")

                # Adicionar timestamp e salvar
                agora = datetime.now()
                pessoa["ultima_edicao"] = agora.strftime("%d/%m/%Y às %H:%M:%S")
                salvar_contatos(register)
            else:
                print(f"\nNenhum contato encontrado com '{search}'\n")

#Encerramento do programa    
    elif option == "0":
        print("Programa encerrado!")
        break
#Para comando que não pentence as opções
    else:
        print("Comando Inválido, tente novamente!")