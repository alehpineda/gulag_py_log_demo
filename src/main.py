import logging
from datetime import date

from modulos.operaciones import division, multiplicacion
from utilidades.logger_helper import get_logger

logger = get_logger(
    log_file=f"logs/main_app_log_{date.today()}",
    log_name="MainApp",
    log_level=logging.DEBUG,
    console_level=logging.DEBUG,
)


def hello_world():
    logger.debug("Hola soy un log debug")
    print("Hola Mundo")
    logger.info("Hola soy un log info")


if __name__ == "__main__":
    hello_world()
    division(8, 2)
    multiplicacion(2, 3, 4)
    division(8, 0)
