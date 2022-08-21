# Mostrar los numero pares comprendidos entre un valor inicial y un valor final de números enteros.

v_inicial = int(input("Ingrese el numero por el cual desea comenzar: "))
v_final = int(input("Ingrese el numero en el que desea terminar: "))

for num in range(v_inicial, v_final+1):
    if num % 2 == 0:
        print(num)
