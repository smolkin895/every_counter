import os
from collections import Counter
from string import punctuation



def load_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text


def delete_punctuation(text:str):
    for sign in punctuation:
        text = text.replace(sign, "")
    return text.split()


def count_entries(file_path):
    """Count words in a text file.
    Words are made lowercase
    and punctuation is removed
    before counting.

    Parameters
    ----------
    input_file: str
    Path to text file.

    Returns
    -------
    collections.Counter
    dict - like object where keys are words and values are counts.
    Examples
    --------

    >>> count_entries('text.txt')
    """
    if os.path.isfile(file_path):
        dirty_text = load_file(file_path)
        text_without_punctuation = delete_punctuation(dirty_text)
        return Counter(text_without_punctuation)
    elif isinstance(file_path, str):
        text_without_punctuation = delete_punctuation(file_path)
        return Counter(text_without_punctuation)

