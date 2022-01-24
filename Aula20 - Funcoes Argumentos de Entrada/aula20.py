def somar(n1,n2):
    r=n1+n2
    print("Soma de " + str(n1) + " e " + str(n2) + " = " +str(r))
    print("Funcoes agora\n")

somar(5,7) #chamando a função. obs: deve passar a mesma qtd de variáveis definida (n1,n2)
somar(12,8)
somar(1,2)

def textos(*txt): #Argumentos arbitrários definido por '*'
    for t in txt:
        print(t)

textos("CFB Cursos","Python","Anderson","Sampaio")

def somar_(*num):#Argumentos arbitrários. quando ñ definimos a qtd de variáveis
    r=0
    for n in num:
        r+=n
    print("\nSoma = " + str(r))
    print("Funcoes agora\n")

somar_(5,2,3,2,13)

def carros(c="Golf"): #vc pode definir um valor padrão para a função caso não seja passado nenhum valor ao chama-la
    print("Modelo: " + c)

carros("Ford") #ex: passando um valor
carros() #ex; sem passar valor (retorna golf)   