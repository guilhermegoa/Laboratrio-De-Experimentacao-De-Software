# %%
import pandas as pd
import seaborn as sns

df = pd.read_csv("../files/analysed-java-repos.csv", sep=";")

sns.set_theme(style="darkgrid")


a = sns.regplot(x="stars", y="lcom", data=df)
b = sns.jointplot(x="stars", y="lcom", data=df, kind="reg", truncate=False)
