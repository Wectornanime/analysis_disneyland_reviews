# analysis_disneyland_reviews

dataset: https://www.kaggle.com/datasets/arushchillar/disneyland-reviews

## como rodar um modelo exportado:
```python
import pickle

# Carregar o modelo
with open('modelo_sentimentos.pkl', 'rb') as f:
    dados = pickle.load(f)

model = dados['model'] # modelo em sí
vectorizer = dados['vectorizer'] # vetorizador

# Agora você pode usar:
texto = ["This was amazing!"]
X = vectorizer.transform(texto)
pred = model.predict(X)
print(pred)

```

