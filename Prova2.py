#Velocidade do usuário
velocidade = int(input('Qual é a velocidade atual do carro? '))

#Análise de multa
if velocidade > 80:
    print('\033[31mMULTADO! Você excedeu o limite permitido que é de 80Km/h\033[m')
    print(f'\033[31mVocê deve pagar uma multa de R$\033[m \033[31m{(velocidade - 80)*20}\033[m')
    print('\033[33mTenha um bom dia! Dirija com segurança!\033[m')
else:
    print('\033[33mTenha um bom dia! Dirija com segurança!\033[m')
