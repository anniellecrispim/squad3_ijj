import requests
from faker import Faker

faker = Faker('pt_BR')

def dados_cadastro() -> dict: 
    data= {
   "username": faker.user_name(),
    "email": faker.email(),
    "password": faker.password(digits=8 ) ,
    "phone": faker.phone_number(),
    "address": faker.address(),
    "cpf": faker.cpf()  
    }
    return data

#dados = dados_cadastro()

#print("Dados enviados:", dados)

def cadastra(dados):
    response = requests.post(f'https://desafiopython.jogajuntoinstituto.org/api/users/', json=dados)
    print(response.text)
    return response


def login(dados):
    response = requests.post(f'http://desafiopython.jogajuntoinstituto.org/api/users/login/', json=dados)

    return response

def status(response):

    return response.json,response.text
    

def main():
    dados = dados_cadastro()

    print("Dados enviados:", dados)
    print(status(cadastra(dados)))
    #cadastra()
    #login()
    print(status(login(dados)))

    
   
if __name__ == "__main__": 

    main()