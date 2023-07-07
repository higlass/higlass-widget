import hglib from "https://esm.sh/higlass@1.12?deps=react@17,react-dom@17,pixi.js@6"

/**
 * @param {{
 *   xDomain: [number, number],
 *   yDomain: [number, number],
 * }} location
 */
function toPts({ xDomain, yDomain }) {
	let [x, xe] = xDomain;
	let [y, ye] = yDomain;
	return [x, xe, y, ye];
}

export async function render({ model, el }) {
	let viewconf = JSON.parse(model.get("_viewconf"));
	let api = await hglib.viewer(el, viewconf);

	model.on("msg:custom", (msg) => {
		msg = JSON.parse(msg);
		let [fn, ...args] = msg;
		api[fn](...args);
	});

	if (viewconf.views.length === 1) {
		api.on("location", (loc) => {
			model.set("location", toPts(loc));
			model.save_changes();
		}, viewconf.views[0].uid);
	} else {
		viewconf.views.forEach((_view, idx) => {
			api.on("location", (loc) => {
				let copy = model.get("location").slice();
				copy[idx] = toPts(loc);
				model.set("location", copy);
				model.save_changes();
			}, uid);
		});
	}
}
