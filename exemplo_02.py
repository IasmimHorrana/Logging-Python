from utils_log import log_decorator
from print_decorator import hello

@hello
def soma(x,y):
    return x + y

soma(2,3)
soma(2,7)