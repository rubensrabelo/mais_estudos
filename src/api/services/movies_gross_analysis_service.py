from sklearn.linear_model import LinearRegression

from api.repositories import df


def gross_correlation() -> dict:
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
    return {
        "correlations": gross_correlation(),
        "regression": gross_regression(),
        "top_categories": gross_top_categories()
    }
