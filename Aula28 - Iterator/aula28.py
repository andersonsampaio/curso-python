carros=["HRV","Polo","Jetta","Cruze","Fusion","Golf","Focus","Onyx","Fit"]

#iterator 'iter' peccore a lista utilizando o while sem precisar
#utilizar o contador 'i=0''i+=1'. Ele iria peccorer a lista
#com o 'next' e quando chegar ao final irá sinalizar com
#'stopIteration'
itCarros=iter(carros)

while itCarros:
    try:
        print(next(itCarros))
    except StopIteration:
        break