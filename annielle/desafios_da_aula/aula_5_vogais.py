#programa que leia a quantidade de letras vogais está na palavra: a,e,i,o,u 

palavra = input('Digite uma palavra: \n')
vogais = ('a', 'e', 'i', 'o', 'u')
contador = 0

for i in palavra.lower():
    if i in vogais:
        contador += 1
print(f'A palavra ou mais {palavra} contém {contador} vogais')