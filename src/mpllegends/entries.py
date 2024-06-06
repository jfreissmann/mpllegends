from matplotlib.lines import Line2D
from matplotlib.patches import Patch


class Entry():
    """Base class of legend entries."""

    def check_necessary_args(self, **kwargs):
        """Check **kwargs for None values raise ValueError if any is found."""
        for name, value in kwargs.items():
            if value is None:
                raise ValueError(
                    f'The argument `{name}` is necessary and has to be set.'
                    )


class Line(Entry):
    """
    Legend entry of a line with or without marker.

    Parameters
    ----------

    label : str
        Label to be placed beside the line.

    color : str
        Color of the line. Any color that is available in matplotlib.

    **kwargs : dict of keyword arguments
        Any keyword arguments that `matplotlib.lines.Line2D` class takes, except
        `label` and `color`. Set `marker` to add a marker to the line.
    """

    def __init__(self, label=None, color=None, **kwargs):
        self.label = label
        self.color = color

        self.check_necessary_args(label=self.label, color=self.color)

        self.obj = Line2D(
            [0], [0],
            label=self.label, color=self.color,
            **kwargs
        )


class Marker(Entry):
    """
    Legend entry of a marker.

    Parameters
    ----------

    label : str
        Label to be placed beside the marker.

    marker : str
        Marker type as defined by matplotlib, e.g. 'o', 'x' or 's'.

    facecolor : str
        Color of the face of the marker. Any color that is available in
        matplotlib. If only `facecolor` is set, `edgecolor` takes the same
        value.

    edgecolor : str
        Color of the edge of the marker. Any color that is available in
        matplotlib. If only `edgecolor` is set, `facecolor` takes the same
        value.

    **kwargs : dict of keyword arguments
        Any keyword arguments that `matplotlib.lines.Line2D` class takes, except
        `label`, `marker`, `facecolor` and `edgecolor`. If `color` is set and
        `facecolor` and `edgecolor` are not, that color is used for both of
        them. `color` can not be set, if any of `facecolor` and `edgecolor` are
        set.
    """

    def __init__(self, label=None, marker=None, facecolor=None, edgecolor=None,
                 **kwargs):
        self.label = label
        self.marker = marker

        if facecolor is not None and edgecolor is None:
            self.facecolor = facecolor
            self.edgecolor = facecolor
        elif edgecolor is not None and facecolor is None:
            self.edgecolor = edgecolor
            self.facecolor = edgecolor
        elif 'color' in kwargs and facecolor is None and edgecolor is None:
            self.facecolor = kwargs['color']
            self.edgecolor = kwargs['color']
            del kwargs['color']
        else:
            self.facecolor = facecolor
            self.edgecolor = edgecolor

        self.check_necessary_args(
            label=self.label, marker=self.marker, facecolor=self.facecolor,
            edgecolor=self.edgecolor
        )

        self.obj = Line2D(
            [0], [0],
            label=self.label, marker=self.marker,
            markerfacecolor=self.facecolor, markeredgecolor=self.edgecolor,
            color='w',
            **kwargs
        )


class Rectangle(Entry):
    """
    Legend entry of a rectangle.

    Parameters
    ----------

    label : str
        Label to be placed beside the rectangle.

    facecolor : str
        Color of the face of the rectangle. Any color that is available in
        matplotlib. If only `facecolor` is set, `edgecolor` takes the same
        value.

    edgecolor : str
        Color of the edge of the rectangle. Any color that is available in
        matplotlib. If only `edgecolor` is set, `facecolor` takes the same
        value.

    **kwargs : dict of keyword arguments
        Any keyword arguments that `matplotlib.lines.Line2D` class takes, except
        `label`, `facecolor` and `edgecolor`. If `color` is set and `facecolor`
        and `edgecolor` are not, that color is used for both of them. `color`
        can not be set, if any of `facecolor` and `edgecolor` are set.
    """

    def __init__(self, label=None, facecolor=None, edgecolor=None, **kwargs):
        self.label = label

        if facecolor is not None and edgecolor is None:
            self.facecolor = facecolor
            self.edgecolor = facecolor
        elif edgecolor is not None and facecolor is None:
            self.edgecolor = edgecolor
            self.facecolor = edgecolor
        elif 'color' in kwargs and facecolor is None and edgecolor is None:
            self.facecolor = kwargs['color']
            self.edgecolor = kwargs['color']
            del kwargs['color']
        else:
            self.facecolor = facecolor
            self.edgecolor = edgecolor

        self.check_necessary_args(
            label=self.label, facecolor=self.facecolor
        )

        self.obj = Patch(
            label=self.label, facecolor=self.facecolor,
            **kwargs
        )
