class conta:
    def __init__(self,titular,numero,saldo,limite):
        self._titular = titular
        self._numero = numero
        self._saldo = saldo
        self._limite = limite

    def setTitular(self,titular):
        self._titular = titular
    def getTitular(self):
        return self._titular

    def setNumero(self,numero):
        self._numero = numero
    def getNumero(self):
        return self._numero

    def setSaldo(self,saldo):
        self._saldo = saldo
    def getSaldo(self):
        return self._saldo

    def setLimite(self,limite):
        self._limite = limite
    def getLimite(self):
        return self._limite

    def deposito(self,valor):
        self._saldo += valor
    def saque(self,valor):
        if self._saldo > valor:
            self._saldo -= valor
        else:
            print("Saldo insuficiente para saque")
    def transferencia(self,destino,valor):
        if self._saldo >= valor:
            self._saldo -= valor
            destino._saldo += valor
        else:
            print("Saldo insuficiente para transferencia")