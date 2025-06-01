"""
Módulo de funções auxiliares para a análise no jupyter notebook

Functions:
    get_sentiment(rating): Retorna o sentimento associado a uma avaliação.
"""

def get_sentiment(rating):
    """
    Retorna o sentimento correspondente ao rating, onde:
    1 e 2 retorna 'Negativo',
    3 retorna 'Neutro',
    4 e 5 retorna 'Positivo'

    Args:
        rating (int): Avaliação numérica entre 1 e 5.

    Returns:
        str: Sentimento associado à avaliação ('Positivo', 'Neutro' ou 'Negativo').
    """
    if rating >= 4:
        return 'Positivo'
    elif rating <= 2:
        return 'Negativo'
    else: # rating == 3
        return 'Neutro'
