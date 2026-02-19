# ============================================
# IMPORTS
# ============================================
import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style("whitegrid")
# ============================================
# CRIAÇÃO DE PASTAS
# ============================================
os.makedirs("eda_output/01_histograms", exist_ok=True)
os.makedirs("eda_output/02_correlation", exist_ok=True)
os.makedirs("eda_output/03_boxplots", exist_ok=True)
os.makedirs("eda_output/04_countplots", exist_ok=True)
os.makedirs("eda_output/05_scatter_target", exist_ok=True)
os.makedirs("eda_output/06_boxplot_target", exist_ok=True)


# ============================================
# LEITURA DOS DADOS
# ============================================
HOUSING_PATH = "housing-data/Housing.csv"
df = pd.read_csv(HOUSING_PATH)


# ============================================
# INSPEÇÃO INICIAL
# ============================================
print("\n------ SHAPE ------")
print(df.shape)

print("\n------ HEAD ------")
print(df.head())

print("\n------ INFO ------")
print(df.info())

print("\n------ DESCRIBE ------")
print(df.describe())

print("\n------ MISSING VALUES ------")
print(df.isnull().sum())


# ============================================
# SEPARAÇÃO NUMÉRICAS E CATEGÓRICAS
# ============================================
df_num = df.select_dtypes(include=["int64", "float64"])
df_cat = df.select_dtypes(include=["object", "category"])


# ============================================
# HISTOGRAMAS (Análise Univariada Numérica)
# ============================================
for col in df_num.columns:
    plt.figure(figsize=(8,5))
    sns.histplot(df_num[col].dropna(), kde=True)
    plt.title(f"Histogram - {col}")
    plt.tight_layout()
    plt.savefig(f"eda_output/01_histograms/{col}.png", dpi=300, bbox_inches="tight")
    plt.close()


# ============================================
# MATRIZ DE CORRELAÇÃO
# ============================================
plt.figure(figsize=(10,8))
num_corr = df_num.corr()
sns.heatmap(num_corr, annot=True, fmt=".2f", cmap="coolwarm", center=0)
plt.title("Correlation Matrix - Numeric Variables")
plt.tight_layout()
plt.savefig("eda_output/02_correlation/correlation_matrix.png", dpi=300, bbox_inches="tight")
plt.close()


# ============================================
# BOXPLOTS (Outliers Numéricos)
# ============================================
for col in df_num.columns:
    plt.figure(figsize=(8,5))
    sns.boxplot(x=df_num[col])
    plt.title(f"Boxplot - {col}")
    plt.tight_layout()
    plt.savefig(f"eda_output/03_boxplots/{col}.png", dpi=300, bbox_inches="tight")
    plt.close()


# ============================================
# COUNTPLOTS (Análise Univariada Categórica)
# ============================================
for col in df_cat.columns:
    plt.figure(figsize=(8,5))
    sns.countplot(x=df_cat[col], order=df_cat[col].value_counts().index)
    plt.title(f"Countplot - {col}")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f"eda_output/04_countplots/{col}.png", dpi=300, bbox_inches="tight")
    plt.close()


# ============================================
# SCATTERPLOTS (Numéricas contínuas vs Target)
# ============================================
TARGET = "price"


plt.figure(figsize=(8,5))
sns.scatterplot(x=df['area'], y=df[TARGET])
plt.title(f"area vs {TARGET}")
plt.tight_layout()
plt.savefig(f"eda_output/05_scatter_target/area_vs_{TARGET}.png",
        dpi=300, bbox_inches="tight")
plt.close()


# ============================================
# BOXPLOTS (Categóricas e numéricas discretas vs Target)
# ============================================
for col in df_cat.columns:
    plt.figure(figsize=(8,5))
    sns.boxplot(x=df[col], y=df[TARGET])
    plt.xticks(rotation=45)
    plt.title(f"{col} vs {TARGET}")
    plt.tight_layout()
    plt.savefig(f"eda_output/06_boxplot_target/{col}_vs_{TARGET}.png",
                dpi=300, bbox_inches="tight")
    plt.close()
    
for col in df_num.columns:
    if col != TARGET and col != "area":
        plt.figure(figsize=(8,5))
        sns.boxplot(x=df[col], y=df[TARGET])
        plt.xticks(rotation=45)
        plt.title(f"{col} vs {TARGET}")
        plt.tight_layout()
        plt.savefig(f"eda_output/06_boxplot_target/{col}_vs_{TARGET}.png",
                    dpi=300, bbox_inches="tight")
        plt.close()


