# -*- coding: utf-8 -*-
# Copyright 2019-2020 The kikuchipy developers
#
# This file is part of kikuchipy.
#
# kikuchipy is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# kikuchipy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with kikuchipy. If not, see <http://www.gnu.org/licenses/>.

from typing import Union

from hyperspy.utils.markers import line_segment, point, text
import numpy as np


def get_line_segment_list(lines: Union[list, np.ndarray], **kwargs) -> list:
    """Return a list of line segment markers.

    Parameters
    ----------
    lines :
        On the form [[x00, y00, x01, y01], [x10, y10, x11, y11], ...].
    kwargs :
        Keyword arguments allowed by :class:`matplotlib.pyplot.axvline`.

    Returns
    -------
    marker_list :
        List of :class:`hyperspy.utils.markers.line_segment`.
    """
    lines = np.asarray(lines)
    if lines.ndim == 1:
        lines = lines[np.newaxis, ...]

    marker_list = []
    for i in range(lines.shape[-2]):  # Iterate over bands
        # TODO: Exclude np.nan bands (not visible in that pattern)
        x1 = lines[..., i, 0]
        y1 = lines[..., i, 1]
        x2 = lines[..., i, 2]
        y2 = lines[..., i, 3]
        marker_list.append(line_segment(x1=x1, y1=y1, x2=x2, y2=y2, **kwargs))

    return marker_list


def get_point_list(points: Union[list, np.ndarray], **kwargs) -> list:
    """Return a list of point markers.

    Parameters
    ----------
    points :
        On the form [[x0, y0], [x1, y1], ...].
    kwargs :
        Keyword arguments allowed by :class:`matplotlib.pyplot.axvline`.

    Returns
    -------
    marker_list :
        List of :class:`hyperspy.utils.markers.point`.
    """
    points = np.atleast_2d(points)
    return [point(x=x, y=y, **kwargs) for x, y in points]


def get_text_list(texts: list, coordinates: np.ndarray, **kwargs) -> list:
    """Return a list of text markers.

    Parameters
    ----------
    texts :
        A list of texts.
    coordinates :
        On the form [[x0, y0], [x1, y1], ...].
    kwargs :
        Keyword arguments allowed by :class:`matplotlib.pyplot.axvline.`

    Returns
    -------
    marker_list :
        List of :class:`hyperspy.utils.markers.text`.
    """
    coordinates = np.atleast_2d(coordinates)
    return [
        text(x=x, y=y, text=t, **kwargs)
        for t, (x, y) in zip(texts, coordinates)
    ]


def permanent_on_signal(signal, marker_list: list):
    """Add a list of markers to a signal.

    Parameters
    ----------
    signal : EBSD or EBSDMasterPattern
        Signal to add markers to.
    marker_list :
        List of HyperSpy markers.
    """
    if not hasattr(signal.metadata, "Markers"):
        signal.metadata.add_node("Markers")
    n_extra = len(signal.metadata.Markers)
    for i, marker in enumerate(marker_list):
        signal.metadata.Markers[f"marker{i + n_extra}"] = marker
