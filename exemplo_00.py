from loguru import logger

logger.add("meu_app.log")

#logger.info("Isso é uma mensagem informativa")

def soma(x, y):
    logger.info(x)
    logger.info(y)
    logger.info(x + y)
    return x + y
soma(2,3)

