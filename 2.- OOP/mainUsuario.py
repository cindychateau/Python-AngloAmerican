#Importar el archivo
from Usuario import Usuario

guido = Usuario("Guido van Rossum", "guido@python.com")
monty = Usuario("Monty Python", "monty@python.com")
elena = Usuario("Elena De Troya", "elena@codingdojo.com")

guido.hacer_depósito(100)
guido.hacer_depósito(20)
guido.hacer_depósito(10) #guido.balance_cuenta = 130
guido.hacer_retiro(50)
guido.mostrar_balance_usuario()

monty.hacer_depósito(1)
monty.hacer_depósito(2)
monty.hacer_retiro(2)
monty.hacer_retiro(1)
monty.mostrar_balance_usuario()

elena.hacer_depósito(1000)
elena.hacer_retiro(1)
elena.hacer_retiro(2)
elena.hacer_retiro(3)
elena.mostrar_balance_usuario()

guido.transfer_dinero(elena, 57)
guido.mostrar_balance_usuario()
elena.mostrar_balance_usuario()

elena.transfer_dinero(monty, 500)
elena.mostrar_balance_usuario()
monty.mostrar_balance_usuario()

elena.hacer_depósito(100).hacer_depósito(50).hacer_retiro(10)
#elena.hacer_depósito(50)
#elena.hacer_retiro(10)
#elena

print(elena.banco)
print(monty.banco)
print(guido.banco)

elena.banco = "Coding Dojo"
print(elena.banco)
print(monty.banco)
print(guido.banco)

Usuario.banco = "Coding Dojo"
print(elena.banco)
print(monty.banco)
print(guido.banco)

Usuario.muestra_usuarios()