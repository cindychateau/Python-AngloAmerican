class CuentaBancaria:

    lista_cuentas = []

    def __init__(self, tasa_interés=0, balance=0):
        self.tasa_interés = tasa_interés
        self.balance = balance
        CuentaBancaria.lista_cuentas.append(self)
    
    def depósito(self, amount):
        self.balance += amount
        return self
    
    def retiro(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Fondos insuficientes: cobrando una tarifa de $5")
            self.balance -= 5
        return self
    
    def mostrar_info_cuenta(self):
        print(f'Balance: ${self.balance}')
        return self
    
    def generar_interés(self):
        if self.balance > 0:
            self.balance += self.balance * self.tasa_interés
        return self
    
    #CuentaBancaria = [cuenta_ahorros, cuenta_cheques]
    @classmethod
    def imprimir_todas_cuentas(cls):
        for cuenta in cls.lista_cuentas:
            cuenta.mostrar_info_cuenta()