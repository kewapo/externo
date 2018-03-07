import os.path
import modelo

def recorrer_directorios(ruta):
    """
    Recorre la ruta de forma recursiva recopilando datos de los
    archivos y directorios.

    ALGORITMO:
    Usa os.walk() para efectuar el recorrido. Va primero a los directorios
    más profundos y obtener así su tamaño para poder calcular el tamaño de
    los directorios menos profundos.
    Dentro de ese bucle, primero recorre los ficheros y luego los directorios.

    PARAMETROS:
    ruta: directorio desde el que se comienza el recorrido.
    Ejemplos:
    ruta = r'\\10.36.29.19\Rosa\Back_D\INFORME CONSULTORIO'
    ruta = r'E:'

    VARIABLES:
    tamanios: dict(directorio: tamaño)

    DEVUELVE:
    tamanios: diccionario con los tamaños de los directorios

    EFECTOS COLATERALES:

    PENDIENTE:
    * Crear fichero modelo.py con las funciones de almacenar los datos
    * Guardar los datos en un almacen externo en modelo.py
    """

    tamanios = dict()
    for raiz, directorios, ficheros in os.walk(ruta, topdown=False):
        tamanio_dir = 0
        for fichero in ficheros:
            nombre = os.path.join(raiz, fichero)
            tamanio = os.path.getsize(nombre)
            # fecha = os.path.getmtime(nombre)
            tamanio_dir += tamanio
        for directorio in directorios:
            tamanio_dir += tamanios[os.path.join(raiz, directorio)]
        tamanios[raiz] = tamanio_dir
    return tamanios


# ########################################################################

datos = modelo.crear_dbase('archivos.db')
