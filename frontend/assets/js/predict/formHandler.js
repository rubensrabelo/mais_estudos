import { buildPayload } from "./utils/helpers.js";
import { predictMovie } from "./api.js";
import { renderPrediction } from "./ui.js";

export function setupForm() {
  const form = document.getElementById("predict-form");
  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    const payload = buildPayload(new FormData(e.target));
    const prediction = await predictMovie(payload);
    renderPrediction(payload, prediction);
  });

  const toggleBtn = document.getElementById("predict-toggle");
  toggleBtn.addEventListener("click", () => {
    import("./ui.js").then(ui => ui.togglePredictContainer());
  });
}
