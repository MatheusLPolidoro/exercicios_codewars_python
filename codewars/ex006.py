# Nesta pequena tarefa, você recebe uma sequência de números separados
# por espaços e deve retornar o número mais alto e o mais baixo.

# Exemplos
# high_and_low("1 2 3 4 5")  # return "5 1"
# high_and_low("1 2 -3 4 5") # return "5 -3"
# high_and_low("1 9 3 4 -5") # return "9 -5"
from re import findall


def high_and_low(numbers):
    """Highest and Lowest."""
    numbers = findall(r'-\d+|\d+', numbers)
    numbers = [int(num) for num in numbers]
    return f'{max(numbers)} {min(numbers)}'
