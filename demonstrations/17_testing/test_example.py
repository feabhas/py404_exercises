#!/usr/bin/env python3

import unittest

class TestExample(unittest.TestCase):
    def test_success(self):
        self.assertTrue(True)

    def test_failure(self):
        self.fail('Example failed test')


if __name__ == '__main__':
    unittest.main()