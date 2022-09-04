from pytest import mark

from codewars.ex012 import dirReduc


@mark.medio
@mark.parametrize(
    'param, expected',
    [(['NORTH', 'SOUTH', 'SOUTH', 'EAST', 'WEST', 'NORTH', 'WEST'], ['WEST'])],
)
def test_dirReduc_deve_retornar_esperado(param, expected):
    """SUT (dicReduc)."""
    assert dirReduc(param) == expected
