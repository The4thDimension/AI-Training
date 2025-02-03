import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = sns.load_dataset("titanic")
print(df.isnull().sum())
print(df["survived"].value_counts())
sns.barplot(x="sex", y="survived", palette="coolwarm", data=df)
plt.title("Survival Count by Gender")
plt.show()