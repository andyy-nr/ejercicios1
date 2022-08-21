# Aplicar el IVA al precio de un producto
precio = int(input("Cual es el precio de su producto? \n"))
iva = int(input("Cual es el procentaje del IVA?\n"))

iva = (precio*iva)/100
precio = precio + iva

print("Su total con IVA incluido es de: ",precio)