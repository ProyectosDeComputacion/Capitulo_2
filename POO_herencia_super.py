# Definición de la clase base
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años."


# Definición de la clase derivada
class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        # Usa la función super() para llamar al __init__ de la clase base
        super().__init__(nombre, edad)
        # Atributo adicional de la clase Estudiante
        self.grado = grado

    # Extensión del método saludar
    def saludar(self):
        # Primero llama al método saludar de la clase base
        saludo_base = super().saludar()
        # Luego agrega información adicional
        return f"{saludo_base} Estoy estudiando {self.grado}."


# Crear una instancia de la clase Estudiante
estudiante1 = Estudiante("Juan", 20, "Informática")

# Llamar al método saludar
saludo = estudiante1.saludar()
print(saludo)  # Imprime "Hola, mi nombre es Juan y tengo 20 años. Estoy estudiando Informática."
