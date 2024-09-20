nome = input('Digite o nome do contato: ')
numero = int(input('Digite o número do contato: '))
email = input('Digite o email do contato: ')

contato = {'Nome': nome, 'Número de Celular': numero, 'Email': email}

print('\033[34m\nInformações do contato:\033[m')
for chave, valor in contato.items():
    print(f'\033[32m{chave.capitalize()}: {valor}\033[m')
