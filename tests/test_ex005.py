from pytest import mark

from codewars.ex005 import is_isogram


@mark.facil
@mark.parametrize(
    'param, expected',
    [
        ('Dermatoglyphics', True),
        ('aba', False),
        ('moOse', False),
        ('isogram', True),
        ('isIsogram', False),
        ('', True),
    ],
)
def test_is_isogram_deve_retornar_esperado(param, expected):
    assert is_isogram(param) == expected
