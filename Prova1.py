#Criando as variáveis do usuário
nome = str(input('Nome: '))
idade = int(input('Idade: '))
altura = float(input('Altura: '))
maior_de_idade = bool

#Condição se for maior de idade
if idade >= 18:
    maior_de_idade = True
else:
    maior_de_idade = False

#Printando os tipos da variáveis e a mensagem para o usuário
print(type(nome), type(idade), type(altura), type(maior_de_idade))
print(f'Olá, {nome}! Sua idade é de {idade} anos e sua altura é de {altura:.2f} m, ou seja, você é {'maior de idade' if maior_de_idade == True else 'menor de idade'}.')
