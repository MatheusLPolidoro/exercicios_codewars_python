from pytest import mark

from codewars.ex010 import to_camel_case


@mark.facil
@mark.parametrize(
    'param, expected',
    [
        ('', ''),
        ('the_stealth_warrior', 'theStealthWarrior'),
        ('The-Stealth-Warrior', 'TheStealthWarrior'),
        ('A-B-C', 'ABC'),
    ],
)
def test_to_camel_case_deve_retornar_camel_case(param, expected):
    """SUT (to_camel_case)"""
    assert to_camel_case(param) == expected
