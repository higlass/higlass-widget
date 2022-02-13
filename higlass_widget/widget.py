import json
import pathlib

import ipywidgets
import traitlets.traitlets as t

import hg.utils as utils

here = pathlib.Path(__file__).parent

with open(here / "labextension" / "package.json") as f:
    pkg = json.load(f)

version = pkg["version"]

def save_b64_image_to_png(filename, b64str):
    """Save a base64 encoded image to a file."""
    import base64

    imgdata = base64.b64decode(b64str.split(",")[1])
    with open(filename, "wb") as f:
        f.write(imgdata)


@ipywidgets.register
class HiGlassWidget(ipywidgets.DOMWidget):
    _model_name = t.Unicode("HiGlassModel").tag(sync=True)
    _model_module = t.Unicode("higlass-widget").tag(sync=True)
    _model_module_version = t.Unicode(version).tag(sync=True)

    _view_name = t.Unicode("HiGlassView").tag(sync=True)
    _view_module = t.Unicode("higlass-widget").tag(sync=True)
    _view_module_version = t.Unicode(version).tag(sync=True)

    _model_data = t.List([]).tag(sync=True)

    viewconf = t.Dict({}).tag(sync=True)
    height = t.Int().tag(sync=True)

    dom_element_id = t.Unicode(read_only=True).tag(sync=True)

    # Read-only properties that get updated by HiGlass exclusively
    location = t.List(t.Union([t.Float(), t.List()]), read_only=True).tag(sync=True)
    cursor_location = t.List([], read_only=True).tag(sync=True)
    selection = t.List([], read_only=True).tag(sync=True)

    # Short-hand options
    auth_token = t.Unicode().tag(sync=True)
    bounded = t.Bool(None, allow_none=True).tag(sync=True)
    default_track_options = t.Dict({}).tag(sync=True)
    dark_mode = t.Bool(False).tag(sync=True)
    renderer = t.Unicode().tag(sync=True)
    select_mode = t.Bool(False).tag(sync=True)
    selection_on_alt = t.Bool(False).tag(sync=True)

    # For any kind of options. Note that whatever is defined in options will
    # be overwritten by the short-hand options
    options = t.Dict({}).tag(sync=True)

    def __init__(self, viewconf, **kwargs):
        self.on_msg(self._handle_js_events)
        self.callbacks = {}
        super().__init__(viewconf=viewconf, **kwargs)

    def get_base64_img(self, callback):
        uuid = utils.uid()

        self.callbacks[uuid] = callback

        self.send(
            json.dumps(
                {
                    "request": "save_as_png",
                    "params": {"uuid": uuid},
                }
            )
        )

    def _handle_js_events(self, widget, content, buffers=None):
        try:
            if self.callbacks[content["params"]["uuid"]]:
                self.callbacks[content["params"]["uuid"]](content["imgData"])
                del self.callbacks[content["params"]["uuid"]]
        except Exception as e:
            self.log.error(e)
            self.log.exception("Unhandled exception while handling msg")
