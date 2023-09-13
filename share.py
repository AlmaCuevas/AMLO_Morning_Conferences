import pandas as pd
from sklearn.cluster import KMeans
import nltk
from nltk.corpus import stopwords
import numpy as np
from pattern.text.es import singularize
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import re
from tqdm.notebook import tqdm
tqdm.pandas()

years = ["2018", "2019", "2020", "2021", "2022", "2023"]

def select_secondary_keywords_ngrams(txt_list: list[str], ngram_min: int, ngram_max: int) -> pd.DataFrame:
    # Stopword removal
    stop_words = set(stopwords.words('spanish'))
    txt1 = []
    for line in txt_list:
        txt1.append(' '.join([x for
                            x in nltk.word_tokenize(line) if
                            (x not in stop_words)]))

    # Getting trigrams
    vectorizer = CountVectorizer(ngram_range=(ngram_min, ngram_max))
    X1 = vectorizer.fit_transform(txt1)
    features = (vectorizer.get_feature_names_out())

    # Applying TFIDF
    vectorizer = TfidfVectorizer(ngram_range=(ngram_min, ngram_max))
    X2 = vectorizer.fit_transform(txt1)
    scores = (X2.toarray())

    # Getting top ranking features
    sums = X2.sum(axis=0)
    data1 = []
    for col, term in enumerate(features):
        data1.append((term, sums[0, col]))
    ranking = pd.DataFrame(data1, columns=['term', 'rank'])
    words = (ranking.sort_values('rank', ascending=False))
    return words.reset_index(drop=True)
