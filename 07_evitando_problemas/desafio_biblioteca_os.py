import os
import random

#diretorio atual
diretorio_atual = os.getcwd()
print(diretorio_atual)

#mudei o diretorio
novo_diretorio = os.chdir('C:\\Users\\opala\\OneDrive\\Documentos\\IJJ')

#diretorio atual
diretorio_atual = os.getcwd()
print(diretorio_atual)

#criando a lista usando random
list = []
n = 10
for i in range(n):
    list.append(random.randint(1, 100))

print(list)

#criar pasta
try:
    os.mkdir(os.mkdir('C:\\Users\\opala\\OneDrive\\Documentos\\IJJ\\pastanova'))
except FileExistsError:
    print(f"A pasta já existe.")


#mudei o diretorio
novo_diretorio = os.chdir('C:\\Users\\opala\\OneDrive\\Documentos\\IJJ\\pastanova')

#diretorio atual
diretorio_atual = os.getcwd()
print(diretorio_atual)


#salvar lista

with open('list.txt', 'w') as arquivo:
    [arquivo.write(f"{list}\n") for list in list]


