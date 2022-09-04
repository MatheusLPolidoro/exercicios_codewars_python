from pytest import mark

from codewars.ex003 import nb_year


@mark.facil
@mark.parametrize(
    'p0, percent, aug, p, expected',
    [
        (1500, 5, 100, 5000, 15),
        (1500000, 2.5, 10000, 2000000, 10),
        (1500000, 0.25, 1000, 2000000, 94),
    ],
)
def test_nb_year_deve_retornar_esperado(p0, percent, aug, p, expected):
    assert nb_year(p0, percent, aug, p) == expected
