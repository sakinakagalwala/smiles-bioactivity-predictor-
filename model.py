import numpy as np
from sklearn.ensemble import RandomForestClassifier

def train_dummy_model():
    X = np.random.rand(100, 10)
    y = np.random.randint(2, size=100)
    model = RandomForestClassifier()
    model.fit(X, y)
    return model

