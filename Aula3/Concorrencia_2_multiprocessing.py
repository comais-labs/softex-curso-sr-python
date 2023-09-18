# Concorrência a Nível de Processo (Multiprocessing):

import numpy as np
from sklearn.linear_model import LinearRegression
import multiprocessing
import time

# Função para gerar dados aleatórios
def generate_data(n_samples=100):
    X = np.random.rand(n_samples, 1) * 10  # Valores entre 0 e 10
    y = 2.5 * X + np.random.randn(n_samples, 1) * 2  # Linha reta com algum ruído
    return X, y

# Função para treinar um modelo de regressão linear
def train_model(process_id):
    X, y = generate_data()
    print(f"Process-{process_id} iniciando treinamento...")
    model = LinearRegression()
    model.fit(X, y)
    time.sleep(2)  # Simulando um treinamento mais longo
    print(f"Process-{process_id} finalizou treinamento. Coeficiente: {model.coef_[0][0]:.2f}")

if __name__ == "__main__":  # Importante para garantir que o multiprocessing funcione corretamente
    processes = []
    for i in range(50):  # Vamos treinar 4 modelos em paralelo
        process = multiprocessing.Process(target=train_model, args=(i,))
        processes.append(process)
        process.start()

    # Aguardando todos os processos finalizarem
    for process in processes:
        process.join()

    print("Todos os modelos foram treinados!")
