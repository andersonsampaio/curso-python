#Tupla é determinada pelo parÊnteses'()' a diferença
#para Lista é que a tupla não se muda os elementos

t_carros=("HRV","Golf","Argo")

#para editar a tupla basta converter para uma lista 
#por meio de casts e depois retornar a tupla

l_carros=list(t_carros)
l_carros[2]="Focus"
t_carros=tuple(l_carros)

for x in t_carros:
    print(x)
