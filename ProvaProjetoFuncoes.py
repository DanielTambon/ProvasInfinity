# task_manager.py
import sys
import time

# Lista de tarefas, onde cada tarefa é um dicionário
tarefas = []

# Função para adicionar uma tarefa
def adicionar_tarefa(nome, descricao, prioridade, categoria):
    tarefa = {
        "nome": nome,
        "descricao": descricao,
        "prioridade": prioridade,
        "categoria": categoria,
        "concluida": False
    }
    tarefas.append(tarefa)
    print(f"Tarefa '{nome}' adicionada com sucesso!")

# Função para listar todas as tarefas
def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return
    for idx, tarefa in enumerate(tarefas, 1):
        status = "Concluída" if tarefa["concluida"] else "Pendente"
        print(f"{idx}. {tarefa['nome']} - {tarefa['descricao']} | Prioridade: {tarefa['prioridade']} | Categoria: {tarefa['categoria']} | Status: {status}")

# Função para marcar uma tarefa como concluída
def concluir_tarefa(id_tarefa):
    try:
        tarefa = tarefas[id_tarefa - 1]
        tarefa["concluida"] = True
        print(f"Tarefa '{tarefa['nome']}' marcada como concluída.")
    except IndexError:
        print("ID de tarefa inválido.")

# Função para filtrar tarefas por prioridade
def filtrar_por_prioridade(prioridade):
    tarefas_filtradas = [t for t in tarefas if t["prioridade"].lower() == prioridade.lower()]
    if tarefas_filtradas:
        for tarefa in tarefas_filtradas:
            status = "Concluída" if tarefa["concluida"] else "Pendente"
            print(f"{tarefa['nome']} - {tarefa['descricao']} | Prioridade: {tarefa['prioridade']} | Categoria: {tarefa['categoria']} | Status: {status}")
    else:
        print(f"Nenhuma tarefa encontrada com a prioridade '{prioridade}'.")

# Função para filtrar tarefas por categoria
def filtrar_por_categoria(categoria):
    tarefas_filtradas = [t for t in tarefas if t["categoria"].lower() == categoria.lower()]
    if tarefas_filtradas:
        for tarefa in tarefas_filtradas:
            status = "Concluída" if tarefa["concluida"] else "Pendente"
            print(f"{tarefa['nome']} - {tarefa['descricao']} | Prioridade: {tarefa['prioridade']} | Categoria: {tarefa['categoria']} | Status: {status}")
    else:
        print(f"Nenhuma tarefa encontrada com a categoria '{categoria}'.")

# Função para exibir o menu
def exibir_menu():
    print("\nGerenciador de Tarefas")
    print("1. Adicionar Tarefa")
    print("2. Listar Tarefas")
    print("3. Marcar Tarefa como Concluída")
    print("4. Filtrar Tarefas por Prioridade")
    print("5. Filtrar Tarefas por Categoria")
    print("6. Sair")

# Função principal
def main():
    while True:
        exibir_menu()
        escolha = input("\nEscolha uma opção: ")
        
        if escolha == "1":
            nome = input("Nome da Tarefa: ")
            descricao = input("Descrição da Tarefa: ")
            prioridade = input("Prioridade (Alta, Média, Baixa): ")
            categoria = input("Categoria: ")
            adicionar_tarefa(nome, descricao, prioridade, categoria)
        
        elif escolha == "2":
            listar_tarefas()
        
        elif escolha == "3":
            try:
                id_tarefa = int(input("ID da Tarefa a ser concluída: "))
                concluir_tarefa(id_tarefa)
            except ValueError:
                print("ID inválido. Por favor, insira um número.")
        
        elif escolha == "4":
            prioridade = input("Digite a prioridade (Alta, Média, Baixa) para filtrar: ")
            filtrar_por_prioridade(prioridade)
        
        elif escolha == "5":
            categoria = input("Digite a categoria para filtrar: ")
            filtrar_por_categoria(categoria)
        
        elif escolha == "6":
            print("Saindo...")
            time.sleep(2)
            print("Até logo!")
            sys.exit()
        
        else:
            print("Opção inválida, por favor, tente novamente.")

# Executa o programa
if __name__ == "__main__":
    main()