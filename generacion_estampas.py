import random
from constantes import ESTAMPAS_DE_ALBUM, ESTAMPAS_POR_CAJA, ESTAMPAS_POR_SOBRE


def obtener_estampa(n_max: int = ESTAMPAS_DE_ALBUM) -> int:
    """
    Dado un número máximo de estampas, regresa un valor aleatorio entre 0 y
    n_max - 1.
    """
    return random.randrange(n_max)


def obtener_estampas(n_estampas: int, n_max: int = ESTAMPAS_DE_ALBUM) -> list[int]:
    """
    Dado un número máximo de estampas y un número deseado de estampas, 
    regresa una lista de n_estampas con valores entre 0 y n_max - 1.
    """
    estampas = []
    for i in range(n_estampas):
        estampas.append(obtener_estampa(n_max))

    return estampas


def obtener_sobre(n_max: int = ESTAMPAS_DE_ALBUM) -> list[int]:
    """
    Regresa un sobre de estampas.
    """
    return obtener_estampas(n_max=n_max, n_estampas=ESTAMPAS_POR_SOBRE)


def obtener_caja(n_max: int = ESTAMPAS_DE_ALBUM) -> list[int]:
    """
    Regresa una caja de estampas aleatorias.
    """
    return obtener_estampas(n_max=n_max, n_estampas=ESTAMPAS_POR_CAJA)
