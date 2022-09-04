from pytest import mark

from codewars.ex011 import max_sequence


@mark.medio
@mark.parametrize(
    'param, expected',
    [([], 0), ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6)],
)
def test_max_sequence_deve_retornar_soma_do_maior(param, expected):
    """SUT (max_sequence)"""
    assert max_sequence(param) == expected
