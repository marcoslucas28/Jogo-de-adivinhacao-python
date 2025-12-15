from random import randint

def gerarNumero():
    n = randint(0, 10)
    return n

continuar = True

while(continuar):
    numeroEscolhido = gerarNumero()
    print("Bem-vindo ao jogo de adivinhação!")
    
    