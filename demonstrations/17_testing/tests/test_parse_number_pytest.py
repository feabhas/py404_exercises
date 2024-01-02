import pytest
from utils import parse_number

def test_parse_123_returns_int_123():
    assert parse_number('123') == 123

def test_parse_12_34_returns_float_12_34():
    assert parse_number('12.34') == pytest.approx(12.34)

@pytest.mark.parametrize("text,value", (
    ('0x0', 0), ('0x1', 1), ('0xa', 10), ('0xA', 10),
    ('0xf', 15), ('0xF', 15), ('0x10', 16), ('0xA00', 2560),
))
def test_parse_hex_numbers_returns_int(text, value):
    assert parse_number(text) == value

def test_parse_junk_raises_ValueError():
    with pytest.raises(ValueError):
        parse_number('junk')

def test_parse_junk_raises_ValueError_invalid_literal():
    with pytest.raises(ValueError, match='invalid literal'):
        parse_number('junk')

class TestParseNumber:
    def test_parse_123_returns_int_123(self):
        assert parse_number('123') == 123
