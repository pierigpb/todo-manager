
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


def remover_tarefa(tarefas, indice):
    """Remove a tarefa da lista com base no índice."""
    if 0 <= indice < len(tarefas):
        del tarefas[indice]
        salvar_tarefas(tarefas)       