import os
os.system('cls') #limpar tela

#======================
#Parte 1
print("\n=======================")
print("   Parte 01\n")
i=0
while i<=9:
    print(i)
    i+=1
    if(i>=5):
        break
print("\nFim do Loop")

#======================
#Parte 2
print("\n=======================")
print("   Parte 02\n")
carros=["HRV","Golf","Argo","Onix","Focus"]
i=0
tam=len(carros)
while i<tam:
    print(carros[i])
    i+=1
print("\nFim do Loop")

#======================
#Parte 3
print("\n=======================")
print("   Parte 03\n")
carros=[]
carro=input("Digite o nome do novo carro: ")

while carro != "-1":
    carros.append(carro)
    carro=input("Digite o nome do novo carro: ")

os.system('cls')
for x in carros:
    print(x)
    
print("\nFim do Loop")

