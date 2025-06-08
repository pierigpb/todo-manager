
import json
import os

DATA_FILE = "data.json"

def carregar_tarefas():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def salvar_tarefas(tarefas):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(tarefas, f, indent=2, ensure_ascii=False)

def listar_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa.")
        return
    for i, t in enumerate(tarefas):
        status = "✔" if t["concluida"] else "✘"
        print(f"{i+1}. [{status}] {t['descricao']}")

def adicionar_tarefa(tarefas):
    descricao = input("Descrição da tarefa: ").strip()
    if not descricao:
        print("Tarefa vazia. Ignorado.")
        return
    tarefas.append({"descricao": descricao, "concluida": False})
    salvar_tarefas(tarefas)

def marcar_concluida(tarefas):
    listar_tarefas(tarefas)
    try:
        idx = int(input("Número da tarefa concluída: ")) - 1
        if 0 <= idx < len(tarefas):
            tarefas[idx]["concluida"] = True
            salvar_tarefas(tarefas)
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada inválida.")

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

if __name__ == "__main__":
    menu()
