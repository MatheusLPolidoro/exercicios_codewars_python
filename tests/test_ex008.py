from pytest import mark

from codewars.ex008 import get_middle


@mark.facil
@mark.parametrize(
    'param, expected',
    [
        ('test', 'es'),
        ('testing', 't'),
        ('middle', 'dd'),
        ('A', 'A'),
        ('of', 'of'),
    ],
)
def test_get_middle_deve_retornar_esperado(param, expected):
    """SUT (get_middle)."""
    assert get_middle(param) == expected
