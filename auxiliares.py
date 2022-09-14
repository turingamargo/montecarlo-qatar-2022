from constantes import VALOR_INFERIOR_PAIS, VALOR_SUPERIOR_PAIS, VALOR_SUPERIOR_FWC_P1, NO_ESTAMPAS_EN_FWC_P1, VALOR_INFERIOR_FWC_P2
from constantes import CODIGO_PAIS, CODIGO_SECCIONES


def obtener_codigo_estampa(n: int) -> tuple[str, int]:
    """
    Dado un número entero regresa el valor de la estampa en el albúm.
    Ejemplo: Si n = 19 -> ("QAT", 1)
    """

    # caso complicado "FWC"
    if n <= VALOR_SUPERIOR_FWC_P1:
        return ("FWC", n)
    
    if n >= VALOR_INFERIOR_FWC_P2:
        return ("FWC", n - (VALOR_INFERIOR_FWC_P2 - NO_ESTAMPAS_EN_FWC_P1))

    # demás escenarios posibles
    for i in range(len(CODIGO_PAIS)):
        if n <= VALOR_SUPERIOR_PAIS[i]:
            return (CODIGO_PAIS[i], n - VALOR_INFERIOR_PAIS[i] + 1)


def obtener_codigo_estampas(estampas: list[int]) -> list[tuple[str, int]]:
    """
    Dada una lista de números de estampas, regresa una lista con los códigos equivalentes. 
    Ejemplo: [1, 2, 3] -> [("FWC", 1), ("FWC", 2), ("FWC", 3)].
    """
    codigos = [obtener_codigo_estampa(estampa) for estampa in estampas]
    return codigos


def eliminar_duplicados(lista: list[int]) -> list[int]:
    return list(dict.fromkeys(lista))


def agrupar_por_seccion(estampas: list[int]) -> dict[str, list[tuple[str, int]]]:
    estampas_unicas = eliminar_duplicados(estampas)
    codigos = obtener_codigo_estampas(estampas_unicas)

    secciones = {}
    for codigo_album in CODIGO_SECCIONES:
        secciones[codigo_album] = []

    # agrupando las estampas por la sección correspondiente del álbum
    for seccion, numero in codigos:
        secciones[seccion].append(numero)

    return secciones
 