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

__all__ = ['plot_lorenz']


# ===
# add
# ===

def add(*args):
    """
    Add multiple vectors, optionally scaling each vector.

    Each argument is a tuple where the first element is the vector and the
    second element is the scale (if not provided, default to 1).
    """

    if not args:
        return []
    length = len(args[0][0])
    result = [0.0] * length
    for arg in args:
        vector, scale = arg if len(arg) == 2 else (arg[0], 1)
        result = [current + scale * value
                  for current, value in zip(result, vector)]
    return result


# =====
# scale
# =====

def scale(v, scale):
    """
    Scale a vector by a given factor.
    """

    return [x * scale for x in v]


# ====
# norm
# ====

def norm(v):
    """
    Calculate the infinity norm (max absolute value) of a vector.
    """

    return max(abs(x) for x in v)


# =========
# solve ivp
# =========

def _solve_ivp(f, t_span, y0, tol=1e-6):
    """
    An implementation of the RK45 method with adaptive step size for solving
    systems of ODEs.

    Parameters:
        f: Function representing the ODE system (dy/dt = f(t, y))
        t_span: Tuple of (start, end) times
        y0: Initial condition (array for systems of ODEs)
        tol: Tolerance for adaptive step size control (default is 1e-6)

    Returns:
        t_values: List of time values at computed points
        y_values: List of solution values at computed points

    Notes:
        This implementation does not require numpy and scipy. All vector
        operations are performed using Python's lists. This might be slow, but
        the advantage os that the package does not require numpy dependency.
    """

    t0, tf = t_span
    t_values = [t0]
    y_values = [y0]

    t = t0
    y = y0
    h = min(0.1, tf-t0)  # Initial step size

    while t < tf:
        if t + h > tf:
            h = tf - t

        k1 = f(t, y)
        k2 = f(t + 0.25 * h, add((y, 1), (scale(k1, 0.25 * h), 1)))
        k3 = f(t + 3/8 * h, add((y, 1),
                                (scale(k1, 3/32 * h), 1),
                                (scale(k2, 9/32 * h), 1)))
        k4 = f(t + 12/13 * h, add((y, 1),
                                  (scale(k1, 1932/2197 * h), 1),
                                  (scale(k2, -7200/2197 * h), 1),
                                  (scale(k3, 7296/2197 * h), 1)))
        k5 = f(t + h, add((y, 1),
                          (scale(k1, 439/216 * h), 1),
                          (scale(k2, -8 * h), 1),
                          (scale(k3, 3680/513 * h), 1),
                          (scale(k4, -845/4104 * h), 1)))
        k6 = f(t + 0.5 * h, add((y, 1),
                                (scale(k1, -8/27 * h), 1),
                                (scale(k2, 2 * h), 1),
                                (scale(k3, -3544/2565 * h), 1),
                                (scale(k4, 1859/4104 * h), 1),
                                (scale(k5, -11/40 * h), 1)))

        y4 = add((y, 1),
                 (scale(k1, 25/216 * h), 1),
                 (scale(k3, 1408/2565 * h), 1),
                 (scale(k4, 2197/4104 * h), 1),
                 (scale(k5, -0.2 * h), 1))
        y5 = add((y, 1),
                 (scale(k1, 16/135 * h), 1),
                 (scale(k3, 6656/12825 * h), 1),
                 (scale(k4, 28561/56430 * h), 1),
                 (scale(k5, -9/50 * h), 1),
                 (scale(k6, 2/55 * h), 1))

        error = norm([a - b for a, b in zip(y4, y5)]) / h

        # Adjust the step size
        if error < tol:
            t += h
            y = y5
            t_values.append(t)
            y_values.append(y)
            h *= min(1.5, (tol / error) ** 0.25)  # Safely increase step size
        else:
            h *= max(0.5, (tol / error) ** 0.25)  # Reduce step size

    return t_values, y_values


# ======
# lorenz
# ======

def _lorenz(t, x):
    """
    Lorenz dynamical system.
    """

    sigma, rho, beta = 10, 28, 8/3

    dx = [sigma * (x[1] - x[0]),
          x[0] * (rho - x[2]) - x[1],
          x[0] * x[1] - x[2] * beta]

    return dx


# ===========
# plot lorenz
# ===========

def plot_lorenz(ax):
    """
    Plots the x variable of the Lorentx dynamical system.
    """

    fig = ax.figure
    fig.set_size_inches(9, 3)

    t_span = [0, 90]
    y0 = [1, 1, 1]
    t, y = _solve_ivp(_lorenz, t_span, y0)

    # Get the first compoent of the vector
    y_0 = [y_[0] for y_ in y]

    ax.plot(t, y_0, label='x(t)', color='k')
    ax.set_xlim(t[0], t[-1])
    ax.set_title(r'Lorenz System - $x(t)$ vs Time')
    ax.set_xlabel('Time')
    ax.set_ylabel(r'$x(t)$')

    fig.tight_layout()
