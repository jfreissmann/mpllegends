from matplotlib.lines import Line2D
from matplotlib.patches import Patch


class Entry():
    """Base class of legend entries."""

    def check_necessary_args(self, **kwargs):
        for name, value in kwargs.items():
            if value is None:
                raise ValueError(
                    f'The argument `{name}` is necessary and has to be set.'
                    )


class Line(Entry):
    """Legend entry of a line with or without marker."""

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
    """Legend entry of a marker."""

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
    """Legend entry of a rectangle."""

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

        self.check_necessary_args(
            label=self.label, facecolor=self.facecolor
        )

        self.obj = Patch(
            label=self.label, facecolor=self.facecolor,
            **kwargs
        )
