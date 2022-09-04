# O problema do subarray de soma máxima consiste em encontrar
# a soma máxima de uma subsequência contígua em um array
# ou lista de inteiros:

# max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# # should be 6: [4, -1, 2, 1]
# Caso fácil é quando a lista é composta apenas por números
# positivos e a soma máxima é a soma de todo o array.
# Se a lista for composta apenas de números negativos, retorne 0.

# A lista vazia é considerada como tendo a maior soma zero.
# Observe que a lista ou matriz vazia também é uma sublista/subarray válida.


def max_sequence(arr):
    """Maximum subarray sum."""
    high, curr = 0, 0
    for num in arr:
        curr += num  # Soma atual
        curr = max(curr, 0)
        if curr > high:
            high = curr
    return high
