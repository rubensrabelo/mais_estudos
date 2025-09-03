import os
import pandas as pd


def save_to_csv(df: pd.DataFrame, filename: str):
    """
    Salva o DataFrame em CSV na pasta backend/src/data de forma relativa.
    """
    base_dir = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "..",
            "..",
            "..",
            "backend",
            "src",
            "data"
        )
    )
    os.makedirs(base_dir, exist_ok=True)
    filepath = os.path.join(base_dir, filename)
    df.to_csv(filepath, index=False, encoding="utf-8")
    print(f"Arquivo salvo em: {filepath}")
