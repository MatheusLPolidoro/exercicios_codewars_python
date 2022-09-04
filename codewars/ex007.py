# Há um ônibus circulando na cidade, e leva e deixa algumas
# pessoas em cada ponto de ônibus.

# Você recebe uma lista (ou array) de pares de inteiros.
# Os elementos de cada par representam o número de pessoas
# que entram no ônibus (o primeiro item) e o número de pessoas
# que descem do ônibus (o segundo item) em um ponto de ônibus.

# Sua tarefa é retornar o número de pessoas que ainda estão
# no ônibus após a última rodoviária (após a última matriz).
# Mesmo sendo o último ponto de ônibus, o ônibus não está vazio
# e algumas pessoas ainda estão no ônibus, e provavelmente
# estão dormindo lá :D

# Por favor, tenha em mente que os casos de teste garantem
# que o número de pessoas no ônibus seja sempre >= 0.
# Portanto, o inteiro retornado não pode ser negativo.

# O segundo valor na primeira matriz de inteiros é 0,
# pois o ônibus está vazio no primeiro ponto de ônibus.


def number(bus_stops):
    """Number of People in the Bus."""
    # generator object
    return sum(n_input - n_output for n_input, n_output in bus_stops)
