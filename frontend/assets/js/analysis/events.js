// events.js
import { predictGenreAPI } from "./api.js";
import { renderPredictionGenre, renderErrorGenre } from "./ui.js";

export function setupEvents() {
  const h4 = document.querySelector("#overview-predict-section h4");
  const content = document.getElementById("overview-predict-content");

  h4.addEventListener("click", () => {
    content.style.display = content.style.display === "none" ? "block" : "none";
  });
  content.style.display = "none";

  const btn = document.getElementById("predict-btn");
  btn.addEventListener("click", async () => {
    const overviewText = document.getElementById("overview-input").value.trim();
    if (!overviewText) {
      document.getElementById("predict-genre").innerHTML =
        `<p style="color:red;">Por favor, digite uma descrição.</p>`;
      return;
    }
    try {
      const predict = await predictGenreAPI(overviewText);
      renderPredictionGenre(predict);
    } catch {
      renderErrorGenre();
    }
  });

  const backToTopBtn = document.getElementById("back-to-top");
  window.onscroll = function() {
    if (document.body.scrollTop > 300 || document.documentElement.scrollTop > 300) {
      backToTopBtn.style.display = "block";
    } else {
      backToTopBtn.style.display = "none";
    }
  };
  backToTopBtn.addEventListener("click", () => {
    window.scrollTo({ top: 0, behavior: "smooth" });
  });
}
