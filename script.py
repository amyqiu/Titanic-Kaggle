import pandas

titanic = pandas.read_csv("train.csv")
print(titanic.head(5))
print(titanic.describe())
