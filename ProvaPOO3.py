class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        # Atributos privados
        self._titular = titular
        self._saldo = saldo_inicial

    # Método para depositar valor
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f"Depósito de {valor} realizado com sucesso.")
        else:
            print("Valor inválido para depósito. O valor deve ser maior que zero.")

    # Método para sacar valor
    def sacar(self, valor):
        if valor > 0 and valor <= self._saldo:
            self._saldo -= valor
            print(f"Saque de {valor} realizado com sucesso.")
        else:
            print("Saldo insuficiente ou valor inválido para saque.")

    # Método para exibir saldo
    def exibir_saldo(self):
        print(f"Saldo atual da conta de {self._titular}: {self._saldo}")

# Testando a classe
conta = ContaBancaria("Maria", 1000)  # Criando a conta com saldo inicial de 1000
conta.exibir_saldo()  # Exibindo o saldo inicial

conta.depositar(500)  # Realizando um depósito
conta.exibir_saldo()  # Exibindo o saldo após o depósito

conta.sacar(200)  # Realizando um saque
conta.exibir_saldo()  # Exibindo o saldo após o saque

conta.sacar(2000)  # Tentando realizar um saque maior que o saldo
