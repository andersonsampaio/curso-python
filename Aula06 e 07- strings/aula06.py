curso="Curso de Python"

#========================
# Aula 06

#print(curso[9:15]) #Imprime apenas os espaços de memória que escolher
#print(curso.strip()) #'.strip' Imprime sem os espaços do início e fim
#print(curso.lower().strip()) #'.lower' imprime tudo minusculo / #'.strip' Imprime sem os espaços do início e fim
#print(curso.upper()) #'.upper' imprime tudo maiusculo
#print(curso.replace("Python","C#").strip()) #'replace' trocou Python por C# / '.strip' Imprime sem os espaços do início e fim

#a=curso.split(" ")
#print(a)

#print("Tamanho: "+str(len(curso))) #'Len' imprime tamanho

#========================
# Aula 07

#res="Python" in curso # Verifica se existe a string apontada na variável
#res="Python" not in curso # Verifica se NÃO existe a string apontada na variável

#canal="CFB Cursos"
#res=curso+" do canal "+canal #concatenação

#print(res)

#método format
cidade="Belo Horizonte"
dia=15
mes="Dezembro"
ano=2019
canal="CBF Cursos"
data="{}, {} de {} de {}\n \"{}\""

print(data.format(cidade,dia,mes,ano,canal))