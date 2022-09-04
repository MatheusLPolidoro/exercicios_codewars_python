# Um isograma é uma palavra que não tem letras repetidas,
# consecutivas ou não consecutivas. Implemente uma função
# que determina se uma string que contém apenas letras é um isograma.
# Suponha que a string vazia seja um isograma.
# Ignorar maiúsculas e minúsculas.

# Exemplo: (Entrada --> Saída)

# "Dermatoglyphics" --> true
# "aba" --> false
# "moOse" --> false (ignore letter case)


def is_isogram(string):
    """Isograms."""
    return len(string) == len(set(string.lower()))
