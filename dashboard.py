# dashboard.py: Streamlit dashboard with refined presentation and user-friendly layout

import re
from collections import Counter

import matplotlib.pyplot as plt
import nltk
import pandas as pd
import plotly.express as px
import streamlit as st
from wordcloud import WordCloud

# Define colors and styles
GRADIENT = "linear-gradient(135deg, #f5f5dc, #e0d6a2)"  # Light beige gradient
PALETTE = {
    "background": "#f0e5d8",  # Lighter beige background color
    "text": "#3c3836",
    "primary": "#d65d0e",
    "secondary": "#98971a",
    "accent": "#458588",
    "hover": "#fabd2f",
}

# Load stopwords and data
nltk.download('stopwords')
stop_words = set(nltk.corpus.stopwords.words('portuguese'))
df = pd.read_csv('toots_com_sentimento.csv')

# Format and sort data
df['criado_em'] = pd.to_datetime(df['criado_em'], format='ISO8601')
df.sort_values(by='criado_em', inplace=True)

# Set Streamlit configuration and styles
st.set_page_config(page_title="Análise de Sentimento", layout="wide")



# Project Introduction Section



# Feature Highlights
st.markdown(
    f"""
    <div class="card">
    <h1 style="text-align: center; color: {PALETTE['primary']};">Análise de Sentimento no Mastodon</h1>
    <p><strong>Autor:</strong> Ricardo Henrique</p>
    <p>Este projeto realiza uma análise de sentimentos sobre toots da plataforma Mastodon com a hashtag <strong>#Python</strong>. O Mastodon é uma plataforma de microblogging semelhante ao Twitter, onde os usuários compartilham mensagens curtas chamadas toots, que desempenham um papel similar aos tweets no Twitter.</p>
    <p>O principal objetivo deste projeto é entender as percepções e sentimentos da comunidade do Mastodon em relação ao Python. Para isso, utilizamos algoritmos avançados de <strong>machine learning</strong> que classificam os sentimentos dos toots em <strong>positivos</strong>, <strong>negativos</strong> ou <strong>neutros</strong>. Além disso, foram gerados insights detalhados sobre as palavras mais recorrentes associadas ao Python.</p>
    <p><strong>Algoritmos Utilizados:</strong></p>
    <ul>
        <li><strong>Naive Bayes:</strong> Utilizado como base para classificação de texto. Este modelo probabilístico é eficaz em tarefas de análise de sentimento ao prever a probabilidade de um sentimento com base nas palavras presentes nos toots.</li>
        <li><strong>TF-IDF (Term Frequency - Inverse Document Frequency):</strong> Empregado para transformar os textos em vetores numéricos, destacando as palavras mais relevantes em cada toot ao equilibrar a frequência de uso local e global das palavras.</li>
        <li><strong>Word Embeddings (ex.: Word2Vec ou GloVe):</strong> Implementados para representar semanticamente os textos em um espaço vetorial, permitindo ao modelo capturar relações contextuais entre palavras.</li>
        <li><strong>Random Forest:</strong> Algoritmo de aprendizado supervisionado usado como classificador alternativo para aumentar a precisão, combinando múltiplas árvores de decisão e reduzindo o risco de overfitting.</li>
    </ul>
    <p>Os algoritmos foram treinados e avaliados com um conjunto de dados representativo, garantindo resultados confiáveis na identificação de sentimentos e tendências da comunidade Python no Mastodon.</p>
    <p>Explore gráficos interativos, descubra as emoções predominantes e visualize as palavras mais frequentes associadas ao Python!</p>
</div>

    """,
    unsafe_allow_html=True,
)
st.markdown(
    f"""
    <style>
        body {{
            background: {GRADIENT};
            color: {PALETTE['text']};
            font-family: Arial, sans-serif;
        }}
        .card {{
            padding: 20px;
            border-radius: 15px;
            background-color: {PALETTE['background']};
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.15);
            margin-bottom: 50px; /* Espaçamento entre caixas */
            transition: transform 0.8s;
        }}
        .card:hover {{
            transform: scale(1.02);
            box-shadow: 0px 8px 12px rgba(0, 0, 0, 0.3);
        }}
        .stButton > button {{
            background-color: {PALETTE['primary']};
            color: white;
            border-radius: 8px;
            border: none;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
            transition: transform 0.2s;
        }}
        .stButton > button:hover {{
            background-color: {PALETTE['hover']};
            transform: scale(1.05);
        }}
    </style>
    """,
    unsafe_allow_html=True,
)


# Sidebar Filters
st.sidebar.header("Filtros")
sentimento_selecionado = st.sidebar.multiselect(
    "Selecione o(s) sentimento(s):",
    df['sentimento'].unique(),
    default=df['sentimento'].unique(),
)
df_filtrado = df[df['sentimento'].isin(sentimento_selecionado)]

# Sentiment Analysis Visualizations
st.header("Análise de Sentimento")
col1, col2 = st.columns(2)

with col1:
    fig_pizza = px.pie(
        df_filtrado,
        names='sentimento',
        title='Proporção de Sentimentos',
        color_discrete_sequence=px.colors.qualitative.Set2,
    )
    fig_pizza.update_traces(textinfo='percent+label', textfont_size=16)
    fig_pizza.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=20, r=20, t=30, b=20),
        title_font_size=24,
        title_x=0.5,
    )
    st.plotly_chart(fig_pizza, use_container_width=True)

with col2:
    fig_barras = px.bar(
        df_filtrado,
        x='sentimento',
        title='Distribuição de Sentimentos',
        color='sentimento',
        color_discrete_sequence=px.colors.qualitative.Set3,
    )
    fig_barras.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=20, r=20, t=30, b=20),
        title_font_size=24,
        title_x=0.5,
    )
    fig_barras.update_traces(marker=dict(line=dict(width=0)))
    st.plotly_chart(fig_barras, use_container_width=True)

# WordCloud Visualization
st.header("Nuvem de Palavras")
def gerar_nuvem_palavras(df):
    texto = ' '.join(df['texto'])
    wordcloud = WordCloud(
        width=800,
        height=400,
        background_color='white',
        colormap='viridis',
    ).generate(texto)
    fig, ax = plt.subplots()
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    st.pyplot(fig)

gerar_nuvem_palavras(df_filtrado)

# Simplified Toots Table with Explanation
st.header("Toots Analisados")
st.write("Aqui estão os toots analisados, incluindo o texto, data de criação, usuário e sentimento associado. Explore o conteúdo e entenda melhor os dados analisados.")
st.dataframe(
    df_filtrado[['texto', 'criado_em', 'usuario', 'sentimento']],
    use_container_width=True,
    height=300,
)
