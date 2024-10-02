# Digitação dos valores que serão comparados na função
num1 = int(input('\033[34mDigite o primeiro número: \033[m'))
num2 = int(input('\033[31mDigite o segundo número: \033[m'))
num3 = int(input('\033[33mDigite o terceiro número: \033[m'))

# Criação da função que analisa qual é o maior número entre os 3 valores digitados
def maior_numero(num1, num2, num3):
    lista = []
    # Usando extend() para adicionar múltiplos valores à lista
    lista.extend([num1, num2, num3])
    maior_valor = max(lista)
    return maior_valor

# Passando os argumentos para a função
print(f'\033[32mO maior valor entre os 3 valores digitados foi o número {maior_numero(num1, num2, num3)}!\033[m')
