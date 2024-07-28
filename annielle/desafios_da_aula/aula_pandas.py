import pandas as pd

dados = {
    'nome' : ['Ana', 'Maria', 'Matheus', 'Marcos', 'Julie', 'Harvey', 'Clebs'],
    'idade' : ['15',  '30', '40', '17', '89', '19', '55'],
    'cidade' : ['Recife', 'Recife', 'Recife', 'São Paulo', 'Salvador', 'Salvador', 'Manaus']
} 

df = pd.DataFrame(data=dados)

print(df[df['cidade'] == 'Recife']) #somente pessoas de Recife

