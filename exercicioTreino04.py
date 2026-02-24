#- Contar palavras em um texto
#- Contar caracteres
#- Palavras mais frequentes
#---------------------------------------------------------

import json
from collections import Counter   # Usado para contar frequência de palavras

# ======================== ARQUIVO ========================

def salvar_dados(textos):
    """Salva a lista de textos no arquivo JSON"""
    try:
        with open("textos.json", "w", encoding="utf-8") as arquivo:
            json.dump(textos, arquivo, indent=4, ensure_ascii=False)
        print("✅ Salvo com sucesso!")
    except Exception as erro:
        print(f"❌ Erro ao salvar: {erro}")

def carregar_dados():
    """Carrega os textos do arquivo JSON (retorna lista vazia se não existir)"""
    try:
        with open("textos.json", "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        print("📁 Arquivo não encontrado. Iniciando lista vazia.")
        return []
    except Exception as erro:
        print(f"❌ Erro ao carregar: {erro}")
        return []

# ======================== ENTRADA DO USUÁRIO ========================

def digitar_titulo():
    """Pede um título ao usuário e o retorna formatado (primeira letra maiúscula)"""
    return input("\nDigite o título:\n").title()

def digitar_texto():
    """Pede um texto multilinha ao usuário. Encerra quando digitar 'FIM'"""
    print("\n---- Digitando Texto ----")
    print("(Digite 'FIM' para terminar)\n")
    linhas = []
    while True:
        linha = input()
        if linha.strip().upper() == "FIM":
            break
        linhas.append(linha)
    return '\n'.join(linhas)

# ======================== FUNÇÕES PRINCIPAIS ========================

def listar_titulos(registros):
    """
    Exibe todos os títulos cadastrados.
    Retorna True se houver registros, False se a lista estiver vazia.
    """
    if not registros:
        print("\n📭 Nenhum texto cadastrado ainda.")
        return False
    print("\n========== TÍTULOS CADASTRADOS ==========")
    for i, item in enumerate(registros):
        print(f"  [{i + 1}] {item['titulo']}")
    print("==========================================")
    return True

def selecionar_texto(registros, mensagem="Escolha o número do texto (0 para cancelar):"):
    """
    Exibe os títulos e pede que o usuário selecione um.
    Retorna o item selecionado ou None se cancelado/inválido.
    """
    if not listar_titulos(registros):
        return None
    try:
        escolha = int(input(f"\n{mensagem}\n"))
        if escolha == 0 or escolha > len(registros):
            return None
        return registros[escolha - 1]
    except ValueError:
        print("❌ Opção inválida.")
        return None

def buscar_por_titulo(registros):
    """
    Pede um termo de busca ao usuário e filtra os títulos que o contenham.
    Retorna o item selecionado nos resultados ou None.
    """
    if not registros:
        print("\n📭 Nenhum texto cadastrado ainda.")
        return None

    busca = input("\nDigite parte do título para buscar:\n").lower()
    # Filtra os registros cujo título contenha o termo buscado
    resultados = [item for item in registros if busca in item['titulo'].lower()]

    if not resultados:
        print("\n🔍 Nenhum resultado encontrado.")
        return None

    print(f"\n🔍 {len(resultados)} resultado(s) encontrado(s):")
    return selecionar_texto(resultados, "Escolha o número do texto:")

def contar_estatisticas(item):
    """
    Exibe as estatísticas do texto: total de palavras, caracteres
    e as 5 palavras mais usadas.
    """
    texto = item['texto']
    palavras = texto.lower().split()

    print(f"\n📊 ===== ESTATÍSTICAS: {item['titulo']} =====")
    print(f"   Palavras:                    {len(palavras)}")
    print(f"   Caracteres (com espaços):    {len(texto)}")
    # Remove espaços e quebras de linha para contar só os caracteres visíveis
    print(f"   Caracteres (sem espaços):    {len(texto.replace(' ', '').replace(chr(10), ''))}")
    print(f"\n   🏆 Top 5 palavras mais usadas:")
    for palavra, qtd in Counter(palavras).most_common(5):
        print(f"      '{palavra}': {qtd}x")
    print("===========================================")

def ler_texto(item):
    """Exibe o título e o conteúdo completo do texto selecionado"""
    print(f"\n📖 ===== {item['titulo'].upper()} =====")
    print(item['texto'])
    print("=" * (len(item['titulo']) + 12))

def editar(registros, item):
    """
    Permite ao usuário editar o título e/ou texto de um registro existente
    e salva as alterações no arquivo.
    """
    # Localiza o índice do item na lista original para poder atualizá-lo
    indice = registros.index(item)

    print(f"\n✏️  Editando: '{item['titulo']}'")
    print("[1] Editar título")
    print("[2] Editar texto")
    print("[3] Editar título e texto")
    print("[0] Cancelar")
    opcao = input("O que deseja editar?\n")

    if opcao == "1":
        registros[indice]['titulo'] = digitar_titulo()
    elif opcao == "2":
        registros[indice]['texto'] = digitar_texto()
    elif opcao == "3":
        registros[indice]['titulo'] = digitar_titulo()
        registros[indice]['texto'] = digitar_texto()
    else:
        print("Edição cancelada.")
        return

    salvar_dados(registros)
    print(f"✅ '{registros[indice]['titulo']}' editado com sucesso!")

# ======================== SUBMENUS ========================

def submenu_pos_ver_titulos(registros):
    """
    Exibido após [2] Ver títulos.
    Opções: [1] Selecionar um texto | [2] Buscar por título
    """
    print("\nO que deseja fazer agora?")
    print("[1] Selecionar um texto")
    print("[2] Buscar por título")
    print("[0] Voltar ao menu principal")
    opcao = input("Escolha:\n")

    if opcao == "1":
        # Usuário escolhe um texto da lista para ler, contar ou editar
        item = selecionar_texto(registros, "Escolha o número do texto:")
        if item:
            submenu_texto_selecionado(registros, item)
    elif opcao == "2":
        # Redireciona para o fluxo de busca
        item = buscar_por_titulo(registros)
        if item:
            submenu_texto_selecionado(registros, item)

def submenu_texto_selecionado(registros, item):
    """
    Submenu unificado exibido sempre que um texto é selecionado,
    independente de como chegou até ele.
    Opções: [1] Ler texto | [2] Contar palavras e caracteres | [3] Editar
    """
    print(f"\n📄 Texto selecionado: '{item['titulo']}'")
    print("\nO que deseja fazer com este texto?")
    print("[1] Ler texto")
    print("[2] Contar palavras e caracteres")
    print("[3] Editar este texto")
    print("[0] Voltar ao menu principal")
    opcao = input("Escolha:\n")

    if opcao == "1":
        # Exibe o conteúdo completo do texto
        ler_texto(item)
        submenu_texto_selecionado(registros, item)  # Oferece as opções novamente após a leitura
    elif opcao == "2":
        contar_estatisticas(item)
        submenu_pos_contagem(registros)
    elif opcao == "3":
        editar(registros, item)
        submenu_pos_edicao(registros)

def submenu_pos_contagem(registros):
    """
    Exibido após [4] Contar palavras.
    Opções: [1] Ver títulos | [2] Buscar por título
    """
    print("\nO que deseja fazer agora?")
    print("[1] Ver títulos")
    print("[2] Buscar por título")
    print("[0] Voltar ao menu principal")
    opcao = input("Escolha:\n")

    if opcao == "1":
        if listar_titulos(registros):
            submenu_pos_ver_titulos(registros)
    elif opcao == "2":
        item = buscar_por_titulo(registros)
        if item:
            submenu_texto_selecionado(registros, item)

def submenu_pos_edicao(registros):
    """
    Exibido após [5] Editar texto.
    Opções: [1] Ver títulos | [2] Buscar por título
    """
    print("\nO que deseja fazer agora?")
    print("[1] Ver títulos")
    print("[2] Buscar por título")
    print("[0] Voltar ao menu principal")
    opcao = input("Escolha:\n")

    if opcao == "1":
        if listar_titulos(registros):
            submenu_pos_ver_titulos(registros)
    elif opcao == "2":
        item = buscar_por_titulo(registros)
        if item:
            submenu_texto_selecionado(registros, item)

# ======================== MENU PRINCIPAL ========================

def menu_principal():
    """Exibe o menu principal e retorna a opção escolhida pelo usuário"""
    print("\n========== MENU PRINCIPAL ==========")
    print("[1] Adicionar texto")
    print("[2] Ver títulos")
    print("[3] Buscar por título")
    print("[4] Contar palavras em um texto")
    print("[5] Editar texto")
    print("[0] Sair")
    print("=====================================")
    return input("Escolha uma opção:\n")

# ======================== INÍCIO DO PROGRAMA ========================

# Carrega os registros existentes ao iniciar
registros = carregar_dados()

while True:
    opcao = menu_principal()

    if opcao == "1":
        # Pede título e texto, cria o registro e salva
        titulo = digitar_titulo()
        texto = digitar_texto()
        registros.append({"titulo": titulo, "texto": texto})
        salvar_dados(registros)
        print(f"\n✅ '{titulo}' adicionado com sucesso!")

    elif opcao == "2":
        # Exibe todos os títulos e oferece submenu (buscar ou editar)
        if listar_titulos(registros):
            submenu_pos_ver_titulos(registros)

    elif opcao == "3":
        # Busca um texto pelo título e abre o submenu com as opções
        item = buscar_por_titulo(registros)
        if item:
            submenu_texto_selecionado(registros, item)

    elif opcao == "4":
        # Usuário seleciona um texto para ver suas estatísticas
        item = selecionar_texto(registros, "Escolha o texto para analisar:")
        if item:
            contar_estatisticas(item)
            submenu_pos_contagem(registros)

    elif opcao == "5":
        # Usuário seleciona um texto para editar
        item = selecionar_texto(registros, "Escolha o texto para editar:")
        if item:
            editar(registros, item)
            submenu_pos_edicao(registros)

    elif opcao == "0":
        print("\n👋 Até logo!")
        break

    else:
        print("\n❌ Opção inválida. Tente novamente.")