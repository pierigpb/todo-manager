# Aqui você importa as funções que agora estão em tarefas.py
from tarefas import (
    carregar_tarefas,
    salvar_tarefas,
    listar_tarefas,
    adicionar_tarefa,
    marcar_concluida,
)

# Este é o fluxo principal do programa
def menu():
    tarefas = carregar_tarefas()
    while True:
        print("\n1. Listar\n2. Adicionar\n3. Marcar concluída\n4. Sair")
        escolha = input("Escolha uma opção: ").strip()
        if escolha == "1":
            listar_tarefas(tarefas)
        elif escolha == "2":
            adicionar_tarefa(tarefas)
        elif escolha == "3":
            marcar_concluida(tarefas)
        elif escolha == "4":
            break
        else:
            print("Opção inválida.")

# Isso garante que o programa só execute quando for rodado diretamente
if __name__ == "__main__":
    menu()
