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

__all__ = ['plot_bifurcation_diagram']


# ========================
# plot bifurcation diagram
# ========================

def plot_bifurcation_diagram(ax):
    """
    Plots bifurcation diagram for Logistic map.
    """

    fig = ax.figure
    fig.set_size_inches(9, 4)

    # Parameters for the bifurcation diagram
    r_values = numpy.linspace(2.5, 4.0, 10000)
    iterations = 10000
    last_iterations = 150

    # Initialize the array to store the values of x for plotting
    x = 0.1 * numpy.ones(r_values.size)

    # Compute the bifurcation diagram
    for i in range(iterations):
        x = r_values * x * (1 - x)
        if i >= (iterations - last_iterations):
            ax.plot(r_values, x, ',w', alpha=0.13)

    ax.set_title('Bifurcation Diagram of the Logistic Map')
    ax.set_xlabel(r'Rate of Reproduction $(r)$')
    ax.set_ylabel(r'Population Ratio $(x)$')
    ax.set_xlim([2.5, 4.0])
    ax.set_ylim([0, 1])

    fig.tight_layout()
