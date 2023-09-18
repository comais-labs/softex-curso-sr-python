# Paralelismo de tarefas

import numpy as np
from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from concurrent.futures import ProcessPoolExecutor

# Gerar dados sintéticos
X, y = make_regression(n_samples=1000, n_features=20, noise=0.1)

# Funções de treinamento para diferentes modelos
def train_linear_regression(data):
    X, y = data
    model = LinearRegression()
    model.fit(X, y)
    return model.coef_

def train_ridge(data):
    X, y = data
    model = Ridge()
    model.fit(X, y)
    return model.coef_

def train_lasso(data):
    X, y = data
    model = Lasso()
    model.fit(X, y)
    return model.coef_

def train_model(func_data):
    func, data = func_data
    return func(data)

def main():
    functions = [train_linear_regression, train_ridge, train_lasso]
    tasks = [(func, (X, y)) for func in functions]

    # Usando Task Parallelism para treinar os modelos em paralelo
    with ProcessPoolExecutor(max_workers=3) as executor:
        print("Treinando modelos...")
        results = list(executor.map(train_model, tasks))

    # Exibindo os coeficientes dos modelos treinados
    model_names = ["Linear Regression", "Ridge", "Lasso"]
    for name, coef in zip(model_names, results):
        print(f"{name} Coefficients: {coef[:2]}...")  # Mostrando apenas os primeiros 5 coeficientes para brevidade

if __name__ == "__main__":
    main()