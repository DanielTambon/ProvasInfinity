# Cadastro de senha
usuario = input('\033[34mQual será seu usuário? \033[m')
senha_cadastrada = input('\033[34mQual será a sua senha? \033[m')

# Variável para definir o número máximo de tentativas
tentativas_maximas = 3

# Loop para tentar inserir a senha até 3 vezes
for tentativa in range(1, tentativas_maximas + 1):
    # Solicita que o usuário insira a senha
    senha_inserida = input('\033[36mPor favor, insira a sua senha para desbloquear o telefone: \033[m')

    # Verifica se a senha inserida está correta e calcula a quantida de tentaivas restantes
    if senha_inserida == senha_cadastrada:
        print(f'\033[32mBem-vindo, {usuario}!\033[m')
        break
    else:
        tentativas_restantes = tentativas_maximas - tentativa
        if tentativas_restantes > 0:
            print(f'\033[33mSenha incorreta. Você tem mais {tentativas_restantes} tentativa(s).\033[m')
        else:
            print('\033[31mTelefone bloqueado. Todas as tentativas foram utilizadas.\033[m')
