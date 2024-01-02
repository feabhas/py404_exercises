import unittest
from post_codes import validate_postcode, capture_town

GOOD = (
    'B1 1AA',    'M13 9PL',
    'EX1 3PB',    'AB22 8GT',
    'W1A 1AA',    'SW1A 0AA',
)

BAD = (
    '1B 1AA',    'B1 11A',
    'B1 111',    'MA 9PL',
    'EX1 33P',   'EX1 3PBB',
    'AB228 GT',  'AB228 8GT',
    'WAA 1AA',   'W10A 1AA',
    'W1A1 1AA',  'SW10A 0AA',
    'SW1 A0AA',  '_A1 1AA', 
    'A1 9__',    '<=> +++'
)

class PostcodeTests(unittest.TestCase):
    def test_simple_A9_9AA_postcode_passes(self):
        result = validate_postcode('A9 9AA')
        self.assertTrue(result)

    def test_simple_A9_9AA_captures_A(self):
        result = capture_town('A9 9AA')
        self.assertEqual(result, 'A')

    def test_good_list_of_postcodes(self):
        for good in GOOD:
            with self.subTest(good=good):
                self.assertTrue(validate_postcode(good))

    def test_bad_list_of_postcodes(self):
        for bad in BAD:
            with self.subTest(bad=bad):
                self.assertFalse(validate_postcode(bad))


if __name__ == '__main__':
    unittest.main()