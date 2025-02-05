import flet as ft

def main(page):
    # Função chamada quando o botão de envio é clicado
    def on_submit_click(e):
        # Recupera os dados inseridos nos campos de texto
        nome = name_field.value
        email = email_field.value
        mensagem = message_field.value
        
        # Exibe a mensagem de confirmação
        confirmation_text.value = f"Formulário enviado com sucesso!\nNome: {nome}\nEmail: {email}\nMensagem: {mensagem}"
        confirmation_text.update()

    # Criando os campos de texto para o formulário
    name_field = ft.TextField(label="Nome", autofocus=True)
    email_field = ft.TextField(label="Email", keyboard_type=ft.KeyboardType.EMAIL)
    message_field = ft.TextField(label="Mensagem", multiline=True)  # Corrigido aqui
    
    # Botão de envio
    submit_button = ft.ElevatedButton("Enviar", on_click=on_submit_click)

    # Texto de confirmação
    confirmation_text = ft.Text()

    # Adicionando os componentes à página
    page.add(name_field, email_field, message_field, submit_button, confirmation_text)

# Inicializando a aplicação Flet
ft.app(target=main)