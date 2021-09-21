# %%
import pandas as pd
import seaborn as sns
from scipy import stats

df = pd.read_csv("../files/analysed-java-repos-fixed.csv", sep=";")
q_low_lcom = df["lcom"].quantile(0.1)
q_hi_lcom = df["lcom"].quantile(0.9)
df_for_lcom = df[(df["lcom"] < q_hi_lcom) & (df["lcom"] > q_low_lcom)]

q_low_cbo = df["cbo"].quantile(0.1)
q_hi_cbo = df["cbo"].quantile(0.9)
df_for_cbo = df[(df["cbo"] < q_hi_cbo) & (df["cbo"] > q_low_cbo)]

q_low_dit = df["dit"].quantile(0.1)
q_hi_dit = df["dit"].quantile(0.9)
df_for_dit = df[(df["dit"] < q_hi_dit) & (df["dit"] > q_low_dit)]


# popularidade

# r, _ = stats.spearmanr(df_for_lcom['stars'], df_for_lcom['lcom'])
# sns.regplot(x="stars", y="lcom", data=df_for_lcom, ci=25,)
# print(f"Coeficiente de correlação de Spearman para estrelas e lcom r = {r}")

# r, _ = stats.spearmanr(df_for_cbo['stars'], df_for_cbo['cbo'])
# sns.regplot(x="stars", y="cbo", data=df_for_cbo, ci=25)
# print(f"Coeficiente de correlação de Spearman para estrelas e cbo r = {r}")

# r, _ = stats.spearmanr(df_for_dit['stars'], df_for_dit['dit'])
# sns.regplot(x="stars", y="dit", data=df_for_dit, ci=25)
# print(f"Coeficiente de correlação de Spearman para estrelas e dit r = {r}")


# maturidade

# r, _ = stats.spearmanr(df_for_lcom['age'], df_for_lcom['lcom'])
# sns.regplot(x="age", y="lcom", data=df_for_lcom, ci=25)
# print(f"Coeficiente de correlação de Spearman para age and lcom r = {r}")

# r, _ = stats.spearmanr(df_for_cbo['age'], df_for_cbo['cbo'])
# sns.regplot(x="age", y="cbo", data=df_for_cbo, ci=25)
# print(f"Coeficiente de correlação de Spearman para age and cbo r = {r}")

# r, _ = stats.spearmanr(df_for_dit['age'], df_for_dit['dit'])
# sns.regplot(x="age", y="dit", data=df_for_dit, ci=25)
# print(f"Coeficiente de correlação de Spearman para age and dti r = {r}")


# atividade

# r, _ = stats.spearmanr(df_for_lcom['releases'], df_for_lcom['lcom'])
# sns.regplot(x="releases", y="lcom", data=df_for_lcom, ci=25)
# print(f"Coeficiente de correlação de Spearman para releases and lcom r = {r}")

# r, _ = stats.spearmanr(df_for_cbo['releases'], df_for_cbo['cbo'])
# sns.regplot(x="releases", y="cbo", data=df_for_cbo, ci=25)
# print(f"Coeficiente de correlação de Spearman para releases and cbo r = {r}")

# r, _ = stats.spearmanr(df_for_dit['releases'], df_for_dit['dit'])
# sns.regplot(x="releases", y="dit", data=df_for_dit, ci=25)
# print(f"Coeficiente de correlação de Spearman para releases and dit r = {r}")


# tamanho

# r, _ = stats.spearmanr(df_for_lcom['loc'], df_for_lcom['lcom'])
# sns.regplot(x="loc", y="lcom", data=df_for_lcom, ci=25)
# print(f"Coeficiente de correlação de Spearman para loc and lcom r = {r}")

# r, _ = stats.spearmanr(df_for_cbo['loc'], df_for_cbo['cbo'])
# sns.regplot(x="loc", y="cbo", data=df_for_cbo, ci=25)
# print(f"Coeficiente de correlação de Spearman para loc and cbo r = {r}")

# r, _ = stats.spearmanr(df_for_dit['loc'], df_for_dit['dit'])
# sns.regplot(x="loc", y="dit", data=df_for_dit, ci=25)
# print(f"Coeficiente de correlação de Spearman para loc and dit r = {r}")

# %%
