
print(f'Bem vindo ao PETSHOP da LUCRASHOP ')
nome = ('Qual o nome do pet?')
idade_pet = int(input('Por favor, insira a idade do seu pet '))
porte = int(input('Digite apenas número\n1.Porte pequeno\n2.Porte Médio\n3.Porte Grande '))
idade_pet_convertida = idade_pet*7

# g = 55, m = 45, p= 45
def idade(tamanho_pet: int, idade: int) -> int:
    if tamanho_pet == 1 or 2:
        lucro_pet_pequeno = idade*45
        return lucro_pet_pequeno
    else:
        lucro_pet_grande = idade*55
        return lucro_pet_grande

conta_final = idade(porte, idade_pet_convertida)

print(f'Olá, {nome} tem {idade_pet_convertida} e nos últimos 12 meses o lucro com esse animal foi de {conta_final}, caso esse animal tomado 10 banhos em 12 meses')