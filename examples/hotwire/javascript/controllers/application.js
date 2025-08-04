// javascript/controllers/application.js
import { Application } from "@hotwired/stimulus";
import controllers from "./index.js"; // Import all controllers via index.js

const application = Application.start();
controllers.forEach((controller) => {
    application.register(controller.name, controller.module);
});