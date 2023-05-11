from __future__ import annotations
import json
import pathlib

import anywidget
import traitlets as t


class HiGlassWidget(anywidget.AnyWidget):
    _esm = pathlib.Path(__file__).parent / "widget.js"
    _css = "https://esm.sh/higlass@1.12/dist/hglib.css"
    _viewconf = t.Unicode("null").tag(sync=True)

    # readonly properties
    location = t.List(t.Union([t.Float(), t.Tuple()]), read_only=True).tag(sync=True)

    def __init__(self, viewconf: dict, **kwargs):
        super().__init__(_viewconf=json.dumps(viewconf), **kwargs)

    def reload(self, *items):
        msg = json.dumps(["reload", items])
        self.send(msg)

    def zoom_to(
        self,
        view_id: str,
        start1: int,
        end1: int,
        start2: int | None = None,
        end2: int | None = None,
        animate_time: int = 500,
    ):
        msg = json.dumps(["zoomTo", view_id, start1, end1, start2, end2, animate_time])
        self.send(msg)
