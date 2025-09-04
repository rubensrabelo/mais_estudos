import { plotRoutes } from "./api.js";

export function renderSummary(summary, corr) {
  const intro = document.getElementById("eda-intro");

  const grossVotesCorr = corr.Gross.No_of_Votes.toFixed(2);
  const grossAgeCorr = corr.Gross.Age.toFixed(2);
  const imdbVotesCorr = corr.IMDB_Rating.No_of_Votes.toFixed(2);

  const missingValues =
    Object.keys(summary.missing_values).length > 0
      ? Object.entries(summary.missing_values)
        .map(([col, val]) => `**${col}** (${val} registros)`)
        .join(", ")
      : "nenhuma coluna apresenta valores ausentes";

  intro.innerHTML = `
    <h2>Análise Geral da Base de Filmes</h2>
    <p>
      A base contém <strong>${summary.count}</strong> filmes, abrangendo produções
      de <strong>${summary.years.min}</strong> até <strong>${summary.years.max}</strong>. 
      O ano mais comum é <strong>${summary.years.most_common_year}</strong>, 
      com <strong>${summary.years.most_common_year_count}</strong> filmes.
    </p>
    <p>
      Em relação aos diretores, há uma diversidade significativa, com 
      <strong>${summary.directors.unique_count}</strong> nomes únicos.
      O mais recorrente é <strong>${summary.directors.top_director}</strong>, 
      com <strong>${summary.directors.top_director_count}</strong> filmes.
    </p>

    <h3>Receita (Gross)</h3>
    <p>
      A média de receita é de <strong>$${summary.gross.mean.toLocaleString()}</strong>,
      mas a mediana é de apenas <strong>$${summary.gross.median.toLocaleString()}</strong>, 
      revelando forte assimetria: poucos filmes de altíssimo faturamento puxam a média para cima. 
      O maior sucesso é <em>${summary.gross.top_movie}</em>, 
      com mais de <strong>$${summary.gross.max.toLocaleString()}</strong>, 
      enquanto o menor faturamento registrado é de apenas 
      <strong>$${summary.gross.min.toLocaleString()}</strong>.
    </p>

    <h3>Avaliações</h3>
    <p>
      A média de avaliação no IMDb é <strong>${summary.imdb_rating.mean.toFixed(2)}</strong>,
      e no Meta Score é <strong>${summary.meta_score.mean.toFixed(2)}</strong>. 
      O destaque é o filme <em>${summary.imdb_rating.top_movie}</em>, 
      considerado o mais bem avaliado.
    </p>

    <h3>Valores Ausentes</h3>
    ${Object.keys(summary.missing_values).length > 0
          ? (() => {
            const missingFormatted = Object.entries(summary.missing_values)
              .map(([col, val]) => `${col} (${val} filmes)`)
              .join(", ");

            return `
              <p>
                A presença de valores ausentes em variáveis importantes — como <strong>${missingFormatted}</strong> —
                pode comprometer a qualidade das previsões, especialmente em modelos que buscam estimar a nota do IMDb
                com base em múltiplos atributos. Para mitigar esse problema, é essencial aplicar estratégias adequadas de 
                tratamento, garantindo maior confiabilidade e desempenho nos resultados.
              </p>
            `;
          })()
          : "<p>Nenhuma coluna possui valores ausentes 🎉</p>"
        }`;

  const heatmapIntro = document.querySelector("#heatmap p");
  heatmapIntro.innerHTML += `
    <p>Observando as correlações entre variáveis apresentada no gráfico:</p>
    <ul>
      <li>A receita (Gross) apresenta correlação moderada e positiva com o número de votos (<strong>${grossVotesCorr}</strong>), indicando que filmes mais votados tendem a arrecadar mais.</li>
      <li>A idade do filme (Age) tem correlação negativa com a receita (<strong>${grossAgeCorr}</strong>), sugerindo que filmes mais antigos arrecadam menos atualmente.</li>
      <li>A nota do IMDB tem correlação positiva com o número de votos (<strong>${imdbVotesCorr}</strong>), mostrando que filmes mais votados costumam ter melhores avaliações.</li>
      <li>Outras variáveis, como Meta Score, número de gêneros e frequência do diretor, apresentam correlações baixas, indicando menor influência direta sobre receita e notas.</li>
    </ul>
  `;
}

