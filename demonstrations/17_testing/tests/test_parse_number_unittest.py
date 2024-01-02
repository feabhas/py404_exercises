import unittest
from utils import parse_number

HEX_VALUES = (
    ('0x0', 0),  ('0x1', 1),  ('0xa', 10), ('0xA', 10),
    ('0xf', 15), ('0xF', 15), ('0x10', 16), ('0xA00', 2560),
)

class TestParseNumber(unittest.TestCase):
    def test_parse_123_returns_int_123(self):
        self.assertEqual(parse_number('123'), 123)

    def test_parse_12_34_returns_float_12_34(self):
        self.assertAlmostEqual(parse_number('12.34'), 12.34)

    def test_parse_hex_numbers_returns_int(self):
        for text, value in HEX_VALUES:
            with self.subTest(text=text, value=value):
                self.assertEqual(parse_number(text), value)

    def test_parse_junk_raises_ValueError(self):
        with self.assertRaises(ValueError):
            parse_number('junk')

    def test_parse_junk_raises_ValueError_invalid_literal(self):
        with self.assertRaisesRegex(ValueError, 'invalid literal'):
            parse_number('junk')

if __name__ == "__main__":
    unittest.main()
