print('---LISTA---')
# Definición de la lista
mi_lista = [1, 2, 3, 4, 5]

# Bucle for que recorre cada elemento de la lista
for elemento in mi_lista:
    print(elemento)

print('---REPETIR---')
# Bucle for que se repite 5 veces
for i in range(5):
    print(i)

print('---DICCIONARIO---')
# Definición del diccionario
mi_diccionario = {"clave1": "valor1", "clave2": "valor2", "clave3": "valor3"}

# Bucle for que recorre cada clave-valor del diccionario
for clave, valor in mi_diccionario.items():
    print(f"La clave es '{clave}' y el valor es '{valor}'")

print('---STRING---')
# Definición del string
mi_string = "Hola mundo"

# Bucle for que recorre cada carácter del string
for caracter in mi_string:
    print(caracter, end='')
