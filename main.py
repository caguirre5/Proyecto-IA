import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

text = open('text.txt', encoding='utf-8').read()

#Convertimos todo a minusculas
text = text.lower()

#Se eliminan los signos de puntuacion
text = text.translate(str.maketrans('', '', string.punctuation))

tokenized_words = word_tokenize(text, "english")

print(tokenized_words)


final_words = []

for word in tokenized_words:
    if word not in stopwords.words('english'):
        final_words.append(word)