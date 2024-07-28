from faker import Faker
import pandas as pd

from typing import  List, Dict

fake = Faker('pt_BR')

def gerar_personas() -> dict:
 
    data = {
        'nome': fake.name(),
        'cidade': fake.city(),
        'idade': fake.random_int(min=18, max=30),
    }

    return data

def gerar_personas_quant(quantPersonas: int) -> List[Dict]:
    return [gerar_personas() for _ in range(quantPersonas)]


lista_de_personas = gerar_personas_quant(20)

df_lista_personas = pd.DataFrame(lista_de_personas)

print(df_lista_personas)

df_lista_personas.to_csv('lista_de_personas.csv', index=False)