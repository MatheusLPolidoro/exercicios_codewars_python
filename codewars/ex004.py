# O objetivo deste exercício é converter uma string em uma nova string
# onde cada caractere na nova string é "("se esse caractere aparecer
# apenas uma vez na string original ou ")"se esse caractere aparecer
# mais de uma vez na string original.
# Ignore a capitalização ao determinar se um caractere é uma duplicata.

# Exemplos
# "din"      =>  "((("
# "recede"   =>  "()()()"
# "Success"  =>  ")())())"
# "(( @"     =>  "))(("


def duplicate_encode(word):
    """Duplicate Encoder."""
    result = ''
    word = word.upper()
    for caract in word:
        if word.count(caract) > 1:
            result += ')'
        else:
            result += '('
    return result
