## Collections

Collections são estruturas de dados pré-definidas que permitem armazenar e organizar grupos de objetos relacionados na memória durante a execução de um programa.

## Listas

Uma Lista é que uma coleção ordenada de valores, separados por vírgula e dentro de colchetes [] e podemos manipular listas. 

> frutas = ['banana', 'maça']

Exemplo de manipulação: **adicionando um novo elemento a lista:**

> frutas.append('pera')

Agora a Lista terá:

> frutas = ['banana', 'maça', pera]

## Tuplas

Igualmente as listas as usamos para armazenar valores, só que são valores imutáveis. Sua sintaxe é por dentro de ()

## Dicionários

Os dicionários são coleções desordenada de itens. ´Possui uma {key} e um {valor} associado a essa key.
Sua sintaxe básica é: {'chave': 'valor'}. Utiliza-se {} para delimitar o dicionário e a chave é separada do valor por dois pontos :.

Exemplo de dicionário:
> dicionario_do_QA = {

    'nome' : {'Annielle'},
    'idade' : {'24 anos'},
    'profissao' : {'Estudante'}
> }

## Sets

Um conjunto é uma coleção desordenada de itens únicos. Em Python, os conjuntos são definidos por valores separados por vírgulas dentro de chaves {}. Diferentemente das listas ou tuplas, os conjuntos não suportam indexação ou slicing, pois os itens não são armazenados em uma ordem específica.

1. Não poderá repetir valores no set
2. Não é possível pegar o elemento pelo index (afinal nem ordenado os elementos são armazenados)
3. Seu uso é semelhante ao uso de conjuntos matemáticos por fazemos:
 > *  união, interseção e diferença
 4. Bom para remover duplicatas

## Index

O método Index() é uma maneira de encontrar a posição de um elemento na Lista: 

> frutas = ['banana', 'maça']

> encontrar_index = frutas.index('banana')

> print(encontrar_index)

No terminal:
>0

Ou seja, banana se encontra no indíce 0
