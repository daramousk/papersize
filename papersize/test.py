# Copyright 2015 Louis Paternault
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""Tests"""

from decimal import Decimal
import doctest
import os
import unittest

import papersize

class TestParse(unittest.TestCase):
    # pylint: disable = invalid-name, star-args

    def assertIterAlmostEqual(self, iter1, iter2):
        for left, right in zip(iter1, iter2):
            self.assertAlmostEqual(Decimal(left), Decimal(right))

    def testParseLength(self):
        for (args, result) in [
                (("10cm", "mm"), 100),
                (("10in",), 722.7),
            ]:
            self.assertAlmostEqual(
                papersize.parse_length(*args),
                Decimal(result),
                )

    def testParseCouple(self):
        for (args, result) in [
                (("10cmx1mm",), (284.5275591, 2.845275591)),
                (("10cmx1mm", "mm"), (100, 1)),
                (("2pc x 3dd", "pt"), (24, 3.21)),
            ]:
            self.assertIterAlmostEqual(
                papersize.parse_couple(*args),
                result,
                )

    def testParsePaperSize(self):
        for (args, result) in [
                (("a4", "cm"), (21, 29.7)),
                (("20cm x 1mm", "cm"), (20, 0.1)),
                (("quarto", ), (650.43, 794.97)),
            ]:
            self.assertIterAlmostEqual(
                papersize.parse_papersize(*args),
                result,
                )

    def testConvertLength(self):
        for (args, result) in [
                ((10, "cm", "mm"), 100),
                ((1, "mm", "pt"), 2.845275591),
            ]:
            self.assertAlmostEqual(
                papersize.convert_length(*args),
                Decimal(result),
                )

class TestOrientation(unittest.TestCase):
    # pylint: disable = invalid-name, star-args

    def testPortraitLandscape(self):
        self.assertTrue(papersize.is_portrait(10, 11))
        self.assertTrue(papersize.is_portrait(10, 10))
        self.assertFalse(papersize.is_portrait(11, 10))

        self.assertFalse(papersize.is_landscape(10, 11))
        self.assertTrue(papersize.is_landscape(10, 10))
        self.assertTrue(papersize.is_landscape(11, 10))

        self.assertFalse(papersize.is_square(10, 11))
        self.assertTrue(papersize.is_square(10, 10))
        self.assertFalse(papersize.is_square(11, 10))

    def testRotate(self):
        self.assertEqual(
            papersize.rotate((10, 11), True),
            (10, 11),
            )
        self.assertEqual(
            papersize.rotate((10, 11), False),
            (11, 10),
            )

def suite():
    """Return a :class:`TestSuite` object, testing all module :mod:`papersize`.
    """
    test_loader = unittest.defaultTestLoader
    return test_loader.discover(os.path.dirname(__file__))

def load_tests(__loader, tests, __pattern):
    # Loading doctests
    tests.addTests(doctest.DocTestSuite(papersize))

    # Unittests are loaded by default

    return tests

if __name__ == "__main__":
    unittest.TextTestRunner().run(suite())
