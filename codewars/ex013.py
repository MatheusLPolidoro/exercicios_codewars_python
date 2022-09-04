# Você receberá uma matriz de números. Você deve classificar os números
# ímpares em ordem crescente, deixando os números pares em
# suas posições originais.

# Exemplos
# [7, 1]  =>  [1, 7]
# [5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]


def sort_array(source_array):
    """Sort the odd."""
    # list_iterator
    odd = iter(sorted([num for num in source_array if num % 2]))
    return [next(odd) if num % 2 else num for num in source_array]
