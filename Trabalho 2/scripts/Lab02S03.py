# %%
import pandas as pd
import seaborn as sns
from scipy import stats

df = pd.read_csv("../files/analysed-java-repos-fixed.csv", sep=";")
q_low = df["lcom"].quantile(0.1)
q_hi = df["lcom"].quantile(0.9)

df_filtered = df[(df["lcom"] < q_hi) & (df["lcom"] > q_low)]

# popularidade

# r, _ = stats.spearmanr(df_filtered['stars'], df_filtered['lcom'])
# sns.regplot(x="stars", y="lcom", data=df_filtered, ci=25,)
# print(f"Coeficiente de correlação de Spearman para estrelas e lcom r = {r}")

# r, _ = stats.spearmanr(df_filtered['stars'], df_filtered['cbo'])
# sns.regplot(x="stars", y="cbo", data=df_filtered, ci=25)
# print(f"Coeficiente de correlação de Spearman para estrelas e cbo r = {r}")

# r, _ = stats.spearmanr(df_filtered['stars'], df_filtered['dit'])
# sns.regplot(x="stars", y="dit", data=df_filtered, ci=25)
# print(f"Coeficiente de correlação de Spearman para estrelas e dit r = {r}")


# maturidade

# r, _ = stats.spearmanr(df_filtered['age'], df_filtered['lcom'])
# sns.regplot(x="age", y="lcom", data=df_filtered, ci=25)
# print(f"Coeficiente de correlação de Spearman para age and lcom r = {r}")

# r, _ = stats.spearmanr(df_filtered['age'], df_filtered['cbo'])
# sns.regplot(x="age", y="cbo", data=df_filtered, ci=25)
# print(f"Coeficiente de correlação de Spearman para age and cbo r = {r}")

# r, _ = stats.spearmanr(df_filtered['age'], df_filtered['dti'])
# sns.regplot(x="age", y="dti", data=df_filtered, ci=25)
# print(f"Coeficiente de correlação de Spearman para age and dti r = {r}")


# atividade

# r, _ = stats.spearmanr(df_filtered['releases'], df_filtered['lcom'])
# sns.regplot(x="releases", y="lcom", data=df_filtered, ci=25)
# print(f"Coeficiente de correlação de Spearman para releases and lcom r = {r}")

# r, _ = stats.spearmanr(df_filtered['releases'], df_filtered['cbo'])
# sns.regplot(x="releases", y="cbo", data=df_filtered, ci=25)
# print(f"Coeficiente de correlação de Spearman para releases and cbo r = {r}")

# r, _ = stats.spearmanr(df_filtered['releases'], df_filtered['dit'])
# sns.regplot(x="releases", y="dit", data=df_filtered, ci=25)
# print(f"Coeficiente de correlação de Spearman para releases and dit r = {r}")


# tamanho

# r, _ = stats.spearmanr(df_filtered['loc'], df_filtered['lcom'])
# sns.regplot(x="loc", y="lcom", data=df_filtered, ci=25)
# print(f"Coeficiente de correlação de Spearman para loc and lcom r = {r}")

# r, _ = stats.spearmanr(df_filtered['loc'], df_filtered['cbo'])
# sns.regplot(x="loc", y="cbo", data=df_filtered, ci=25)
# print(f"Coeficiente de correlação de Spearman para loc and cbo r = {r}")

# r, _ = stats.spearmanr(df_filtered['loc'], df_filtered['dit'])
# sns.regplot(x="loc", y="dit", data=df_filtered, ci=25)
# print(f"Coeficiente de correlação de Spearman para loc and dit r = {r}")
