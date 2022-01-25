class Carro:
    velMax=0
    ligado=False
    cor=""
    #método construtor '__init__' cria-se as variáveis de entrada
    # 'self' pq ele irá receber dentro da própria classe Carro
    def __init__(self,v,l,c):
        self.velMax=v
        self.ligado=l
        self.cor=c
    #método Mostrar 
    def mostrar(self):
        print("Velocidade Maxima: " + str(self.velMax))
        print("Cor..............: " + self.cor)
        estado="sim" if self.ligado else "nao"
        print("Ligado...........: " + estado)
        print("----------------------------")
    def ligar(self):
        self.ligado=True
    def desligar(self):
        self.ligado=False
    def andar(self):
        if(self.ligado):
            print("Andando")
        else:
            print("Carro desligado")

c1=Carro(200,False,"Preto") #chamando o construtor e passando os valores
c2=Carro(120,False,"Branco")
c3=Carro(350,False,"Vermelho")

c1.ligar()

c1.mostrar()
c2.mostrar()
c3.mostrar()

c1.andar()
c2.andar()