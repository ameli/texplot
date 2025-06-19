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

import sys


# ===========
# is notebook
# ===========

def is_notebook():
    """
    Returns ``True`` if this script is running in a jupyter notebook. Returns
    ``False`` otherwise, including both ipython and python.
    """

    try:
        from IPython import get_ipython
        ip = get_ipython()

        if ip is None:
            return False

        else:
            shell = ip.__class__.__name__

            if shell == 'ZMQInteractiveShell':
                # Jupyter notebook or qtconsole
                return True

            elif shell == 'TerminalInteractiveShell':
                # Terminal running IPython
                return False

            elif "ipykernel" in sys.modules:
                # Any front-end built on ipykernel (Colab, Kaggle, VS Code)
                return True

            elif 'google.colab' in str(type(shell)):
                # Colab’s shell (older runtimes)
                return True

            else:
                # Other type
                return False

    except NameError:

        # Probably standard Python interpreter
        return False
