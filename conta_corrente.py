from conta import *
class conta_corrente(conta):
    def __init__(self,numero=0,saldo=0,limite=100):
        super().__init__(numero,saldo)
        self._limite = limite

    def getLimite(self):
        return self._limite
    def setLimite(self,limite):
        self._limite = limite

    def sacar(self,saque):
        if self.getSaldo() + self.getLimite() > saque:
            self._saldo -= saque
            return True
        else:
            return False

