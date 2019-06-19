from cliente import *
class agencia:
    def __init__(self,num_agencia=1):
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

ag = agencia()
c = cliente()
c.setCPF("064")
c.setNome("Diego")
ag.addCliente(c)

busca = ag.buscaCliente("064")
if busca:
    print("Achou")
else:
    print("Deu ruim")