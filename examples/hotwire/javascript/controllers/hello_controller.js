// javascript/controllers/hello_controller.js
import { Controller } from "@hotwired/stimulus";

export default class extends Controller {
  static targets = ["output"];
  static values = { name: String };

  greet() {
    this.outputTarget.textContent = `Hello, ${this.nameValue}!`;
  }
}