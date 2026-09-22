import os
import sqlite3

PASTA_DESTINO = "modulo11"
NOME_BANCO = "gerenciador_tarefas.db"


if not os.path.exists(PASTA_DESTINO):
    os.makedirs(PASTA_DESTINO)

CAMINHO_BANCO = os.path.join(PASTA_DESTINO, NOME_BANCO)


def conectar():
   
    return sqlite3.connect(CAMINHO_BANCO)


def inicializar_modulo_tarefas():
    
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            descricao TEXT NOT NULL,
            status TEXT DEFAULT 'Pendente'
        )
    """)
    conexao.commit()
    conexao.close()


def adicionar_tarefa(descricao):
    
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO Tarefas (descricao) VALUES (?)", (descricao,))
    conexao.commit()
    conexao.close()
    print(f"\n✓ Tarefa '{descricao}' adicionada com sucesso no banco em '{CAMINHO_BANCO}'!")


def visualizar_tarefas():
    
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM Tarefas")
    tarefas = cursor.fetchall()
    conexao.close()

    print("\n==========================================")
    print("           LISTA DE TAREFAS              ")
    print("==========================================")
    if not tarefas:
        print("Nenhuma tarefa cadastrada no momento.")
    else:
        for t in tarefas:
            print(f"ID: {t[0]:<3} | Tarefa: {t[1]:<25} | Status: {t[2]}")
    print("==========================================")


def excluir_tarefa(id_tarefa):
   
    conexao = conectar()
    cursor = conexao.cursor()

   
    cursor.execute("SELECT * FROM Tarefas WHERE id = ?", (id_tarefa,))
    tarefa = cursor.fetchone()

    if tarefa:
        cursor.execute("DELETE FROM Tarefas WHERE id = ?", (id_tarefa,))
        conexao.commit()
        print(f"\n✓ Tarefa ID {id_tarefa} foi excluída com sucesso!")
    else:
        print(f"\n❌ Erro: Não existe tarefa com ID {id_tarefa}.")

    conexao.close()


def menu_principal():
    
    inicializar_modulo_tarefas()

    while True:
        print("\n=== SISTEMA DE GERENCIAMENTO DE TAREFAS (SQLITE) ===")
        print(f"Local do banco: {CAMINHO_BANCO}")
        print("1. Adicionar Tarefa")
        print("2. Visualizar Tarefas")
        print("3. Excluir Tarefa")
        print("0. Sair")

        opcao = input("\nEscolha uma opção (0-3): ").strip()

        if opcao == "1":
            desc = input("Digite a descrição da nova tarefa: ").strip()
            if desc:
                adicionar_tarefa(desc)
            else:
                print("\n❌ A descrição da tarefa não pode ser vazia.")

        elif opcao == "2":
            visualizar_tarefas()

        elif opcao == "3":
            visualizar_tarefas()
            id_input = input("\nDigite o ID da tarefa que deseja excluir: ").strip()
            if id_input.isdigit():
                excluir_tarefa(int(id_input))
            else:
                print("\n❌ Por favor, informe um número de ID válido.")

        elif opcao == "0":
            print("\nSaindo do Gerenciador de Tarefas. Até logo!")
            break

        else:
            print("\n❌ Opção inválida! Tente novamente.")


if __name__ == "__main__":
    menu_principal()