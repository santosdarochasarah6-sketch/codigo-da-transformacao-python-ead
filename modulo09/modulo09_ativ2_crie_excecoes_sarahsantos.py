
class SaldoInsuficienteError(Exception):
    
    pass



class ContaBancaria:
    def __init__(self, saldo_inicial):
        
      
        
        self.saldo = saldo_inicial

    def sacar(self, valor):
       
        if valor > self.saldo:
            
            raise SaldoInsuficienteError(
                f"Saque negado! Valor solicitado: R$ {valor:.2f} | Saldo disponível: R$ {self.saldo:.2f}"
            )
        
      
        self.saldo -= valor
        return f"Saque de R$ {valor:.2f} realizado com sucesso! Saldo restante: R$ {self.saldo:.2f}"


if __name__ == "__main__":
    
    minha_conta = ContaBancaria(saldo_inicial=100.0)

   
    print("--- Teste 1: Saque Permitido ---")
    try:
        mensagem_sucesso = minha_conta.sacar(40.0)
        print(mensagem_sucesso)
    except SaldoInsuficienteError as erro:
        print(f"Erro: {erro}")

    
    print("\n--- Teste 2: Saque Sem Saldo ---")
    try:
        mensagem_sucesso = minha_conta.sacar(100.0)
        print(mensagem_sucesso)
    except SaldoInsuficienteError as erro:
       
        print(f"Erro capturado: {erro}")