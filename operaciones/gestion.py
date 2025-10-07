from datos.persistencia import guardar_datos

def agregar_titulo(titulos, ejemplares):
    """Opción 6: Agregar un nuevo título al catálogo"""
    print("\n--- Agregar Nuevo Título ---")
    titulo = input("Ingrese el título del libro: ").strip()

    if not titulo:
        print("Error: El título no puede estar vacío")
        return titulos, ejemplares

    cantidad = input("¿Cuántos ejemplares tiene este título? ")

    if not cantidad.isdigit():
        print("Error: Debe ingresar un número válido")
        return titulos, ejemplares

    cantidad = int(cantidad)

    titulos.append(titulo)
    ejemplares.append(cantidad)

    guardar_datos(titulos, ejemplares)
    print(f"\nTítulo '{titulo}' agregado con {cantidad} ejemplar(es)")
    return titulos, ejemplares


def actualizar_ejemplares(titulos, ejemplares):
    """Opción 7: Actualizar ejemplares (préstamo/devolución)"""
    if not titulos:
        print("\nEl catálogo está vacío")
        return titulos, ejemplares

    print("\n--- Actualizar Ejemplares ---")
    for i in range(len(titulos)):
        print(f"{i+1}. {titulos[i]} ({ejemplares[i]} ejemplares)")

    indice = input("\nSeleccione el número del título: ")

    if not indice.isdigit():
        print("Error: Debe ingresar un número válido")
        return titulos, ejemplares

    indice = int(indice) - 1

    if indice < 0 or indice >= len(titulos):
        print("Error: Número de título inválido")
        return titulos, ejemplares

    print(f"\nTítulo seleccionado: {titulos[indice]}")
    print(f"Ejemplares actuales: {ejemplares[indice]}")
    print("\n1. Préstamo (disminuir)")
    print("2. Devolución (aumentar)")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        if ejemplares[indice] > 0:
            ejemplares[indice] -= 1
            guardar_datos(titulos, ejemplares)
            print(f"\nPréstamo registrado. Ejemplares restantes: {ejemplares[indice]}")
        else:
            print("\nError: No hay ejemplares disponibles para préstamo")
    elif opcion == "2":
        ejemplares[indice] += 1
        guardar_datos(titulos, ejemplares)
        print(f"\nDevolución registrada. Ejemplares actuales: {ejemplares[indice]}")
    else:
        print("\nOpción inválida")

    return titulos, ejemplares
