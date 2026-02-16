# 🎬 Análise Exploratória - Top 1000 Filmes IMDb

![Python](https://img.shields.io/badge/Python-3.9+-blue?style=flat&logo=python)
![Pandas](https://img.shields.io/badge/Pandas-1.3+-orange?style=flat)
![Seaborn](https://img.shields.io/badge/Seaborn-0.11+-green?style=flat)

## 📊 Descrição

Análise exploratória de dados (EDA) dos 1000 melhores filmes do IMDb, buscando entender padrões e tendências na indústria cinematográfica.

---

## 🚀 Como Executar (FÁCIL!)

### Opção 1: Executar o Script (Recomendado)

```bash
# 1. Clone o projeto
git clone https://github.com/HarinShermiel/imdb-analysis.git
cd imdb-analysis

# 2. Instale as bibliotecas
pip install pandas numpy matplotlib seaborn

# 3. Execute
python analise.py
```

O script vai:
- Baixar o dataset automaticamente (se não tiver)
- Limpar os dados
- Fazer todas as análises
- Gerar os gráficos na pasta `results/`
- Mostrar os insights no terminal

---

### Opção 2: Usar o Jupyter Notebook

```bash
# Instale Jupyter
pip install jupyter

# Execute
jupyter notebook
```

Abra `notebooks/analise_filmes.ipynb` e execute célula por célula.

---

## 📁 Estrutura do Projeto

```
imdb-analysis/
├── data/                    # Dataset (baixe do Kaggle se necessário)
│   └── imdb_top_1000.csv
├── notebooks/
│   └── analise_filmes.ipynb # Jupyter Notebook
├── results/                 # 📊 Resultados já gerados!
│   ├── histograma_notas.png
│   ├── grafico_genero.png
│   ├── grafico_ano.png
│   ├── grafico_duracao.png
│   └── insights.txt
├── analise.py              # 🎯 Script principal (execute este!)
├── README.md
└── requirements.txt
```

---

## 📈 Análises Realizadas

### 5 Perguntas Respondidas

| # | Pergunta |
|---|----------|
| 1 | Qual a distribuição de notas IMDb? |
| 2 | Qual gênero tem maior nota média? |
| 3 | Qual a relação entre ano e nota? |
| 4 | Top 10 diretores por média de avaliação? |
| 5 | Evolução da duração média por década? |

### 4 Visualizações

| Gráfico | Descrição |
|---------|-----------|
| 📊 histograma_notas.png | Distribuição das notas IMDb |
| 📈 grafico_genero.png | Nota média por gênero |
| 📉 grafico_ano.png | Evolução da nota por ano |
| 🔵 grafico_duracao.png | Relação duração vs nota |

---

## 💡 Principais Insights

1. **Distribuição de Notas:** Média ~7.9, maioria entre 7.5 e 8.5

2. **Gêneros de Maior Qualidade:** Film-Noir, War e Biography lideram

3. **Evolução Temporal:** Filmes mais recentes têm notas levemente melhores

4. **Diretores Consistentes:** Christopher Nolan, Tarantino, Spielberg

---

## 📝 Autor

**Guilherme Fernandes** - Analista de Dados Júnior

- 📧 guilherme.f.medeiros.o@gmail.com
- 🔗 [LinkedIn](https://www.linkedin.com/in/guilherme-fernandes-b2ab99364/)

---

⭐ *Se te agradou, considere dar uma estrela!*
