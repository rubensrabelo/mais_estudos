import seaborn as sns
import matplotlib.pyplot as plt
import io
from api.repositories import get_dataset

df = get_dataset()


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