export async function renderPlots() {
  for (const [key, route] of Object.entries(plotRoutes)) {
    try {
      const data = await fetch(route).then(res => res.json());
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

export function renderHypotheses(genreData, runtimeData, votesData, ageData) {
  // 1️⃣ Gênero vs Gross
  const genreSection = document.getElementById("genre-gross");
  const topGenres = Object.entries(genreData)
    .sort((a, b) => b[1] - a[1])
    .slice(0, 5)
    .map(([g, v]) => `<li>${g}: $${v.toLocaleString()}</li>`)
    .join('');
  const genreResultP = genreSection.querySelector(".hypothesis-result");
  if (genreResultP) genreResultP.innerHTML = `<ul>${topGenres}</ul>`;

  // 2️⃣ Runtime vs IMDB Rating
  const runtimeResultP = document.querySelector("#runtime-rating .hypothesis-result");
  if (runtimeResultP) runtimeResultP.innerHTML = `Correlação Spearman: <strong>${runtimeData.spearman_corr.toFixed(2)}</strong>.`;

  // 3️⃣ Votes vs Gross
  const votesResultP = document.querySelector("#votes-gross .hypothesis-result");
  if (votesResultP) votesResultP.innerHTML = `Correlação Spearman: <strong>${votesData.spearman_corr.toFixed(2)}</strong>.`;

  // 4️⃣ Idade vs Gross
  const ageResultP = document.querySelector("#age-gross .hypothesis-result");
  const topYears = Object.entries(ageData)
    .filter(([year, v]) => v !== null)
    .sort((a, b) => b[1] - a[1])
    .slice(0, 5)
    .map(([y, v]) => `<li>${y}: $${v.toLocaleString()}</li>`)
    .join('');
  if (ageResultP) ageResultP.innerHTML = `<ul>${topYears}</ul>`;
}


export function renderRecommendation(rec) {
  const container = document.getElementById("recommendation-content");
  container.innerHTML = `
    <div class="recommendation-card">
      <h3 class="rec-title">${rec.title} <span class="rec-year">(${rec.year})</span></h3>
      <p>
        ⭐ IMDb: <strong>${rec.imdb}</strong> | 📰 Meta Score: <strong>${rec.meta_score}</strong><br>
        👥 Votos: ${rec.votes.toLocaleString()} | 💰 Bilheteria: $${rec.gross.toLocaleString()}
      </p>
    </div>
  `;
}

export function renderTop10(top10) {
  const tableEl = document.getElementById("top10-list");
  const trilogy = [
    "The Lord of the Rings: The Return of the King",
    "The Lord of the Rings: The Fellowship of the Ring",
    "The Lord of the Rings: The Two Towers"
  ];

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
    const isTrilogy = trilogy.includes(m.title);
    table += `
      <tr class="${isTrilogy ? "highlight-trilogy" : ""}">
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
  tableEl.innerHTML = table;
}

export function renderGrossAnalysis(gross) {
  const container = document.getElementById("gross-content");
  container.innerHTML = `
    <p>Mais votos no IMDB (<strong>${gross.correlations.No_of_Votes.toFixed(2)}</strong>) → maior receita.</p>
    <p>Tempo de duração (<strong>${gross.correlations.Runtime_min.toFixed(2)}</strong>) → filmes mais longos tendem a arrecadar um pouco mais.</p>
    <p>IMDb Rating (<strong>${gross.correlations.IMDB_Rating.toFixed(2)}</strong>) → relação positiva, mas baixa.</p>
    <p>Idade do filme (<strong>${gross.correlations.Age.toFixed(2)}</strong>) → obras mais antigas arrecadam menos.</p>
    <h3>Principais categorias vencedoras:</h3>
    <p><strong>Gêneros:</strong> ${Object.keys(gross.top_categories.top_genres).slice(0, 5).join(", ")}</p>
    <p><strong>Diretores:</strong> ${Object.keys(gross.top_categories.top_directors).slice(0, 2).join(" e ")}</p>
  `;
}

export function renderWordcloud(fileName) {
  const img = document.getElementById("wordcloud-img");
  img.src = `http://localhost:8000/img/${fileName}`;
}

export function renderPredictionGenre(predict) {
  const topPredictions = predict.predicted_genres.slice(0, 2);
  document.getElementById("predict-genre").innerHTML = `
    <p><strong>Output:</strong></p>
    <ul>
      ${topPredictions.map(g => `<li>${g} (${(predict.top_probs[g] * 100).toFixed(1)}%)</li>`).join("")}
    </ul>
  `;
}

export function renderErrorGenre() {
  document.getElementById("predict-genre").innerHTML =
    `<p style="color:red;">Erro ao carregar previsão.</p>`;
}
