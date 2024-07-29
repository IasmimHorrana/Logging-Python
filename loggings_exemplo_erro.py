from loguru import logger

logger.debug("Um aviso para o dev (ou me) no futuro.")
logger.info("Informação importante do processo.")
logger.warning("Um aviso de que algo vai parar de funcionar no futuro.")
logger.error("Aconteceu um falha.")
logger.critical("Aconteceu uma falha que aborta a aplicação.")

