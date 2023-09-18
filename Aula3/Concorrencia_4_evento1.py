# Concorrência Baseada em Eventos (1)

# Instale a biblioteca Twisted antes de executar: 
# !pip install twisted

# A concorrência baseada em eventos é um modelo onde o 
# fluxo de execução é determinado pela ocorrência de eventos 
# externos. Em Python, uma biblioteca popular que permite a 
# programação orientada a eventos é a asyncio, mas ela é mais 
# voltada para a concorrência assíncrona. Para um exemplo mais 
# puro de concorrência baseada em eventos, podemos usar a 
# biblioteca Twisted, que é um framework orientado a eventos 
# para Python.

# No contexto de MLOps, um exemplo prático de concorrência 
# baseada em eventos pode ser um servidor que escuta solicitações 
# de previsão e responde com os resultados do modelo. Cada 
# solicitação e resposta são tratadas como eventos.

# Vamos criar um servidor simples usando Twisted que simula 
# a recepção de solicitações de previsão e retorna uma resposta:

# Neste exemplo:

# - PredictionProtocol define como lidar com eventos de dados recebidos.
# - PredictionFactory é uma fábrica que produz instâncias do protocolo.
# - O servidor começa a escutar na porta 8000 e, quando os dados são 
# recebidos (um evento), ele chama a função dataReceived.
# Para testar, você pode usar qualquer cliente TCP (como telnet ou nc) 
# para se conectar ao servidor e enviar uma solicitação.

# Este é um exemplo básico e, em cenários reais de MLOps, você teria que 
# integrar com um modelo real de ML, lidar com serialização de dados, 
# erros, etc. No entanto, o conceito principal é que a lógica é acionada 
# em resposta a eventos (neste caso, solicitações recebidas).


from twisted.internet import protocol, reactor, endpoints

class PredictionProtocol(protocol.Protocol):
    def dataReceived(self, data):
        """Esta função é chamada quando dados (um evento) são recebidos"""
        # Simulando o processamento de uma solicitação de previsão
        response = self.process_prediction_request(data)
        self.transport.write(response)

    def process_prediction_request(self, data):
        """Simula o processamento de uma solicitação e retorna uma resposta"""
        # Aqui, em um cenário real, você chamaria seu modelo de ML para obter uma previsão
        # Para simplificar, estamos apenas retornando uma resposta mock
        return b"Predicted value: 123\n"

class PredictionFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return PredictionProtocol()

# Iniciando o servidor
endpoints.serverFromString(reactor, "tcp:8000").listen(PredictionFactory())
print("Prediction server started on port 8000...")
reactor.run()
