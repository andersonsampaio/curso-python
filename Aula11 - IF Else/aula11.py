#==============
# #Parte 01
a=10
b=5
res=0
op="+"

if op=="+": # 'ELIF'(ELSE + IF) só verifica se o IF ou ELIF anterior ñ for verdadeiro
    res=a+b
elif op=="-":
    res=a-b
elif op=="*":
    res=a*b
elif op=="/":
    res=a/b
else: # 'else' se nenhuma condição anterior satisfazer já entra nele
    print("Operador invalido")

print(str(a) + op + str(b) + " = " + str(res)) 

#==============
# #Parte 02
clima="sol"
dinheiro=301
lugar=""

if clima=="sol" and (dinheiro>300 and dinheiro<=500):
    lugar="clube"
else:
    lugar="cinema" 

print("\nVou ao "+lugar)

