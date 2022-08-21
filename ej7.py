# Leer x cantidad de edades y mostrar el promedio de dichas edades.

total_edades = int(input("Ingrese el total de edades que se van a evaluar: "))
edades = []

for i in range(total_edades):
    edad = int(input(f"Ingrese la edad {i+1}: "))
    edades.append(edad)

promedio = sum(edades) / total_edades
print(f"El promedio de edades es de {promedio}")