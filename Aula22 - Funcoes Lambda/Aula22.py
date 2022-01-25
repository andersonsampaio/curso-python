#Função LAMBDA são funções anônimas. A primeira etapa deni-se as váriaveis
# 'a,b'após o ':' faz a expressão desejada 'a+b'

soma=lambda a,b:a+b
mult=lambda a,b,c:(a+b)*c

#na chamada da função passa-se os valores
print(soma(2,5)) 
print(mult(2,5,3))

#ou já faz função e valores direto:
print((lambda a,b:a+b)(3,2))

#ou passar uma função:
r=lambda x,func:x+func(x)

res=r(2,lambda x:x*x)
print(res)
