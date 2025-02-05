class Veiculo:
    def movimentar(self):
        print("Veículo está em movimento.")

class Carro(Veiculo):
    def movimentar(self):
        print("Carro está dirigindo.")

class Moto(Veiculo):
    def movimentar(self):
        print("Moto está acelerando.")

# Testando as classes
veiculo = Veiculo()
veiculo.movimentar()  # Saída: Veículo está em movimento.

carro = Carro()
carro.movimentar()  # Saída: Carro está dirigindo.

moto = Moto()
moto.movimentar()  # Saída: Moto está acelerando.
