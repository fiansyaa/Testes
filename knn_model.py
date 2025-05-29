from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier

def train_model():
    iris = load_iris()
    X = iris.data
    y = iris.target

    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(X, y)

    return model, iris
