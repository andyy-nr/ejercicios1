"""Dado el numero de cuenta, el saldo y el monto de retiro de una cuenta de ahorra verifique
si la persona puede realizar el retiro. Una vez evaluado debe mostrarse el saldo que queda
después del retiro."""

num_cuenta = int(input("Ingrese su numero de cuenta: "))
saldo = int(input("Ingrese el saldo de su cuenta: "))
retiro = int(input("Ingrese el monto que desea retirar: "))

if retiro < saldo:
    saldo = saldo - retiro
    print(f"La cuenta {num_cuenta}, tiene un saldo actual de {saldo}")
else:
    print("Lo sentimos, no cuenta con dinero suficiente para hacer este retiro.")
