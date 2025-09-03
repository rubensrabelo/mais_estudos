import { fetchMetrics } from "./api.js";
import { renderMetrics } from "./ui.js";
import { setupForm } from "./formHandler.js";

// Inicialização
document.addEventListener("DOMContentLoaded", async () => {
  setupForm();
  const metrics = await fetchMetrics();
  renderMetrics(metrics);
});
