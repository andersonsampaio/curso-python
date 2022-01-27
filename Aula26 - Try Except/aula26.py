# try:
#     print(x)
# except NameError:
#     print("X nao definido")
# except:
#     print("Erro desconhecido")

# #================================
# y=10
# try:
#     print(y)
# except:
#     print("Erro no programa")
# else:
#     print("Tudo Certo")
# finally:
#     print("Fim do tratamento")

# #================================
# num=-10

# if num < 1:
#     raise Exception("Valor nao permitido")

#================================
num_="Bruno"

if not type(num_) is int:
    raise Exception("Somente numeros permitidos")
else:
    print(str(num_))