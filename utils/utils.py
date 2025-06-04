"""
Módulo de funções auxiliares para a análise no jupyter notebook

Functions:
    get_sentiment(rating): Retorna o sentimento associado a uma avaliação.
"""

def get_sentiment(rating):
    """
    Retorna o sentimento correspondente ao rating, onde:
    1 e 2 retorna 'negative',
    3 retorna 'neutral',
    4 e 5 retorna 'positive'

    Args:
        rating (int): Avaliação numérica entre 1 e 5.

    Returns:
        str: Sentimento associado à avaliação ('positive', 'neutral' ou 'negative').
    """
    if rating >= 4:
        return 'positive'
    elif rating <= 2:
        return 'negative'
    else: # rating == 3
        return 'neutral'
