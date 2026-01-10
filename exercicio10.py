import random

def startingProgram():
    print("Pressiona 0 para encerrar jogo")
    print("Pressione 1 para jogar novamente")
    selectOptionm = input("Escolha uma opção:\n")
    return selectOptionm

def compararCartas(cartaJogador, cartaComputer):
    global jogador, computador
    
    if cartaJogador < cartaComputer:
        jogador -= 1
        return "computador" 
    elif cartaJogador > cartaComputer:
        computador -= 1
        return "jogador"
    else:
        return "empate"

def lifezero():
    if jogador == 0:
        print("Suas vidas acabaram, você Perdeu!")
        return True
    elif computador == 0:
        print("As vidas do computador chegaram a zero, você Ganhou!")
        return True
    return False

print("="*50)
print("Mini-projeto: Jogo de Cartas – Batalha Simples")
print("="*50)
print("\n🃏 Regras do jogo:")
print("• Cada jogador começa com 3 vidas")
print("• Em cada rodada, ambos tiram uma carta")
print("• A carta tem um valor de 1 a 10")
print("• Quem tirar a maior carta faz o outro perder 1 vida")
print("• Em empate, ninguém perde vida")
print("• O jogo termina quando alguém ficar sem vidas")

jogador = 0
computador = 0

while True:
    option = startingProgram()

    if option == "1":
        jogador = 3
        computador = 3
        print(f" Vidas do Jogador: {jogador}")
        print(f" Vidas do Computador: {computador}")

        while True:
            # Verifica se alguém perdeu
            if lifezero():
                break
            
            while True:
                rondContinue = input("\nPressione ENTER para comprar cartas: ")
                if rondContinue != "":
                    print(" Comando inválido, pressione apenas ENTER!")
                else:
                    break

            # Compra as cartas
            cartaJogador = random.randint(1, 10)
            cartaComputer = random.randint(1, 10)
            
            # Compara as cartas
            vencedor = compararCartas(cartaJogador, cartaComputer)
            
            # Mostra resultado
            print(f"\n Carta do Jogador: {cartaJogador}")
            print(f" Carta do Computador: {cartaComputer}")
            
            if vencedor == "computador":
                print(" Rodada do computador!")
                print(f"  Vidas do Jogador: {jogador}")
            elif vencedor == "jogador":
                print(" Rodada do jogador!")
                print(f" Vidas do Computador: {computador}")
            else:
                print(" Empate! Ninguém perde vida nesta rodada!")
                print(f"  Vidas do Jogador: {jogador}")
                print(f" Vidas do Computador: {computador}")

    elif option == "0":
        print("Prograna encerrado")
        break
    else:
        print("Comando Inválido, tente novamente!")
