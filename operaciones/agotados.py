def listar_agotados(titulos, ejemplares):
    """Opción 5: Listar títulos agotados (0 ejemplares)"""
    if not titulos:
        print("\nEl catálogo está vacío")
        return

    print("\n--- Títulos Agotados ---")
    agotados = [titulos[i] for i in range(len(titulos)) if ejemplares[i] == 0]

    if not agotados:
        print("No hay títulos agotados")
    else:
        for titulo in agotados:
            print(f"- {titulo}")
