# Importando o módulo os
import os

# Obtém o diretório atual onde o script está sendo executado
diretorio_atual = os.getcwd()

# Lista os arquivos e pastas no diretório atual
itens = os.listdir(diretorio_atual)

# Exibe cada item individualmente
for item in itens:
    print(item)
