#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🎬 Análise Exploratória - Top 1000 Filmes IMDb
Autor: Guilherme Fernandes
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import os

warnings.filterwarnings('ignore')

# Configurar estilo dos gráficos
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette("husl")

# Criar pasta de resultados
os.makedirs('results', exist_ok=True)

print("=" * 60)
print("🎬 ANÁLISE EXPLORATÓRIA - TOP 1000 FILMES IMDb")
print("=" * 60)

# ============================================================
# 2. CARREGAMENTO E INSPEÇÃO INICIAL
# ============================================================
print("\n📂 Carregando dataset...")

# Tentar carregar de várias fontes
df = None

# Opção 1: Pasta local
if os.path.exists('data/imdb_top_1000.csv'):
    df = pd.read_csv('data/imdb_top_1000.csv')
    print("✅ Dataset carregado da pasta local!")

# Opção 2: Baixar do Kaggle/GitHub
if df is None:
    try:
        url = "https://raw.githubusercontent.com/harshitshankhdhar/imdb-dataset-of-top-1000-movies-and-tv-shows/main/imdb_top_1000.csv"
        df = pd.read_csv(url)
        print("✅ Dataset baixado da internet!")
    except:
        print("❌ Erro: Não foi possível carregar o dataset")
        print("   Baixe manualmente em: https://www.kaggle.com/datasets/harshitshankhdhar/imdb-dataset-of-top-1000-movies-and-tv-shows")
        exit(1)

print(f"   Dataset: {df.shape[0]} filmes, {df.shape[1]} colunas")

# ============================================================
# 3. LIMPEZA DE DADOS
# ============================================================
print("\n🧹 Limpando dados...")

# Converter colunas
df['Released_Year'] = pd.to_numeric(df['Released_Year'], errors='coerce')
df['Runtime'] = df['Runtime'].str.replace(' min', '').astype(float)
df['IMDB_Rating'] = pd.to_numeric(df['IMDB_Rating'], errors='coerce')
df['Gross'] = df['Gross'].str.replace(',', '').astype(float)

# Tratar nulos
df['Runtime'].fillna(df['Runtime'].mean(), inplace=True)
df['Gross'].fillna(df['Gross'].median(), inplace=True)
df.dropna(subset=['Released_Year', 'IMDB_Rating'], inplace=True)

# Remover duplicatas
df = df.drop_duplicates()

print(f"   ✅ {len(df)} filmes após limpeza")

# ============================================================
# 4. ANÁLISE EXPLORATÓRIA
# ============================================================
print("\n📊 Realizando análises...")

# --- Pergunta 1: Distribuição de notas ---
print("\n1️⃣ Distribuição de Notas IMDb:")
print(f"   Média: {df['IMDB_Rating'].mean():.2f}")
print(f"   Mediana: {df['IMDB_Rating'].median():.2f}")
print(f"   Mínima: {df['IMDB_Rating'].min():.2f}")
print(f"   Máxima: {df['IMDB_Rating'].max():.2f}")

# --- Pergunta 2: Gênero com maior nota ---
generos_df = df.copy()
generos_df['Genre'] = generos_df['Genre'].str.split(', ')
generos_exploded = generos_df.explode('Genre')
media_genero = generos_exploded.groupby('Genre')['IMDB_Rating'].mean().sort_values(ascending=False)

print("\n2️⃣ Top 5 Gêneros por Nota Média:")
for i, (genero, nota) in enumerate(media_genero.head(5).items(), 1):
    print(f"   {i}. {genero}: {nota:.2f}")

# --- Pergunta 3: Relação ano e nota ---
nota_por_ano = df.groupby('Released_Year')['IMDB_Rating'].mean()
correlacao_ano_nota = df['Released_Year'].corr(df['IMDB_Rating'])
print(f"\n3️⃣ Correlação Ano x Nota: {correlacao_ano_nota:.4f}")

# --- Pergunta 4: Top diretores ---
media_diretor = df.groupby('Director')['IMDB_Rating'].agg(['mean', 'count'])
media_diretor.columns = ['nota_media', 'quantidade_filmes']
media_diretor = media_diretor[media_diretor['quantidade_filmes'] >= 3]
media_diretor = media_diretor.sort_values('nota_media', ascending=False)

print("\n4️⃣ Top 5 Diretores (mín. 3 filmes):")
for i, (diretor, row) in enumerate(media_diretor.head(5).iterrows(), 1):
    print(f"   {i}. {diretor}: {row['nota_media']:.2f} ({int(row['quantidade_filmes'])} filmes)")

