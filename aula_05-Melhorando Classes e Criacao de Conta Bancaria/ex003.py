class ContaBancaria:
    """
    Cria uma conta bancária e permite fazer saques e depósitos
    """
    def __init__(self, id, nome, saldo = 0 ):
        self.id = id
        self.titular = nome
        self.saldo = saldo
        print(f'\033[35mConta {self.id} criada com sucesso. Saldo atual de R${self.saldo:,.2f}\033[m')

    def __str__(self):
        return f'A conta {self.id} de {self.titular} tem R${self.saldo:,.2f} de saldo.'

    def depositar(self,valor):
        self.saldo += valor
        print(f'\033[32mR${valor:,.2f} Depósitado na conta {self.id}.\033[m')
    def sacar(self,valor):
        if valor > self.saldo:
            print(f'\033[31mSAQUE DE R${valor} RECUSADO POR SALDO INSUFICIENTE NA CONTA {self.id}\033[m')
        else:
            self.saldo -= valor
            print(f'\033[34mR${valor:,.2f} Sacado na conta {self.id}.\033[m')

c1 = ContaBancaria(112, 'Rian', 3000)
print(c1)
c1.depositar(500)
print(c1)
c1.sacar(50)
c1.sacar(2_000_000)
print(c1)
