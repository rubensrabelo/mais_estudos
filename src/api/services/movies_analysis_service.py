import io

from api.config import plt, sns
from api.repositories import df
from api.utils import correlations


def plot_corr_heatmap():
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


def plot_imbd_vs_gross():
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=df, x="IMDB_Rating", y="Gross", alpha=0.5)
    plt.yscale("log")
    plt.title("IMDB Rating vs Gross")
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    return buf


def plot_genres():
    plt.figure(figsize=(10, 6))
    genre_counts = (
        df.explode("Genre_list")["Genre_list"].value_counts().head(10)
    )
    sns.barplot(x=genre_counts.values, y=genre_counts.index)
    plt.title("Top 10 Gêneros")
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    return buf
