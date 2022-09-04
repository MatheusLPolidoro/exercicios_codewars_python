# Em uma pequena cidade a população está p0 = 1000
# no início de um ano. A população aumenta regularmente a 2 percent cada
# ano e, além disso, 50 novos habitantes por ano vêm morar na cidade.
# Quantos anos a cidade precisa para ver sua população
# maior ou igual aos p = 1200 habitantes?

# Parâmetros dados:

# p0,
# percent,
# aug (habitantes que chegam ou saem a cada ano),
# p (população a ultrapassar)

# Exemplos:
# nb_year(1500, 5, 100, 5000) -> 15
# nb_year(1500000, 2.5, 10000, 2000000) -> 10


def nb_year(p0, percent, aug, p):
    """Growth of a Population."""
    years = 0
    while p0 < p:
        p0 = int(p0 + (p0 / 100 * percent) + aug)
        years += 1
    return years
