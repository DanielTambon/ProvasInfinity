import flet as ft

def main(page: ft.Page):
    page.title = "Lista de Tarefas"
    
    # Lista para armazenar as tarefas
    task_list = ft.Column()
    
    # Campo de entrada de texto
    task_input = ft.TextField(label="Digite uma tarefa")
    
    # Função para adicionar tarefa
    def add_task(e):
        if task_input.value.strip():  # Verifica se o campo não está vazio
            task_list.controls.append(ft.Text(task_input.value))
            task_input.value = ""  # Limpa o campo de entrada
            page.update()  # Atualiza a interface
    
    # Botão para adicionar a tarefa
    add_button = ft.ElevatedButton("Adicionar", on_click=add_task)
    
    # Adiciona os elementos à página
    page.add(task_input, add_button, task_list)

ft.app(target=main)     