from pathlib import Path

from config import plt, sns, format_ticks
from api.repositories import df
from api.utils import correlations

# Pasta onde as imagens serão salvas
IMG_DIR = Path(r"C:\github_projetos\python\mais_estudos\img")
IMG_DIR.mkdir(parents=True, exist_ok=True)


def plot_corr_heatmap() -> str:
    plt.figure(figsize=(10, 8))
    corr = correlations(df)
    ax = sns.heatmap(
        corr,
        annot=True,
        fmt=".2f",
        cmap="coolwarm",
        center=0,
        square=True
    )
    plt.title("Heatmap de Correlações", fontsize=14)
    format_ticks(ax)

    file_path = IMG_DIR / "heatmap_correlations.png"
    plt.savefig(file_path, format="png", bbox_inches="tight", dpi=150)
    plt.close()
    return str(file_path)


def plot_imbd_vs_gross() -> str:
    plt.figure(figsize=(10, 6))
    ax = sns.scatterplot(
        data=df,
        x="IMDB_Rating",
        y="Gross",
        alpha=0.6,
        color="royalblue",
        edgecolor="white",
        linewidth=0.5
    )
    plt.yscale("log")
    plt.title("IMDB Rating vs Gross", fontsize=16, fontweight="bold")
    plt.xlabel("IMDB Rating", fontsize=12)
    plt.ylabel("Gross (log scale)", fontsize=12)
    plt.grid(True, which="both", ls="--", lw=0.5, alpha=0.7)
    sns.despine()
    format_ticks(ax)

    file_path = IMG_DIR / "imdb_vs_gross.png"
    plt.savefig(file_path, format="png", dpi=120, bbox_inches="tight")
    plt.close()
    return str(file_path)


def plot_genres() -> str:
    plt.figure(figsize=(10, 6))
    genre_counts = (
        df.explode("Genre_list")["Genre_list"].value_counts().head(10)
    )
    ax = sns.barplot(
        x=genre_counts.values,
        y=genre_counts.index
    )
    for i, v in enumerate(genre_counts.values):
        ax.text(v + 5, i, str(v), color="black", va="center", fontsize=10)

    sns.despine(left=True, bottom=True)
    plt.title("Top 10 Gêneros Mais Frequentes", fontsize=14, weight="bold")
    plt.xlabel("Número de Filmes")
    plt.ylabel("Gênero")
    format_ticks(ax)

    file_path = IMG_DIR / "top10_genres.png"
    plt.savefig(file_path, format="png", dpi=150, bbox_inches="tight")
    plt.close()
    return str(file_path)


def plot_histogram(column: str) -> str:
    print(df.columns.values)
    plt.figure(figsize=(8, 6))
    ax = sns.histplot(
        df[column].dropna(),
        kde=True,
        bins=30,
        color="steelblue",
        edgecolor="black",
        alpha=0.7
    )
    sns.despine(top=True, right=True, left=False, bottom=False)
    plt.title(f"Distribuição de {column}", fontsize=16, fontweight="bold")
    plt.xlabel(column, fontsize=14)
    plt.ylabel("Frequência", fontsize=14)
    plt.grid(axis="y", linestyle="--", alpha=0.6)
    format_ticks(ax)

    file_path = IMG_DIR / f"histogram_{column}.png"
    plt.savefig(file_path, format="png", dpi=120, bbox_inches="tight")
    plt.close()
    return str(file_path)
