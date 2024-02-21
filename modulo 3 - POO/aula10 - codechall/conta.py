from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, agencia:int, numero_conta:int, saldo:float = 0 ) -> None:
        self.agencia = agencia    
        self.numero_conta = numero_conta    
        self.saldo = saldo    

    @abstractmethod
    def sacar(self, valor_saque:float) -> None: ...
    
    @abstractmethod
    def checar_extrato (self) -> None: ...
    
    def deposito(self, valor_deposito:float) -> None: 
        self.saldo += valor_deposito


class ContaPoupanca(Conta):
    ... 
    
    def deposito(self, valor_deposito: float) -> None:
        self.saldo += valor_deposito
    
    
    def sacar(self, valor_saque: float) -> None:
        
        if self.saldo > valor_saque:

            self.saldo -= valor_saque

            return print(f"[OPERACAO EFETUADA COM SUCESSO] - SALDO: {self.saldo:.2f}")

        return print(f'[OPERACAO NEGADA] Saldo insuficiente para realizar esta operacao.')
    
    def checar_extrato(self) -> None:
        return print(f"[SALDO ATUAL] - R$ {self.saldo:.2f}")
    

class ContaCorrente(Conta):
    def __init__(self, agencia: int, numero_conta: int, saldo: float = 0, limite_extra:float = 150) -> None:
        
        super().__init__(agencia, numero_conta, saldo)
        
        self._limite_extra = limite_extra

    def sacar(self, valor_saque: float) -> None:
        
        if self.saldo > valor_saque:

            self.saldo -= valor_saque

            return print(f"[OPERACAO EFETUADA COM SUCESSO] - SALDO: {self.saldo:.2f}")

        elif self.saldo + self._limite_extra > valor_saque:

            self.saldo -= valor_saque

            return print(f"[OPERACAO EFETUADA COM SUCESSO] - SALDO: {self.saldo:.2f}")


        return print(f'[OPERACAO NEGADA] Saldo insuficiente para realizar esta operacao.')

    def deposito(self, valor_deposito: float) -> None:
        
        self.saldo += valor_deposito;
    
    def checar_extrato(self) -> None:
        return print(f"[SALDO ATUAL] - R$ {self.saldo:.2f}")
    


if __name__ == '__main__':

    cCorr = ContaCorrente(10,2222)

    cCorr.deposito(1000)
    cCorr.checar_extrato()

    cCorr.sacar(500)
    cCorr.checar_extrato()
   
    cCorr.sacar(600)
    cCorr.checar_extrato()
    
    cCorr.sacar(600)
    cCorr.checar_extrato()
    
    print('-' * 25)
    
    cPoup = ContaPoupanca(11,33333)
    cPoup.deposito(20)
    cPoup.checar_extrato()
    
    cPoup.sacar(30)
    cPoup.checar_extrato()

