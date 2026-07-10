#!/usr/bin/env python
##############################################################################
#
# (c) 2025 Sangjoon Lee.
# All rights reserved.
#
# File coded by: Sangjoon Lee.
#
# See GitHub contributions for a more detailed list of contributors.
# https://github.com/bobleesj/'/graphs/contributors
#
# See LICENSE.rst for license information.
#
##############################################################################
"""Python package for doing science."""

import warnings

warnings.warn(
    "bobleesj.utils is deprecated: its elemental data modules "
    "(oliynyk, mendeleev, ptable, radius, Formula, ElementSorter, numbers, Element) "
    "moved to cifkit>=1.2.1. Replace 'bobleesj.utils' with 'cifkit' in imports.",
    DeprecationWarning,
    stacklevel=2,
)

# package version
from bobleesj.utils.version import __version__

# silence the pyflakes syntax checker
assert __version__ or True

# End of file
