from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from nltk.stem import WordNetLemmatizer

import json
import itertools
import string
import re


def preprocess(post):
    post = convert_to_lower(post)
    post = remove_url(post)
    post = remove_mention(post)
    post = convert_to_unigram(post)
    post = delete_number(post)
    post = tokenize(post)
    post = delete_stop_words(post)
    post = remove_punctuation(post)
    post = stem(post)
    post = lemmatize(post)
    post = ' '.join(post)
    return post


def convert_to_lower(post):
    post = post.lower()
    return post


def remove_url(post):
    post = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', post)
    return post


def remove_mention(post):
    mentions = re.findall(r"@\w+", post)
    for mention in mentions:
        post = post.replace(mention, "")
    return post


def convert_to_unigram(post):
    post = post.replace('-', '_')

    with open("depression_lexicon.json") as f:
        lexicon = json.load(f)

    all_lexicon_words = [
        lexicon_word.replace("_", " ") for lexicon_word in list(
            itertools.chain.from_iterable(
                [lexicon[signal] for signal in lexicon.keys()]))
    ]

    with open("medicine.json") as m:
        medicine_list = json.load(m)

    all_medicine_word = [
        medicine_word.replace("_", " ") for medicine_word in list(
            itertools.chain.from_iterable(
                [medicine_list[key] for key in medicine_list.keys()]))
    ]

    for medicine in all_medicine_word:
        all_lexicon_words.append(medicine)

    for word in all_lexicon_words:
        if word in post and " " in word:
            post = post.replace(word, word.replace(" ", "_"))

    return post


def delete_number(post):
    numbers = '0123456789'
    for number in numbers:
        post = post.replace(number, ' ')
    return post


def tokenize(post):
    tokenizer = TweetTokenizer()
    return tokenizer.tokenize(post)


def delete_stop_words(list_of_words):
    punctuation = list(string.punctuation)
    punctuation.remove('_')
    punctuation.append('“')
    punctuation.append('’')
    punctuation.append('”')
    punctuation.append('…')
    punctuation.append('...')
    punctuation.append('‘')
    punctuation.append('rt')
    stop = stopwords.words('english') + list(punctuation)
    result = [i for i in list_of_words if i not in stop]
    return result


def remove_punctuation(list_of_words):
    punctuation = list("_")
    return [i for i in list_of_words if i not in punctuation]


def stem(list_of_words):
    stemmer = SnowballStemmer('english')
    result = []
    for word in list_of_words:
        word = stemmer.stem(word)
        result.append(word)
    return result


def lemmatize(list_of_words):
    lemma = WordNetLemmatizer()
    result = []
    for word in list_of_words:
        word = lemma.lemmatize(word)
        result.append(word)
    return result
