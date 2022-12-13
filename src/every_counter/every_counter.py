from collections import Counter
from string import punctuation

from src.every_counter.plotting import plot_words


def load_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text


def delete_punctuation(text:str) ->str:
    for sign in punctuation:
        text = text.replace(sign, "")
    return text.split()


def count_entries(file_path:str) ->str:
    dirty_text = load_file(file_path)
    text_without_punctuation = delete_punctuation(dirty_text)
    return Counter(text_without_punctuation)

if __name__=="__main__":
    count = count_entries(r'C:\Users\asmolkin\AppData\Roaming\JetBrains\PyCharm2021.3\scratches\proza')
    plot_words(count, n=13)