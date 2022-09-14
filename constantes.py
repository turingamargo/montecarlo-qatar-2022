SOBRES_POR_CAJA = 104
ESTAMPAS_POR_SOBRE = 5
ESTAMPAS_POR_CAJA = SOBRES_POR_CAJA * ESTAMPAS_POR_SOBRE
ESTAMPAS_DE_ALBUM = 670
ESTAMPAS_POR_SECCION = 20
ESTAMPAS_SECCION_FWC = 30


# código de país como aparece al reverso de las estampas
CODIGO_PAIS = [
    "QAT", "ECU", "SEN", "NED", "ENG", 
    "IRN", "USA", "WAL", "ARG", "KSA", 
    "MEX", "POL", "FRA", "AUS", "DEN", 
    "TUN", "ESP", "CRC", "GER", "JPN", 
    "BEL", "CAN", "MAR", "CRO", "BRA", 
    "SRB", "SUI", "CMR", "POR", "GHA", 
    "URU", "KOR"
]

# código de sección como aparece al reverso de las estampas
CODIGO_SECCIONES = CODIGO_PAIS + ["FWC"]

# primera estampa en cada país
VALOR_INFERIOR_PAIS = [
    19, 39, 59, 79, 99, 
    119, 139, 159, 179, 199, 
    219, 239, 259, 279, 299, 
    319, 339, 359, 379, 399, 
    419, 439, 459, 479, 499, 
    519, 539, 559, 579, 599, 
    619, 639
]

# última estampa en cada país
VALOR_SUPERIOR_PAIS = [num + (ESTAMPAS_POR_SECCION - 1) for num in VALOR_INFERIOR_PAIS]

# valores correspondientes para la sección FWC
VALOR_SUPERIOR_FWC_P1 = 18
VALOR_SUPERIOR_FWC_P2 = 669
VALOR_INFERIOR_FWC_P2 = 659
NO_ESTAMPAS_EN_FWC_P1 = 19
