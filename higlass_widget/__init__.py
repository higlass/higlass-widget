import importlib.metadata

try:
    __version__ = importlib.metadata.version("higlass-widget")
except importlib.metadata.PackageNotFoundError:
    __version__ = "unknown"

from .widget import HiGlassWidget  # noqa
