from cliente import *
class agencia:
    def __init__(self,num_agencia):
        self._num_agencia = num_agencia
        self._clientes = []

    def addCliente(self,cliente):
        self._clientes.append(cliente)

    def buscaCliente(self,cpf):
        for i in self._clientes:
            if i.getCPF() == cpf:
                return True
            else:
                return False


