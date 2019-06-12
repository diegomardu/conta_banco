from cliente import *
from conta import *
class agencia:
    def __init__(self,num_agencia):
        self._num_agencia = num_agencia
        self._clientes = []

    def addCliente(self,cliente):
        self._clientes.append(cliente)


