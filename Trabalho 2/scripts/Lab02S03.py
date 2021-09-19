# %%
import pandas as pd
import seaborn as sns

df_melt = pd.read_csv("../files/analysed-java-repos.csv", sep=";")


sns.regplot(x="stars", y="lcom", data=df_melt)

# sns.regplot(x="stars", y="cbo", data=df_melt)

# sns.regplot(x="stars", y="dit", data=df_melt)

# %%
