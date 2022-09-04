from pytest import mark

from codewars.ex004 import duplicate_encode


@mark.facil
@mark.parametrize(
    'param, expected',
    [
        ('din', '((('),
        ('recede', '()()()'),
        ('Success', ')())())'),
        ('(( @', '))(('),
    ],
)
def test_duplicate_encode_deve_retornar_esperado(param, expected):
    assert duplicate_encode(param) == expected
