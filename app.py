# Importa o streamlit para criar a interface
import streamlit as st

# Importa suas funções reutilizáveis do módulo tarefas.py
import tarefas

# Carrega as tarefas existentes do arquivo JSON
tarefas_lista = tarefas.carregar_tarefas()

# Título da aplicação na interface
st.title("📋 Gerenciador de Tarefas")

# Exibe as tarefas com checkbox (marcar como concluída)
for i, t in enumerate(tarefas_lista):
    # Cria uma linha com 2 colunas: checkbox | botão remover
    col1, col2 = st.columns([0.8, 0.2])  # 80% largura pro texto, 20% pro botão

    # Coluna 1: checkbox da tarefa
    with col1:
        concluida = st.checkbox(t["descricao"], value=t["concluida"], key=f"tarefa_{i}")
        if concluida != t["concluida"]:
            tarefas_lista[i]["concluida"] = concluida
            tarefas.salvar_tarefas(tarefas_lista)
            st.rerun()

    # Coluna 2: botão para remover
    with col2:
        if st.button("🗑️", key=f"remover_{i}"):
            tarefas.remover_tarefa(tarefas_lista, i)
            st.rerun()


# Linha separadora visual
st.markdown("---")

# Campo para digitar nova tarefa
nova = st.text_input("Adicionar nova tarefa:")

# Botão para adicionar a nova tarefa
if st.button("Adicionar"):
    if nova.strip():  # Verifica se não está vazia
        tarefas_lista.append({"descricao": nova.strip(), "concluida": False})
        tarefas.salvar_tarefas(tarefas_lista)
        st.rerun()  # Atualiza a interface após adicionar
