# Leer x cantidad de precios y mostrar el precio mas alto y el precio más bajo.


total_precios = int(input("Ingrese el total de precios que va a ingresar: "))
precios = []

for i in range(total_precios):
    precio = int(input(f"Ingrese el precio {i+1}: "))
    precios.append(precio)

precio_mayor = max(precios)
precio_menor = min(precios)

print(f"El precio mayor es: {precio_mayor} y el precio menor es: {precio_menor}")
