from pytest import mark

from codewars.ex013 import sort_array


@mark.facil
@mark.parametrize(
    'param, expected',
    [
        ([5, 3, 2, 8, 1, 4], [1, 3, 2, 8, 5, 4]),
        ([5, 3, 1, 8, 0], [1, 3, 5, 8, 0]),
        ([], []),
    ],
)
def test_sort_array_deve_retornar_impar_ordenado(param, expected):
    """SUT (sort_array)."""
    assert sort_array(param) == expected
