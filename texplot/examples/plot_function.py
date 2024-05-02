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

import numpy

__all__ = ['plot_function']


# =============
# plot function
# =============

def plot_function(ax):
    """
    Plot examples of two functions with unbounded variation.
    """

    fig = ax.figure
    fig.set_size_inches(9, 2.3)

    x = numpy.logspace(-2, 2, 10000)
    y1 = numpy.sin(1/x) * numpy.cos(x)
    y2 = numpy.sin(x) * numpy.sin(1/x)

    ax.plot(x, y1, label=r'$f: x \mapsto \sin(x^{-1}) \cos(x)$', color='black')
    ax.plot(x, y2, label=r'$g: x \mapsto \sin(x) \sin(x^{-1})$',
            color='maroon')
    ax.set_xlim(x[0], x[-1])
    ax.set_xlabel(r'$x$')
    ax.set_ylabel(r'$f, g$')
    ax.set_title(r'Functions of Unbounded Variation ' +
                 r'$f, g \notin \mathrm{BV}(\mathbb{R}_{+})$')
    ax.legend(loc='lower right', fontsize='small')
    ax.set_xscale('log')
    ax.set_yticks([-1, 0, 1])
    ax.grid(axis='y')

    fig.tight_layout()
