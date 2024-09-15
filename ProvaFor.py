# Inserindo os valores do intervalo
x, y = list(map(int, input('\033[34mDigite o início e o final de seu intervalo: \033[m').split()))

# Lista d números pares
pares = []

# Variável de verificação se existe números pares no intervalo
encontrou_pares = False

# Loop de verificação se o número é par para inseri-lo na lista
for i in range(x, y + 1):
    if i % 2 == 0:
        pares.append(i)
        encontrou_pares = True

# Condições para impressão da soma se tiver números pares ou a impressão de que não há
if encontrou_pares:
    print(f'\033[32mA soma dos números pares foi {sum(pares)}!\033[m')
else:
    print('\033[31mNão há números pares no intervalo!\033[m')
