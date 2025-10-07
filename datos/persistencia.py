import csv
import os

ARCHIVO_CSV = "datos/catalogo.csv"

def cargar_datos():
    """Carga los datos del archivo CSV y devuelve las listas paralelas"""
    titulos, ejemplares = [], []
    if os.path.exists(ARCHIVO_CSV):
        with open(ARCHIVO_CSV, 'r', encoding='utf-8') as archivo:
            lector = csv.reader(archivo)
            for fila in lector:
                if len(fila) == 2:
                    titulos.append(fila[0])
                    ejemplares.append(int(fila[1]))
    return titulos, ejemplares


def guardar_datos(titulos, ejemplares):
    """Guarda los datos de las listas paralelas en el archivo CSV"""
    with open(ARCHIVO_CSV, 'w', encoding='utf-8', newline='') as archivo:
        escritor = csv.writer(archivo)
        for i in range(len(titulos)):
            escritor.writerow([titulos[i], ejemplares[i]])
