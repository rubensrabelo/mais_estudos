// Links referentes a rotas do backend para os gráficos
const plotRoutes = {
  genres: "http://localhost:8000/plots/genres/save",
  corr: "http://localhost:8000/plots/correlations/save",
  imdbVsGross: "http://localhost:8000/plots/imbd_vs_gross/save",
  histogram: "http://localhost:8000/plots/histogram/IMDB_Rating/save"
};

// Carrega resumo da base + análise de correlação
async function loadSummary() {
  try {
    const response = await fetch("http://127.0.0.1:8000/infos/summary");
    const summary = await response.json();

    const correlationResponse = await fetch("http://127.0.0.1:8000/infos/correlations");
    const corr = await correlationResponse.json();

    const intro = document.getElementById("eda-intro");

    // Interpretação de correlações mais relevantes
    const grossVotesCorr = corr.Gross.No_of_Votes.toFixed(2);
    const grossAgeCorr = corr.Gross.Age.toFixed(2);
    const imdbVotesCorr = corr.IMDB_Rating.No_of_Votes.toFixed(2);

    intro.innerHTML = `
      <h2>Resumo Geral da Base de Filmes</h2>
      <p>Total de filmes: <strong>${summary.count}</strong></p>
      <p>Média de receita (Gross): <strong>$${summary.gross_mean.toLocaleString()}</strong></p>
      <p>Média de avaliação IMDB: <strong>${summary.rating_mean.toFixed(2)}</strong></p>
      <p>Média de Meta Score: <strong>${summary.meta_mean.toFixed(2)}</strong></p>
      <p>Diretor mais frequente: <strong>${summary.top_director}</strong></p>
    `;

    // Seleciona o parágrafo da seção do heatmap
const heatmapIntro = document.querySelector("#heatmap p");

// Preenche com o resumo da API
heatmapIntro.innerHTML += `
    <p>Observando as correlações entre variáveis apresentada no gráfico:</p>
    <ul>
      <li>A receita (Gross) apresenta correlação moderada e positiva com o número de votos (<strong>${grossVotesCorr}</strong>), indicando que filmes mais votados tendem a arrecadar mais.</li>
      <li>A idade do filme (Age) tem correlação negativa com a receita (<strong>${grossAgeCorr}</strong>), sugerindo que filmes mais antigos arrecadam menos atualmente.</li>
      <li>A nota do IMDB tem correlação positiva com o número de votos (<strong>${imdbVotesCorr}</strong>), mostrando que filmes mais votados costumam ter melhores avaliações.</li>
      <li>Outras variáveis, como Meta Score, número de gêneros e frequência do diretor, apresentam correlações baixas, indicando menor influência direta sobre receita e notas.</li>
    </ul>
    <p>Essas informações ajudam a identificar padrões de desempenho, relacionando popularidade, avaliações e idade dos filmes.</p>
`;
  } catch (err) {
    console.error("Erro ao carregar resumo:", err);
  }
}

// Carrega gráficos nos containers
async function loadPlots() {
  for (const [key, route] of Object.entries(plotRoutes)) {
    try {
      const response = await fetch(route);
      const data = await response.json();

      if (data.path) {
        const fileName = data.path.split(/[\\/]/).pop();
        const img = document.createElement("img");
        img.src = `http://localhost:8000/img/${fileName}`;
        img.alt = `Gráfico ${key}`;
        img.classList.add("chart-img");

        document.getElementById(`chart-${key}`).appendChild(img);
      }
    } catch (err) {
      console.error(`Erro ao carregar gráfico ${key}:`, err);
    }
  }
}

async function loadHypotheses() {
  try {
    // 1️⃣ Gênero vs Gross
    const genreResponse = await fetch("http://127.0.0.1:8000/hypotheses/genre_vs_gross");
    const genreData = await genreResponse.json();
    const genreSection = document.getElementById("genre-gross");
    const topGenres = Object.entries(genreData)
      .sort((a, b) => b[1] - a[1])
      .slice(0, 5)
      .map(([g, v]) => `<li>${g}: $${v.toLocaleString()}</li>`)
      .join('');
    const genreResultP = genreSection.querySelector(".hypothesis-result");
    if (genreResultP) genreResultP.innerHTML = `<ul>${topGenres}</ul>`;

    // 2️⃣ Runtime vs IMDB Rating
    const runtimeResponse = await fetch("http://127.0.0.1:8000/hypotheses/runtime_vs_rating");
    const runtimeData = await runtimeResponse.json();
    const runtimeResultP = document.querySelector("#runtime-rating .hypothesis-result");
    if (runtimeResultP) runtimeResultP.innerHTML = `Correlação Spearman: <strong>${runtimeData.spearman_corr.toFixed(2)}</strong>.`;

    // 3️⃣ Votes vs Gross
    const votesResponse = await fetch("http://127.0.0.1:8000/hypotheses/votes_vs_gross");
    const votesData = await votesResponse.json();
    const votesResultP = document.querySelector("#votes-gross .hypothesis-result");
    if (votesResultP) votesResultP.innerHTML = `Correlação Spearman: <strong>${votesData.spearman_corr.toFixed(2)}</strong>.`;

    // 4️⃣ Idade vs Gross
    const ageResponse = await fetch("http://127.0.0.1:8000/hypotheses/year_vs_success");
    const ageData = await ageResponse.json();
    const topYears = Object.entries(ageData)
      .filter(([year, v]) => v !== null)
      .sort((a, b) => b[1] - a[1])
      .slice(0, 5)
      .map(([y, v]) => `<li>${y}: $${v.toLocaleString()}</li>`)
      .join('');
    const ageResultP = document.querySelector("#age-gross .hypothesis-result");
    if (ageResultP) ageResultP.innerHTML = `<ul>${topYears}</ul>`;

  } catch(err) {
    console.error("Erro ao carregar hipóteses:", err);
  }
}

