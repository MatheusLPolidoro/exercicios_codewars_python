from pytest import mark

from codewars.ex002 import find_next_square


@mark.facil
@mark.parametrize('param, expected', [(121, 144), (625, 676), (114, -1)])
def test_find_next_square_deve_retornar_esperado(param, expected):
    """SUT (find_next_square)."""
    assert find_next_square(param) == expected
