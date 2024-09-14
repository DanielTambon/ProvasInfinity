# Número inserido pelo usuário
num = int(input('Digite um número: '))

# Verificação se o número é postivo, negativo ou zero
if num > 0:
    print('\033[33mO número é positivo.\033[m')
elif num < 0:
    print('\033[31mO número é negativo.\033[m')
else:
    print('\033[34mO número é zero.\033[m')