"""Exemplo de python."""
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np


def plot_matplotlib(var):
    fig = plt.figure(figsize=(16, 9))
    plt.hist(var, bins=100)
    plt.show()


def plot_pandas(var):
    fig = plt.figure(figsize=(16, 9))
    ax = fig.add_subplot(111)
    var.plot.hist(bins=100, ax=ax)
    plt.show()


def plot_seaborn(var):
    """Faz o plot de um Histograma utilizado seaborn.

    Parameters
    ----------
    var : type
        Minha variável.

    Returns
    -------
    type
        Description of returned object.

    """
    fig = plt.figure(figsize=(16, 9))
    ax = fig.add_subplot(111)
    sns.histplot(var, ax=ax)
    plt.show()


if __name__ == "__main__":
    x = np.random.normal(0, 10, size=1000)
    X = pd.DataFrame(x, columns=["x"])
    plot_seaborn(X)
