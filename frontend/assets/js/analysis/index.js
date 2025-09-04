import { 
  fetchSummary, 
  fetchCorrelations, 
  fetchWordcloud, 
  fetchGrossAnalysis, 
  fetchHypothesis, 
  fetchRecommendation 
} from "./api.js";

import { 
  renderSummary, 
  renderHypotheses, 
  renderPlots, 
  renderGrossAnalysis,
  renderRecommendation,
  renderWordcloud, 
  renderTop10 
} from "./ui.js";

import { setupEvents } from "./events.js";

// Carrega resumo + correlações
async function loadSummaryAndCorrelations() {
  const summary = await fetchSummary();
  const corr = await fetchCorrelations();
  renderSummary(summary, corr);
}

// Carrega recomendações e top 10
async function loadRecommendations() {
  const rec = await fetchRecommendation("http://127.0.0.1:8000/recommendations/");
  renderRecommendation(rec);

  const top10 = await fetchRecommendation("http://127.0.0.1:8000/recommendations/top10");
  renderTop10(top10);
}

// Carrega todas as hipóteses
async function loadHypotheses() {
  try {
    const genreData = await fetchHypothesis("http://127.0.0.1:8000/hypotheses/genre_vs_gross");
    const runtimeData = await fetchHypothesis("http://127.0.0.1:8000/hypotheses/runtime_vs_rating");
    const votesData = await fetchHypothesis("http://127.0.0.1:8000/hypotheses/votes_vs_gross");
    const ageData = await fetchHypothesis("http://127.0.0.1:8000/hypotheses/year_vs_success");

    renderHypotheses(genreData, runtimeData, votesData, ageData);
  } catch (err) {
    console.error("Erro ao carregar hipóteses:", err);
  }
}

// Inicialização
document.addEventListener("DOMContentLoaded", async () => {
  setupEvents();

  await loadSummaryAndCorrelations();
  await renderPlots();
  await loadHypotheses();
  await loadRecommendations();

  const gross = await fetchGrossAnalysis();
  renderGrossAnalysis(gross);

  const wc = await fetchWordcloud();
  const fileName = wc.path.split(/[\\/]/).pop();
  renderWordcloud(fileName);
});
