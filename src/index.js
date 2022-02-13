import create from "./widget.js";
import css from "higlass/dist/hglib.css";

const style = document.createElement('style');
style.textContent = css;
document.head.appendChild(style);

define(["@jupyter-widgets/base"], create);
