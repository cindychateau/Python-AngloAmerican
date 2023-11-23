from CuentaBancaria import CuentaBancaria
class Usuario:	
    
    #Atributo de Clase: En un atributo perteneciente a la clase completa y que el valor es compartido por todas las instancias
    banco = "Banco de Chile"
    lista_usuarios = [] #[guido, monty, elena]


    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.cuentas = {
            "ahorros": CuentaBancaria(.02, 0),
            "cheques": CuentaBancaria(.01, 0)
        }
        Usuario.lista_usuarios.append(self)
    #self = guido
    #amount = 20
    #guido.balance_cuenta = 120
    #tipo = "ahorros" | "cheques"
    def hacer_depósito(self, amount, tipo):
        if tipo == "ahorros":
            self.cuentas["ahorros"].depósito(amount)
        else:
            self.cuentas["cheques"].depósito(amount)
        #self.cuenta.depósito(amount)
        #self.balance_cuenta += amount
        return self

    def hacer_retiro(self, amount, tipo):
        if tipo == "ahorros":
            self.cuentas['ahorros'].retiro(amount)
        else:
            self.cuentas['cheques'].retiro(amount)
        #self.balance_cuenta -= amount
        #self.cuenta.retiro(amount)
        return self
    
    #self = guido
    def mostrar_balance_usuario(self):
        #print(f'Usuario: {self.name}, Balance: ${self.balance_cuenta}')
        print(f'Usuario:{self.name}')
        self.cuentas['ahorros'].mostrar_info_cuenta()
        self.cuentas['cheques'].mostrar_info_cuenta()
    
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
    
    #Método que pertenece a mi clase y que llama o hace referencia a atributos de la clase. NO INSTANCIA
    @classmethod
    def muestra_usuarios(cls):
        for usuario in cls.lista_usuarios:
            es_millonario = Usuario.millonario(usuario.balance_cuenta)

            print(f'{usuario.name} - {usuario.email}: {usuario.balance_cuenta}, es millonario? {es_millonario}')
    
    #Métodos Estáticos: Acción/Método que quiero realizar PERO que no pertenece ni a instancia ni a clase. Ayudar/Organizar nuestro código
    @staticmethod
    def millonario(dinero):
        if dinero > 100:
            return True
        else:
            return False