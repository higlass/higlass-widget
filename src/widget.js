import * as hglib from "higlass";
import { name, version } from "../package.json"

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

/** @param {typeof import("@jupyter-widgets/base")} base */
export default function(base) {

	class HiGlassModel extends base.DOMWidgetModel {
		defaults() {
			return {
				...super.defaults(),

				_model_name: HiGlassModel.model_name,
				_model_module: HiGlassModel.model_module,
				_model_module_version: HiGlassModel.model_module_version,

				_view_name: HiGlassView.view_name,
				_view_module: HiGlassView.view_module,
				_view_module_version: HiGlassView.view_module_version,
			};
		}

		static model_name = 'HiGlassModel';
		static model_module = name;
		static model_module_version = version;

		static view_name = 'HiGlassView';
		static view_module = name;
		static view_module_version = version;
	}

	class HiGlassView extends base.DOMWidgetView {

		async render() {
			let viewconf = JSON.parse(this.model.get("_viewconf"));
			let api = await hglib.viewer(this.el, viewconf);

			this.model.on('msg:custom', msg => {
				msg = JSON.parse(msg);
				let [fn, ...args] = msg;
				api[fn](...args);
			});

			if (viewconf.views.length === 1) {

				api.on('location', loc => {
					this.model.set('location', toPts(loc))
					this.model.save_changes();
				}, viewconf.views[0].uid);

			} else {

				viewconf.views.forEach((view, idx) => {
					api.on('location', loc => {
						let copy = this.model.get('location').slice();
						copy[idx] = toPts(loc);
						this.model.set('location', copy);
						this.model.save_changes();
					}, view.uid);
				});

			}

		}

	}

	return { HiGlassModel, HiGlassView };
}
