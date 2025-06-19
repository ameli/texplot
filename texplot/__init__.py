# SPDX-FileCopyrightText: Copyright 2021, Siavash Ameli <sameli@berkeley.edu>
# SPDX-License-Identifier: BSD-3-Clause
# SPDX-FileType: SOURCE
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the license found in the LICENSE.txt file in the root
# directory of this source tree.


# =======
# Imports
# =======

from .plot_utilities import theme, get_theme, set_theme, reset_theme, \
    save_plot, show_or_save_plot
from .display_utilities import is_notebook
from . import examples

__all__ = ['theme', 'get_theme', 'set_theme', 'reset_theme',
           'save_plot', 'show_or_save_plot', 'examples', 'is_notebook']

from .__version__ import __version__                          # noqa: F401 E402
