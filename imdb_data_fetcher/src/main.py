from .imdb import (
    fetch_movie,
    process_movie_data,
    create_dataframe,
    save_to_csv
)
from .data.movie_list import MOVIE_TITLES


def main():
    """
    Coleta, processa e salva dados de filmes recentes (2021+) em um CSV.
    """
    movies_data = []
    idx = 0
    total_titles = len(MOVIE_TITLES)

    while len(movies_data) < 200:
        title = MOVIE_TITLES[idx % total_titles]
        idx += 1

        data = fetch_movie(title)
        processed = process_movie_data(data)
        if processed:
            try:
                year = int(processed["Released_Year"])
                if year >= 2021:
                    movies_data.append(processed)
            except (TypeError, ValueError):
                continue

        if idx % 10 == 0:
            print(f"Filmes processados: {len(movies_data)}")

    df = create_dataframe(movies_data)
    save_to_csv(df, "imdb_movies_for_test.csv")
    print(f"Total de filmes salvos: {len(df)}")


if __name__ == "__main__":
    main()
