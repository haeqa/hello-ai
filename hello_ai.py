from sklearn.datasets import load_iris
import pandas as pd

# Load a classic dataset
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)

print("First 5 rows of the Iris dataset:")
print(df.head())