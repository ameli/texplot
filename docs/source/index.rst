.. module:: texplot

|project| Documentation
***********************

|deploy-docs|

|project| is a python package to enhance `matplotlib` plots with publication-quality style.

.. grid:: 4

    .. grid-item-card:: GitHub
        :link: https://github.com/ameli/texplot
        :text-align: center
        :class-card: custom-card-link

    .. grid-item-card:: PyPI
        :link: https://pypi.org/project/texplot/
        :text-align: center
        :class-card: custom-card-link

    .. grid-item-card:: Anaconda
        :link: https://anaconda.org/s-ameli/texplot
        :text-align: center
        :class-card: custom-card-link

    .. grid-item-card:: API reference
        :link: api
        :link-type: ref
        :text-align: center
        :class-card: custom-card-link

Install
=======

|pypi| |conda-version|

.. grid:: 2

    .. grid-item-card:: 

        Install with ``pip`` from `PyPI <https://pypi.org/project/texplot/>`_:

        .. prompt:: bash
            
            pip install texplot

    .. grid-item-card::

        Install with ``conda`` from `Anaconda Cloud <https://anaconda.org/s-ameli/texplot>`_:

        .. prompt:: bash
            
            conda install s-ameli::texplot

This package requires :math:`\LaTeX` to be installed. Ensure that the ``latex`` executable is available on your system's ``PATH``.

Set Theme
=========

|project| can set theme either globally or locally:

Set Theme Globally
------------------

Call :func:`texplot.set_theme` function to set the |project| theme globally in your script:

.. code-block:: python
   :emphasize-lines: 2, 3

    >>> import matplotlib.pyplot as plt
    >>> import texplot
    >>> texplot.set_theme()

    >>> # Plot an example function
    >>> fig, ax = plt.subplots()
    >>> texplot.examples.plot_function(ax)
    >>> plt.show()

.. figure:: _static/images/plots/function.png
   :align: left
   :figwidth: 100%
   :width: 100%
   :class: custom-dark

The theme set as described above will affect your entire Python script for its duration. However, you can revert to the default `matplotlib` theme at any time by calling the :func:`texplot.reset_theme` function as shown below:

.. code-block:: python
   :emphasize-lines: 2

    >>> # Resetting to default matplotlib theme
    >>> texplot.reset_theme()

    >>> # Plot another example function
    >>> fig2, ax2 = plt.subplots()
    >>> texplot.examples.plot_function(ax2)
    >>> plt.show()

.. figure:: _static/images/plots/function_no_theme.png
   :align: left
   :figwidth: 100%
   :width: 100%
   :class: custom-dark


Set Theme Within a Local Scope
------------------------------

The :func:`texplot.theme` function acts as a context manager, allowing you to apply the |project| theme within a specific local scope or function. The example below demonstrates setting the theme in a local scope. Outside of this scope, the default `matplotlib` theme remains unchanged.

.. code-block:: python
   :emphasize-lines: 4

    >>> import matplotlib.pyplot as plt
    >>> import texplot

    >>> with texplot.theme():
    >>>     fig, ax = plt.subplots()
    >>>     texplot.examples.plot_function(ax)
    >>>     plt.show()

Similarly, you can use the context manager with a function. In the example below, the |project| theme is applied only within the ``plot()`` function. Outside this function, the default `matplotlib` theme remains unchanged.

.. code-block:: python
   :emphasize-lines: 4

    >>> import matplotlib.pyplot as plt
    >>> import texplot

    >>> @texplot.theme()
    >>> def plot():
    >>>     fig, ax = plt.subplots()
    >>>     texplot.examples.plot_function(ax)
    >>>     plt.show()
    
    >>> plot()

Theme Options
=============

You can customize the theme by passing arguments to either the :func:`texplot.set_theme` or :func:`texplot.theme` functions. The parameters for both functions are identical and detailed in the :ref:`API reference <api>`. The available arguments are as follows:

.. list-table::
    :header-rows: 1

    * - Argument
      - Value
      - Description
    * - ``context``
      - ``'paper'``, ``'notebook'`` (default), ``'talk'``, or ``'poster'``
      - Adjusts font size and scales of the plot depending on the context.
    * - ``style``
      - See `matplotlib.style.available <https://matplotlib.org/stable/api/style_api.html#matplotlib.style.available>`__
      - Sets `matplotlib style <https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html>`__
    * - ``font_scale``
      - float (default is ``1``)
      - Scales the fonts.
    * - ``use_latex``
      - boolean (default is ``None``)
      - If ``True``, the mathematical symbols are rendered with :math:`\LaTeX`.
    * - ``rc``
      - dictionary (default is ``{}``)
      - Passes any additional `matplotlib`'s `rcParam dictionary <https://matplotlib.org/stable/users/explain/customizing.html>`__.

In the example below, we configure a dark background style, increase the font size by a factor of 1.2, and set the font family to sans-serif:

