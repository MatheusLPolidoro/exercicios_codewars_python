# Você vai receber uma palavra. Seu trabalho é retornar o caractere
#  do meio da palavra. Se o comprimento da palavra for ímpar,
# retorne o caractere do meio. Se o comprimento da palavra for par,
# retorne os 2 caracteres do meio.

# #Exemplos:

# Kata.getMiddle("test") should return "es"

# Kata.getMiddle("testing") should return "t"

# Kata.getMiddle("middle") should return "dd"

# Kata.getMiddle("A") should return "A"


def get_middle(string):
    """Get the Middle Character."""
    mid = len(string) // 2
    mid = mid - 1 if not len(string) % 2 else mid
    if mid:
        return string[mid:-mid]
    return string
