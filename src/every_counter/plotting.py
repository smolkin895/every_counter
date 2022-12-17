# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt


def plot_words(word_counts, n=10):
    """Plot abarchartofwordcounts.
Parameters
----------
word_counts :collections.Counter
Counter object of word counts.
n :int,optional
Plot the top n words.By default, 10.
Returns
-------
matplotlib.container.BarContainer
Bar chart of word counts.
Examples
--------
>>> frompycounts.pycountsimportcount_words
>>> frompycounts.plottingimportplot_words
>>> counts=count_words("text.txt")
>>> plot_words(counts)
"""
    top_n_words = word_counts.most_common(n)
    word, count = zip(*top_n_words)
    fig = plt.bar(range(n), count)
    plt.xticks(range(n), labels=word, rotation=45)
    plt.xlabel("Word")
    plt.ylabel("Count")
    fig.show()
    return fig