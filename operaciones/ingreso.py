from datos.persistencia import guardar_datos

def ingresar_titulos(titulos, ejemplares):
    """Opción 1: Ingresar títulos iniciales"""
    print("\n--- Ingresar Títulos ---")
    cantidad = input("¿Cuántos títulos desea ingresar? ")

    if not cantidad.isdigit():
        print("Error: Debe ingresar un número válido")
        return titulos, ejemplares

    cantidad = int(cantidad)

    for i in range(cantidad):
        titulo = input(f"Ingrese el título #{i+1}: ").strip()
        if titulo:
            titulos.append(titulo)
            ejemplares.append(0)
        else:
            print("Error: El título no puede estar vacío")

    guardar_datos(titulos, ejemplares)
    print(f"\n{cantidad} título(s) agregado(s) exitosamente")
    return titulos, ejemplares


def ingresar_ejemplares(titulos, ejemplares):
    """Opción 2: Ingresar ejemplares para cada título"""
    if not titulos:
        print("\nNo hay títulos registrados. Primero ingrese títulos.")
        return titulos, ejemplares

    print("\n--- Ingresar Ejemplares ---")
    for i in range(len(titulos)):
        print(f"{i+1}. {titulos[i]} (Ejemplares actuales: {ejemplares[i]})")

    indice = input("\nSeleccione el número del título: ")

    if not indice.isdigit():
        print("Error: Debe ingresar un número válido")
        return titulos, ejemplares

    indice = int(indice) - 1

    if indice < 0 or indice >= len(titulos):
        print("Error: Número de título inválido")
        return titulos, ejemplares

    cantidad = input(f"¿Cuántos ejemplares desea agregar a '{titulos[indice]}'? ")

    if not cantidad.isdigit():
        print("Error: Debe ingresar un número válido")
        return titulos, ejemplares

    cantidad = int(cantidad)
    ejemplares[indice] += cantidad

    guardar_datos(titulos, ejemplares)
    print(f"\nEjemplares actualizados. Total ahora: {ejemplares[indice]}")
    return titulos, ejemplares
