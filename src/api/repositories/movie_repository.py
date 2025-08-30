import pandas as pd
import os

CSV_FILE = os.path.join("data", "desafio_indicium_imdb.csv")

movie_data = pd.read_csv(CSV_FILE, index_col=0)
