# higlass-widget

```
pip install higlass-widget
```

### Development

```bash
pip install -e .
```

If you are using the classic Jupyter Notebook you need to install the nbextension:

```bash
jupyter nbextension install --py --symlink --sys-prefix higlass_widget
jupyter nbextension enable --py --sys-prefix higlass_widget
```

Note for developers:

- the `-e` pip option allows one to modify the Python code in-place. Restart the kernel in order to see the changes.
- the `--symlink` argument on Linux or OS X allows one to modify the JavaScript code in-place. This feature is not available with Windows.

For developing with JupyterLab:

```
jupyter labextension develop --overwrite higlass_widget
```
