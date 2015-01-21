# Copyright Louis Paternault 2015
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
# along with this program.  If not, see <http://www.gnu.org/licenses/>. 1

"""Paper-size related data and functions"""

from decimal import Decimal
import os
import re
import subprocess

VERSION = "0.0.0"
__AUTHOR__ = "Louis Paternault (spalax@gresille.org)"
__COPYRIGHT__ = "(C) 2015 Louis Paternault. GNU GPL 3 or later."
# TODO Hide every private variable

SIZES = {
    # http://www.printernational.org/iso-paper-sizes.php
    "4a0": "1682mm x 2378mm",
    "2a0": "1189mm x 1682mm",
    "a0": "841mm x 1189mm",
    "a1": "594mm x 841mm",
    "a2": "420mm x 594mm",
    "a3": "297mm x 420mm",
    "a4": "210mm x 297mm",
    "a5": "148mm x 210mm",
    "a6": "105mm x 148mm",
    "a7": "74mm x 105mm",
    "a8": "52mm x 74mm",
    "a9": "37mm x 52mm",
    "a10": "26mm x 37mm",

    "b0": "1000mm x 1414mm",
    "b1": "707mm x 1000mm",
    "b2": "500mm x 707mm",
    "b3": "353mm x 500mm",
    "b4": "250mm x 352mm",
    "b5": "176mm x 250mm",
    "b6": "125mm x 176mm",
    "b7": "88mm x 125mm",
    "b8": "62mm x 88mm",
    "b9": "44mm x 62mm",
    "b10": "31mm x 44mm",

    # http://www.paper-sizes.com/north-american-paper-sizes/north-american-architectural-paper-sizes
    "archA": "9in x 12in",
    "archB": "12in x 18in",
    "archC": "18in x 24in",
    "archD": "24in x 36in",
    "archE": "36in x 48in",

    # http://www.engineeringtoolbox.com/office-paper-sizes-d_213.html
    "letter": "8.5in x 11in",
    "legal": "8.5in x 14in",
    "executive": "7in x 10in",
    "tabloid": "11in x 17in",
    "statement": "5in x 8.5in",
    "halfletter": "5in x 8.5in",
    "folio": "8in x 13in",

    # http://www.paper-sizes.com/north-american-paper-sizes/north-american-loose-paper-sizes
    "ledger": "17in x 11in",

    # http://simple.wikipedia.org/wiki/Paper_size
    "quarto": "8in x 10in",

    # http://hplipopensource.com/hplip-web/tech_docs/page_sizes.html
    "flsa": "8.5in x 13in",

    # http://www.coding-guidelines.com/numbers/ndb/units/area.txt
    "flse": "8.5in x 13in",

    # http://jexcelapi.sourceforge.net/resources/javadocs/2_6_10/docs/jxl/format/PaperSize.html
    "note": "8.5in x 11in",
    "11x17": "11in x 17in",
    "10x14": "10in x 14in",

    }

# Source: http://en.wikibooks.org/wiki/LaTeX/Lengths
UNITS = {
    "": 1, # Default is point (pt)
    "pt": 1,
    "mm": 2.84,
    "cm": 28.4,
    "in": 72.27,
    "bp": 1.00375,
    "pc": 12,
    "dd": 1.07,
    "cc": 12.84,
    "sp": 0.000015,
    }

UNITS_RE = r"({})".format("|".join(UNITS.keys()))
SIZE_RE = r"([\d.]+){}".format(UNITS_RE)
PAPERSIZE_RE = r"^(?P<width>{size}) *[x× ]? *(?P<height>{size})$".format(
    size=SIZE_RE
    )

UNITS_COMPILED_RE = re.compile("^{}$".format(UNITS_RE))
SIZE_COMPILED_RE = re.compile("^{}$".format(SIZE_RE).format("size"))
PAPERSIZE_COMPILED_RE = re.compile(PAPERSIZE_RE.format("width", "height"))

class PapersizeException(Exception):
    """All exceptions of this module inherit from this one."""
    pass

class CouldNotParse(PapersizeException):
    pass

def convert_length(length, orig, dest):
    """TODO"""
    return (Decimal(UNITS[orig]) * length) / Decimal(UNITS[dest])

def parse_length(string, unit="pt"):
    """Return a length corresponding to the string.

    :return: The length, in points.
    :rtype: :class:`decimal.Decimal`
    """
    # TODO return value in the specified unit
    match = SIZE_COMPILED_RE.match(string).groups()
    return Decimal(match[0]) * Decimal(UNITS[match[1]])

def parse_couple(string):
    """Return a tuple of dimensions.

    :param str string: The string to parse, as "LENGTHxLENGTH" (where LENGTH
        are length). Example: ``21cm x 29.7cm``.
    :return: A tuple of :class:`decimal.Decimal`, reprenting the dimensions,
        in points.
    """
    try:
        match = PAPERSIZE_COMPILED_RE.match(string).groupdict()
        return (
            parse_length(match['width']),
            parse_length(match['height']),
            )
    except AttributeError:
        raise CouldNotParse(string)

def parse_paper_size(string):
    """Return the papersize corresponding to string.
    """
    if string.lower() in PAPERSIZES:
        return parse_paper_size(PAPERSIZES[string])
    return parse_couple(string)

def isPortrait(width, height):
    return width <= height

def isLandscape(width, height):
    return height <= width

def isSquare(width, height):
    return width == height

def rotate(size, portrait=True):
    if portrait:
        return (min(size), max(size))
    else:
        return (max(size), min(size))
