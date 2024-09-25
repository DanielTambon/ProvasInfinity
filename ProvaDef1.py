# Criação da média de cálculo do aluno
def media_do_aluno():
    nota1 = float(input('\033[34mDigite a primeira nota: \033[m'))
    nota2 = float(input('\033[33mDigite a segunda nota: \033[m'))
    nota3 = float(input('\033[31mDigite a terceira nota: \033[m'))
    media = (nota1 + nota2 + nota3) / 3
    return media

# Imprime o resultado da média do aluno
print(f'\033[32mA média do aluno foi {media_do_aluno():.1f}!\033[m')
