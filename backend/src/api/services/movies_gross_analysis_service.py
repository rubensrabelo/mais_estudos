from sklearn.linear_model import LinearRegression

from api.repositories import df


def gross_correlation() -> dict:
    """
    Retorna a correlação entre Gross e outras variáveis numéricas do dataset.
    """
    num_cols = [
        "Gross",
        "IMDB_Rating",
        "No_of_Votes",
        "Runtime_min",
        "Age"
    ]
    corr = df[num_cols].corr()["Gross"].sort_values(ascending=False)
    return corr.to_dict()


def gross_regression():
    """
    Ajusta uma regressão linear para Gross usando IMDB_Rating, votos, duração
    e idade. Retorna coeficientes, intercepto e R².
    """
    X = df[[
        "IMDB_Rating",
        "No_of_Votes",
        "Runtime_min",
        "Age"
    ]].fillna(0)
    y = df["Gross"].fillna(0)

    model = LinearRegression()
    model.fit(X, y)

    coef = dict(zip(X.columns, model.coef_))
    intercept = model.intercept_
    r2_score = model.score(X, y)

    return {
        "intercept": intercept,
        "coefficients": coef,
        "r2_score": r2_score
    }


def gross_top_categories():
    """
    Retorna os 5 principais gêneros e diretores em média de Gross.
    """
    top_genres = (
        df.explode("Genre_list")
        .groupby("Genre_list")["Gross"]
        .mean()
        .sort_values(ascending=False)
        .head(5)
    )
    top_directors = (
        df.groupby("Director_top20")["Gross"]
        .mean()
        .sort_values(ascending=False)
        .head(5)
    )
    return {
        "top_genres": top_genres.to_dict(),
        "top_directors": top_directors.to_dict()
    }


def gross_factors_all():
    """
    Retorna correlação, regressão e top categorias em um único dicionário.
    """
    return {
        "correlations": gross_correlation(),
        "regression": gross_regression(),
        "top_categories": gross_top_categories()
    }
