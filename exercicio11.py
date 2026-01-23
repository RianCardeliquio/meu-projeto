#**💻 Prática (30min):** 
#- Exercício 1 - Ler arquivo de notas de alunos
#- Criar arquivo notas.txt com dados de alunos
#- Ler e processar cada linha
#- Calcular médias

import json

# Função para salvar Notas no arquivo JSON
def salvarNotas(lista_de_Notas):
    try:
        with open("alunosNotas.json", "w", encoding="utf-8") as arquivo:
            json.dump(lista_de_Notas, arquivo, indent=4, ensure_ascii=False)
        print("✅ Contatos salvos com sucesso!")
    except Exception as erro:
        print(f"❌ Erro ao salvar: {erro}")

# Função para Notas contatos do arquivo JSON
def carregarNotas():
    try:
        with open("alunosNotas.json", "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        # Se o arquivo não existe, retorna lista vazia
        print("📁 Arquivo não encontrado. Iniciando lista vazia.")
        return []
    except Exception as erro:
        print(f"❌ Erro ao carregar: {erro}")
        return []

#Função para ler lista full com .txt
def listfull():
    try:
        with open("alunosNotas.txt", "r", encoding="utf-8") as arquivo:
            lista_de_Notas = json.load(arquivo)
    except FileNotFoundError:
        # Se o arquivo não existe, retorna lista vazia
        print("📁 Arquivo não encontrado. Iniciando lista vazia.")
        return []
    except Exception as erro:
        print(f"❌ Erro ao carregar: {erro}")
        return []


# Função para o menu
def startingProgram():
    print("\n[1] Adicionar Nota")
    print("[2] Ver todas as notas")
    print("[3] Buscar nota de aluno/a especifíco")
    print("[0] Sair")
    selectOption = input("Escolha uma opção:\n")
    return selectOption

#Função para registro do nome do aluno
def validarNumero(texto):
    try:
        float(texto)
        return True
    except ValueError:
        return False

def obterNota(bimestre):
    while True:
        nota = input(f"Digite a nota do {bimestre} Bimestre:\n")
        if validarNumero(nota):
            return float(nota)
        else:
            print("Digite apenas números!\n")

def registerStudent():
    student = input("Digite o nome do aluno/a \n")
    while not student.replace(" ", "").isalpha():
        print("Digite apenas letras.")
        student = input("Digite o nome do aluno/a \n")
    return student.title()

def registerNotesExam():
    print("Registrando as notas dos 4 bimestres")
    
    firstSemester = obterNota("Primeiro")
    secondSemester = obterNota("Segundo")
    thirdSemester = obterNota("Terceiro")
    fourthSemester = obterNota("Quarto")
    
    return [firstSemester, secondSemester, thirdSemester, fourthSemester]

# CARREGAR CONTATOS DO ARQUIVO AO INICIAR
notasAlunos = carregarNotas()


#Inici do código
while True:
    option = startingProgram()

    if option == "1":
        name = registerStudent()
        notas = registerNotesExam()

        student = {
            "nome": name,
            "notas": notas  # Agora é uma lista de floats
        }
        notasAlunos.append(student)
        print(f"Nota do aluno/a {name} foi registrada!\n")
        salvarNotas(notasAlunos)

    # No elif option == "2":
    elif option == "2":
        if len(notasAlunos) == 0:
            print("Não há registros!\n")
        else:
            print("\n---- Lista de Notas ----")
            for aluno in notasAlunos:
                media = sum(aluno['notas']) / len(aluno['notas'])
                notas_formatadas = ' - '.join(str(nota) for nota in aluno['notas'])
                print(f"Aluno/a: {aluno['nome']}")
                print(f"Notas: {notas_formatadas}")
                print(f"Média: {media:.2f}\n")
