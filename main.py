import string
from nltk.tokenize import word_tokenize

text = open('texto.txt', encoding='utf-8').read()

#Convertimos todo a minusculas
text = text.lower()

#Se eliminan los signos de puntuacion
text = text.translate(str.maketrans('', '', string.punctuation))

tokenized_words = word_tokenize(text, "english")

print(tokenized_words)