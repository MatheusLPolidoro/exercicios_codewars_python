# Escreva uma função, que receba um parâmetro positivo e retorne sua
# persistência multiplicativa, que é o número de vezes que você deve
# multiplicar os dígitos até chegar a um único dígito.

# Por exemplo (Entrada --> Saída) :

# 999 --> 4 (9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2)
# 39 --> 3 (3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit)
# 4 --> 0 (4 já é apenas um digito)

from functools import reduce


def persistence(num):
    """Returns how many times a number should be multiplied."""
    result = 0
    while num > 9:
        list_num = [int(dig) for dig in str(num)]
        num = reduce(
            lambda first_dig, second_dig: first_dig * second_dig, list_num
        )
        result += 1
    return result
