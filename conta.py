class conta:
    def __init__(self,numero = 0,saldo = 0):
        self._numero = numero
        self._saldo = saldo

    def setNumero(self,numero):
        self._numero = numero
    def getNumero(self):
        return self._numero

    def setSaldo(self,saldo):
        self._saldo = saldo
    def getSaldo(self):
        return self._saldo

    def sacar(self,saque):
        if self._saldo > saque:
            self._saldo -= saque

    def despositar(self,deposito):
        self._saldo += deposito

    def transferencia(self,valor):
        if self._saldo > valor:
            self._saldo -= valor



