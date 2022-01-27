import random
import os

os.system('cls')

erros=0
sorteado=random.randrange(0,100)
jogador=int(input("Digite seu número: "))

while (sorteado!=jogador):
    os.system('cls')
    if(sorteado>jogador):
        print("Erro, o número é maior")
    elif(sorteado<jogador):
        print("Erro, número é menor")
    erros+=1
    jogador=int(input("Digite seu número: "))

print("Número " + str(jogador) + ", você acertou em " + str(erros+1) + " tentativas.")