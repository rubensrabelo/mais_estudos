import io

from api.config import plt, sns
from api.repositories import df
from api.utils import correlations


def plot_corr_heatmap() -> io.BytesIO:
    plt.figure(figsize=(10, 8))
    corr = correlations(df)
    sns.heatmap(
        corr,
        annot=True,
        fmt=".2f",
        cmap="coolwarm",
        center=0,
        square=True
    )
    plt.title("Heatmap de Correlações", fontsize=14)

    buf = io.BytesIO()
    plt.savefig(buf, format="png", bbox_inches="tight")
    buf.seek(0)
    return buf


def plot_imbd_vs_gross() -> io.BytesIO:
    plt.figure(figsize=(10, 6))
    sns.scatterplot(
        data=df,
        x="IMDB_Rating",
        y="Gross",
        alpha=0.6,
        color="royalblue",
        edgecolor="white",
        linewidth=0.5
    )
    plt.yscale("log")
    plt.title(
        "IMDB Rating vs Gross", fontsize=16, fontweight="bold"
    )
    plt.xlabel("IMDB Rating", fontsize=12)
    plt.ylabel("Gross (log scale)", fontsize=12)
    plt.grid(True, which="both", ls="--", lw=0.5, alpha=0.7)
    sns.despine()
    buf = io.BytesIO()
    plt.tight_layout()
    plt.savefig(buf, format="png", dpi=120)
    buf.seek(0)
    return buf


def plot_genres() -> io.BytesIO:
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
    buf = io.BytesIO()
    plt.tight_layout()
    plt.savefig(buf, format="png", dpi=150)
    buf.seek(0)
    return buf


def plot_histogram(column: str) -> io.BytesIO:
    plt.figure(figsize=(8, 6))
    sns.histplot(
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
    plt.tight_layout()
    buf = io.BytesIO()
    plt.savefig(buf, format="png", dpi=120, bbox_inches="tight")
    buf.seek(0)
    return buf
