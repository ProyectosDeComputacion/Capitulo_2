class MiClase:
    # Atributo de clase
    atributo_clase = "Soy un atributo de clase"

    def __init__(self, nombre, edad):
        # Atributos de objeto
        self.nombre = nombre
        self.edad = edad

    # Método de instancia
    def saludar(self):
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años."

    # Método de clase (decorador @classmethod)
    @classmethod
    def metodo_de_clase(cls):
        return f"Este es un método de clase. {cls.atributo_clase}"

    # Método estático (decorador @staticmethod)
    @staticmethod
    def metodo_estatico():
        return "Este es un método estático."


# Crear una instancia de la clase
objeto1 = MiClase("Juan", 30)

# Acceder a los atributos de objeto
print(objeto1.nombre)  # Imprime "Juan"
print(objeto1.edad)  # Imprime 30

# Llamar a un método de instancia
saludo = objeto1.saludar()
print(saludo)  # Imprime "Hola, mi nombre es Juan y tengo 30 años."

# Acceder al atributo de clase desde la instancia
print(objeto1.atributo_clase)  # Imprime "Soy un atributo de clase"

# Llamar al método de clase desde la instancia
resultado_metodo_clase = objeto1.metodo_de_clase()
print(resultado_metodo_clase)  # Imprime "Este es un método de clase. Soy un atributo de clase"

# Llamar al método estático desde la instancia
resultado_metodo_estatico = objeto1.metodo_estatico()
print(resultado_metodo_estatico)  # Imprime "Este es un método estático."

# Llamar al método de clase directamente desde la clase (sin necesidad de instancia)
resultado_metodo_clase2 = MiClase.metodo_de_clase()
print(resultado_metodo_clase2)  # Imprime "Este es un método de clase. Soy un atributo de clase"

# Llamar al método estático directamente desde la clase (sin necesidad de instancia)
resultado_metodo_estatico2 = MiClase.metodo_estatico()
print(resultado_metodo_estatico2)  # Imprime "Este es un método estático."
