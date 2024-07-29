import pandas as pd


dados = pd.read_csv('./dados_ficticios.csv')

df = pd.DataFrame(data=dados)

def listMatchCase():
    match menu:
        case 1:
            print(f'LISTA de todos{df}')
        case 2:
            print(f'LISTA ACIMAD DE 40 {acima40}')
        case 3:
            print(f'LISTA DE RENDA ACIMA DE 5 MIL {renda5mil}')
        case 4:
            print(f'LISTA DE RENDA ACIMA DE 15 MIL {renda15mil}')


acima40 = (df[df['idade'] > 39 ])
renda5mil = (df[df['renda'] > 5000.00])
renda15mil = (df[df['renda'] > 15000.00])

menu = int(input(f'Selecione para o print \n1.Todos\n2.Acima de 40 anos\n3.Acima de 5 mil de renda\n4.Acima de 15 mil de renda '))
listMatchCase()