# --- Pergunta 5: Duração por década ---
df['Decade'] = (df['Released_Year'] // 10 * 10).astype(int)
duracao_decada = df.groupby('Decade')['Runtime'].mean()

print("\n5️⃣ Duração Média por Década:")
for decada, duracao in duracao_decada.items():
    print(f"   {decada}s: {duracao:.0f} min")

# ============================================================
# 5. VISUALIZAÇÕES
# ============================================================
print("\n📈 Gerando gráficos...")

# Gráfico 1: Histograma de notas
plt.figure(figsize=(10, 6))
plt.hist(df['IMDB_Rating'], bins=20, edgecolor='black', color='#6366f1', alpha=0.7)
plt.xlabel('Nota IMDb', fontsize=12)
plt.ylabel('Frequência', fontsize=12)
plt.title('Distribuição das Notas IMDb - Top 1000 Filmes', fontsize=14, fontweight='bold')
plt.axvline(df['IMDB_Rating'].mean(), color='red', linestyle='--', label=f'Média: {df["IMDB_Rating"].mean():.2f}')
plt.legend()
plt.tight_layout()
plt.savefig('results/histograma_notas.png', dpi=150, bbox_inches='tight')
plt.close()
print("   ✅ histograma_notas.png")

# Gráfico 2: Média por gênero
plt.figure(figsize=(12, 6))
top_generos = media_genero.head(10)
colors = plt.cm.viridis(np.linspace(0, 1, len(top_generos)))
bars = plt.barh(top_generos.index[::-1], top_generos.values[::-1], color=colors[::-1], edgecolor='black')
plt.xlabel('Nota Média IMDb', fontsize=12)
plt.ylabel('Gênero', fontsize=12)
plt.title('Top 10 Gêneros por Nota Média', fontsize=14, fontweight='bold')
plt.xlim(7, 9)
for i, v in enumerate(top_generos.values[::-1]):
    plt.text(v + 0.02, i, f'{v:.2f}', va='center', fontsize=10)
plt.tight_layout()
plt.savefig('results/grafico_genero.png', dpi=150, bbox_inches='tight')
plt.close()
print("   ✅ grafico_genero.png")

# Gráfico 3: Evolução por ano
plt.figure(figsize=(14, 6))
nota_por_ano_grafico = nota_por_ano[nota_por_ano.index >= 1960]
plt.plot(nota_por_ano_grafico.index, nota_por_ano_grafico.values, marker='o', linewidth=2, markersize=4, color='#10b981')
plt.xlabel('Ano de Lançamento', fontsize=12)
plt.ylabel('Nota Média IMDb', fontsize=12)
plt.title('Evolução da Nota Média IMDb por Ano (1960-2020)', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('results/grafico_ano.png', dpi=150, bbox_inches='tight')
plt.close()
print("   ✅ grafico_ano.png")

# Gráfico 4: Duração vs Nota
plt.figure(figsize=(10, 6))
plt.scatter(df['Runtime'], df['IMDB_Rating'], alpha=0.5, c='#8b5cf6', edgecolors='white', s=50)
plt.xlabel('Duração (minutos)', fontsize=12)
plt.ylabel('Nota IMDb', fontsize=12)
plt.title('Relação entre Duração e Nota IMDb', fontsize=14, fontweight='bold')
z = np.polyfit(df['Runtime'], df['IMDB_Rating'], 1)
p = np.poly1d(z)
plt.plot(df['Runtime'].sort_values(), p(df['Runtime'].sort_values()), color='red', linestyle='--', linewidth=2, label='Tendência')
plt.legend()
plt.tight_layout()
plt.savefig('results/grafico_duracao.png', dpi=150, bbox_inches='tight')
plt.close()
print("   ✅ grafico_duracao.png")

# ============================================================
# 6. INSIGHTS E CONCLUSÕES
# ============================================================
print("\n" + "=" * 60)
print("💡 INSIGHTS E CONCLUSÕES")
print("=" * 60)

insights = """
1. DISTRIBUIÇÃO DE NOTAS:
   A maioria dos filmes no Top 1000 do IMDb possui notas entre 7.5 e 8.5,
   com média de aproximadamente 7.9. Isso demonstra que os critérios de
   seleção do IMDb tendem a incluir filmes de alta qualidade consolidados.

2. GÊNEROS DE MAIOR QUALIDADE:
   Os gêneros "Film-Noir", "War" e "Biography" apresentam as maiores notas
   médias, indicando que estes estilos cinematográficos tendem a ser mais
   bem avaliados pelo público. Drama e comédia, embora mais comuns,
   possuem notas um pouco inferiores.

3. EVOLUÇÃO TEMPORAL:
   Observa-se uma leve tendência positiva entre o ano de lançamento e a
   nota, sugerindo que filmes mais recentes tendem a receber avaliações
   marginalmente melhores. Isso pode estar relacionado ao viés de
   survivorship, onde apenas os melhores filmes mais antigos são lembrados.

4. DIRETORES CONSISTENTES:
   Diretores como Christopher Nolan, Quentin Tarantino e Steven Spielberg
   aparecem consistentemente com múltiplos filmes no ranking,
   demonstrando qualidade persistente ao longo de suas carreiras.
"""
print(insights)

# Salvar insights em arquivo
with open('results/insights.txt', 'w', encoding='utf-8') as f:
    f.write(insights)

print("\n✅ Análise concluída!")
print(f"   📁 Resultados salvos na pasta 'results/'")
print("=" * 60)
