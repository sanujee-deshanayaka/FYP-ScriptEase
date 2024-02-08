import re
from Modules.SplitdataModel import split_data_model

def split_sentence(sentence):
    full_sentence = sentence.split()

    stop_words = [
        "for",
        "the",
        "do",
        "did",
        "does",
        "this",
        "to",
        "of",
        "with",
        "and",
        "or",
        "have",
        "has",
        "as",
        "is",
        "in",
        "button"
    ]

    words_list = []
    for word in full_sentence:
        if word not in stop_words:
            words_list.append(word)
            print(words_list)

    prediction_dic = split_data_model(words_list)

    return prediction_dic
