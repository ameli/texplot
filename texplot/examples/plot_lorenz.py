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
from scipy.integrate import solve_ivp

__all__ = ['plot_lorenz']


# ======
# lorenz
# ======

def _lorenz(t, x):
    """
    Lorenz dynamical system.
    """

    return [10*(x[1]-x[0]), x[0]*(28-x[2])-x[1], x[0]*x[1]-x[2]*8/3]


# ===========
# plot lorenz
# ===========

def plot_lorenz(ax):
    """
    Plots the x variable of the Lorentx dynamical system.
    """

    fig = ax.figure
    fig.set_size_inches(9, 3)

    t = numpy.linspace(0, 90, 10000)
    sol = solve_ivp(_lorenz, [t[0], t[-1]], [1, 1, 1], t_eval=t, method='RK45')

    ax.plot(sol.t, sol.y[0], label='x(t)', color='k')
    ax.set_xlim(t[0], t[-1])
    ax.set_title(r'Lorenz System - $x(t)$ vs Time')
    ax.set_xlabel('Time')
    ax.set_ylabel(r'$x(t)$')

    fig.tight_layout()
