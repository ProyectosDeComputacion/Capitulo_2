print('1.Indexación de los strings:')
s = "Hola Mundo"
print(s[0])  # Imprime "H"
print(s[4])  # Imprime " "
print(s[-1])  # Imprime "o"

print('2. Cortar un string (Slicing):')
s = "Hola Mundo"
print(s[0:4])  # Imprime "Hola"
print(s[5:])  # Imprime "Mundo"

print('3. Concatenar strings:')
s1 = "Hola"
s2 = "Mundo"
s3 = s1 + " " + s2  # Concatena los strings con un espacio en medio
print(s3)  # Imprime "Hola Mundo"

print('4. Cambiar un valor en un string:')
s = "Hola Mundo"
s = s.replace("H", "h")  # Reemplaza "H" con "h"
print(s)  # Imprime "hola Mundo"

print('5. Métodos de los strings:')
s = " Hola Mundo "

print(s.upper())  # Imprime " HOLA MUNDO "
print(s.lower())  # Imprime " hola mundo "
print(s.replace("H", "h"))  # Imprime " hola Mundo "
print(s.lstrip())  # Imprime "Hola Mundo "
print(s.rstrip())  # Imprime " Hola Mundo"
print(s.strip())  # Imprime "Hola Mundo"
print(s.split())  # Imprime ['Hola', 'Mundo']
