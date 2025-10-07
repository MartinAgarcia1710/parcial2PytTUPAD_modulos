def mostrar_catalogo(titulos, ejemplares):
    """Opción 3: Mostrar catálogo completo"""
    if not titulos:
        print("\nEl catálogo está vacío")
        return

    print("\n--- Catálogo de la Biblioteca ---")
    print(f"{'#':<5} {'Título':<40} {'Ejemplares':<12}")
    print("-" * 57)

    for i in range(len(titulos)):
        print(f"{i+1:<5} {titulos[i]:<40} {ejemplares[i]:<12}")


def consultar_disponibilidad(titulos, ejemplares):
    """Opción 4: Consultar disponibilidad de un título específico"""
    if not titulos:
        print("\nEl catálogo está vacío")
        return

    print("\n--- Consultar Disponibilidad ---")
    busqueda = input("Ingrese el título a buscar: ").strip().lower()

    encontrado = False
    for i in range(len(titulos)):
        if busqueda in titulos[i].lower():
            print(f"\nTítulo: {titulos[i]}")
            print(f"Ejemplares disponibles: {ejemplares[i]}")
            encontrado = True

    if not encontrado:
        print("\nNo se encontró ningún título con ese nombre")
