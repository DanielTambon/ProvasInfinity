# Importa uma biblioteca que escolhe aleatoriamente um número
import random
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Número que o jogador deve adivinhar
numero_correto = random.choice(lista)
# Número máximo de tentativas
tentativas_maximas = 3
# Inicializa o número de tentativas
tentativas = 0

while tentativas < tentativas_maximas:
    # Solicita ao jogador que adivinhe o número
    usuario_escolha = int(input('Adivinhe o número (entre 1 e 10): '))
    tentativas += 1
    
    if usuario_escolha == numero_correto:
        print('\033[32mParabéns! Você acertou o número!\033[m')
        # Encerra o loop se o número estiver correto
        break
else:
    # Executado se o loop terminar sem o comando 'break'
    print(f'\033[31mQue pena! Você esgotou suas tentativas. O número correto era {numero_correto}! Mas não desista, tente novamente!\033[m')
