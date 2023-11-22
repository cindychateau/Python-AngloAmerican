class Usuario:		
    
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.balance_cuenta = 0
    #self = guido
    #amount = 20
    #guido.balance_cuenta = 120
    def hacer_depósito(self, amount):
    	self.balance_cuenta += amount	# la cuenta del usuario específico aumenta en la cantidad del valor recibido
        return self
    
    def hacer_retiro(self, amount):
        self.balance_cuenta -= amount
        return self
    
    #self = guido
    def mostrar_balance_usuario(self):
        print(f'Usuario: {self.name}, Balance: ${self.balance_cuenta}')
    
    #self: el que manda transfer
    #other_user: recibe transferencia
    #amount es cantidad a mandar
    #self = elena
    #other_user = monty
    #amount = 500
    #elena.balance_cuenta = 1051 - 500 = 551
    #monty.balance_cuenta = 0 + 500 = 500
    def transfer_dinero(self, other_user, amount): 
        self.balance_cuenta -= amount
        other_user.balance_cuenta += amount
        print(f"[!] El Usuario {self.name} hizo una transferencia de ${amount} a {other_user.name}")