# This file is part of the pyMOR project (http://www.pymor.org).
# Copyright 2013-2020 pyMOR developers and contributors. All rights reserved.
# License: BSD 2-Clause License (http://opensource.org/licenses/BSD-2-Clause)
from pymor.core.exceptions import CythonExtensionNotBuiltError


def iadd_masked(U, V, U_ind):
    """This cython function is defined in pymor/discretizers/builtin/inplace.pyx."""
    raise CythonExtensionNotBuiltError()


def isub_masked(U, V, U_ind):
    """This cython function is defined in pymor/discretizers/builtin/inplace.pyx."""
    raise CythonExtensionNotBuiltError()
