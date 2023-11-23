from CuentaBancaria import CuentaBancaria

cuenta_ahorros = CuentaBancaria(.02, 100)
cuenta_cheques = CuentaBancaria(.01, 5000)

cuenta_ahorros.depósito(50).depósito(100).depósito(1500).retiro(6000).generar_interés().mostrar_info_cuenta()

cuenta_cheques.depósito(50).depósito(1000).retiro(1).retiro(20).retiro(40).retiro(80).generar_interés().mostrar_info_cuenta()


cuenta_credito = CuentaBancaria(0, 1000)

print("--------")
CuentaBancaria.imprimir_todas_cuentas()