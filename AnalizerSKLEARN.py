from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression


import pandas as pd
import string


class SentimentAnalizer:
    def __init__(self) -> None:
        data = pd.read_csv('./train.csv', encoding='latin-1',
                           delimiter=',', quotechar='"')
        data = data.dropna()

        class_distribution = data['Sentiment'].value_counts()
        minority_class_size = min(class_distribution)

        # Undersampling de la clase mayoritaria
        undersampled_df = pd.concat([
            data[data['Sentiment'] == 0],
            data[data['Sentiment'] == 1].sample(
                minority_class_size, replace=True)
        ])

        # Almacenamos el nuevo balance obtenido en el df original
        data = undersampled_df
        # Renombramos la columna para que el codigo sea mas legible
        data = data.rename(columns={'SentimentText;;;;;;;;': 'SentimentText'})
        # Convertimos la columna Sentiment a entero ya que solo son valores binarios
        data['Sentiment'] = data['Sentiment'].astype(int)

        # limpiamos todos los tweets en el dataset para que el modelo sea mas eficiente
        for index, row in data.iterrows():
            text = row['SentimentText']
            lower_case = text.lower()
            cleaned_text = lower_case.translate(
                str.maketrans('', '', string.punctuation))
            data.at[index, 'SentimentText'] = cleaned_text

        self.vectorizer, self.model = self.build_model(data)
        print('El modelo se ha entrenado correctamente')

    def build_model(self, data):
        # Dividir los datos en características (X) y etiquetas (y)
        X = data['SentimentText']
        y = data['Sentiment']

        # Dividir los datos en conjuntos de entrenamiento y prueba
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42)

        # Crear un vectorizador TF-IDF
        vectorizer = TfidfVectorizer()
        X_train_vectorized = vectorizer.fit_transform(X_train)
        X_test_vectorized = vectorizer.transform(X_test)

        # Crear y entrenar el modelo de Regresión Logística
        model = LogisticRegression()
        model.fit(X_train_vectorized, y_train)

        # Realizar predicciones en el conjunto de prueba
        y_pred = model.predict(X_test_vectorized)

        return vectorizer, model

    def find_sentiment(self, sentiment_text):
        new_text_vectorized = self.vectorizer.transform([sentiment_text])
        predicted_sentiment = self.model.predict(new_text_vectorized)
        if predicted_sentiment == 0:
            return 'negative'
        return 'positive'
