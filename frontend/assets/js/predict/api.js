export async function fetchMetrics() {
  try {
    const res = await fetch("http://127.0.0.1:8000/imdb_rating_analysis/metrics");
    return await res.json();
  } catch (err) {
    console.error("Erro ao carregar métricas:", err);
    return null;
  }
}

export async function predictMovie(payload) {
  try {
    const res = await fetch("http://127.0.0.1:8000/imdb_rating_analysis/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
    });
    return await res.json();
  } catch (err) {
    console.error("Erro ao prever:", err);
    return null;
  }
}
