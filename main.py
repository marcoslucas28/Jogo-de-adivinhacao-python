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

print("Bem-vindo ao jogo de adivinhação!")

while(continuar):
    numeroEscolhido = gerarNumero()
    
    
    
