# higlass-widget

[![PyPI](https://img.shields.io/pypi/v/higlass-widget.svg?color=green)](https://pypi.org/project/higlass-widget)
[![License](https://img.shields.io/pypi/l/gosling.svg?color=green)](https://github.com/higlass/higlass-widget/raw/main/LICENSE)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/higlass/higlass-widget/blob/main/notebooks/Widget.ipynb)

```
pip install higlass-widget
```

### Development

This project uses [`hatch`](https://github.com/pypa/hatch), which installs and sync
all dependencies from `pyproject.toml` automatically.

```sh
hatch shell
```

Alternatively, you can create and manage your own virtual environments and install
an editable version of `higlass-widget`:

```sh
pip install -e ".[dev]"
```

Finally, you can now run the notebooks with:

```sh
jupyterlab
```

`higlass_widget.HiGlassWidget` is built with [`anywidget`](https://github.com/manzt/anywidget).
You can edit the contents of `higlass_widget/widget.js` and changes will be reflected automatically
in your active Jupyter notebook.

### Release

```
npm version [major|minor|patch]
git tag -a vX.X.X -m "vX.X.X"
git push --follow-tags
```
