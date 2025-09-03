import matplotlib
matplotlib.use("Agg")

# flake8: noqa: E402
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as ticker

matplotlib.rcParams["text.usetex"] = False
matplotlib.rcParams["mathtext.default"] = "regular"

def format_ticks(ax):
    """
    Formata os eixos de um gráfico para exibir os valores em notação padrão (sem notação científica).
    """
    ax.xaxis.set_major_formatter(ticker.ScalarFormatter())
    ax.yaxis.set_major_formatter(ticker.ScalarFormatter())
    ax.ticklabel_format(style='plain')

__all__ = ["plt", "sns", "format_ticks"]
