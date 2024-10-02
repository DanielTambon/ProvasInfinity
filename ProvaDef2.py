num1 = int(input('\033[34mDigite o primeiro número: \033[m'))
num2 = int(input('\033[31mDigite o segundo número: \033[m'))
num3 = int(input('\033[33mDigite o terceiro número: \033[m'))

def maior_numero(num1, num2, num3):
    lista = []
    lista.extend([num1, num2, num3])
    maior_valor = max(lista)
    return maior_valor
    
print(f'\033[32mO maior valor entre os 3 valores digitados foi o número {maior_numero(num1, num2, num3)}!\033[m')
