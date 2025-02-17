Análise de Sentimentos no Mastodon #Python
Um projeto que utiliza aprendizado de máquina para classificar os sentimentos de toots do Mastodon contendo a hashtag #Python. Ele apresenta os resultados por meio de um dashboard interativo, fornecendo insights sobre os dados encontrados.

Visão Geral do Projeto
Objetivo: Desenvolver uma ferramenta que analise automaticamente os sentimentos de publicações no Mastodon, permitindo explorar os resultados com visualizações interativas.

O que o projeto faz?

Coleta de Dados: Captura de toots com a hashtag #Python.
Análise de Sentimentos: Classificação dos textos como positivos, negativos ou neutros.
Visualizações: Criação de gráficos e nuvens de palavras para análise interativa dos dados.
Como funciona?

O sistema utiliza a API do Mastodon para buscar publicações.
As publicações são pré-processadas (remoção de stopwords, tokenização, etc.).
Um modelo de aprendizado de máquina classifica os textos.
Os resultados são exibidos em um painel interativo construído com Streamlit.
Ferramentas e Tecnologias Utilizadas
Linguagens e Frameworks:

Python: Linguagem principal para processamento e análise de dados.
Streamlit: Framework para construção do dashboard interativo.
Bibliotecas Principais:

nltk e re: Processamento de linguagem natural e limpeza de texto.
scikit-learn: Modelagem e treinamento de algoritmos de aprendizado de máquina.
pandas e numpy: Manipulação e análise de dados tabulares.
matplotlib e plotly: Visualizações gráficas.
wordcloud: Geração de nuvens de palavras.
Como Construímos o Código?
1. Coleta de Dados:

Utilizamos a API do Mastodon para extrair toots com a hashtag #Python.

2. Pré processamento dos textos:

Conversão para maiúsculas.
Remoção de stopwords e resultados.
Tokenização e stemming com nltk.

3. Treinamento do modelo:

Treinamos um classificador Naive Bayes com TF-IDF para identificar sentimentos

4. Construção do Dashboard:

Criamos um painel interativo com Streamlit, que exibe gráficos e permite explorar os dados.

Estrutura do Projeto:
📁 analise-sentimento-mastodon
├── 📄 dashboard.py         # Código principal para o dashboard
├── 📄 data_preprocessing.py # Funções de pré-processamento de texto
├── 📄 requirements.txt     # Dependências do projeto
├── 📄 README.md             # Documentação do projeto
├── 📁 assets               # Imagens e outros recursos visuais
└── 📁 models               # Modelos treinados para análise de sentimentos

Contribua com o Projeto: 

Se você tem ideias ou sugestões, fique à vontade para contribuir!

Faça um fork do repositório.
Crie uma branch (git checkout -b feature/nova-feature).
Faça commit das alterações (git commit -m 'Adicionei minha nova feature').
Envie suas mudanças para o repositório remoto (git push origin feature/nova-feature).
Abra um Pull Request explicando suas mudanças.
