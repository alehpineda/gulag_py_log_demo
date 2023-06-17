import logging

# Mandar llamar el root logger por nombre

logger = logging.getLogger(name="MainApp")


def division(x: int, y: int) -> float:
    """Division

    Args:
        x (int): Parte de arriba
        y (int): Parte de abajo

    Returns:
        float: Resultado
    """

    try:
        logger.info("Ejecutando division")
        logger.debug(f"Dividiendo x:{x} / y:{y}")
        return x / y
    except ZeroDivisionError:
        logger.error("Error: Division por 0")
        logger.exception("Excepcion: Division por 0, mas el traceback")


def multiplicacion(a: int, b: int, c: int) -> int:
    """_summary_

    Args:
        a (int): _description_
        b (int): _description_
        c (int): _description_

    Returns:
        int: _description_
    """
    logger.info(f"Multiplicando {a}, {b}, {c}")
    logger.debug(f"Resultado {a*b*c}")
    return a * b * c
