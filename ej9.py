"""Leer los datos de un estudiante como el nombre, los apellidos, la carrera y su promedio.
Evaluar si apto para beca, el estudiante podrá optar a beca si su promedio es mayor a 85
en todas las carreras excepto Ingeniería de Sistemas donde su promedio debe ser mayor a
95."""

nombre_completo = input("Escriba su nombre completo: ")
print("\n1. Ingeniería en Sistemas"
      "\n2. Ingeniería Ambiental"
      "\n3. Ingeniería Civil"
      "\n4. Psicología"
      "\n5. Sociología"
      "\n6. Marketing")

carrera = int(input("Escriba el nombre que corresponde a su carrera: "))

promedio = int(input("Escriba su promedio: "))


if carrera == 1 and promedio > 95:
    print(f"Felicidades {nombre_completo}! Es apto para beca")
elif carrera != 1 and promedio > 85:
    print(f"Felicidades {nombre_completo}! Es apto para beca")
else:
    print("Lo lamentamos, no es apto para beca")


