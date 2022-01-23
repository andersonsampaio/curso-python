#======================
#Parte 1
print("==================")
print("Inicio parte 01")
carros=["HRV","Golf","Argo","Focus"]

for x in carros: # cria um elemento 'x' para receber o valor de uma lista 'carros no ex'
    print(x)
    if(x=="Golf"):
        print("  VW")

#======================
#Parte 2
print("\n==================")
print("Inicio parte 02")
carros=["HRV","Golf","Argo","Focus"]

for x in carros: # cria um elemento 'x' para receber o valor de uma lista 'carros no ex'
    if(x=="Argo"):
        break
    print(x)

#======================
#Parte 3
print("\n==================")
print("Inicio parte 03")
for x in "CBF cursos": # cria um elemento 'x' para receber o valor de cada posição da string
    print(x)