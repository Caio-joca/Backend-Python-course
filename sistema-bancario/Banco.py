class BancoDinheiro :
    def __init__(self, nome, conta_num, saldo, limite) :
        self.nome = nome
        self.conta_num = conta_num
        self.saldo = saldo
        self.limite = limite

    def depositar(self, valor_deposito):
        self.saldo += valor_deposito

    def sacar(self, valor_saque) :
        valorlimite=0
        valorlimite = 0 - self.limite
        if self.saldo<valorlimite :
            print('passou do limite possível')

        elif (self.saldo - valor_saque) >= valorlimite :
            self.saldo -= valor_saque

        elif (self.saldo - valor_saque) <= valorlimite:
            print('passou do limite possível')

    def mostrar_extrato(self):
        print(f'Nome da conta : {self.nome} \nNúmero da conta : {self.conta_num} \nSaldo da conta: {self.saldo} \nLimite da conta : {self.limite} \n')