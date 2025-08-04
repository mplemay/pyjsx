// javascript/hotwire.js
import { Turbo } from "https://cdn.jsdelivr.net/npm/@hotwired/turbo@latest/dist/turbo.es2017-esm.min.js";
import { Application } from "https://unpkg.com/@hotwired/stimulus/dist/stimulus.js";
import controllers from "./controllers/index.js"; // Import all controllers via index.js

// Turbo configuration (optional)
// Turbo.session.drive = false;

// Stimulus application setup
const application = Application.start();
controllers.forEach((controller) => {
    application.register(controller.name, controller.module);
});

// WebSocket connection for Turbo Streams
import { connectStreamSource } from "https://cdn.jsdelivr.net/npm/@hotwired/turbo@latest/dist/turbo.es2017-esm.min.js";
const ws = new WebSocket("ws://localhost:8000/cable"); // Adjust host/port as needed
connectStreamSource(ws);