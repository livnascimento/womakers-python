from abc import ABC, abstractmethod

class ContaBase(ABC):
    def __init__(self, titulares):
        self.titulares = titulares
        self.saldo = 0
    
    @abstractmethod
    def sacar(self, valor):
        pass

    def depositar(self, valor):
            self.saldo += valor
            print(f"Depósito de R$ {valor},00 realizado. O saldo atual é de R$ {self.saldo},00.")

    def extrato(self):
        print("----------------------------------------")
        print(f"Seu saldo é de {self.saldo}")
        print("----------------------------------------")

class ContaMulher(ContaBase):
    cheque_especial = 0

    def __init__(self, titulares):
        super().__init__(titulares)
        for titular in self.titulares:
            if titular.genero == 'f':
                self.cheque_especial += titular.renda

    def sacar(self, valor):
            if valor > self.saldo + self.cheque_especial:
                print(f"Saldo insuficiente. Você pode sacar até R$ {self.saldo + self.cheque_especial}.")
            else:
                self.saldo -= valor
                print(f"Saque realizado. Saldo atual {self.saldo}")


class ContaHomem(ContaBase):
    def sacar(self, valor):
        if (valor > self.saldo):
            print("Saldo insuficiente.")
        else: 
            self.saldo -= valor
            print(f"Saque realizado. Seu saldo é: R$ {self.saldo}")

class Cliente:
    def __init__(self, nome, telefone, renda, genero):
        self.nome = nome
        self.telefone = telefone
        self.renda = renda
        self.genero = genero

cliente01 = Cliente("Mariana Silva", "5581990000000", 2900, 'f')
cliente02 = Cliente("Celso Santos", "5581990000000", 2400, 'm')

contaMariana = ContaMulher([cliente01])
contaCelso = ContaHomem([cliente02])
contaConjunta = ContaMulher([cliente01, cliente02])

contaMariana.depositar(400)
contaMariana.sacar(500)
contaMariana.sacar(1400)
contaCelso.depositar(100)
contaCelso.sacar(110)
contaCelso.sacar(100)
contaConjunta.depositar(500)
contaConjunta.sacar(2000)
contaConjunta.sacar(20000)