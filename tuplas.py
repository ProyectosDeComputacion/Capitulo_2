print('1. Ejemplo de tupla:')
# Definición de una tupla
mi_tupla = (1, "dos", 3.0, True, [5, 6])
print(mi_tupla)  # Imprime (1, "dos", 3.0, True, [5, 6])

print('2. Operaciones con tuplas:')
mi_tupla = (1, 2, 3, 2, 4)

# Cuenta el número de veces que aparece un elemento en la tupla
conteo = mi_tupla.count(2)
print(conteo)  # Imprime 2

# Devuelve el índice del primer elemento con el valor especificado
indice = mi_tupla.index(3)
print(indice)  # Imprime 2
