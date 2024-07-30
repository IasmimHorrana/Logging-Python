from loguru import logger

#logger.add("meu_log.log")
logger.add("meu_log.log", level="CRITICAL")

#logger.info("Isso é uma mensagem informativa")

def soma(x, y):
    try:
        soma = x + y
        logger.info(f"Você digitou corretamente!{soma}")
        return soma
    except:
        logger.critical("Você precisa digitar valores corretos.")

soma(2,3)
soma(2,7)
soma(2,"3")
