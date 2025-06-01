"""
Módulo de funções auxiliares para a análise no jupyter notebook

Functions:
    get_sentiment(rating): Retorna o sentimento associado a uma avaliação.
"""

import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    # 1. Minúsculas
    text = text.lower()

    # 2. Remover pontuação e números (mantém letras e espaços)
    text = re.sub(r'[^a-zA-Z\s]', '', text)

    # 3. Cria Token
    tokens = word_tokenize(text)

    # 4. Remover stopwords e Lematização
    processed_tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words]

    # 5. Juntar os tokens novamente em uma string
    return ' '.join(processed_tokens)
