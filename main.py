from datos.persistencia import cargar_datos
from ui.menu import mostrar_menu
from operaciones.ingreso import ingresar_titulos, ingresar_ejemplares
from operaciones.consulta import mostrar_catalogo, consultar_disponibilidad
from operaciones.agotados import listar_agotados
from operaciones.gestion import agregar_titulo, actualizar_ejemplares


def main():
    """Función principal del programa"""
    titulos, ejemplares = cargar_datos()
    continuar = True

    while continuar:
        mostrar_menu()
        opcion = input("\nSeleccione una opción: ")

        match opcion:
            case "1":
                titulos, ejemplares = ingresar_titulos(titulos, ejemplares)
            case "2":
                titulos, ejemplares = ingresar_ejemplares(titulos, ejemplares)
            case "3":
                mostrar_catalogo(titulos, ejemplares)
            case "4":
                consultar_disponibilidad(titulos, ejemplares)
            case "5":
                listar_agotados(titulos, ejemplares)
            case "6":
                titulos, ejemplares = agregar_titulo(titulos, ejemplares)
            case "7":
                titulos, ejemplares = actualizar_ejemplares(titulos, ejemplares)
            case "8":
                print("\nGracias por usar el sistema. ¡Hasta luego!")
                continuar = False
            case _:
                print("\nOpción inválida. Por favor, seleccione una opción del 1 al 8")


if __name__ == "__main__":
    main()
