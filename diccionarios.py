print('1.Ejemplo de diccionario:')
# Definición de un diccionario
mi_diccionario = {"clave1": "valor1", "clave2": "valor2", "clave3": "valor3"}
print(mi_diccionario)  # Imprime {"clave1": "valor1", "clave2": "valor2", "clave3": "valor3"}

print('2. Acceder a un valor de una clave:')
print(mi_diccionario["clave1"])  # Imprime "valor1"

print('3. Asignar un nuevo valor a una clave:')
mi_diccionario["clave1"] = "nuevo valor1"
print(mi_diccionario)  # Imprime {"clave1": "nuevo valor1", "clave2": "valor2", "clave3": "valor3"}

print('4. Iteración de un diccionario:')
for clave, valor in mi_diccionario.items():
    print(f"La clave es '{clave}' y el valor es '{valor}'")

print('5. Métodos de los diccionarios:')
# Limpia el diccionario
mi_diccionario.clear()
print(mi_diccionario)  # Imprime {}

# Copia el diccionario
mi_diccionario = {"clave1": "valor1", "clave2": "valor2", "clave3": "valor3"}
nuevo_diccionario = mi_diccionario.copy()
print(nuevo_diccionario)  # Imprime {"clave1": "valor1", "clave2": "valor2", "clave3": "valor3"}

# Crea un nuevo diccionario con las claves dadas y el mismo valor
claves = ('clave1', 'clave2', 'clave3')
valor = 'valor'
diccionario_fromkeys = dict.fromkeys(claves, valor)
print(diccionario_fromkeys)  # Imprime {'clave1': 'valor', 'clave2': 'valor', 'clave3': 'valor'}

# Devuelve el valor para la clave especificada si existe
print(mi_diccionario.get("clave1"))  # Imprime "valor1"

# Comprueba si la clave especificada existe en el diccionario
print("clave1" in mi_diccionario)  # Imprime True

# Devuelve una lista de todos los pares clave-valor
print(mi_diccionario.items())  # Imprime dict_items([('clave1', 'valor1'), ('clave2', 'valor2'), ('clave3', 'valor3')])

# Devuelve una lista de todas las claves
print(mi_diccionario.keys())  # Imprime dict_keys(['clave1', 'clave2', 'clave3'])

# Actualiza el diccionario con los pares clave-valor especificados
mi_diccionario.update({"clave1": "nuevo valor1", "clave4": "valor4"})
print(mi_diccionario)  # Imprime {'clave1': 'nuevo valor1', 'clave2': 'valor2', 'clave3': 'valor3', 'clave4': 'valor4'}

# Devuelve una lista de todos los valores
print(mi_diccionario.values())  # Imprime dict_values(['nuevo valor1', 'valor2', 'valor3', 'valor4'])
