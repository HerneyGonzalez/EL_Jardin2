class MiniFinder:
    def __init__(self, objects):
        self.objects = objects

    def find_objects(self):
        found_objects = []

        # Simulación de la lógica del juego
        for obj in self.objects:
            found = input(f"¿Has encontrado el objeto '{obj}'? (Sí/No): ")
            if found.lower() == "sí" or found.lower() == "si":
                found_objects.append(obj)

        return found_objects

# Prueba del juego
def test_mini_finder():
    objects = ["Libro", "Cinturón", "Bolso", "Zapatos", "Dinero"]
    game = MiniFinder(objects)
    found_objects = game.find_objects()

    assert len(found_objects) == len(objects), "No se encontraron todos los objetos"
    print("¡Todos los objetos fueron encontrados con éxito!")

if __name__ == "__main__":
    test_mini_finder()
