
import hashlib

# Dicionário para simular um banco de dados (chave: usuário, valor: hash da senha)
banco_de_dados = {}

def gerar_hash(senha):
    """Gera um hash SHA-256 para armazenar a senha de forma segura."""
    return hashlib.sha256(senha.encode()).hexdigest()

def cadastrar():
    print("\n--- CADASTRO ---")
    usuario = input("Digite um nome de usuário: ").strip()
    
    if usuario in banco_de_dados:
        print("Erro: Usuário já existe!")
        return
        
    senha = input("Digite uma senha: ").strip()
    if not usuario or not senha:
        print("Erro: Usuário e senha não podem ser vazios.")
        return
        
    banco_de_dados[usuario] = gerar_hash(senha)
    print(f"Usuário '{usuario}' cadastrado com sucesso!")

def login():
    print("\n--- LOGIN ---")
    usuario = input("Usuário: ").strip()
    senha = input("Senha: ").strip()
    
    senha_hash = gerar_hash(senha)
    
    if usuario in banco_de_dados and banco_de_dados[usuario] == senha_hash:
        print(f"\nLogin bem-sucedido! Bem-vindo(a), {usuario}!")
        return True
    else:
        print("\nErro: Usuário ou senha incorretos.")
        return False

def menu():
    while True:
        print("\n=== SISTEMA DE ACESSO ===")
        print("1. Cadastrar")
        print("2. Fazer Login")
        print("3. Sair")
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            cadastrar()
        elif opcao == "2":
            login()
        elif opcao == "3":
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executar o programa
if __name__ == "__main__":
    menu()