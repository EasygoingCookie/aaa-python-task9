from morse import decode
import pytest


@pytest.mark.parametrize(
    'test_input, expected',
    [
        ('... --- ...', 'SOS'),
        ('.--. -.-- - .... --- -.', 'PYTHON'),
        ('....- ..---', '42')
    ]
)
def test_morse_can_decode(test_input: str, expected: str):
    """Checking: func morse decodes a morse password to the text correctly"""
    assert decode(test_input) == expected
