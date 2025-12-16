from random import randint
import time
import os

def gerarNumero():
    n = randint(0, 10)
    return n

def limparTerminal():
    os.system("cls" if os.name == "nt" else "clear")


def lerNumero(msg):
    while True:
        entrada = input(msg)
        try:
            return float(entrada)
        except ValueError:
            print("Entrada inválida! Digite um número.")
            time.sleep(1)
            limparTerminal()

continuar = True

arquivo = open("arquivo.txt", "a")
arquivo = open("arquivo.txt", "r")

acertos = arquivo.readline()

if(acertos == ""): acertos = 0

acertos = int(acertos)

print("Bem-vindo ao jogo de adivinhação!")

while(continuar):
    numeroEscolhido = gerarNumero()
    print("Você tem", acertos, "acertos" )
    tentativa = lerNumero("tente adivinhar o número: ")

    if(tentativa == numeroEscolhido): 
        acertos += 1
        print("Parabéns, você acertou!")

    if(tentativa != numeroEscolhido): print("Você errou")
    while(1):
        querContinuar = input("Você deseja tentar de novo?(s/n): ")
        if querContinuar in ('s', 'S', 'n', 'N'):
            limparTerminal()
            break
        print("Escolha uma opção valida")
        time.sleep(2)
        limparTerminal()

    if querContinuar in ('s', 'S'): continuar = True
    if querContinuar in ('n', 'N'): continuar = False
    limparTerminal()

arquivo = open("arquivo.txt", "w")   
acertos = str(acertos)
arquivo.write(acertos)
print("Obrigado por jogar")
    
    
    
