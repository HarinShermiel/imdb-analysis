# 🎬 Análise Exploratória - Top 1000 Filmes IMDb

![Python](https://img.shields.io/badge/Python-3.9+-blue?style=flat&logo=python)
![Pandas](https://img.shields.io/badge/Pandas-1.3+-orange?style=flat)
![Seaborn](https://img.shields.io/badge/Seaborn-0.11+-green?style=flat)

## 📊 Descrição do Projeto

Este projeto consiste em uma análise exploratória de dados (EDA) detalhada dos 1000 melhores filmes do IMDb, buscando entender padrões, tendências e insights sobre a indústria cinematográfica através de dados objetivos.

---

## 📁 Estrutura do Projeto

```
imdb-analysis/
├── data/                    # Dataset CSV
│   └── imdb_top_1000.csv
├── notebooks/
│   └── analise_filmes.ipynb # Notebook principal
├── images/                  # Gráficos gerados
├── README.md                # Este arquivo
└── requirements.txt         # Bibliotecas Python
```

---

## 🛠️ Tecnologias e Bibliotecas

- **Python 3.9+** - Linguagem principal
- **Pandas** - Manipulação e análise de dados
- **NumPy** - Operações numéricas
- **Matplotlib** - Visualização de dados
- **Seaborn** - Gráficos estatísticos

---

## 🚀 Como Executar

### 1. Clone o repositório

```bash
git clone https://github.com/HarinShermiel/imdb-analysis.git
cd imdb-analysis
```

### 2. Crie um ambiente virtual (opcional)

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Baixe o dataset

O dataset está disponível em: [IMDb Dataset - Kaggle](https://www.kaggle.com/datasets/harshitshankhdhar/imdb-dataset-of-top-1000-movies-and-tv-shows)

Coloque o arquivo `imdb_top_1000.csv` na pasta `data/`.

### 5. Execute o Jupyter Notebook

```bash
jupyter notebook notebooks/analise_filmes.ipynb
```

---

## 📈 Análises Realizadas

### Perguntas Respondidas

1. **Qual a distribuição de notas IMDb?**
2. **Qual gênero tem maior nota média?**
3. **Qual a relação entre ano e nota?**
4. **Top 10 diretores por média de avaliação?**
5. **Evolução da duração média dos filmes por década?**

### Visualizações Geradas

| Gráfico | Descrição |
|---------|-----------|
| 📊 Histograma | Distribuição das notas IMDb |
| 📈 Barras | Nota média por gênero |
| 📉 Linha | Evolução da nota por ano |
| 🔵 Scatter | Relação duração vs nota |

---

## 💡 Principais Insights

1. **Distribuição de Notas:** A maioria dos filmes possui notas entre 7.5 e 8.5, com média de ~7.9

2. **Gêneros de Maior Qualidade:** Film-Noir, War e Biography lideram as avaliações

3. **Evolução Temporal:** Filmes mais recentes apresentam tendência levemente superior de notas

4. **Diretores Consistentes:** Christopher Nolan, Quentin Tarantino e Steven Spielberg aparecem múltiplas vezes

---

## 📝 Autor

**Guilherme Fernandes**

- 📍 Brasília, DF
- 💼 Buscando oportunidades como Analista de Dados Júnior
- 📧 guilherme.f.medeiros.o@gmail.com
- 🔗 [LinkedIn](https://www.linkedin.com/in/guilherme-fernandes-b2ab99364/)

---

## 📜 Licença

Este projeto está sob a licença MIT.

---

*⭐ Se este projeto te ajudou, considere dar uma estrela!*
