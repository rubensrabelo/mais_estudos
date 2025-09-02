document.getElementById("predict-form").addEventListener("submit", async (e) => {
  e.preventDefault();

  const formData = new FormData(e.target);
  const movie = Object.fromEntries(formData);

  const response = await fetch("http://127.0.0.1:8000/imdb_notes_analysis/predict", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(movie)
  });

  const data = await response.json();
  document.getElementById("result").innerText =
    `🎯 Previsão IMDB: ${data.IMDB_Prediction.toFixed(2)}`;
});
