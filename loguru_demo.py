from loguru import logger
import time
from sys import stderr
from functools import wraps


logger.remove()

logger.add(
    sink=stderr,
    format="{time} <r>{level}</r> <g>{message}</g> {file}",
    level="INFO",
)
logger.add(
    sink="loguru_demo.log",
    format="{time} <r>{level}</r> <g>{message}</g> {file}",
    level="INFO",
    rotation="00:00",
)

logger.add(
    sink="loguru_demo1.log",
    format="{time} <r>{level}</r> <g>{message}</g> {file}",
    level="DEBUG",
    rotation="00:00",
)


@logger.catch
def log_function(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(
            f"Chamando função {func.__name__} com argumentos: {args}, kwargs: {kwargs}"
        )
        try:
            result = func(*args, **kwargs)
        except Exception as e:
            logger.exception(
                f"Exceção ao chamar a função {func.__name__}: {e}", exc_info=True
            )
            raise
        logger.info(f"Função {func.__name__} retornou: {result}")
        return result

    return wrapper


def time_function(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        logger.info(
            f"Função {func.__name__} demorou {end - start} segundos para ser executada"
        )

        return result

    return wrapper


@time_function
@log_function
def example_function(x, y):
    return x / y


# Test the decorated function
print(example_function(3, 0))
