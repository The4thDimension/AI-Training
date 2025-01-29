import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset("iris")

print(df.head())
print(df.info())
print(df.describe())

plt.hist(df["sepal_length"], bins=20, color="blue", alpha=0.7)
plt.xlabel("Sepal Length")
plt.ylabel("Frequency")
plt.title("Distribution of Sepal Length")
plt.show()

plt.hist(df["petal_length"], bins=20, alpha=0.7, color="red")
plt.xlabel("Petal Length")
plt.ylabel("Frequency")
plt.title("Distribution of Petal Length")
plt.show()

plt.scatter(df["petal_length"], df["petal_width"], color="blue")
plt.xlabel("Petal Length")
plt.ylabel("Petal Width")
plt.title("New Title")
plt.show()

df["sepal_length"].plot(kind="line", figsize=(8, 4), color="green")
plt.title("Another Title")
plt.show()

sns.pairplot(df, hue="species")
plt.show()