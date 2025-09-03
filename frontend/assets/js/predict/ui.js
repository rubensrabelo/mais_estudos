export function renderMetrics(metrics) {
  const metricsEl = document.getElementById("metrics");
  if (!metrics) {
    metricsEl.innerText = "Erro ao carregar métricas.";
    return;
  }

  metricsEl.innerHTML = `
    <ul>
      <li><strong>RMSE:</strong> ${metrics.RMSE.toFixed(3)}</li>
      <li><strong>MAE:</strong> ${metrics.MAE.toFixed(3)}</li>
      <li><strong>R²:</strong> ${metrics.R2.toFixed(3)}</li>
    </ul>
  `;
}

export function renderPrediction(payload, prediction) {
  const resultEl = document.getElementById("result");
  if (!prediction) {
    resultEl.innerText = "Erro ao prever nota.";
    return;
  }

  resultEl.innerHTML = `
    <h4>⭐ Previsão:</h4>
    <p><strong>${payload.Series_Title}</strong> (${payload.Released_Year})<br>
    Nota prevista: <span style="color:green;font-weight:bold;">${prediction.IMDB_Prediction.toFixed(2)}</span></p>
  `;
}

export function togglePredictContainer() {
  const container = document.getElementById("predict-container");
  container.style.display = container.style.display === "none" ? "block" : "none";
}
