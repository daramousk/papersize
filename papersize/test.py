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

import os
import unittest

import papersize

class TestUnits(unittest.TestCase):
    def testConvert(self):
        self.assertEqual(papersize.convert_length(1, "cm", "mm"), 10)
        self.assertEqual(papersize.convert_length(10, "mm", "cm"), 1)

def suite():
    """Return a :class:`TestSuite` object, testing all module :mod:`papersize`.
    """
    test_loader = unittest.defaultTestLoader
    return test_loader.discover(os.path.dirname(__file__))

if __name__ == "__main__":
    unittest.TextTestRunner().run(suite())
