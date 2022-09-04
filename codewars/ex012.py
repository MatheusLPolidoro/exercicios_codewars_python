# Escreva uma função que pegue um array de strings e retorne um array de strings com as direções desnecessárias removidas
# (W<->E ou S<->N lado a lado).

# Nem todos os caminhos podem ser simplificados.
# O caminho ["NORTH", "WEST", "SOUTH", "EAST"] não é redutível.
# "NORTH" e "WEST", "WEST" e "SOUTH", "SOUTH" e "EAST" não são
# diretamente opostos um do outro e não podem se tornar tais.
# Portanto, o caminho do resultado é ele mesmo:
# ["NORTH", "WEST", "SOUTH", "EAST"].


def dirReduc(arr):
    """Directions Reduction."""
    data = ' '.join(arr)
    data = data.replace('NORTH SOUTH', '')
    data = data.replace('SOUTH NORTH', '')
    data = data.replace('EAST WEST', '')
    data = data.replace('WEST EAST', '')
    dir_result = data.split()
    return dirReduc(dir_result) if len(dir_result) < len(arr) else dir_result
