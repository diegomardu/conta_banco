from conta import *
class cliente:
    def __init__(self,nome = "",cpf = ""):
        self._nome = nome
        self._cpf = cpf
        self._contas = []

    def getNome(self):
        return self._nome
    def setNome(self,nome):
        self._nome = nome

    def getCPF(self):
        return self._cpf
    def setCPF(self,cpf):
        self._cpf = cpf

    def addConta(self,conta):
        self._contas.append(conta)




