from pytest import mark

from codewars.ex007 import number


@mark.facil
@mark.parametrize(
    'param, expected',
    [
        ([[10, 0], [3, 5], [5, 8]], 5),
        ([[3, 0], [9, 1], [4, 10], [12, 2], [6, 1], [7, 10]], 17),
        ([[3, 0], [9, 1], [4, 8], [12, 2], [6, 1], [7, 8]], 21),
    ],
)
def test_number_deve_retornar_esperado(param, expected):
    assert number(param) == expected
