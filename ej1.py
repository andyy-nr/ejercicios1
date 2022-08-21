#Mostrar el total a pagar por la compra de n cantidad de productos a un precio desconocido.

unidades = int(input("¿Cuantas unidades desea comprar de este producto?\n"))
precio = int(input("¿Cual es el precio de este producto?\n"))

precio_final = unidades * precio

print("El total de su compra es de: $", precio_final)
