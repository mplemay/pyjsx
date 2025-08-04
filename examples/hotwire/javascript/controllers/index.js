// javascript/controllers/index.js
import HelloController from "./hello_controller";
import DropdownController from "./dropdown_controller";

export default [
    { name: "hello", module: HelloController },
    { name: "dropdown", module: DropdownController },
    // Add other controllers here
];