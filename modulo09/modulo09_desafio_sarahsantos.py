
class CredenciaisInvalidasError(Exception):
  
    pass

class LimiteTentativasExcedidoError(Exception):
 
    pass



class AuthService:
    def __init__(self, usuario_valido="admin", senha_valida="admin123", max_tentativas=3):
        
        self._usuario_valido = usuario_valido
        self._senha_valida = senha_valida
        self.max_tentativas = max_tentativas
        self.tentativas_atuais = 0

    def autenticar(self, usuario, senha):
        
        if self.tentativas_atuais >= self.max_tentativas:
            raise LimiteTentativasExcedidoError("Conta bloqueada temporariamente por segurança.")

        
        if usuario != self._usuario_valido or senha != self._senha_valida:
            self.tentativas_atuais += 1
            tentativas_restantes = self.max_tentativas - self.tentativas_atuais
            
            if self.tentativas_atuais >= self.max_tentativas:
                raise LimiteTentativasExcedidoError("Acesso bloqueado! Limite máximo de tentativas atingido.")
            
            raise CredenciaisInvalidasError(
                f"Credenciais incorretas. Tentativas restantes: {tentativas_restantes}"
            )

        self.tentativas_atuais = 0
        return True



def executar_interface_login():
    
    auth_system = AuthService(usuario_valido="dev_user", senha_valida="pass123", max_tentativas=3)
    
    print("==========================================")
    print("      SISTEMA DE AUTENTICAÇÃO - DEV       ")
    print("==========================================")
    
    while True:
        try:
            usr = input("\n[LOGIN] Usuário: ")
            pwd = input("[LOGIN] Senha:   ")
            
           
            if auth_system.autenticar(usr, pwd):
                print("\n[OK] Autenticação bem-sucedida! Acessando o painel...")
                break
                
        except CredenciaisInvalidasError as e:
      
            print(f"[ERRO] {e}")
            
        
            print(f"\n[BLOQUEADO] {e}")
            print("Encerrando a sessão...")
            break



if __name__ == "__main__":
    executar_interface_login()