.. code-block:: python
   :emphasize-lines: 4, 5, 6, 7

    >>> import matplotlib.pyplot as plt
    >>> import texplot

    >>> with texplot.theme(
    ...         rc={'font.family': 'sans-serif'},
    ...         style='dark_background',
    ...         font_scale=1.2):
    >>>
    >>>     # Plot an example diagram
    >>>     fig, ax = plt.subplots()
    >>>     texplot.examples.plot_bifurcation_diagram(ax)
    >>>     plt.show()

.. figure:: _static/images/plots/logistic.png
   :align: left
   :figwidth: 100%
   :width: 100%

Show and Save Plots
===================

When working on a machine without display graphics, such as a remote server that lacks X11, displaying plots is not possible. Instead, plots should be saved. The :func:`texplot.save_plot` function provides a simple wrapper around `matplotlib.pyplot.savefig <https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html>`__ to facilitate this. Additionally, the :func:`texplot.show_or_save_plot` function attempts to display plots initially. If no graphical backend is available, it saves the plot instead. Additionally, you can configure it to both show and save the plot. Here is an example:

.. code-block:: python
   :emphasize-lines: 11, 12, 13

    >>> import matplotlib.pyplot as plt
    >>> import texplot

    >>> with texplot.theme(rc={'font.family': 'sans-serif'}):
    >>>
    >>>     # Plot an example function
    >>>     fig, ax = plt.subplots()
    >>>     texplot.examples.lorenz(ax)
    >>>
    >>>     # Show and save plot
    >>>     texplot.show_or_save_plot(plt, default_filename='lorenz.pdf',
    ...                               transparent_background=True, dpi=200,
    ...                               show_and_save=True, verbose=True)
    plot saved to '/home/user/lorenz.pdf'.

.. figure:: _static/images/plots/lorenz.png
   :align: left
   :figwidth: 100%
   :width: 100%
   :class: custom-dark

Test Package
============

|build-linux| |codecov-devel|

To test the package, first clone the source code from the repository and install the required test packages by:

.. prompt:: bash

    git clone https://github.com/ameli/texplot.git
    cd texplot
    python -m pip install -r tests/requirements.txt
    python -m pip install .

Then, test with `pytest <https://docs.pytest.org/>`__:

.. prompt:: bash

    pytest

How to Contribute
=================

We welcome contributions via `GitHub's pull request <https://github.com/ameli/texplot/pulls>`_. If you do not feel comfortable modifying the code, we also welcome feature requests and bug reports as `GitHub issues <https://github.com/ameli/texplot/issues>`_.

License
=======

|license|

.. This package includes `Computer Modern <https://tug.org/FontCatalogue/computermodern/>`__ font for rendering :math:`\LaTeX`, which is distributed under `Knuth license <https://www.ctan.org/license/knuth>`__, a permissive license authored by Donald Knuth.

.. |deploy-docs| image:: https://img.shields.io/github/actions/workflow/status/ameli/texplot/deploy-docs.yml?label=docs
   :target: https://github.com/ameli/texplot/actions?query=workflow%3Adeploy-docs
.. |deploy-docker| image:: https://img.shields.io/github/actions/workflow/status/ameli/texplot/deploy-docker.yml?label=build%20docker
   :target: https://github.com/ameli/texplot/actions?query=workflow%3Adeploy-docker
.. |codecov-devel| image:: https://codecov.io/gh/ameli/texplot/graph/badge.svg?token=52HVURUBK1
   :target: https://codecov.io/gh/ameli/texplot
.. |license| image:: https://img.shields.io/github/license/ameli/texplot
   :target: https://opensource.org/licenses/BSD-3-Clause
.. |implementation| image:: https://img.shields.io/pypi/implementation/texplot
.. |pyversions| image:: https://img.shields.io/pypi/pyversions/texplot
.. |format| image:: https://img.shields.io/pypi/format/texplot
.. |pypi| image:: https://img.shields.io/pypi/v/texplot
.. |conda| image:: https://anaconda.org/s-ameli/texplot/badges/installer/conda.svg
   :target: https://anaconda.org/s-ameli/texplot
.. |platforms| image:: https://img.shields.io/conda/pn/s-ameli/texplot?color=orange?label=platforms
   :target: https://anaconda.org/s-ameli/texplot
.. |conda-version| image:: https://img.shields.io/conda/v/s-ameli/texplot
   :target: https://anaconda.org/s-ameli/texplot
.. |conda-downloads| image:: https://img.shields.io/conda/dn/s-ameli/texplot
   :target: https://anaconda.org/s-ameli/texplot
.. |tokei| image:: https://tokei.ekzhang.com/b1/github/ameli/texplot?category=lines
   :target: https://github.com/ameli/texplot
.. |languages| image:: https://img.shields.io/github/languages/count/ameli/texplot
   :target: https://github.com/ameli/texplot
.. |build-linux| image:: https://img.shields.io/github/actions/workflow/status/ameli/texplot/build-linux.yml
   :target: https://github.com/ameli/texplot/actions?query=workflow%3Abuild-linux 
.. .. |binder| image:: https://mybinder.org/badge_logo.svg
..    :target: https://mybinder.org/v2/gh/ameli/texplot/HEAD?filepath=notebooks%2Fquick_start.ipynb
