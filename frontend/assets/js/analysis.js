// Rotas do backend que geram e salvam os gráficos
const plotRoutes = [
  "http://localhost:8000/plots/histogram/Genre/save",
  "http://localhost:8000/plots/imbd_vs_gross/save"
];

async function loadPlots() {
  const chartContainer = document.getElementById("charts");

  for (const route of plotRoutes) {
    try {
      const response = await fetch(route);
      const data = await response.json();

      if (data.path) {
        // Pega apenas o nome do arquivo (independente de "\" ou "/")
        const fileName = data.path.split(/[\\/]/).pop();

        // Monta a URL pública usando a rota /img/
        const img = document.createElement("img");
        img.src = `http://localhost:8000/img/${fileName}`;
        img.alt = "Gráfico de filmes";
        img.classList.add("chart");

        chartContainer.appendChild(img);
      } else {
        console.warn("Não recebeu 'path' do backend:", data);
      }
    } catch (err) {
      console.error("Erro ao carregar gráfico:", err);
    }
  }
}

// Carrega os gráficos quando a página estiver pronta
document.addEventListener("DOMContentLoaded", loadPlots);
