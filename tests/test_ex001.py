from pytest import mark

from codewars.ex001 import persistence


@mark.facil
@mark.parametrize('param, expected', [(999, 4), (39, 3), (4, 0)])
def test_persistence_deve_retornar_esperado(param, expected):
    """SUT (persistence)."""
    assert persistence(param) == expected
