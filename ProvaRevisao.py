# Criando um dicionário para armazenar os produtos e preços
estoque = {}

# Pedindo ao usuário para inserir o nome e o preço de 5 produtos
for i in range(5):
    nome_produto = input(f"Digite o nome do produto {i+1}: ")
    preco_produto = float(input(f"Digite o preço do produto {i+1}: "))
    estoque[nome_produto] = preco_produto

# Calculando o valor total da compra
valor_total = sum(estoque.values())

# Exibindo o valor total da compra
print(f"O valor total da compra é: R$ {valor_total:.2f}")
