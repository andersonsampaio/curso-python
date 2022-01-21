"""
n1=5
n2=2
x=complex(n1,n2) #n. complexo - forma 1
x=complex(22+4j)  #n. complexo - forma 2

print(x.real)
print(x.imag)
"""

x=["Carro","Aviao","Navio",1,58.3,True] #List / Array
x[0]="Onibus" #Alterando elemento na LIST

x=("Carro","Aviao","Navio",1,58.3,True) #Tupla - ñ conseguimos alterar os valores

x=range(0,100,1) #List

x={ #Dict
    "Canal":"CBF Cursos",
    "curso":"Curso de Python",
    "nome":"Bruno"
}

x={5,7,5,7,8,9,6,5} # SET não repete valores
x=frozenset({2,5,6,7,5,6}) #bloqueia o SET
print("Valor: "+str(x))
print("Tipo: "+str(type(x)))