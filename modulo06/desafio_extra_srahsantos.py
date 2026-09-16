import shutil
import os

def realizar_backup(pasta_origem, pasta_destino):
    
    if not os.path.exists(pasta_origem):
        print(f"Erro: A pasta de origem '{pasta_origem}' não existe.")
        return

    
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)
        print(f"Diretório de destino '{pasta_destino}' criado.")

    arquivos = os.listdir(pasta_origem)
    for arquivo in arquivos:
        caminho_origem = os.path.join(pasta_origem, arquivo)
        caminho_destino = os.path.join(pasta_destino, arquivo)
        
        if os.path.isfile(caminho_origem):
            shutil.copy2(caminho_origem, caminho_destino)
            print(f"Copiado: {arquivo} -> {pasta_destino}")

    print("\nBackup concluído com sucesso!")

if __name__ == "__main__":
   
    origem = "meus_arquivos"
    destino = "backup_arquivos"
    
  
    if not os.path.exists(origem):
        os.makedirs(origem)
        with open(os.path.join(origem, "exemplo.txt"), "w") as f:
            f.write("Arquivo de teste para backup.")
            
    realizar_backup(origem, destino)