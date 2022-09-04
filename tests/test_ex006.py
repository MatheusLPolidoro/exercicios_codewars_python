from pytest import mark

from codewars.ex006 import high_and_low


@mark.facil
@mark.parametrize(
    'param, expected',
    [
        ('8 3 -5 42 -1 0 0 -9 4 7 4 -4', '42 -9'),
        ('1 2 3', '3 1'),
        ('test test -198 +182i1', '182 -198'),
    ],
)
def test_high_and_low_deve_retornar_esperado(param, expected):
    assert high_and_low(param) == expected
