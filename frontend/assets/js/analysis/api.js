export const plotRoutes = {
  genres: "http://localhost:8000/plots/genres/save",
  corr: "http://localhost:8000/plots/correlations/save",
  imdbVsGross: "http://localhost:8000/plots/imbd_vs_gross/save",
  histogram: "http://localhost:8000/plots/histogram/IMDB_Rating/save"
};

export async function fetchSummary() {
  const res = await fetch("http://127.0.0.1:8000/infos/summary");
  return await res.json();
}

export async function fetchCorrelations() {
  const res = await fetch("http://127.0.0.1:8000/infos/correlations");
  return await res.json();
}

export async function fetchPlot(route) {
  const res = await fetch(route);
  return await res.json();
}

export async function fetchHypothesis(url) {
  const res = await fetch(url);
  return await res.json();
}

export async function fetchRecommendation(url) {
  const res = await fetch(url);
  return await res.json();
}

export async function fetchGrossAnalysis() {
  const res = await fetch("http://127.0.0.1:8000/gross_analysis/all");
  return await res.json();
}

export async function fetchWordcloud() {
  const res = await fetch("http://127.0.0.1:8000/overview_analysis/wordcloud/save");
  return await res.json();
}

export async function predictGenreAPI(overviewText) {
  const res = await fetch("http://127.0.0.1:8000/overview_analysis/predict-genre", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ overview: overviewText })
  });
  return await res.json();
}
