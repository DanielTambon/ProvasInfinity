# Importa uma biblioteca que escolhe aleatoriamente um número
import random

# Cria uma função para lançar os dados
def lancar_dado():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    print(f'''\033[34mO valor do primeiro dado é: {dado1}\033[m
\033[31mO valor do segundo dado é: {dado2}\033[m
\033[35mA soma dos dois dados é: {dado1 + dado2}\033[m''')

lancar_dado()
