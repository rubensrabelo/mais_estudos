from .imdb import (
    fetch_movie,
    process_movie_data,
    create_dataframe,
    save_to_csv
)
from .data.movie_list import MOVIE_TITLES


def main():
    movie_titles_to_fetch = []
    while len(movie_titles_to_fetch) < 200:
        movie_titles_to_fetch.extend(MOVIE_TITLES)
    movie_titles_to_fetch = movie_titles_to_fetch[:201]

    movies_data = []
    for idx, title in enumerate(movie_titles_to_fetch, 1):
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
            print(f"Processados {idx} filmes...")

    df = create_dataframe(movies_data)
    save_to_csv(df, "imdb_movies_for_test.csv")
    print(f"Total de filmes salvos: {len(df)}")


if __name__ == "__main__":
    main()
