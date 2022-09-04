from pytest import mark

from codewars.ex009 import rgb


@mark.facil
@mark.parametrize(
    'r, g, b, expected',
    [
        (0, 0, 0, '000000'),
        (1, 2, 3, '010203'),
        (255, 255, 255, 'FFFFFF'),
        (254, 253, 252, 'FEFDFC'),
        (-20, 275, 125, '00FF7D'),
    ],
)
def test_rgb_deve_retornar_esperado(r, g, b, expected):
    """SUT (rgb)"""
    assert rgb(r, g, b) == expected
