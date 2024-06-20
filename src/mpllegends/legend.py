import matplotlib as mpl
import matplotlib.pyplot as plt


class Legend():
    """Customizable standalone matplotlib legend."""

    def __init__(self, ncol=1, border=True, roundborder=True, shadow=False,
                 fontfamily='sans-serif', fontstyle='normal',
                 fontweight='normal', fontsize='medium', borderpad=0.4,
                 labelspacing=0.5, columnspacing=2.0):
        """
        Initialize `Legend` instance.

        Most parameters are so called `run time configuration parameters` of
        matplotlib. See https://matplotlib.org/stable/users/explain/customizing.html#the-default-matplotlibrc-file
        for a describtion of them.

        Parameters
        ----------

        ncol : int
            Number of columns of the legend. Entries are filled top to bottom
            and left to right.

        border : bool
            Corresponds to `legend.frameon` rcParam

        roundborder : bool
            Corresponds to `legend.fancybox` rcParam

        shadow : bool
            Corresponds to `legend.shadow` rcParam

        fontfamily : str
            Corresponds to `font.family` rcParam

        fontstyle : str
            Corresponds to `font.style` rcParam

        fontweight : str or int
            Corresponds to `font.weight` rcParam

        fontsize: str or int
            Corresponds to `legend.fontsize` rcParam

        borderpad: float
            Corresponds to `legend.borderpad` rcParam

        labelspacing: float
            Corresponds to `legend.labelspacing` rcParam

        columnspacing: float
            Corresponds to `legend.columnspacing` rcParam
        """
        self.entries = []
        self.fig = None
        self.ax = None
        self.legend = None
        self.ncol = ncol
        self.rcParams = {
            'font.family': fontfamily,
            'font.style': fontstyle,
            'font.weight': fontweight,
            'legend.frameon' : border,
            'legend.fancybox' : roundborder,
            'legend.shadow' : shadow,
            'legend.fontsize' : fontsize,
            'legend.borderpad' : borderpad,
            'legend.labelspacing' : labelspacing,
            'legend.columnspacing' : columnspacing,
        }

    def add_entry(self, entry):
        """
        Add entry to legend.

        Entries will be displayed in the order they are added.

        Parameters
        ----------

        entry : any mpllengends.entries.Entry subclass
            The entry to be added to the `Legend`.
        """
        self.entries.append(entry.obj)

    def create(self, figsize=None):
        """
        Create matplotlib legend instance.
        
        Parameters
        ----------

        figsize : sequence of int or sequence of float
            Size of figure in inches. First is width and second is height.
        """
        with mpl.rc_context(self.rcParams):
            if figsize is not None:
                self.fig, self.ax = plt.subplots(figsize=figsize)
            else:
                self.fig, self.ax = plt.subplots()

            self.ax.set_axis_off()

            self.legend = self.ax.legend(
                handles=self.entries, loc='center', ncol=self.ncol
            )

        if figsize is None:
            tight_width_inches = (
                self.legend.get_window_extent().width
                / mpl.rcParams['figure.dpi']
                + mpl.rcParams['legend.borderpad']
            )
            tight_height_inches = (
                self.legend.get_window_extent().height
                / mpl.rcParams['figure.dpi']
                + mpl.rcParams['legend.borderpad']
            )
            self.fig.set_size_inches(tight_width_inches, tight_height_inches)

    def show(self):
        """Show matplot figure containing the legend."""
        if self.legend is None:
            print('No legend exists that can be shown. Use `create` method.')
        else:
            plt.tight_layout()
            plt.show()

    def save(self, filepath, **kwargs):
        """
        Save file of the legend.

        Parameters
        ----------

        filepath : str
            Absolute or relative path to the file that should be created. See
            matplotlib documentation for supported file types.

        **kwargs
            Keyword arguments the matplotlib.pyplot.savefig takes in.
        """
        if self.legend is None:
            print('No legend exists that can be shown. Use `create` method.')
        else:
            plt.tight_layout()
            plt.savefig(filepath, **kwargs)
