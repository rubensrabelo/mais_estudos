const plots = [
    { url: "http://127.0.0.1:8000/plots/correlations/download", name: "heatmap_correlations" },
    { url: "http://127.0.0.1:8000/plots/imbd_vs_gross/download", name: "imdb_vs_gross" },
    { url: "http://127.0.0.1:8000/plots/genres/download", name: "top10_genres" },
    { url: "http://127.0.0.1:8000/plots/histogram/IMDB_Rating/download", name: "histogram_IMDB_Rating" },
];

const container = document.getElementById("plots-container");

plots.forEach(plot => {
    fetch(plot.url)
        .then(response => response.blob())
        .then(blob => {
            const imgURL = URL.createObjectURL(blob);

            const img = document.createElement("img");
            img.src = imgURL;
            img.alt = plot.name;
            img.style.maxWidth = "600px";
            img.style.marginBottom = "20px";

            const link = document.createElement("a");
            link.href = imgURL;
            link.download = plot.name + ".png";
            link.textContent = "Download " + plot.name;
            link.style.display = "block";
            link.style.marginBottom = "40px";

            container.appendChild(img);
            container.appendChild(link);
        })
        .catch(err => console.error("Erro ao baixar plot:", err));
});
