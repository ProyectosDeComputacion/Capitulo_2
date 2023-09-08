def procesar_datos(numero, cadena, lista):
    """Esta función toma un entero, una cadena y una lista, y realiza operaciones en cada uno."""

    # Dobla el número
    numero = numero * 2

    # Convierte la cadena en mayúsculas
    cadena = cadena.upper()

    # Añade un elemento a la lista
    lista.append("Nuevo elemento")

    # Devuelve los nuevos valores
    return numero, cadena, lista

# Enviar datos a la función y recibir datos de la función
mi_numero = 5
mi_cadena = "Hola mundo"
mi_lista = ["elemento1", "elemento2"]

nuevo_numero, nueva_cadena, nueva_lista = procesar_datos(mi_numero, mi_cadena, mi_lista)

print(f"El nuevo número es {nuevo_numero}")
print(f"La nueva cadena es '{nueva_cadena}'")
print(f"La nueva lista es {nueva_lista}")
