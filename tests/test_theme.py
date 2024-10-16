#! /usr/bin/env python

# SPDX-FileCopyrightText: Copyright 2022, Siavash Ameli <sameli@berkeley.edu>
# SPDX-License-Identifier: BSD-3-Clause
# SPDX-FileType: SOURCE
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the license found in the LICENSE.txt file in the root directory
# of this source tree.


# =======
# Imports
# =======

import matplotlib.pyplot as plt
import texplot
import os
import glob

# import warnings
# warnings.resetwarnings()
# warnings.filterwarnings("error")


# ===========
# remove file
# ===========

def remove_file(filename):
    """
    Remove file.
    """

    # Get a list of all files matching wildcard
    files_list = glob.glob(filename)

    # Iterate over files
    for file in files_list:
        try:
            os.remove(file)
        except BaseException as error:
            print('An exception occurred: {}'.format(error))
            print("Error while removing file : ", file)


# ==========
# test theme
# ==========

def test_theme():
    """
    Test for `theme`, `set_theme`, `reset_theme`, and `save_plot` functions.
    """

    texplot.set_theme(use_latex=False)

    # Plot an example function
    fig1, ax1 = plt.subplots()
    texplot.examples.plot_function(ax1)
    texplot.save_plot(plt, filename='function1.pdf',
                      transparent_background=True, dpi=200, verbose=True)

    # Reset theme
    texplot.reset_theme()

    # Check context manager for with environmebt
    with texplot.theme():
        fig2, ax2 = plt.subplots()
        texplot.examples.plot_function(ax2)
        texplot.save_plot(plt, filename='function2.pdf',
                          transparent_background=True, dpi=200, verbose=True)

    # Check context manager for function
    def plot():
        fig3, ax3 = plt.subplots()
        texplot.examples.plot_lorenz(ax3)
        texplot.save_plot(plt, filename='lorenz.pdf',
                          transparent_background=True, dpi=200, verbose=True)

    plot()

    # Chech theme options
    with texplot.theme(
            rc={'font.family': 'sans-serif'},
            style='dark_background',
            font_scale=1.2,
            use_latex=False):

        # Plot an example diagram
        fig4, ax4 = plt.subplots()
        texplot.examples.plot_bifurcation_diagram(ax4)
        texplot.save_plot(plt, filename='bifircation.pdf',
                          transparent_background=True, dpi=200, verbose=True)

    # Remove outputs
    remove_file('*.svg')
    remove_file('*.pdf')


# ===========
# Script main
# ===========

if __name__ == "__main__":
    test_theme()
