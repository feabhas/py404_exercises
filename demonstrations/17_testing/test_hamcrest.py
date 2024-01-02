#!/usr/bin/env python3

import unittest, platform
import triangle
from hamcrest import *

class TestMatchers(unittest.TestCase):
    def testPlatform(self):
        assert_that(platform.system(), is_(equal_to_ignoring_case('linux')))

    def testSorted(self):
        results = sorted( (6, 3, 8, 7, 1) )
        assert_that(len(results), is_(equal_to(5)))
        assert_that(results, has_length(5))
        assert_that(results, contains(1, 3, 6, 7, 8))

    def test_create_invalid_123_triangle_raises_TriangleError(self):
        assert_that(calling(triangle.Triangle).with_args(1, 2, 3),
                    raises(triangle.TriangleError, 'invalid sides'))


if __name__ == '__main__':
    unittest.main()