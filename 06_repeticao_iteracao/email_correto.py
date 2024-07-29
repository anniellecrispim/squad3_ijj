#Cenarios BDD: (Dado / Quando / Então / E)

#Email Válido
"""eu como testador
quando rodar o script
então terei sabrei quais são os emails validos do instituto validos"""

#Email Inválido
"""eu como testador
quando rodar o script
então terei sabrei quais são os emails invalidos do instituto validos"""

#email = input ('digite seu email: ')
emails = ['annie@gmail.com', 'brother@jogajuntoinstituto']

emails = ['annie@gmail.com', 'brother@jogajuntoinstituto']
email_ijj = 'jogajuntoinstituto'

for email in emails:
    partes = email.split("@")
    dominio = partes[-1]  
    if dominio == email_ijj:
        print(f"{email} contém o domínio {email_ijj}.")
    else:
        print(f"{email} não contém o domínio {email_ijj}.")

 


