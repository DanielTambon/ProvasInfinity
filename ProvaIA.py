print('\033[34mCÁLCULO DA MÉDIA DOS ALUNOS\033[m')

# Solicitação da quantidade alunos e a criação das listas de nomes, notas e medias
quantidade_de_alunos = int(input('Qual é a quantidade de alunos? '))
lista_nome = []
lista_nota1 = []
lista_nota2 = []
lista_nota3 = []
lista_media = []

# Criação do loop de apresentação dos alunos, suas respectivas notas e cálculo de sua média
for i in range(quantidade_de_alunos):
    nome = input('Nome: ')
    lista_nome.append(nome)
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    nota3 = float(input('Nota 3: '))
    lista_nota1.append(nota1)
    lista_nota2.append(nota2)
    lista_nota3.append(nota3)
    media = (nota1 + nota2 + nota3) / 3
    lista_media.append(media)

# Cálculo da média da turma
media_turma = sum(lista_media) / quantidade_de_alunos

# Criação do loop de impressão dos alunos, suas respectivas notas e sua média
for i in range(quantidade_de_alunos):
    print(f'''{'='*20}
Aluno {lista_nome[i]}:
Nota 1 = {lista_nota1[i]:.1f}
Nota 2 = {lista_nota2[i]:.1f}
Nota 3 = {lista_nota3[i]:.1f}
Média = {lista_media[i]:.1f}''')
    # Verificação e impressão se o aluno foi aprovado ou reprovado
    print('\033[32mAPROVADO!\033[m' if lista_media[i] >= 7 else '\033[31mREPROVADO!\033[m')
    print('='*20)

# Impressão da média da turma e caso for acima de 7 será verde e se for abaixo de 7 será vermelha
print(f'\033[32mA média da turma foi {media_turma:.1f}\033[m' if lista_media[i] >= 7 else f'\033[31mA média da turma foi {media_turma:.1f}\033[m')
