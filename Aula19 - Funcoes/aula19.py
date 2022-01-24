n1=15
n2=25

def somar():
    r=n1+n2
    print("Soma de " + str(n1) + " e " + str(n2) + " = " +str(r))
    print("Funcoes agora\n")

def subtrair():
    r=n1-n2
    print("Subtracao de " + str(n1) + " e " + str(n2) + " = " +str(r))
    print("Funcoes agora\n")

def multiplicacao():
    r=n1*n2
    print("Multiplicacao de " + str(n1) + " e " + str(n2) + " = " +str(r))
    print("Funcoes agora\n")

def divisao():
    r=n1/n2
    print("Divisao de " + str(n1) + " e " + str(n2) + " = " +str(r))
    print("Funcoes agora\n")


def calculos():
    somar()
    subtrair()
    multiplicacao()
    divisao()

calculos()