import json
from typing import Any, Dict

import ipywidgets
import traitlets.traitlets as t

from ._version import __version__


class HiGlassWidget(ipywidgets.DOMWidget):
    _model_name = t.Unicode("HiGlassModel").tag(sync=True)
    _model_module = t.Unicode("higlass-widget").tag(sync=True)
    _model_module_version = t.Unicode(__version__).tag(sync=True)

    _view_name = t.Unicode("HiGlassView").tag(sync=True)
    _view_module = t.Unicode("higlass-widget").tag(sync=True)
    _view_module_version = t.Unicode(__version__).tag(sync=True)

    _viewconf = t.Unicode("null").tag(sync=True)

    # readonly properties
    location = t.List(t.Union([t.Float(), t.Tuple()]), read_only=True).tag(sync=True)

    def __init__(self, viewconf: Dict[str, Any], **kwargs):
        super().__init__(_viewconf=json.dumps(viewconf), **kwargs)

    def reload(self, *items):
        msg = json.dumps(["reload", items])
        self.send(msg)

    def zoom_to(
        self,
        view_id: str,
        start1: int,
        end1: int,
        start2: int = None,
        end2: int = None,
        animate_time: int = 500,
    ):
        msg = json.dumps(["zoomTo", view_id, start1, end1, start2, end2, animate_time])
        self.send(msg)
