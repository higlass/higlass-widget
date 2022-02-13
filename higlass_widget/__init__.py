import sys

from .widget import HiGlassWidget

try:
    if "google.colab" in sys.modules:
        from google.colab import output

        output.enable_custom_widget_manager()
except ImportError:
    pass


def _jupyter_labextension_paths():
    return [{"src": "labextension", "dest": "higlass-widget"}]


def _jupyter_nbextension_paths():
    return [
        {
            "section": "notebook",
            "src": "nbextension",
            "dest": "higlass-widget",
            "require": "higlass-widget/extension",
        }
    ]
