#Criando o somatório e a lista de números
soma = 0
lista = []

#Geração do loop de digitação dos números
while True:
    num = int(input('\033[33mDigite um número: \033[m'))
    soma += num
    if num != 0:
        lista.append(num) 
    if num == 0:
        break
    
#Variável para fazer o cálculo da média aritimética
media = soma / len(lista)

#Imprimindo os resultados da soma e da média
print(f'\033[31mVocê digitou {len(lista)} números e a soma entre eles foi {soma}, enquanto a média aritimética entre eles deu {media:.2f}, com duas casas decimais.\033[m')
