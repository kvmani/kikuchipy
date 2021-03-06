=============
API reference
=============

This reference manual details the public classes, modules and functions in
kikuchipy, as generated from their docstrings. Many of the docstrings contain
examples, however, see the user guide for how to use kikuchipy.

.. caution::

    kikuchipy is in an alpha stage, and there will be breaking changes with each
    release.

signals
=======

.. automodule:: kikuchipy.signals

EBSD
----

All methods listed here are also available to
:class:`~kikuchipy.signals.LazyEBSD` objects.

.. currentmodule:: kikuchipy.signals.EBSD

.. autosummary::
    adaptive_histogram_equalization
    average_neighbour_patterns
    fft_filter
    get_decomposition_model
    get_dynamic_background
    get_image_quality
    get_virtual_bse_intensity
    normalize_intensity
    plot_virtual_bse_intensity
    rebin
    remove_dynamic_background
    remove_static_background
    rescale_intensity
    save
    set_detector_calibration
    set_experimental_parameters
    set_phase_parameters
    set_scan_calibration

.. autoclass:: kikuchipy.signals.EBSD
    :members:
    :undoc-members:
    :inherited-members: Signal2D
    :show-inheritance:

....

These methods are exclusive to LazyEBSD objects.

.. currentmodule:: kikuchipy.signals.LazyEBSD

.. autosummary::
    get_decomposition_model_write

.. autoclass:: kikuchipy.signals.LazyEBSD
    :members:
    :undoc-members:
    :show-inheritance:

....

EBSDMasterPattern
-----------------

All methods listed here are also available to
:class:`~kikuchipy.signals.LazyEBSDMasterPattern` objects.

.. currentmodule:: kikuchipy.signals.EBSDMasterPattern

.. autosummary::
    normalize_intensity
    rescale_intensity
    set_simulation_parameters
    set_phase_parameters

.. autoclass:: kikuchipy.signals.EBSDMasterPattern
    :members:
    :undoc-members:
    :inherited-members: Signal2D
    :show-inheritance:

....

There are no methods exclusive to LazyEBSDMasterPattern objects.

.. autoclass:: kikuchipy.signals.LazyEBSDMasterPattern
    :members:
    :undoc-members:
    :show-inheritance:

....

VirtualBSEImage
---------------

.. currentmodule:: kikuchipy.signals.VirtualBSEImage

.. autosummary::
    normalize_intensity
    rescale_intensity

.. autoclass:: kikuchipy.signals.VirtualBSEImage
    :members:
    :undoc-members:
    :inherited-members: Signal2D

....

util
----

.. currentmodule:: kikuchipy.signals.util

.. automodule:: kikuchipy.signals.util
    :members:
    :undoc-members:

....

detectors
=========

.. automodule:: kikuchipy.detectors

.. currentmodule:: kikuchipy.detectors.EBSDDetector

.. autosummary::
    plot

.. autoclass:: kikuchipy.detectors.EBSDDetector
    :members:
    :undoc-members:

    .. automethod:: __init__

....

generators
==========

.. automodule:: kikuchipy.generators

EBSDSimulationGenerator
-----------------------

.. currentmodule:: kikuchipy.generators.EBSDSimulationGenerator

.. autosummary::
    geometrical_simulation

.. autoclass:: kikuchipy.generators.EBSDSimulationGenerator
    :members:
    :undoc-members:

    .. automethod:: __init__

VirtualBSEGenerator
-------------------

.. currentmodule:: kikuchipy.generators.VirtualBSEGenerator

.. autosummary::
    get_images_from_grid
    get_rgb_image
    plot_grid
    roi_from_grid

.. autoclass:: kikuchipy.generators.VirtualBSEGenerator
    :members:
    :undoc-members:

    .. automethod:: __init__

util
----

.. currentmodule:: kikuchipy.generators.util

.. automodule:: kikuchipy.generators.util
    :members:
    :undoc-members:

....

pattern
=======

Module for single and chunk pattern processing, used by signals.

Functions operating on single EBSD patterns as :class:`numpy.ndarray`.

.. currentmodule:: kikuchipy.pattern

.. autosummary::
    fft
    fft_filter
    fft_frequency_vectors
    fft_spectrum
    get_dynamic_background
    get_image_quality
    ifft
    normalize_intensity
    remove_dynamic_background
    rescale_intensity

.. automodule:: kikuchipy.pattern
    :members:
    :undoc-members:

....

chunk
-----

Functions for operating on :class:`numpy.ndarray` or :class:`dask.array.Array`
chunks of EBSD patterns.

.. currentmodule:: kikuchipy.pattern.chunk

.. autosummary::
    adaptive_histogram_equalization
    average_neighbour_patterns
    fft_filter
    get_dynamic_background
    get_image_quality
    normalize_intensity
    remove_dynamic_background
    remove_static_background
    rescale_intensity

.. automodule:: kikuchipy.pattern.chunk
    :members:
    :undoc-members:

....

correlate
---------

.. currentmodule:: kikuchipy.pattern.correlate

.. automodule:: kikuchipy.pattern.correlate
    :members:
    :undoc-members:

....

filters
=======

.. currentmodule:: kikuchipy.filters

.. automodule:: kikuchipy.filters
    :members:
    :undoc-members:

....

io
==

.. automodule:: kikuchipy.io

.. automodule:: kikuchipy.io._io
    :members:
    :undoc-members:

These plugin functions import patterns and parameters from file formats into
:class:`~kikuchipy.signals.EBSD` or
:class:`~kikuchipy.signals.EBSDMasterPattern` (or
:class:`~kikuchipy.signals.LazyEBSD` or
:class:`~kikuchipy.signals.LazyEBSDMasterPattern` if loading lazily) objects.

....

h5ebsd
------

.. automodule:: kikuchipy.io.plugins.h5ebsd
    :members:
    :undoc-members:

....

nordif
------

.. automodule:: kikuchipy.io.plugins.nordif
    :members:
    :undoc-members:

....

emsoft_ebsd
-----------

.. automodule:: kikuchipy.io.plugins.emsoft_ebsd
    :members:
    :undoc-members:

....

emsoft_ebsd_master_pattern
--------------------------

.. automodule:: kikuchipy.io.plugins.emsoft_ebsd_master_pattern
    :members:
    :undoc-members:
