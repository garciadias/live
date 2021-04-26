"""Hello world de data science."""
from sklearn.datasets import load_iris
from matplotlib import pyplot as plt
import pandas as pd

data = load_iris()
X = pd.DataFrame(data.data, columns=data.feature_names)

X.describe()

fig = plt.figure(figsize=(16, 9))
plt.scatter(X["sepal width (cm)"], X["sepal length (cm)"], c=data.target)
plt.show()
