// Be careful editing the contents of this file!

/** @param {URL} url */
function loadCss(url) {
	var link = document.createElement("link");
	link.type = "text/css";
	link.rel = "stylesheet";
	link.href = url.href;
	document.getElementsByTagName("head")[0].appendChild(link);
}

define(["@jupyter-widgets/base", "module"], function (base, module) {
	let baseUrl;

	try {
		// from CDN
		baseUrl = new URL(module.uri);
	} catch {
		// relative to localhost
		baseUrl = new URL(module.uri, document.baseURI);
	}

	let js = new URL("widget.js", baseUrl);
	let css = new URL("widget.css", baseUrl);

	loadCss(css);
	return import(js.href).then(mod => mod.default(base));
})
