import matplotlib.pyplot as plt


class Legend():
    """Customizable standalone matplotlib legend."""

    def __init__(self):
        self.entries = []
        self.fig = None
        self.ax = None
        self.legend = None

    def add_entry(self, entry):
        """
        Add entry to legend.

        Entries will be displayed in the order they are added.
        """
        self.entries.append(entry.obj)

    def create(self, figsize=None):
        """Create matplotlib legend instance."""
        if figsize is not None:
            self.fig, self.ax = plt.subplots(figsize=figsize)
        else:
            self.fig, self.ax = plt.subplots()

        self.ax.set_axis_off()

        self.legend = self.ax.legend(handles=self.entries, loc='center')

    def show(self):
        """Show matplot figure containing the legend."""
        if self.legend is None:
            print('No legend exists that can be shown. Use `create` method.')
        else:
            plt.tight_layout()
            plt.show()

    def save(self, filepath):
        """Save file of the legend."""
        if self.legend is None:
            print('No legend exists that can be shown. Use `create` method.')
        else:
            plt.tight_layout()
            plt.savefig(filepath)
