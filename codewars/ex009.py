# A função rgb está incompleta. Complete-o para que a passagem de valores
# decimais RGB resulte no retorno de uma representação hexadecimal.
# Os valores decimais válidos para RGB são 0 - 255.
# Quaisquer valores que estejam fora desse intervalo devem ser arredondados
# para o valor válido mais próximo.

# Nota: Sua resposta deve ter sempre 6 caracteres, a abreviação com 3 não funcionará aqui.

# A seguir estão exemplos de valores de saída esperados:

# rgb(255, 255, 255) # returns FFFFFF
# rgb(255, 255, 300) # returns FFFFFF
# rgb(0,0,0) # returns 000000
# rgb(148, 0, 211) # returns 9400D3


def rgb(r, g, b):
    """RGB To Hex Conversion."""

    def arred(num):
        return min(255, max(num, 0))

    return ('{:02X}' * 3).format(arred(r), arred(g), arred(b))
