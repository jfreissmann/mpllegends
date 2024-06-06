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
python setup.py sdist bdist_wheel
```

```
python -m pip install .
```

If you want to use an editable version of the package, e.g. if you want to contribute to the project and test your own changes, skip the commands above and use this one:

```
python -m pip install -e "path/to/the/mpllengends/dir/"
```

## License

See the `LICENSE` file for further information.
