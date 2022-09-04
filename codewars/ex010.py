# Complete o método/função para que ele converta palavras
# delimitadas por traço/sublinhado em caixa de camelo.
# A primeira palavra na saída deve ser maiúscula apenas se a palavra
# original estiver em maiúscula (conhecida como Upper Camel Case,
# também conhecida como Pascal case).

# Exemplos
# "the-stealth-warrior"se converte em "theStealthWarrior"
# "The_Stealth_Warrior"se converte em"TheStealthWarrior"


def to_camel_case(text):
    """Convert string to camel case."""
    return (
        text[0] + text.title().translate(str.maketrans('', '', '-_'))[1:]
        if text
        else text
    )
