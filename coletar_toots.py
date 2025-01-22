import csv
import re

import nltk
import pandas as pd
from bs4 import BeautifulSoup
from mastodon import Mastodon
from nltk.corpus import stopwords
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Substitua pelo seu Access Token e URL da instância
access_token = "UNK0yjHF6HydP9MN7wT3zVcExKWtAefngmoCP8U-yTA"  # Substitua pelo seu token
api_base_url = "https://mastodon.social"

# Criar uma instância da API
mastodon = Mastodon(
    access_token=access_token,
    api_base_url=api_base_url
)

# Definir a palavra-chave ou hashtag
keyword = "Python"

# Coletar toots (posts) com a hashtag
toots = mastodon.timeline_hashtag(keyword)

# Salvar os dados em uma lista de dicionários
dados_toots = []
for toot in toots:
    dados_toots.append({
        'texto': toot['content'],
        'criado_em': toot['created_at'],
        'usuario': toot['account']['username']
    })

# Imprimir os dados coletados
print(dados_toots)

# Nome do arquivo CSV
nome_arquivo = "toots.csv"

# Abrir o arquivo em modo de escrita ('w')
with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:
    # Criar um objeto writer
    writer = csv.DictWriter(arquivo_csv, fieldnames=dados_toots[0].keys())

    # Escrever o cabeçalho (nomes das colunas)
    writer.writeheader()

    # Escrever os dados dos toots
    for toot in dados_toots:
        writer.writerow(toot)

# Carregar os dados do arquivo CSV
df = pd.read_csv('toots.csv')

# Remover tags HTML
df['texto'] = df['texto'].apply(lambda x: BeautifulSoup(x, 'html.parser').get_text())

# Remover caracteres especiais (exceto letras, números e espaços)
df['texto'] = df['texto'].apply(lambda x: re.sub(r'[^a-zA-Z0-9\s]', '', x))

# Converter para minúsculas
df['texto'] = df['texto'].str.lower()

# Baixar as stop words em português (se necessário)
nltk.download('stopwords')

# Obter a lista de stop words em português
stop_words = set(stopwords.words('portuguese'))

# Remover stop words
df['texto'] = df['texto'].apply(lambda x: ' '.join([word for word in x.split() if word not in stop_words]))

# Remover linhas com valores faltantes
df.dropna(inplace=True)

# Salvar o DataFrame em um novo arquivo CSV
df.to_csv('toots_processados.csv', index=False)

# Criar o analisador VADER
analyzer = SentimentIntensityAnalyzer()

def analisar_sentimento(texto):
    scores = analyzer.polarity_scores(texto)
    if scores['compound'] >= 0.05:
        return 'positivo'
    elif scores['compound'] <= -0.05:
        return 'negativo'
    else:
        return 'neutro'

# Aplicar a função à coluna 'texto'
df['sentimento'] = df['texto'].apply(analisar_sentimento)

# Salvar o DataFrame em um novo arquivo CSV
df.to_csv('toots_com_sentimento.csv', index=False)