import sqlite3

def conectar():
   
    return sqlite3.connect("exercicio.db")


def criar_tabela():
   
    conexao = conectar()
    cursor = conexao.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL
        )
    """)
    
    conexao.commit()
    conexao.close()
    print("✓ Tabela 'Clientes' configurada com sucesso!")




def inserir_cliente(nome, email):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO Clientes (nome, email) VALUES (?, ?)", (nome, email))
    conexao.commit()
    conexao.close()
    print(f"✓ Cliente '{nome}' inserido.")


def listar_clientes():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM Clientes")
    clientes = cursor.fetchall()
    conexao.close()

    print("\n--- LISTA DE CLIENTES ---")
    if not clientes:
        print("Nenhum cliente cadastrado.")
    else:
        for c in clientes:
            print(f"ID: {c[0]} | Nome: {c[1]} | Email: {c[2]}")

def atualizar_email_cliente(id_cliente, novo_email):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("UPDATE Clientes SET email = ? WHERE id = ?", (novo_email, id_cliente))
    conexao.commit()
    conexao.close()
    print(f"\n✓ E-mail do cliente ID {id_cliente} atualizado para '{novo_email}'.")


def deletar_cliente(id_cliente):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM Clientes WHERE id = ?", (id_cliente,))
    conexao.commit()
    conexao.close()
    print(f"\n✓ Cliente ID {id_cliente} deletado.")

def filtrar_clientes_por_letra(letra="A"):
    conexao = conectar()
    cursor = conexao.cursor()
    
    cursor.execute("SELECT * FROM Clientes WHERE nome LIKE ?", (f"{letra}%",))
    clientes = cursor.fetchall()
    conexao.close()

    print(f"\n--- FILTRO: CLIENTES COMEÇANDO COM '{letra}' ---")
    if not clientes:
        print(f"Nenhum cliente encontrado com a letra '{letra}'.")
    else:
        for c in clientes:
            print(f"ID: {c[0]} | Nome: {c[1]} | Email: {c[2]}")


if __name__ == "__main__":
   
    criar_tabela()

 
    print("\n1. [CREATE] Inserindo clientes...")
    inserir_cliente("Ana Silva", "ana@email.com")
    inserir_cliente("Bruno Costa", "bruno@email.com")
    inserir_cliente("Amanda Souza", "amanda@email.com")
    inserir_cliente("Carlos Oliveira", "carlos@email.com")

    print("\n2. [READ] Consultando todos os clientes...")
    listar_clientes()

    print("\n3. [UPDATE] Atualizando e-mail do cliente ID 2...")
    atualizar_email_cliente(2, "bruno.costa@novodominio.com")
    listar_clientes()

    print("\n4. [DELETE] Excluindo cliente ID 4...")
    deletar_cliente(4)
    listar_clientes()

    # Item 3: Filtro SQL
    filtrar_clientes_por_letra("A")