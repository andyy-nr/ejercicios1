"""
Dado el primer nombre, segundo nombre, primer apellido y el segundo apellido de un
estudiante de manera individual, escriba un código en Python que permita crear un correo
electrónico utilizando la siguiente sintaxis: primer nombre + punto (.) + primer apellido +
“@est.uca.edu.ni”
"""

nombre_completo = input("Escriba su nombre completo (2 nombres y 2 apellidos). Por favor separe cada nombre con espacios\n")
nombre_separado = nombre_completo.split()

correo= nombre_separado[0].lower() + "." + nombre_separado[2].lower() + "@est.uca.edu.ni"

print("Su correo institucional es", correo)