async function loadRecommendationData() {
  try {
    // 1. Recomendação
    const recRes = await fetch("http://127.0.0.1:8000/recommendations/");
    const rec = await recRes.json();
    document.getElementById("recommendation-content").innerHTML = `
      <p>
        <strong>${rec.title}</strong> (${rec.year})<br>
        IMDb: <strong>${rec.imdb}</strong> | Meta Score: <strong>${rec.meta_score}</strong><br>
        Votos: ${rec.votes.toLocaleString()} | Bilheteria: $${rec.gross.toLocaleString()}
      </p>
    `;

    // 2. Top 10 (em tabela)
    const topRes = await fetch("http://127.0.0.1:8000/recommendations/top10");
    const top10 = await topRes.json();

    let table = `
      <table border="1" cellspacing="0" cellpadding="5">
        <thead>
          <tr>
            <th>Posição</th>
            <th>Título</th>
            <th>Ano</th>
            <th>IMDb</th>
            <th>Meta</th>
            <th>Votos</th>
            <th>Bilheteria</th>
            <th>Global Score</th>
          </tr>
        </thead>
        <tbody>
    `;

    top10.forEach((m, i) => {
      table += `
        <tr>
          <td>${i + 1}</td>
          <td><strong>${m.title}</strong></td>
          <td>${m.year}</td>
          <td>${m.imdb}</td>
          <td>${m.meta_score}</td>
          <td>${m.votes.toLocaleString()}</td>
          <td>$${m.gross.toLocaleString()}</td>
          <td>${m.global_score}</td>
        </tr>
      `;
    });

    table += "</tbody></table>";
    document.getElementById("top10-list").innerHTML = table;

    // 3. Fatores de Faturamento (apresentação melhor)
    const grossRes = await fetch("http://127.0.0.1:8000/gross_analysis/all");
    const gross = await grossRes.json();

    document.getElementById("gross-content").innerHTML = `
      <h3>📈 Correlações com Receita</h3>
      <ul>
        <li>Votos (No_of_Votes): <strong>${gross.correlations.No_of_Votes.toFixed(2)}</strong></li>
        <li>Tempo de Duração (Runtime_min): <strong>${gross.correlations.Runtime_min.toFixed(2)}</strong></li>
        <li>Nota IMDb: <strong>${gross.correlations.IMDB_Rating.toFixed(2)}</strong></li>
        <li>Idade do Filme (Age): <strong>${gross.correlations.Age.toFixed(2)}</strong></li>
      </ul>

      <h3>🧮 Regressão Linear</h3>
      <p>R² Score: <strong>${gross.regression.r2_score.toFixed(2)}</strong></p>
      <ul>
        <li>Intercepto: ${gross.regression.intercept.toFixed(2)}</li>
        <li>Coef. IMDb: ${gross.regression.coefficients.IMDB_Rating.toFixed(2)}</li>
        <li>Coef. Votos: ${gross.regression.coefficients.No_of_Votes.toFixed(2)}</li>
        <li>Coef. Runtime: ${gross.regression.coefficients.Runtime_min.toFixed(2)}</li>
        <li>Coef. Age: ${gross.regression.coefficients.Age.toFixed(2)}</li>
      </ul>

      <h3>🏆 Gêneros mais lucrativos</h3>
      <ul>
        ${Object.entries(gross.top_categories.top_genres)
          .map(([g, v]) => `<li>${g}: $${v.toLocaleString()}</li>`)
          .join("")}
      </ul>

      <h3>🎬 Diretores mais lucrativos</h3>
      <ul>
        ${Object.entries(gross.top_categories.top_directors)
          .map(([d, v]) => `<li>${d}: $${v.toLocaleString()}</li>`)
          .join("")}
      </ul>
    `;

    // 4. Overview Wordcloud
    document.getElementById("wordcloud").src =
      "http://127.0.0.1:8000/overview_analysis/wordcloud";

    // 5. Overview Top Words
    const topWordsRes = await fetch("http://127.0.0.1:8000/overview_analysis/top-words?genre=action&top_n=10");
    const topWords = await topWordsRes.json();
    document.getElementById("top-words").innerHTML = `
      <ul>
        ${Object.entries(topWords)
          .map(([w, v]) => `<li>${w} (${(v * 100).toFixed(2)}%)</li>`)
          .join("")}
      </ul>
    `;

    // 6. Predição de Gênero
    const predictRes = await fetch("http://127.0.0.1:8000/overview_analysis/predict-genre", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({
        overview: "A young wizard fights dark forces in a magical world full of mysteries and adventures."
      })
    });
    const predict = await predictRes.json();

    document.getElementById("predict-genre").innerHTML = `
      <p><strong>Gêneros previstos:</strong> ${predict.predicted_genres.join(", ")}</p>
      <h4>Probabilidades:</h4>
      <ul>
        ${Object.entries(predict.top_probs)
          .map(([g, v]) => `<li>${g}: ${(v * 100).toFixed(1)}%</li>`)
          .join("")}
      </ul>
    `;

  } catch (err) {
    console.error("Erro ao carregar dados:", err);
  }
}


document.addEventListener("DOMContentLoaded", () => {
  loadSummary();
  loadPlots();
  loadHypotheses();
  loadRecommendationData();
});
