import string
from nltk.tokenize import word_tokenize
from collections import Counter

import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.stem import WordNetLemmatizer


class SentimentAnalizer:
    def __init__(self) -> None:
        pass

    def procesar_texto(self, text: str):
        # text = open('text.txt', encoding='utf-8').read()
        # text = "I can't believe how poorly this game is designed. The controls are clunky, the graphics are outdated, and the gameplay is incredibly boring. I regret wasting my money on it."
        lower_case = text.lower()
        cleaned_text = lower_case.translate(
            str.maketrans('', '', string.punctuation))

        # Using word_tokenize because it's faster than split()
        tokenized_words = word_tokenize(cleaned_text, "english")

        # Removing Stop Words
        final_words = []
        for word in tokenized_words:
            if word not in stopwords.words('english'):
                final_words.append(word)

        # Lemmatization - From plural to single + Base form of a word (example better-> good)
        lemma_words = []
        for word in final_words:
            word = WordNetLemmatizer().lemmatize(word)
            lemma_words.append(word)
        processed_text = ' '.join(lemma_words)

        return self.sentiment_analyse(processed_text)

    def sentiment_analyse(self, sentiment_text):
        score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
        if score['neg'] > score['pos']:
            # Retorna negative
            return 'negative'
        # elif score['neg'] < score['pos']:
        #     print("Positive Sentiment")
        # else:
        #     print("Neutral Sentiment")
        #     return 'neutral'
