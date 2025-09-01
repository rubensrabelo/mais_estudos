import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.multiclass import OneVsRestClassifier

_vectorizer = None
_model = None
_mlb = None

CUSTOM_STOPWORDS = [
    "movie", "film", "story", "character", "characters",
    "man", "woman", "young", "world", "life"
]


def _prepare_data(df: pd.DataFrame):
    """Filtra Overview e Genre_list e converte gêneros para lowercase"""
    data = df.dropna(subset=["Overview", "Genre_list"]).copy()
    data["Genres_lower"] = (
        data["Genre_list"]
        .apply(lambda lst: [g.lower() for g in lst if g])
    )
    data = data[data["Genres_lower"].map(len) > 0]
    return data


def _fit_vectorizer(texts):
    """Treina TF-IDF com unigrams + bigrams + stopwords customizadas"""
    vectorizer = TfidfVectorizer(
        stop_words="english",
        max_features=10000,
        ngram_range=(1, 2)
    )
    vectorizer.stop_words_ = vectorizer.get_stop_words().union(
        CUSTOM_STOPWORDS
    )
    X = vectorizer.fit_transform(texts)
    return vectorizer, X


def _fit_model(X, y):
    """Treina modelo OneVsRestClassifier com MultinomialNB"""
    model = OneVsRestClassifier(MultinomialNB())
    model.fit(X, y)
    return model


def init_model(df: pd.DataFrame):
    """
    Função principal para inicializar TF-IDF + MultiLabelBinarizer + modelo
    """
    global _vectorizer, _model, _mlb

    if _vectorizer is not None and _model is not None:
        return _vectorizer, _model, _mlb

    data = _prepare_data(df)

    vectorizer, X = _fit_vectorizer(data["Overview"])

    mlb = MultiLabelBinarizer()
    y = mlb.fit_transform(data["Genres_lower"])

    model = _fit_model(X, y)

    _vectorizer, _model, _mlb = vectorizer, model, mlb
    return _vectorizer, _model, _mlb
