from pathlib import Path
import matplotlib.pyplot as plt
from wordcloud import WordCloud

from api.repositories import df
from api.utils import init_model

BASE_DIR = Path(__file__).resolve().parent.parent
IMG_DIR = BASE_DIR.parent / "img"
IMG_DIR.mkdir(parents=True, exist_ok=True)


def save_wordcloud() -> str:
    """
    Gera WordCloud com todas as sinopses e salva a imagem
    """
    text = " ".join(df["Overview"].dropna().astype(str).tolist())

    if not text.strip():
        raise ValueError(
            "Não há dados válidos em df['Overview'] para gerar a wordcloud."
        )

    wc = WordCloud(
        width=800,
        height=400,
        background_color="white"
    ).generate(text)

    plt.figure(figsize=(10, 5))
    plt.imshow(wc.to_array(), interpolation="bilinear")
    plt.axis("off")
    plt.tight_layout()

    file_path = IMG_DIR / "wordcloud_overview.png"
    plt.savefig(file_path, format="png", bbox_inches="tight", dpi=150)
    plt.close()

    return str(file_path)


def top_words_by_genre(genre: str, top_n: int = 15) -> dict:
    """Top palavras por gênero via TF-IDF (case-insensitive)"""
    genre = genre.lower()
    vectorizer, _, mlb = init_model(df)

    mask = (
        df["Genre_list"].apply(lambda lst: genre in [g.lower() for g in lst])
    )
    docs = df[mask]["Overview"]
    if docs.empty:
        return {"error": f"Gênero '{genre}' não encontrado."}

    X_genre = vectorizer.transform(docs)
    mean_tfidf = X_genre.mean(axis=0).A1
    features = vectorizer.get_feature_names_out()
    top_idx = mean_tfidf.argsort()[::-1][:top_n]

    return {features[i]: float(mean_tfidf[i]) for i in top_idx}


def predict_genre(overview: str, top_n: int = 5) -> dict:
    """Prediz gênero(s) a partir da sinopse"""
    vectorizer, model, mlb = init_model(df)
    X_new = vectorizer.transform([overview])
    y_prob = model.predict_proba(X_new)[0]

    top_idx = y_prob.argsort()[::-1][:top_n]

    top_preds = {mlb.classes_[i]: float(y_prob[i]) for i in top_idx}

    predicted_genres = [g for g, p in top_preds.items() if p > 0.2]
    if not predicted_genres:
        predicted_genres = [mlb.classes_[top_idx[0]]]

    return {
        "predicted_genres": predicted_genres,
        "top_probs": top_preds
    }
