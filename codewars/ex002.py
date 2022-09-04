# Você pode conhecer alguns quadrados perfeitos bem grandes. Mas e o PRÓXIMO?

# Complete o findNextSquare método que encontra o próximo quadrado perfeito
#  integral após passado como parâmetro. Lembre-se de que um quadrado perfeito
#  integral é um inteiro n tal que sqrt(n) também é um inteiro.

# Se o parâmetro em si não for um quadrado perfeito, -1 deverá ser retornado.
# Você pode assumir que o parâmetro é não negativo.

# Exemplos:(Entrada --> Saída)

# 121 --> 144
# 625 --> 676
# 114 --> -1 since 114 is not a perfect square


def find_next_square(sq):
    """Return the next square if sq is a square, -1 otherwise."""
    raiz = sq**0.5  # ** Exponencial de 0.5 é a raiz quadrada.
    if not raiz % 1:
        return (raiz + 1) ** 2
    return -1
