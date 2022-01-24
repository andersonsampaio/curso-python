#Chave/Key - Valor/Value
carro={
    "Fabricante":"Honda",
    "Modelo":"Hrv",
    "Ano":"2016",
    "Cor":"Prata"
}

carro["Cambio"]="Automatico" #Adicionar chave e valor

# carro.pop("Cambio") #remover chave
del carro["Cambio"] #remover chave

fab=carro["Fabricante"] #entre '[]' imprime valores
# fab=carro.get("Fabricante") #imprime valores

#print(fab)

carro["Cor"]="Preto"

for x in carro:
    print(x) #imprime chave
    print(carro[x]) #imprime valor

print("Tamanho do Dictionary: "+ str(len(carro)))

#carro.clear() #remove todas as chaves

if "Modelo" in carro:
    print("\nSIM, modelo é uma chave")

print("\n================")
for c,v in carro.items():
    print(c + ": " + v)

#=====================================
# Dictionary dentro de Dictonary

carros={
    "Carro1":{
        "Fabricante":"Honda",
        "Modelo":"HRV"
    },
    "Carro2":{
        "Fabricante":"Volks",
        "Modelo":"Golf"
    },
    "Carro3":{
        "Fabricante":"Ford",
        "Modelo":"Focus"
    }
}

print("==============")
print("Parte 03\n")
print(carros["Carro1"])
print(carros["Carro1"]["Fabricante"])



Carro1={
    "Fabricante":"Honda",
    "Modelo":"HRV"
}

Carro2={
    "Fabricante":"Volks",
    "Modelo":"Golf"
}

Carro3={
    "Fabricante":"Ford",
    "Modelo":"Focus"
}

Carros_={
    "C1":Carro1,
    "C2":Carro2,
    "C3":Carro3
}

print(Carros_["C1"])