class ContaBancaria:
    def __init__(self, numero, titular, limite):
        self.numero = numero
        self.titular = titular
        self.limite = limite
        self.saldo = 0

    def sacar(self):
        valor = float(input("Digite o valor para sacar: "))
        if valor <= self.saldo + self.limite:
            self.saldo -= valor
            print("Saque realizado com sucesso.")
        else:
            print("Saldo insuficiente.")

    def depositar(self):
        valor = float(input("Digite o valor para depositar: "))
        if valor > 0:
            self.saldo += valor
            print("Depósito realizado com sucesso.")
        else:
            print("Valor inválido.")

    def ver_saldo(self):
        print(f"Saldo atual: R${self.saldo:.2f}")
