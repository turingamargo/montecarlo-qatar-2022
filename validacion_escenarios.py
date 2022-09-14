from auxiliares import eliminar_duplicados, agrupar_por_seccion
from constantes import ESTAMPAS_DE_ALBUM, ESTAMPAS_POR_SECCION, ESTAMPAS_SECCION_FWC


def esta_album_completo(estampas: list[int]) -> bool:
    estampas_unicas = eliminar_duplicados(estampas)
    return len(estampas_unicas) == ESTAMPAS_DE_ALBUM


def numero_secciones_completas(estampas: list[int]) -> int:
    """
    Dado un diccionario de sección a lista de estampas, determina el número de secciones
    que se encuentran completas.
    """
    secciones = agrupar_por_seccion(estampas)
    n = 0
    for seccion, estampas in secciones.items():
        if seccion == "FWC":
            if len(estampas) == ESTAMPAS_SECCION_FWC:
                n += 1
        else:
            if len(estampas) == ESTAMPAS_POR_SECCION:
                n += 1

    return n


def numero_estampas_faltantes(estampas: list[int]) -> int:
    estampas_unicas = eliminar_duplicados(estampas)
    return ESTAMPAS_DE_ALBUM - len(estampas_unicas)
