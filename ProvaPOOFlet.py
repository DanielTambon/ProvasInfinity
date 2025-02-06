import flet as ft
from datetime import datetime

class Cliente:
    def __init__(self, nome, telefone, email, cliente_id):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.cliente_id = cliente_id

class Quarto:
    def __init__(self, numero, tipo, preco_diaria):
        self.numero = numero
        self.tipo = tipo
        self.preco_diaria = preco_diaria
        self.disponivel = True

class Reserva:
    def __init__(self, cliente, quarto, check_in, check_out):
        self.cliente = cliente
        self.quarto = quarto
        self.check_in = check_in
        self.check_out = check_out
        self.status = "Ativa"
        quarto.disponivel = False

class GerenciadorDeReservas:
    def __init__(self):
        self.reservas = []
        self.clientes = []
        self.quartos = []

    def verificar_disponibilidade(self, tipo):
        return [q for q in self.quartos if q.tipo == tipo and q.disponivel]

    def criar_reserva(self, cliente_id, numero_quarto, check_in, check_out):
        cliente = next((c for c in self.clientes if c.cliente_id == cliente_id), None)
        quarto = next((q for q in self.quartos if q.numero == numero_quarto and q.disponivel), None)
        
        if cliente and quarto:
            reserva = Reserva(cliente, quarto, check_in, check_out)
            self.reservas.append(reserva)
            return reserva
        return None
    
    def cancelar_reserva(self, reserva):
        if reserva in self.reservas:
            reserva.quarto.disponivel = True
            reserva.status = "Cancelada"
            self.reservas.remove(reserva)

    def listar_reservas(self):
        return self.reservas

def main(page: ft.Page):
    page.title = "Refúgio dos Sonhos - Gerenciador de Reservas"
    page.scroll = "auto"
    page.bgcolor = "#4B3B30"  # Cor de fundo marrom
    page.theme_mode = "dark"
    
    gerenciador = GerenciadorDeReservas()
    
    clientes_lista = ft.ListView(expand=True)
    quartos_lista = ft.ListView(expand=True)
    reservas_lista = ft.ListView(expand=True)
    
    def atualizar_listas():
        clientes_lista.controls.clear()
        quartos_lista.controls.clear()
        reservas_lista.controls.clear()
        
        for cliente in gerenciador.clientes:
            clientes_lista.controls.append(ft.Text(f"ID: {cliente.cliente_id} - {cliente.nome}, {cliente.telefone}, {cliente.email}"))
        
        for quarto in gerenciador.quartos:
            status = "Disponível" if quarto.disponivel else "Ocupado"
            quartos_lista.controls.append(ft.Text(f"Quarto {quarto.numero} ({quarto.tipo}) - R$ {quarto.preco_diaria}/dia - {status}"))
        
        for reserva in gerenciador.listar_reservas():
            reservas_lista.controls.append(ft.Text(f"Cliente: {reserva.cliente.nome}, Quarto: {reserva.quarto.numero}, Check-in: {reserva.check_in}, Check-out: {reserva.check_out}, Status: {reserva.status}"))
        
        page.update()
    
    def adicionar_cliente(e):
        cliente = Cliente(nome_input.value, telefone_input.value, email_input.value, len(gerenciador.clientes) + 1)
        gerenciador.clientes.append(cliente)
        nome_input.value = ""
        telefone_input.value = ""
        email_input.value = ""
        atualizar_listas()
    
    nome_input = ft.TextField(label="Nome")
    telefone_input = ft.TextField(label="Telefone")
    email_input = ft.TextField(label="Email")
    botao_adicionar_cliente = ft.ElevatedButton("Adicionar Cliente", on_click=adicionar_cliente)
    
    def adicionar_quarto(e):
        quarto = Quarto(int(numero_quarto_input.value), tipo_quarto_input.value, float(preco_quarto_input.value))
        gerenciador.quartos.append(quarto)
        numero_quarto_input.value = ""
        tipo_quarto_input.value = ""
        preco_quarto_input.value = ""
        atualizar_listas()
    
    numero_quarto_input = ft.TextField(label="Número do Quarto")
    tipo_quarto_input = ft.TextField(label="Tipo do Quarto")
    preco_quarto_input = ft.TextField(label="Preço da Diária")
    botao_adicionar_quarto = ft.ElevatedButton("Adicionar Quarto", on_click=adicionar_quarto)
    
    def reservar_quarto(e):
        cliente_id = int(cliente_id_input.value)
        numero_quarto = int(numero_quarto_input_reserva.value)
        check_in = check_in_input.value
        check_out = check_out_input.value
        gerenciador.criar_reserva(cliente_id, numero_quarto, check_in, check_out)
        cliente_id_input.value = ""
        numero_quarto_input_reserva.value = ""
        check_in_input.value = ""
        check_out_input.value = ""
        atualizar_listas()
    
    cliente_id_input = ft.TextField(label="ID do Cliente")
    numero_quarto_input_reserva = ft.TextField(label="Número do Quarto")
    check_in_input = ft.TextField(label="Check-in (YYYY-MM-DD)")
    check_out_input = ft.TextField(label="Check-out (YYYY-MM-DD)")
    botao_reservar = ft.ElevatedButton("Reservar Quarto", on_click=reservar_quarto)
    
    page.add(
        ft.Column([
            ft.Text("Cadastro de Cliente", size=20, weight=ft.FontWeight.BOLD),
            nome_input, telefone_input, email_input, botao_adicionar_cliente,
            clientes_lista,
            ft.Divider(),
            ft.Text("Cadastro de Quarto", size=20, weight=ft.FontWeight.BOLD),
            numero_quarto_input, tipo_quarto_input, preco_quarto_input, botao_adicionar_quarto,
            quartos_lista,
            ft.Divider(),
            ft.Text("Criar Reserva", size=20, weight=ft.FontWeight.BOLD),
            cliente_id_input, numero_quarto_input_reserva, check_in_input, check_out_input, botao_reservar,
            reservas_lista
        ], scroll=ft.ScrollMode.AUTO)
    )
    
    page.update()

ft.app(target=main)
