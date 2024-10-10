# mpllegends
Customizable standalone matplotlib legends.

## Installation

For now, only direct download from the [GitHub Repository](https://github.com/jfreissmann/heatpumps) is supported, so just clone it locally or download a ZIP file of the code. If you are using [Miniforge](https://github.com/conda-forge/miniforge), you can create and activate a clean environment like this:

```
conda create -n my_new_env python=3.11
```

```
conda activate my_new_env
```

If you want to build the package locally and install it, you should use these commands from the root directory of the repository:

```
python install flit
```

```
flit buil
```

```
python -m pip install .
```

If you want to use an editable version of the package, e.g. if you want to contribute to the project and test your own changes, skip the commands above and use this one:

```
python -m pip install -e "path/to/the/mpllengends/dir/"
```

## Usage

```python
from mpllegends.entries import Line, Marker, Rectangle
from mpllegends.legend import Legend

legend = Legend(
    ncol=3, borderpad=0.5, fontweight='bold', fontsize='large',
    columnspacing=1.5
)

legend.add_entry(Line(label='Test Line', color='r'))
legend.add_entry(
    Marker(
        label='Test Marker', marker='o', markersize=12,
        facecolor='b', edgecolor='g'
    )
)
legend.add_entry(Rectangle(label='Test Rect', color='#111111'))

legend.create()

legend.save('example_legend.pdf')
legend.save('example_legend.png', dpi=300)

legend.show()
```

![Example of a legend created by the code above.](example_legend.png)

## License

See the `LICENSE` file for further information.
