async function loadMetrics() {
  try {
    const res = await fetch("http://127.0.0.1:8000/imdb_rating_analysis/metrics");
    const metrics = await res.json();

    document.getElementById("metrics").innerHTML = `
      <ul>
        <li><strong>RMSE:</strong> ${metrics.RMSE.toFixed(3)} (quanto menor, melhor – erro médio em torno de 0.1 ponto na nota)</li>
        <li><strong>MAE:</strong> ${metrics.MAE.toFixed(3)} (erro absoluto médio em torno de 0.08 pontos)</li>
        <li><strong>R²:</strong> ${metrics.R2.toFixed(3)} (explica ~87% da variação das notas)</li>
      </ul>
    `;
  } catch (err) {
    console.error("Erro ao carregar métricas:", err);
    document.getElementById("metrics").innerText = "Erro ao carregar métricas.";
  }
}


document.getElementById("predict-form").addEventListener("submit", async (e) => {
  e.preventDefault();

  const formData = new FormData(e.target);
  const movie = Object.fromEntries(formData.entries());

  // Garantir os campos obrigatórios
  const payload = {
    Series_Title: movie.Series_Title,
    Released_Year: movie.Released_Year,
    Certificate: movie.Certificate || "A",
    Runtime: movie.Runtime,
    Genre: movie.Genre,
    Overview: movie.Overview || "Descrição não informada.",
    Meta_score: parseFloat(movie.Meta_score) || 0,
    Director: movie.Director || "Desconhecido",
    Star1: movie.Star1 || "Ator 1",
    Star2: movie.Star2 || "Ator 2",
    Star3: movie.Star3 || "Ator 3",
    Star4: movie.Star4 || "Ator 4",
    No_of_Votes: parseInt(movie.No_of_Votes) || 0,
    Gross: movie.Gross || "0"
  };

  try {
    const res = await fetch("http://127.0.0.1:8000/imdb_rating_analysis/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
    });

    const data = await res.json();

    document.getElementById("result").innerHTML = `
      <h4>⭐ Previsão:</h4>
      <p><strong>${payload.Series_Title}</strong> (${payload.Released_Year})<br>
      Nota prevista: <span style="color:green;font-weight:bold;">${data.IMDB_Prediction.toFixed(2)}</span></p>
    `;
  } catch (err) {
    console.error("Erro ao prever:", err);
    document.getElementById("result").innerText = "Erro ao prever nota.";
  }
});

document.getElementById("predict-toggle").addEventListener("click", () => {
  const container = document.getElementById("predict-container");
  container.style.display = container.style.display === "none" ? "block" : "none";
});

// Inicializar
loadMetrics();
document.addEventListener("DOMContentLoaded", () => {
  loadMetrics();
});
