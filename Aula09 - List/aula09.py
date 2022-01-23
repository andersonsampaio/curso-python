carros=["HRV","Golf","Argo","Focus"]
carros.append("Fit") #comando 'append' adiciona elementos na LIST
carros.append("Fusion")
carros.append("Polo")

carros.remove("Fusion") # comando 'remove' remove da lista
carros.pop() #'pop' remove o último argumento da lista
del carros[2] # 'del' remove de acordo com a posição indicada

#carros.clear() # 'clear' limpa toda a lista

#carros2=list(carros) # copiar uma lista para outra lista

carros2=["Fusca","147","Brasilia","Celta"]
carros3=carros+carros2

print(str(len(carros3)) + " carros na lista")
# comando 'len' retorna tamanho da lista
# comando 'str' é um cast usado para converter em string e poder imprimir com o 'print'
print(carros3)