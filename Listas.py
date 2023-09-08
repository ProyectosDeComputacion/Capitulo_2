print('1. Ejemplo de lista mutable:')
#Lista mutable
lista = [1, 2, 3]
print(lista)  # Imprime [1, 2, 3]
# Cambiar el segundo elemento
lista[1] = 200
print(lista)  # Imprime [1, 200, 3]

print('2. Ejemplo de lista heterogénea:')
# Lista heterogénea
lista = [1, "dos", 3.0, True, [5, 6]]
print(lista)  # Imprime [1, "dos", 3.0, True, [5, 6]]

print('3. Indexación de las listas:')
lista = [1, 2, 3, 4, 5]
print(lista[0])  # Imprime 1
print(lista[2])  # Imprime 3
print(lista[-1])  # Imprime 5

print('4. Métodos de las listas:')
lista = [1, 2, 3, 2, 4]
# Agrega un elemento al final de la lista
lista.append(5)
print(lista)  # Imprime [1, 2, 3, 2, 4, 5]
# Cuenta el número de veces que aparece un elemento en la lista
conteo = lista.count(2)
print(conteo)  # Imprime 2
# Agrega los elementos de otra lista al final de la lista
otra_lista = [6, 7, 8]
lista.extend(otra_lista)
print(lista)  # Imprime [1, 2, 3, 2, 4, 5, 6, 7, 8]
# Devuelve el índice del primer elemento con el valor especificado
indice = lista.index(3)
print(indice)  # Imprime 2
# Inserta un elemento en una posición especificada
lista.insert(0, 0)
print(lista)  # Imprime [0, 1, 2, 3, 2, 4, 5, 6, 7, 8]
# Elimina el primer elemento con el valor especificado
lista.remove(2)
print(lista)  # Imprime [0, 1, 3, 2, 4, 5, 6, 7, 8]
# Ordena la lista
lista.sort()
print(lista)  # Imprime [0, 1, 2, 3, 4, 5, 6, 7, 8]
