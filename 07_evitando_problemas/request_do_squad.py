vitor_back= 79009080
tamires_ana = '07179260'
caio= 41194105
annielle = 58200000
julia = 25268160

def dicionario_de_registro() -> dict:
  data = {
    'Vitor Back' : {'cep': '79009-080', 'logradouro': 'Rua Apulcro Brasil','complemento': '', 'unidade': '', 'bairro': 'Vila Planalto', 'localidade': 'Campo Grande', 'uf': 'MS','ibge': '5002704','gia': '','ddd': '67', 'siafi': '9051'},
    'Tamires Ana' : {'cep': '07179-260','logradouro': 'Rua Zeferino Alves de Oliveira', 'complemento': '', 'unidade': '', 'bairro': 'Jardim Ponte Alta I', 'localidade': 'Guarulhos', 'uf': 'SP', 'ibge': '3518800', 'gia': '3360', 'ddd': '11','siafi': '6477'},
    'Annielle': {'cep': '58200-000', 'logradouro': '', 'complemento': '', 'unidade': '', 'bairro': '', 'localidade': 'Guarabira', 'uf': 'PB', 'ibge': '2506301','gia': '', 'ddd': '83', 'siafi': '2027'},
    'Julia':  { 'cep': '25268-160', 'logradouro': 'Rua J', 'complemento': '(Area II)', 'unidade': '', 'bairro': 'Nova Campinas', 'localidade': 'Duque de Caxias', 'uf': 'RJ', 'ibge': '3301702', 'gia': '', 'ddd': '21', 'siafi': '5833'   },    
}
  return data


dicionario = dicionario_de_registro()

def print_data():
    for pessoa, dados in dicionario.items():
        print(f"Pessoa: {pessoa}")
        for chave, valor in dados.items():
            print(f"  {chave.capitalize()}: {valor}")
        print()


print_data()