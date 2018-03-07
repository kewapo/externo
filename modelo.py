import sqlite3

almacen = ...

def crear_dbase(fichero):
    db = sqlite3.connect(fichero)


def guardar(que, tipo='f'):
    """
    Almacena en un lugar externo el dato que

    PARAMETROS:
    que: lo que hay que almacenar
    tipo: f para fichero, d para directorio, g para un grupo de datos

    DEVUELVE:
    Nada

    EFECTOS COLATERALES
    El almacén externo se ve modificado
    """

def recuperar(que, tipo='f'):
    """
    Recupera del almacén externo el dato solicitado

    PARAMETROS
    que: lo que tenemos que recuperar
    tipo: f para fichero, d para directorio, g para un grupo de datos

    DEVUELVE:
    El dato recuperado

    EFECTOS COLATERALES:
    No tiene
    """


